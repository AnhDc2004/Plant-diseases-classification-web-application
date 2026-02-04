import io

import torch
import torch.nn as nn
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image
from torchvision import models
from torchvision import transforms as T

from deepseek import get_cure, get_info
from Mapping import LabelMapper


def get_mobilenet_v3(num_classes):
    print(f"Building MobileNetV3 for {num_classes} classes...")
    model = models.mobilenet_v3_large(weights=models.MobileNet_V3_Large_Weights.DEFAULT)
    in_features = model.classifier[3].in_features
    model.classifier[3] = nn.Linear(in_features, num_classes)  # type: ignore
    return model


plant_model = get_mobilenet_v3(18)
disease_model = get_mobilenet_v3(56)

state_dict_plant = torch.load("best_plant_mobilenet.pth", map_location="cpu")
state_dict_disease = torch.load("best_disease_mobilenet.pth", map_location="cpu")

plant_model.load_state_dict(state_dict_plant)
disease_model.load_state_dict(state_dict_disease)

plant_model.eval()
disease_model.eval()

transform = T.Compose(
    [
        T.Resize((224, 224)),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


app = FastAPI()


@app.get("/")
def index():
    return FileResponse("index.html", media_type="text/html")


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    # return {"filename": image.filename}
    contents = await image.read()

    img = Image.open(io.BytesIO(contents)).convert("RGB")

    tensor_img = transform(img).unsqueeze(0)  # type: ignore
    with torch.no_grad():
        plant_output = plant_model(tensor_img)
        plant_softmax = torch.softmax(plant_output, dim=1)
        # print(plant_softmax)
        plant_pred = torch.argmax(plant_softmax, dim=1)

        disease_output = disease_model(tensor_img)
        disease_softmax = torch.softmax(disease_output, dim=1)
        # print(disease_softmax)
        disease_pred = torch.argmax(disease_softmax, dim=1)

    if LabelMapper.id_to_label("disease", int(disease_pred.item())) == "healthy":
        return get_info(LabelMapper.id_to_label("plant", int(plant_pred.item())))
    return get_cure(
        LabelMapper.id_to_label("plant", int(plant_pred.item())),
        LabelMapper.id_to_label("disease", int(disease_pred.item())),
    )
    # return {
    #     "status": "received",
    #     "size": img.size,
    #     "plant_output": LabelMapper.id_to_label("plant", int(plant_pred.item())),
    #     "disease_output": LabelMapper.id_to_label("disease", int(disease_pred.item())),
    #     "cure": get_cure(
    #         LabelMapper.id_to_label("plant", int(plant_pred.item())),
    #         LabelMapper.id_to_label("disease", int(disease_pred.item())),
    #     ),
    # }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
