import streamlit as st

st.set_page_config(page_title="Page Title ")
st.title('Title : Streamlit Test')

def response(input_text):
    """
    # 입력받은 input text 를 그대로 출력
    """
    st.info(input_text)

with st.form('Question'):
    text = st.text_area('질문 내용:', '질문 기본값') #첫 페이지가 실행될 때 보여줄 질문
    submitted = st.form_submit_button('보내기') # 버튼 이름
    response(text)