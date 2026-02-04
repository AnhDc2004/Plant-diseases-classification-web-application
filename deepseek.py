import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", ""), base_url="https://api.deepseek.com"
)


def get_info(plant: str):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "You are a person of few words, so eliminate all superfluous phrases, introductions, and explanations, focus on answering the question, and do not like to bold or highlight text in the results.",
            },
            {
                "role": "user",
                "content": f"Gather information on the plant {plant} including description (name, species, origin, identification characteristics), nutritional needs, growing season, and notes on cultivation.",
            },
        ],
        stream=False,
    )
    return response.choices[0].message.content


def get_cure(plant: str, disease: str):
    print(plant)
    print(disease)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "You are a person of few words, so eliminate all superfluous phrases, introductions, and explanations, focus on answering the question, and do not like to bold or highlight text in the results.",
            },
            {
                "role": "user",
                "content": f"For the plant {plant} suffering from the disease {disease}, briefly describe the identification method (including the plant name, disease name, and identifying characteristics/symptoms on the leaves), provide a simple analysis of the origin/cause, mode of infection, prevention methods, and list a maximum of 3 treatment methods arranged by increasing severity of the disease, with each method on a single line and the methods having a relatively high level of detail.",
            },
        ],
        stream=False,
    )
    return response.choices[0].message.content
