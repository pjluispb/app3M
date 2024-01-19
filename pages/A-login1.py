import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
import time

st.set_page_config(
    page_title="ASIGLEH app",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

deta = Deta(st.secrets["deta_key"])
encprof = deta.Base('test02')

st.header('App3M')
st.markdown("<h4 style='text-align: left; color: grey;'>ASIGLEH</h4>", unsafe_allow_html=True)
st.subheader('Iglesia de Los Hermanos - Venezuela')

st.markdown("<h1 style='text-align: center; color: grey;'>Login</h1>", unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)
with col2:
    with st.form('fregini'):
        st.markdown("<h3 style='text-align: center; color: red;'>Usuario </h2>", unsafe_allow_html=True)
        nombreu = st.text_input(label='nombreu', label_visibility='collapsed')
        st.markdown("<h3 style='text-align: center; color: red;'>Clave </h2>", unsafe_allow_html=True)
        claveu = st.text_input(label='clave', label_visibility='collapsed')
        streg, nom, ced = True, nombreu, claveu
        ingresaReg = st.form_submit_button('Enviar')
        if ingresaReg:
            verifregDB = encprof.fetch({"nombreu":nombreu, "key":claveu})
            #verifregDB.count

            if verifregDB.count==1:
                st.session_state['nombreu'] = nombreu
                st.session_state['claveu'] = verifregDB.items[0]['key']

                st.write(verifregDB.count)
                st.write(verifregDB.items)
                switch_page('interface')

            else:
                st.error('''
                         Error en los datos ingresados.
                         Intente de nuevo''')
