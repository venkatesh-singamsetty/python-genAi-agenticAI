# Google DeepMind & Gemini 3

This repository contains notes and example projects demonstrating how to use **Google DeepMind Gemini models** (Gemini 1.5 / Gemini 3) for text generation, image understanding, and building a simple frontend app.

---

## Agenda
- Introduction to Google DeepMind
- Overview of Gemini 3 models
- Build applications using Google Colab
  - Text generation
  - Image-to-text generation
- Build a frontend app using Streamlit + Gemini 3

---

## Google DeepMind Overview
- Website: https://deepmind.google/
- Models: https://deepmind.google/models/

Google DeepMind is Google’s AI research division, responsible for Gemini, AlphaFold, and advanced multimodal AI systems.

---

## Trying Gemini Without Code
- **Google AI Studio (Prompts):**  
  https://aistudio.google.com/prompts/new_chat?model=gemini-3-pro-preview  
  *(Permissions required)*

- **Google AI Studio (Apps):**  
  https://aistudio.google.com/apps

- **Gemini Web App:**  
  https://gemini.google.com/app  
  Example use case: Upload a medical prescription and ask Gemini to summarize it.

---

## Gemini API Key
Create an API key:
- https://aistudio.google.com/api-keys

> ⚠️ Never hardcode API keys in production.

```python
import os
os.environ['GEMINI_API_KEY'] = 'xxxx'
```

---

## Colab Notebook
- Notebook Name: `gemini3-llm-bootcamp.ipynb`
- Colab Link:  
  https://colab.research.google.com/drive/1u8FNn5jkQM6xYl4eQrJiSarWlRPY9W8C

---

## Setup

Install the official Google GenAI SDK:

```bash
pip install -q -U google-genai
```

```python
import os
os.environ['GEMINI_API_KEY'] = 'xxxx'
```

```python
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])
```

---

## Project 1: Text Generation using Gemini

### Basic Text Generation

```python
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents='Explain quantum physics to a five year old.'
)
print(response.text)
```

### List Available Models

```python
for model in client.models.list():
    print(model.name)
```

### Generate Structured Content

```python
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents='Create a table comparing AI vs Agentic AI vs MCP'
)
print(response.text)
```

---

## Project 2: Image to Text using Gemini

### Load Image from Google Drive

```python
from google.colab import drive
from PIL import Image
from IPython.display import display

drive.mount('/content/drive')

img = Image.open('/content/drive/MyDrive/horse.webp')
display(img)
```

### Describe Image

```python
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=['Describe this image', img]
)
print(response.text)
```

---

## Project 3: Frontend App using Streamlit + Gemini 3

### Features
- Upload an image
- Optional text prompt
- Gemini 3 Flash generates a response
- Lightweight web UI

### Run the App

```bash
streamlit run app.py
```

Access the app at:
- http://localhost:8501

### Model Used
- `gemini-3-flash-preview`

---

## Key Takeaways
- Gemini models are **multimodal** (text + image)
- Google AI Studio is best for rapid experimentation
- Colab is ideal for prototyping
- Streamlit enables quick demo applications
- Use **Flash models** for speed, **Pro models** for deeper reasoning

---

## Next Steps
- Add authentication and secret management
- Handle rate limits and cost controls
- Compare Gemini with OpenAI and Claude models
- Deploy Streamlit app to Cloud Run or GKE

---
