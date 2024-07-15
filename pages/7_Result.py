import streamlit as st

if st.button("점수 확인"):
    st.write(st.session_state.name, "님의 점수는", st.session_state.jumsu, "점 입니다.")