# Install the necessary packages
# !pip install pyttsx3 google-generativeai openai

import pyttsx3

import os

import google.generativeai as genai
from openai import OpenAI
engine = pyttsx3.init()
# Configure the Google Generative AI
genai.configure(api_key='AIzaSyBLV6ykZq8l1BBM77qgjHQZ9zIisQUUpaE')

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": ["hii\n"],
        },
        {
            "role": "model",
            "parts": ["Hi! How can I help you today? \n"],
        },
    ]
)

response = chat_session.send_message("What Is Github?")

print(response.text)
engine.say(response.text)
engine.runAndWait()
