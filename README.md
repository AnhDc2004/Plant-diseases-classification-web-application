# Plant Disease Classification & Treatment Recommendation System
📌 Overview
This project is a comprehensive deep learning-based solution designed to identify plant species and diagnose diseases from leaf images. Beyond classification, the system integrates Large Language Models (LLMs) to provide actionable treatment advice for farmers. This was my Graduation Project at FPT University, where I achieved a high academic ranking.

🚀 Key Features
- Dual-Model Architecture: Uses specialized CNN models (MobileNetV3) to first identify the plant species and then diagnose the specific disease.
- Large-Scale Data Processing: Engineered a robust data pipeline that refined a raw dataset of 560,000 images into a high-quality, balanced set of 226,000 samples.
- AI-Powered Filtering: Leveraged Gemini 1.5 Flash for automated data cleaning and quality assurance.
- Intelligent Recommendations: Integrated Grok LLM via FastAPI to generate real-time diagnosis reports and treatment suggestions.

🛠 Tech Stack
- Deep Learning: Pytorch, MobileNetV3, CNNs.
- Generative AI: Gemini 1.5 Flash (for data refinement), Grok LLM (for diagnosis advice).
- Backend: FastAPI, Python.
- Frontend: HTML/CSS (Web-based interface).

📊 Data Pipeline
The project involved a significant data engineering effort:
- Collection: Gathered 560k raw images from various sources.
- Refinement: Used AI-driven filtering to remove low-quality or irrelevant images, resulting in a 226k sample dataset.
- Optimization: Implemented data augmentation and normalization techniques to ensure model robustness.
