import streamlit as st

st.title("광운대학교 퀴즈")

# 객관식 문제
st.header("1. 객관식 문제")
question1 = st.radio(
    "Q1. 광운대학교가 있는 도시는 어디인가요?",
    ("부산시", "대전시", "서울시", "인천시")
)

if question1:
    if question1 == "서울시":
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 정답은 '서울시'입니다.")

# 주관식 문제
st.header("2. 주관식 문제")
answer2 = st.text_input("Q2. 오픈소스 소프트웨어를 가르치는 교수님의 성함은 무엇인가요?")

if answer2:
    if "박규동" in answer2.strip():
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 정답은 '박규동'입니다.")
