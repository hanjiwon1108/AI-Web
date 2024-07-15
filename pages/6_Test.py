import streamlit as st

st.write('1. 페이스북을 만든 사람의 이름을 출력하시오. (70점)')
answer1 = st.text_input("정답 입력")

st.write('2. 16진수 abcde를 8진수로 고쳤을 때 나오는 결과는? (30점)')

options = ["7777777", "1726354", "2536336", "1231577", "1234567"]
answer2 = st.radio("선택지", options)

if st.button("제출"):
    correct_answer1 = "마크 주커버그"
    correct_answer2 = "2536336"
    
    if 'jumsu' not in st.session_state:
        st.session_state.jumsu = 0

    if answer1 == correct_answer1:
        st.session_state.jumsu += 70
    else:
        st.session_state.jumsu += 0
    
    if answer2 == correct_answer2:
        st.session_state.jumsu += 30
    else:
        st.session_state.jumsu += 0
    
