import streamlit as st
import random

st.title("🔍 참/거짓 판독기")

# 문장 입력
statement = st.text_input("판독할 문장을 입력")

# 판독 버튼
if st.button("판독"):
    if statement.strip():  # 입력이 비어있지 않을 때
        result = random.choice(["참 ✅", "거짓 ❌"])
        st.success(f"판독 결과: {result}")
    else:
        st.error("문장을 입력해주세요!")
