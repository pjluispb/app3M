import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
import time

st.set_page_config(
    page_title="APP3M",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    )

def abrerecursosdeta():
    deta = Deta(st.secrets["deta_key"])
    #encuasigleh = deta.Base('asiglehpastores')
    photos = deta.Drive(name='asiglehphotos')
    bdtest01 = deta.Base('test01')
    bdtest02 = deta.Base('test02')
    photosys = deta.Drive(name='modphotos')
    return(bdtest01, bdtest02, photos, photosys)

bdtest01, bdtest02, photos, photosys = abrerecursosdeta()

st.header('App3M')
st.subheader('Iglesia de Los Hermanos - Venezuela')

st.markdown("<h1 style='text-align: center; color: grey;'>Registro Inicial</h1>", unsafe_allow_html=True)
ph1 = st.empty()
col1, col2 = ph1.columns(2)
with ph1:
    col1.markdown("<h6 style='text-align: center; color: red;'>Ingresa el código de invitación: </h6>", unsafe_allow_html=True)
    with col2:
        vercodinv = st.text_input('Ingrese el código de invitación', label_visibility='collapsed')
vercodinv_out=vercodinv
if vercodinv_out in ['app3M-Merida', 'test102023', 'test2024', 'Asigleh2024']:
    ph1.empty()
    with st.form('fregini'):
        nombreu = st.text_input('Ingrese un nombre de usuario')
        claveu = st.text_input('Ingrese su clave')
        pastorOlider = st.radio(label='Rol', options=['Pastor', 'Líder'])
        streg, nom, ced = True, nombreu, claveu
        ingresaReg = st.form_submit_button('Enviar')
        if ingresaReg:
            st.toast('buscando')
            regt1 = bdtest01.get(key=claveu)
            regt2 = bdtest02.get(key=claveu)
            #regt1
            #regt2
            if regt1==None and regt2==None:
                st.toast('Excelente!!!')
                #st.toast(' Se creara un nuevo usuario ')
                st.toast(' Bienvenido ')
                bdtest01.put(data={'nombreu':nombreu}, key= claveu)
                bdtest02.put(data={ "mod1": ["Datos Ministeriales", "Activo - Editable", "0", "editar", "0", "0"],"mod2": ["Siguiendo las pisadas... - Capítulo 1", "en espera", "0", "editar", "0", "30" ], "mod3": ["Siguiendo las pisadas... - Capítulo 2", "en espera", "0", "editar", "0", "70" ], "mod4": ["Siguiendo las pisadas... - Capítulo 3", "en espera", "0", "editar", "0", "150" ],"mod5": ["Siguiendo las pisadas... - Capítulo 4", "en espera", "0", "editar", "0", "250" ],"mod6": ["Siguiendo las pisadas... - Capítulo 5", "en espera", "0", "bloqueado", "0", "300" ],"nombreu": nombreu}, key= claveu,)
                st.switch_page('pages/A-login1.py')
                #dbtest.put(data={k:nnnv}, key=rkey)
                #fielde = ["Apellidos:"+ "","Direccion:"+ "","Edad:0","Edo_Civil:"+ "","Emails: []",]
            else:
                st.toast('Alguno de los datos ingresados ya está registrado')
                st.toast('INTENTE con otros datos')
else:
    st.toast('Código inválido')     
    st.error('Código inválido. Ingrese nuevamente el código de invitación')   
    
