
import streamlit as st
from deta import Deta

st.set_page_config(
    page_title="ASIGLEH app",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

deta = Deta(st.secrets["deta_key"])
dbdatpri = deta.Base('test02')
dbdatmod = deta.Base('test01')

#try:
nombreu = st.session_state.nombreu
claveu = st.session_state.claveu
capi = st.session_state.capi
rcapi =st.session_state.rcapi
progresoMod = st.session_state.progresoMod
modx = st.session_state.modx
regt2 = st.session_state.regt2
#ronda =st.session_state.ronda
st.session_state.ronda = 0
# except:
#     st.session_state.claveu = '789'
#     st.session_state.nombreu = 'vilmapic'
#     st.session_state.capi = 'spjcap04'
#     st.session_state.rcapi = 'rspjcap4'
#     st.session_state.progresoMod = 50
#     st.session_state.ronda = 0

st.switch_page('pages/spjfux.py')