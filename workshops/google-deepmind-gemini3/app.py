import streamlit as st
from PIL import Image
import os
import pathlib
import textwrap

os.environ['GEMINI_API_KEY'] = 'xxxx'

from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

def get_gemini_response(input_text, image):
    model_id = 'gemini-3-flash-preview'
    
    contents = []
    if input_text:
        contents.append(input_text)
    if image:
        contents.append(image)
        
    response = client.models.generate_content(
        model=model_id,
        contents=contents
    )
    return response.text

st.set_page_config(page_title="Gemini 3 Flash Demo by Venkat", page_icon=":camera:", layout="wide")
    
st.header("Gemini 3 Flash Demo")
input_prompt = st.text_input("Input Prompt:", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "webp"])

img = None
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Generate Response about the image using Gemini 3 Flash")

if submit:
    if img is None:
        st.warning("Please upload an image to proceed.")
    else:
        with st.spinner("Generating response..."):
            response_text = get_gemini_response(input_prompt, img)
        st.subheader("Gemini 3 Flash Response:")
        st.write(response_text)
