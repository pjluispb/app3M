
import streamlit as st
# from PIL import Image
# import numpy as np
from deta import Deta
# import random
# import io
# import time
# from streamlit_extras.switch_page_button import switch_page

deta = Deta(st.secrets.deta_key)
photos = deta.Drive(name='asiglehphotos')

namepic = st.session_state['namepic']

img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None: 
    st.write(namepic)
    with st.spinner('Espere un momento...se está guardando la foto'):
        bytes_data = img_file_buffer.getvalue()
        photos.put(namepic, bytes_data)
        st.session_state['namepic'] = namepic
    st.success('listo!!!')
    st.switch_page('pages/regdocmin01.py')


