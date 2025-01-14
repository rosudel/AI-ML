#https://www.youtube.com/watch?v=XWB5DXP-DO8&list=PLZoTAELRMXVOQPRG7VAuHL--y97opD5GQ&index=4
#This is the actual part of mobile/web app.
#User will give prompt from this UI

import requests
import streamlit as st

#post method
def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/golam/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


st.title('Langchain Demo With llama3.2:1b API')
input_text1=st.text_input("Write a poem on")

if input_text1:
    st.write(get_ollama_response(input_text1))