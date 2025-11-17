import streamlit as st
import random

st.title("🎲 숫자 추첨기")

# 사용자 입력
a = st.number_input("최소 숫자를 입력하세요", value=1)
b = st.number_input("최대 숫자를 입력하세요", value=100)
num_count = st.number_input("몇 개의 숫자를 뽑을까요?", min_value=1, value=1, step=1)

# 중복 여부 선택
allow_duplicates = st.checkbox("중복 허용", value=False)

# 추첨 버튼
if st.button("숫자 추첨!"):
    if a > b:
        st.error("❌ 최소 숫자가 최대 숫자보다 클 수 없습니다!")
    elif not allow_duplicates and num_count > (b - a + 1):
        st.error("❌ 범위보다 더 많은 숫자를 중복 없이 뽑을 수 없습니다!")
    else:
        if allow_duplicates:
            results = [random.randint(a, b) for _ in range(num_count)]
        else:
            results = random.sample(range(a, b + 1), num_count)
        st.success(f"🎉 추첨 결과: {results}")
