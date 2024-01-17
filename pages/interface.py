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


st.title('App3M')
st.header('Monitoreo y Mentoreo de Ministros ASIGLEH')
st.subheader('Bienvenido')


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
    # jsaccion
    # jsaccion[0,0], ' <---> ',jsaccion[0,2]
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
    #pass

if swpa != '':
    switch_page(swpa)


# st.write(accion.Módulo)
#valor = accion.loc[0,'Módulo']
#st.write(valor)
#st.write(type(accion.Módulo))
'***'
'***'

# # Crear el DataFrame
# df2 = pd.DataFrame(
#     [
#        {"<link>Módulo</link>": "Datos Ministeriales", "ejecutar": False, "Status": 'Activo - Editable', 'progreso':50, },
#        {"<link>Módulo</link>": "Siguiendo sus pasos - Capítulo 1", "ejecutar": False, "Status": "Activo - Editable", 'progreso':10, },
#        {"<link>Módulo</link>": "Siguiendo sus pasos - Capítulo 2", "ejecutar": False, "Status": "En espera", 'progreso':5, },
#    ]
# )

# # Mostrar el DataFrame en Streamlit
# st.table(df2)

# # Capturar el evento de clic en una celda
# if st.session_state.clicked_row is not None:
#     modulo_seleccionado = df2.loc[st.session_state.clicked_row, "<link>Módulo</link>"]
#     st.write(f"Has seleccionado el módulo: {modulo_seleccionado}")

# # Habilitar el clic en la tabla
# st.write("Haz clic en una celda para seleccionar el módulo.")
# st.write(df.style.set_table_attributes('class="dataframe"').format(
#     {'ejecutar': lambda x: 'cursor: pointer'}), unsafe_allow_html=True)

