import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant"):
    st.write("안녕하세요! 무엇이든 제가 영어로 번역해드릴게요!")



with open(".env") as f:
    api_key = f.read().strip()
 # API Key

prompt = st.chat_input("번역할 문장")


if prompt:
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"{prompt}\n위 문장을 영어로 변역해줄 수 있니?"}])
    st.session_state.messages.append((prompt,completion.choices[0].message.content))

for prompt, answer in st.session_state.messages:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(answer)