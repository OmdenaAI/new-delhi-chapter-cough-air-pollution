import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from project_utils.menu import load_menu_html,load_css
from project_utils.front_page import load_home_page_content

PAGE_TITLE="Identifying the Severity of Cough Due to Air Pollution in New Delhi using Audio Analysis and Machine Learning"

st.set_page_config(page_title=PAGE_TITLE, page_icon="🧊",layout="wide",initial_sidebar_state="collapsed")
load_css()
load_menu_html(True)
load_home_page_content()

st.markdown("""<style>[//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]]{margin-left: 50px;}</style>""", unsafe_allow_html=True)
btn=st.button("Click to diagnose the severity of cough!")
if btn:
    switch_page("Cough_Diagonsis")   

