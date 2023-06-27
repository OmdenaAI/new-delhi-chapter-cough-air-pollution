import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from menu import load_menu_html,load_css
from front_page import load_home_page_content

PAGE_TITLE="Identifying the Severity of Cough Due to Air Pollution in New Delhi using Audio Analysis and Machine Learning"

st.set_page_config(page_title=PAGE_TITLE, page_icon="🧊",layout="wide",initial_sidebar_state="collapsed")
load_css()
load_menu_html(False)
load_home_page_content()

st.markdown("# Diagonose the test",unsafe_allow_html=True)
btn=st.button("Click to Diagnose!")
if btn:
    switch_page("Detect_Cough")
