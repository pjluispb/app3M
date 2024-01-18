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
dbdatpri = deta.Base('test02')
dbdatmod = deta.Base('test01')

def on_change(df):
    # Obtiene los valores de los campos 'ejecutar' y 'Módulo'
    ejecutar = df["ejecutar"]
    modulo = df["Módulo"]

    # Filtra el DataFrame por los valores de 'ejecutar' que cambiaron de False a True
    cambios = df[ejecutar != df.shift(1)["ejecutar"]]

    # Obtiene los valores de 'Módulo' para los cambios
    modulo_cambios = cambios["Módulo"]

    # Muestra los valores de 'Módulo' para los cambios
    if len(modulo_cambios) > 0:
        st.write("Los módulos que cambiaron de estado son:")
        for modulo in modulo_cambios:
            st.write(modulo)

nombreu = st.session_state['nombreu']
claveu = st.session_state['claveu']

st.title('App3M')
st.header('Monitoreo y Mentoreo de Ministros ASIGLEH')
st.subheader('Bienvenido '+nombreu)


df = pd.DataFrame(
    [
       {"Módulo": "Datos Ministeriales", "ejecutar": False, "Status": 'Activo - Editable', 'progreso':50, },
       {"Módulo": "Siguiendo las pisadas... - Capítulo 1", "ejecutar": False, "Status": "Activo - Editable", 'progreso':10, },
       {"Módulo": "Siguiendo las pisadas... - Capítulo 2", "ejecutar": False, "Status": "Activo - Editable", 'progreso':5, },
       {"Módulo": "Siguiendo las pisadas... - Capítulo 3", "ejecutar": False, "Status": "Activo - Editable", 'progreso':5, },
       {"Módulo": "Siguiendo las pisadas... - Capítulo 4", "ejecutar": False, "Status": "En espera", 'progreso':5, },
       {"Módulo": "Siguiendo las pisadas... - Capítulo 5", "ejecutar": False, "Status": "En espera", 'progreso':5, },
   ]
)


edited_df = st.data_editor(
    df,
    column_config={
        "progreso": st.column_config.ProgressColumn(
            "Progreso",
            help="progreso de la actividad",
            format="%f",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
    disabled=("Módulo", "Status"),
    num_rows="dynamic",
)

accion = edited_df.loc[edited_df["ejecutar"]]
jsaccion = accion.to_numpy()
swpa = ''
try:
    if jsaccion[0,2]=='En espera':
        st.toast('Aún No puedes acceder a este múdulo')
    elif jsaccion[0,2]=='Activo - Editable':
        st.header('En camino a '+ str(jsaccion[0,0]))
        if jsaccion[0,0]=="Datos Ministeriales": 
            swpa = 'regdocmin01'
        elif jsaccion[0,0]=='Siguiendo las pisadas... - Capítulo 1': 
            swpa = 'spjcap01'
        elif jsaccion[0,0]=='Siguiendo las pisadas... - Capítulo 2': 
            swpa = 'spjcap02'
        elif jsaccion[0,0]=='Siguiendo las pisadas... - Capítulo 3': 
            swpa = 'spjcap03'
except:
    swpa = ''

if swpa != '':
    switch_page(swpa)



