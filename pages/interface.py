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

verifregDB = dbdatpri.fetch({"nombreu":nombreu, "key":claveu})
if claveu != '919':
    if verifregDB.count>0:
        #verifregDB
        reg = dbdatpri.get(key=claveu)
        # reg
        # st.write(type(reg))
        df0 = pd.DataFrame.from_dict(reg, orient='index')
        # df0 = pd.DataFrame.from_dict(list(reg.items()), columns=['key', 'Values'])
        #df0
        np0 = df0.to_numpy()
        # np0
        listatodf = []
        acum=0
        for i in np0:
            #'Módulo :',i[0][0], '  ejecutar :', i[0][3], '  Status :', i[0][1], '   progreso:', i[0][2]
            #st.write(len(i[0][0]))
            # i, acum, i[0][0], len(i[0][0])
            if (len(i[0][0]))>1:
                try : acum+=int(i[0][2])
                except: acum+=0
                if acum > int(i[0][5]) :
                    status = 'Activo - Editable'
                else: 
                    if i[0][0] != 'Datos Ministeriales' : 
                        status = 'en espera'
                    else:
                        status = 'Activo - Editable'

                diccio = {'Módulo':i[0][0], 'ejecutar':False, 'Status': status, 'progreso': i[0][2], 'puntos': acum, 'Requerido':i[0][5]}
                listatodf.append(diccio)
        #listatodf
        df1 = pd.DataFrame(listatodf)
        #df1
else:
    df1 = pd.DataFrame(
        [
        {"Módulo": "Datos Ministeriales", "ejecutar": False, "Status": 'Activo - Editable', 'progreso':50, 'puntos':50, 'Requerido':0},
        {"Módulo": "Siguiendo las pisadas... - Capítulo 1", "ejecutar": False, "Status": "Activo - Editable", 'progreso':10, 'puntos':60, 'Requerido':30},
        {"Módulo": "Siguiendo las pisadas... - Capítulo 2", "ejecutar": False, "Status": "Activo - Editable", 'progreso':5, 'puntos':60, 'Requerido':70 },
        {"Módulo": "Siguiendo las pisadas... - Capítulo 3", "ejecutar": False, "Status": "Activo - Editable", 'progreso':5, 'puntos':60, 'Requerido':150 },
        {"Módulo": "Siguiendo las pisadas... - Capítulo 4", "ejecutar": False, "Status": "en espera", 'progreso':5, 'puntos':60, 'Requerido':250 },
        {"Módulo": "Siguiendo las pisadas... - Capítulo 5", "ejecutar": False, "Status": "en espera", 'progreso':60, 'puntos':60, 'Requerido':300 },
    ]
    )
#df
edited_df = st.data_editor(
    df1,
    column_config={
        "progreso": st.column_config.ProgressColumn(
            "Progreso",
            help="progreso de la actividad",
            format="%f",
            min_value=0,
            max_value=150,
        ),
    },
    hide_index=True,
    disabled=("Módulo", "Status", "puntos", "Requerido"),
    # num_rows="dynamic",
)

accion = edited_df.loc[edited_df["ejecutar"]]
jsaccion = accion.to_numpy()
swpa = ''
try:
    if jsaccion[0,2]=='en espera':
        st.toast('Aún No puedes acceder a este múdulo')
    elif jsaccion[0,2]=='Activo - Editable':
        st.header('En camino a '+ str(jsaccion[0,0]))
        if jsaccion[0,0]=="Datos Ministeriales": 
            st.toast('vamos a cargar datos ministeriales')
            swpa = 'pages/regdocmin01.py'
        elif jsaccion[0,0]=='Siguiendo las pisadas... - Capítulo 1': 
            st.session_state.capi = 'spjcap01'
            st.session_state.rcapi = 'rspjcap1'
            st.session_state.progresoMod = reg['mod2'][2]
            st.session_state.modx = 'mod2'
            st.session_state.regt2 = reg['mod2']
            swpa = 'pages/spjfu01.py'
        elif jsaccion[0,0]=='Siguiendo las pisadas... - Capítulo 2': 
            st.session_state.capi = 'spjcap02'
            st.session_state.rcapi = 'rspjcap2'
            st.session_state.progresoMod = reg['mod3'][2]
            st.session_state.modx = 'mod3'
            st.session_state.regt2 = reg['mod3']
            swpa = 'pages/spjfu01.py'
        elif jsaccion[0,0]=='Siguiendo las pisadas... - Capítulo 3': 
            st.session_state.capi = 'spjcap03'
            st.session_state.rcapi = 'rspjcap3'
            st.session_state.progresoMod = reg['mod4'][2]
            st.session_state.modx = 'mod4'
            st.session_state.regt2 = reg['mod4']
            swpa = 'pages/spjfu01.py'
        elif jsaccion[0,0]=='Siguiendo las pisadas... - Capítulo 4': 
            st.session_state.capi = 'spjcap04'
            st.session_state.rcapi = 'rspjcap4'
            st.session_state.progresoMod = reg['mod5'][2]
            st.session_state.modx = 'mod5'
            st.session_state.regt2 = reg['mod5']
            swpa = 'pages/spjfu01.py'
except:
    swpa = ''

if swpa != '':
    #switch_page(swpa)
    st.switch_page(swpa)


salir = st.button('Salir')
if salir: switch_page('login')

