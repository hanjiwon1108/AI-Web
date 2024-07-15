import streamlit as st
title = st.text_input("fall in")
if st.button("Save"):
    if 'title' not in st.session_state :
        st.session_state.title = title