from langchain_core.messages import ChatMessage

import streamlit as st
import time

aaa = 123

st.set_page_config(page_title="Page Title123")

@st.cache_resource(show_spinner="loading...")
def init():
    global aaa
    time.sleep(3)
    aaa = 1234

init()

st.info(aaa)


st.title('Title123')
# with st.form('Question123'):
#     text = st.text_area('질문 내용:', '질문 기본값1234') #첫 페이지가 실행될 때 보여줄 질문
#     submitted = st.form_submit_button('보내기') # 버튼 이름
#     st.info(text) # 텍스트 상자

############################ 파일 업로드
@st.cache_resource(show_spinner="Embedding file...")
def embed_file(file):    
    file_content = file.read()
    st.info(file.name)
    st.info(file)
    time.sleep(1)

with st.sidebar:
    file = st.file_uploader("파일 업로드", type=["pdf", "txt", ], )

if file:
    embed_file(file)
    

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        ChatMessage(role="assistant", content="무엇을 도와드릴까요?")
    ]

for msg in st.session_state.messages:
    st.chat_message(msg.role).write(msg.content)

user_input = st.chat_input()

st.info(user_input)







