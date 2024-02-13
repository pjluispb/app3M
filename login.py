import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="ASIGLEH app",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

deta = Deta(st.secrets["deta_key"])
encprof = deta.Base('asiglehpastores')

st.header('App3M')
st.markdown("<h4 style='text-align: left; color: grey;'>ASIGLEH</h4>", unsafe_allow_html=True)
st.subheader('Monitoreo y Mentoreo a Ministros y Líderes')

selected3 = option_menu(None, ["", "Ingresar", "Registro"], 
    icons=['hourglass','door-open-fill', 'person-rolodex'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#4346dc"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#4fdc43"},
        "nav-link-selected": {"background-color": "green"},
    }
)
selected3
if selected3=='Registro':
    # st.toast('Módulo en Construcción')
    st.switch_page('pages/A-regApp3m.py')
elif selected3=='Ingresar':
    # switch_page('A-login1')
    st.switch_page('pages/A-login1.py')

