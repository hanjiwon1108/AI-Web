import streamlit as st

name = st.text_input("학번이름 입력")
if st.button("제출"):
    if 'name' not in st.session_state :
        st.session_state.name = name