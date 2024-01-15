
import streamlit as st
import pandas as pd
import random
from deta import Deta
from streamlit_extras.switch_page_button import switch_page
import datetime


def abrerecursosdeta():
    deta = Deta(st.secrets["deta_key"])
    dbtest = deta.Base('test01')
    photos = deta.Drive(name='asiglehphotos')
    photosys = deta.Drive(name='modphotos')
    return(dbtest, photos, photosys)

def newElemnt(datTexto, num, cond):  
    # newElemnt(['telefono#', 'texto', 'Teléfono', clavetel, '-'], conttel, 'add')
    #newElemnt([nombrefamField, 'texto', etinomfam, clavenomfam, '-'], contrelfam, 'add')
    tik = datTexto[0]+str(num)
    if datTexto[1]=='texto':
        param = st.text_input(label=datTexto[2], value=datTexto[4], key='keyt-'+tik+datTexto[3])
        if cond == 'add': 
            if param not in ['', '-', None]:
                #newvalea.append({tik:param})
                newvalea.append(tik+' --- '+param)
                st.session_state['newvalea'] = newvalea
        else:
            if param not in ['', '-', None]:
                #updvalea.append({tik:param})
                updvalea.append(tik + ' -:- ' + param)
                st.session_state['upvalea'] = updvalea

    if datTexto[1]=='textarea':
        param = st.text_area(label=datTexto[2], value=datTexto[3], key='keyta-'+tik)
        if cond == 'add':
            if param not in ['', '-', None]:
                #newvalea.append({tik:param})
                newvalea.append(tik+' --- '+param)
                st.session_state['newvalea'] = newvalea
                #st.toast(newvalea)
    if datTexto[1]=='radio':
        param1 = st.radio(label=datTexto[2], options=datTexto[3], index=0, horizontal=True, key='keyr-'+tik)
        
        if param1=='Otra': param2 = st.text_input(datTexto[4])
        else: param2 = param1
        param = param2
        #newvalea.append({tik:param})
        newvalea.append(tik+' --- '+param)
        #st.toast(newvalea)
    if datTexto[1]=='radio + texto':
        param1 = st.radio(label=datTexto[2], options=datTexto[3], index=3, horizontal=True, key='keyrt-'+tik)
        
        if param1=='Otra': param2 = st.text_input(datTexto[4])
        else: param2 = param1
        if param1 != '-' : idRedS = st.text_input(label='Ingresa tu ID(nombre, teléfono, etc) en la red social')
        else: idRedS='-'
        param = [param2, idRedS]
        #st.write('param = ', param)
        #st.stop()
        if param[1] not in ['-','',None]: newvalea.append({tik:param})
        #st.toast(newvalea)
    if datTexto[1]=='select slider':
        param = st.select_slider(label=datTexto[2], key='keyss-'+tik, options=datTexto[3])
        # newvalea.append({tik:param})
        newvalea.append(tik+' --- '+param)
        #st.toast(newvalea)
    if datTexto[1]=='range slider':
        param = st.slider(label=datTexto[2], key='keyrs-'+tik, min_value=datTexto[3], max_value=datTexto[4], value=datTexto[5])
        #newvalea.append({tik:param})
        newvalea.append(tik+' --- '+str(param))
    if datTexto[1]=='doble radio':
        #newElemnt(['relfam'+'-rel#', 'doble radio', 'relación', tablaopc,  claverelfam, valores[string][1]], contrelfam, 'show')
        param1 = st.radio(label=datTexto[2], options=datTexto[3], index=0, horizontal=True, key='keyr-'+tik)
        #st.toast(newvalea)
    #st.toast('newvalea = '+str(newvalea))
    #valrelfamTipo = newElemnt(['relfam'+'tipo#', 'valortxt', 'valor', valrelfamRel],contrelfam,'add')
    if datTexto[1]=='valortxt':
        newvalea.append({tik:datTexto[3][0]})
        st.session_state['newvalea'] = newvalea
    return(newvalea)
    
def ordenalip(lip, parame):
    lp=[]
    for it in lip:
        pa=it[:it.find(':')].strip()
        pb=it[it.find(':')+1:].strip()
        pind=parame.index(pa)
        lp.append((pind,pa,pb))
    lps = sorted(lp, key=lambda p:p[0])
    lpout=[]
    for it in lps:
        lpout.append(it[1]+' : '+it[2])
    return(lpout)

def tomaphoto2(nombrepic):
    st.session_state['namepic'] = nombrepic
    st.toast('ejecutando tomaphoto2 '+str(nombrepic))
    switch_page('fototest2')
    return

dbtest, photos, photosys = abrerecursosdeta()


rkey = st.session_state['claveu']
# rkey = '789'
#rkey = '963'
#rkey = '111'
reg = dbtest.get(key=rkey)
nombreu = reg['nombreu']
#nombreu = st.session_state['nombreu']
#st.caption('hola-1')
newvalea, updvalea = [], []

st.write(reg)
st.markdown(':green[ $ \\bold {Hola \,\,\,' + reg['nombreu'] + '}$]')

colt1, colt2 = st.columns((1,3))
imagenCer = photosys.get('testigo2.png')
content = imagenCer.read()
colt1.image(content)
colt2.subheader('Bienvenido al sistema de Apoyo, Monitoreo y Mentoreo de ASIGLEH (Asociación de  Iglesias de Los Hermanos Venezuela)' )
st.write('Estás en el módulo de registro ministerial')
st.write('')
instrucciones = st.button('Instrucciones')

st.write('***')
st.write('')
imagenCer = photosys.get('datper02.png')
#st.stop()
content = imagenCer.read()
st.image(content)

with st.expander(':orange[$\Large Datos\, Personales$]'):
    st.info('ℹ️ 🙂 Aquí solicitamos información básica sobre tu persona, los medios a través de los cuáles nos podemos comunicar contigo, tus redes sociales e información acerca de tu familia más cercana ')
    valores = reg
    try:    vnombre = valores['Nombres']
    except: vnombre = '-'
    try:    vapellido = valores['Apellidos']
    except: vapellido = '-'
    try:    vnac = valores['Nacionalidad']
    except: vnac = '-'
    try:    vedocivil = valores['Edo_Civil']
    except: vedocivil = ''
    try:    vedad = valores['Edad']
    except: vedad = 0
    try:    vdireccion = valores['Direccion']
    except: vdireccion = '-'
    try:    vfotoper = valores['fotopersonal']
    except: vfotoper = '-'
    try:    vfotoID = valores['fotoID']
    except: vfotoID = '-'
    if vedocivil==None: vedocivil=''

    nombre = st.text_input(label=':blue[$ \\bold{Nombres 🚦}$]', value=vnombre)
    apellido = st.text_input(label=':blue[$ \\bold{Apellidos    🚦}$]', value=vapellido)
    nacionalidad = st.text_input(label=':blue[$ \\bold{Nacionalidad}$]', value=vnac)
    indEdo_Civil = ['', 'Soltero','Casado','Viudo','Otro'].index(vedocivil)
    Edo_Civil = st.selectbox(label=':blue[$ \\bold{Estado \,\, Civil}$]',options=['', 'Soltero','Casado','Viudo','Otro'], index=indEdo_Civil)
    #fecnac = st.date_input('Fecha de nacimiento',min_value=datetime.date(1940,1,1))
    edad = st.slider(label=':blue[$ \\bold{Edad}$]', value=vedad)
    direccion = st.text_input(label=':blue[$ \\bold{Dirección\,\, de\,\, habitación}$]', value=vdireccion)
    valif = random.randint(1,1000)
    contF = 1
    st.subheader(':green[$\small 👤Foto \,\,Personal$]')
    try:
        namepic = st.session_state['namepic']
        'namepic = ', namepic
    except:
        nombreuF = '101' + '-' + rkey
        seccionF = 'fotpersonal'
        namepic = 'AFotPer'+nombreuF + '-' + seccionF + '-' + str(valif) + '-' + str(contF) + '.png'
    if vfotoper=='-':
        chefot = st.checkbox(label='Foto personal de frente')
        if chefot:
            if nombre == '-' or apellido == '-':
                st.write('Debe ingresar nombre y  apellido antes de tomar la foto personal')
                st.toast('Debe ingresar nombre y apellido para poder tomar la foto', icon='🚨')
            else:
                #'namepic = ', namepic
                img_file_buffer = st.camera_input("Tomar foto")
                if img_file_buffer is not None: 
                    vali = random.randint(505,600)
                    npic = namepic+'-'+str(vali)+'.png'
                    npic = namepic
                    st.toast(npic)
                    st.write('npic = ',npic)

                    with st.spinner('Espere un momento...se está guardando la foto'):
                        bytes_data = img_file_buffer.getvalue()
                        photosys.put(npic, bytes_data)
                    st.success('listo!!!')
                    #st.stop()
                    valores['fotopersonal']=npic
                    st.session_state['fotopersonal'] = npic
                    dbtest.update({'Nombres':nombre, 'Apellidos':apellido, 'Nacionalidad':nacionalidad, 'Edo_Civil':Edo_Civil, 'Edad':edad,'Direccion':direccion,'fotopersonal':namepic}, key=rkey)
                    st.session_state['clave'] = rkey
                    switch_page('depaso1')
    else:
        #'vfotoper = ', vfotoper
        # st.subheader(':green[$\small Foto Personal$]')
        imagenCer = photosys.get(vfotoper)
        content = imagenCer.read()
        st.image(content)
        st.caption(vfotoper)
 
        cheactfotoper = st.checkbox(label='Actualizar foto personal')
        if cheactfotoper:
            img_file_buffer = st.camera_input("Tamar foto")
            if img_file_buffer is not None: 
                npic = valores['fotopersonal']
                with st.spinner('Espere un momento...se está guardando la foto'):
                    bytes_data = img_file_buffer.getvalue()
                    photosys.put(npic, bytes_data)
                st.success('listo!!!')
                # st.rerun()
                st.session_state['clave'] = rkey
                switch_page('depaso1')
        #st.write('***')
    # st.write('')
    st.subheader(':green[$\small 🆔Foto\,\, de\,\, ID$]')

    try:
        idpic = st.session_state['idpic']
        'idpic = ', idpic
    except:
        nombreuF = '101' + '-' + rkey
        seccionF = 'fotoID'
        idpic = 'AFotID'+nombreuF + '-' + seccionF + '-' + str(valif) + '-' + str(contF) + '.png'
    if vfotoID=='-':
        chefotID = st.checkbox(label='Foto de documento de Identidad (Cédula u otro)')
        if chefotID:
            if nombre == '-' or apellido == '-':
                st.write('Debe ingresar nombre y  apellido antes de tomar la foto personal')
                st.toast('Debe ingresar nombre y apellido para poder tomar la foto', icon='🚨')
            else:
                'idpic = ', idpic
                img_file_buffer = st.camera_input("Tomar foto")
                if img_file_buffer is not None: 
                    vali = random.randint(505,600)
                    npicid = idpic+'-'+str(vali)+'.png'
                    npicid = idpic
                    st.toast(npicid)
                    st.write('npicid = ',npicid)

                    with st.spinner('Espere un momento...se está guardando la foto'):
                        bytes_data = img_file_buffer.getvalue()
                        photosys.put(npicid, bytes_data)
                    st.success('listo!!!')
                    #st.stop()
                    valores['fotoID']=npicid
                    st.session_state['fotoID'] = npicid
                    dbtest.update({'Nombres':nombre, 'Apellidos':apellido, 'Nacionalidad':nacionalidad, 'Edo_Civil':Edo_Civil, 'Edad':edad,'Direccion':direccion, 'fotoID':idpic}, key=rkey)
                    st.session_state['clave'] = rkey
                    switch_page('depaso1')
    else:
        #vfotoper
        #st.subheader(':green[$\small Foto Personal$]')
        imagenCer = photosys.get(vfotoID)
        content = imagenCer.read()
        st.image(content)
        st.caption(vfotoper)
 
        cheactfotoID = st.checkbox(label='Actualizar foto ID')
        if cheactfotoID:
            img_file_buffer = st.camera_input("Tamar foto")
            if img_file_buffer is not None: 
                npic = valores['fotoID']
                with st.spinner('Espere un momento...se está guardando la foto'):
                    bytes_data = img_file_buffer.getvalue()
                    photosys.put(npic, bytes_data)
                st.success('listo!!!')
                # st.rerun()
                st.session_state['clave'] = rkey
                switch_page('depaso1')
        #st.write('***')
    st.write('')

    #---------------------------------------------------------------------------
    st.subheader(':green[$\small Comunicaciones$]')
    # muestra telefonos

    st.write(':blue[$ \\bold{Teléfonos📞}$]')
    try:
        dftel = pd.DataFrame(valores['Teléfonos'], columns=['Número Telefónico', 'Tipo de uso'])
    except:
        dftel = pd.DataFrame([{'Número':'123', 'tipo':'-'}, ])
    edited_dftel = st.data_editor(dftel, column_config=
                    {'Número':st.column_config.TextColumn('Número Telefónico', width='medium', help='Ingrese # telefónico', required=True, validate='[0-1]'),
                     'tipo':st.column_config.SelectboxColumn('Tipo de uso', help='Seleccione el tipo de uso del teléfono', width='small', options=['personal', 'familiar', 'de trabajo'], required=True)
                                    },  num_rows='dynamic')
    #st.write('***')
    st.write(':blue[$ \\bold{Emails (Correos\,\, electrónicos)📧}$]')
    try:
        dfemails = pd.DataFrame(valores['Emails'], columns=['Email'])
    except:
        dfemails = pd.DataFrame([{'Email (Correo Electrónico)':'nombre@yuhu.com',}, ])
    
    edited_dfemails = st.data_editor(dfemails, column_config=
                        {'Email(Correo electrónico)':st.column_config.TextColumn('Email(correo electrónico)',  width='large', help='Ingresar email o correo electrónico', required=True, validate='[a-z]')
                          }, num_rows='dynamic', disabled='False' )
    #st.write('***')
    st.write(':blue[$ \\bold{Redes Sociales🕸}$]')
    try:
        dfredes = pd.DataFrame(valores['RedesSociales'], columns=['Red Social', 'Perfil/Identificador', 'Uso'])
    except:
        dfredes = pd.DataFrame([{'Red Social':'Facebook', 'Perfil/Identificador':'-', 'Uso':'-'}, ])
    
    edited_dfredes = st.data_editor(dfredes, column_config=
                    {'Red Social':st.column_config.TextColumn('Red Social',
                    width='small', help='Nombre de la Red Social', required=True, validate='[a-z]'), 
                    'Perfil/Identificador':st.column_config.TextColumn('Perfil/Identificador', width='medium', help='Ingresa tu perfil o Id en dicha red social', required=True,),
                    'Uso':st.column_config.SelectboxColumn('Uso de la red', help='Selecciona de que manera usas dicha red social', width='medium', options=['personal', 'de trabajo o negocio'], required=True)},
                    num_rows='dynamic')
    #
    #---------------------------------------------------------------------------
    st.subheader(':green[$\small Relaciones\, Familiares$]')

    #st.markdown(':grey[$\\normalsize Relaciones\, Familiares\, Consanguineas$]')
    st.write(':blue[$ \\bold{Consanguineas}$]')
    st.write(':grey[$ \\scriptsize Abarcan: Padres, Hijos, Hermanos, Tíos, Primos, Abuelos\, \\newline y\, Nietos$]')
    try:
        dfrfcon = pd.DataFrame(valores['RelFamCon'], columns=['Nombre', 'tipo de relación'])
    except:
        dfrfcon = pd.DataFrame([{'Nombre':'-', 'tipo de relación':'-'}, ])
    
    edited_dfrfcon = st.data_editor(dfrfcon, column_config=
                    {'Nombre':st.column_config.TextColumn('Nombre', width='medium', help='Ingrese nombre de familiar', required=True, validate='[a-z]'),
                     'tipo':st.column_config.SelectboxColumn('Tipo de relción', help='Seleccione el tipo de relación familiar consanguinea', width='medium', options=['Padres', 'Hijos', 'Hermanos', 'Tíos', 'Primos', 'Abuelos', 'nieto'], required=True)  },  num_rows='dynamic')

    st.write(':blue[$ \\bold{Políticas}$]')
    st.markdown(':grey[$ \\scriptsize Abarcan: Cónyuges,Suegros,Yernos,Nueras \,y\, Cuñados $]')
    try:
        dfrfpol = pd.DataFrame(valores['RelFamPol'], columns=['Nombre', 'tipo de relación'])
    except:
        dfrfpol = pd.DataFrame([{'Nombre':'-', 'tipo de relación':'-'}, ])

    
    edited_dfrfpol = st.data_editor(dfrfpol, column_config=
                    {'Nombre':st.column_config.TextColumn('Nombre', width='medium', help='Ingrese nombre de familiar', required=True, validate='[a-z]'),
                     'tipo de relación':st.column_config.SelectboxColumn('Tipo de relación', help='Seleccione el tipo de relación familiar consanguinea', width='medium', options=['Cónyuges','Suegros','Yernos','Nueras', 'Cuñados'], required=True)  },  num_rows='dynamic')

    st.write(':blue[$ \\bold{De\,\, Adopción}$]')
    st.markdown(':grey[$ \\scriptsize Abarcan: Padres,Hermanos\, e\, Hijos $]')
    try:
        dfrdadop = pd.DataFrame(valores['RelFamAdop'], columns=['Nombre', 'tipo de relación'])
    except:
        dfrdadop = pd.DataFrame([{'Nombre':'-', 'tipo de relación':'-'}, ])
    
    edited_dfrdadop = st.data_editor(dfrdadop, column_config=
                    {'Nombre':st.column_config.TextColumn('Nombre', width='medium', help='Ingrese nombre de familiar', required=True, validate='[a-z]'),
                     'tipo de relación':st.column_config.SelectboxColumn('Tipo de relación', help='Seleccione el tipo de relación familiar consanguinea', width='medium', options=['Padre adoptado','Hermano de adopción','Hijo adoptado'], required=True)  },  num_rows='dynamic')
    

    st.write(':blue[$ \\bold{De\,\, Crianza}$]')
    st.markdown(':grey[$ \\scriptsize Abarcan: Padres,Hermanos\, e\, Hijos $]')
    try:
        dfrdcrian = pd.DataFrame(valores['RelFamCrian'], columns=['Nombre', 'tipo de relación'])
    except:
        dfrdcrian = pd.DataFrame([{'Nombre':'-', 'tipo de relación':'-'}, ])
    
    edited_dfrdcrian = st.data_editor(dfrdcrian, column_config=
                    {'Nombre':st.column_config.TextColumn('Nombre', width='medium', help='Ingrese nombre de familiar de crianza', required=True, validate='[a-z]'),
                     'tipo de relación':st.column_config.SelectboxColumn('Tipo de relación', help='Seleccione el tipo de relación familiar de grianza', width='medium', options=['Padre de crianza','Hermano de crianza','Hijo de crianza'], required=True)  },  num_rows='dynamic')
    

#     # btn = st.button(label='Guardar')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btndatper', use_container_width=True)
    if btn:
        try:
            st.write('se guarda como:',st.session_state['newvalea'])
        except:
            st.write('error')


        ltel = edited_dftel.values.tolist()
        lemail = edited_dfemails.values.tolist()
        lredess = edited_dfredes.values.tolist()
        lrfcon = edited_dfrfcon.values.tolist()
        lrfpol = edited_dfrfpol.values.tolist()
        lrfdadop = edited_dfrdadop.values.tolist()
        lrfdcrian = edited_dfrdcrian.values.tolist()

        
        newregistro = {'Nombres': nombre, 'Apellidos':apellido, 'Nacionalidad': nacionalidad,  'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad, 'Teléfonos': ltel, 'Emails': lemail, 'RedesSociales': lredess, 'RelFamCon': lrfcon, 'RelFamPol': lrfpol, 'RelFamAdop': lrfdadop, 'RelFamCrian': lrfdcrian}

        st.write('***')
        st.write(newregistro)
        #st.stop()
        dbtest.update(updates=newregistro, key=rkey)
        #contrelfam
        #st.stop()

        st.session_state['clave'] = rkey
        switch_page('depaso1')

    
    st.write('***')
   

st.write('')
st.write('***')
st.write('')
imagenCer = photosys.get('iglesia2.png')
#st.stop()
content = imagenCer.read()
st.image(content)



with st.expander(':orange[$ \large Ministerios/iglesia\, que\, preside\, ó\\newline participa\, actualmente $]'):
    st.info('ℹ️ 🙂 Datos acerca de la iglesia y/o ministerios que presides actualmente. Por ejemplo eres el pastor Asociado de la iglesia de La Pradera y el tesorero de la confraternidad de pastores de La Montaña. ')
    valores = reg
    conIgleMin = 0
    listiglemin = []
    igleminval = {}

    nombreu, clave = reg['nombreu'], reg['key']
    for k,v in reg.items():
        if 'IgleMin#' in k:
            #k, v
            conIgleMin = k.split('#')[1]
            claveIgleMin = 'ParMinHoy#'+str(conIgleMin)+' : '
            st.markdown('#### 📌Registro #:  '+str(conIgleMin))

            conIgleMin= int(conIgleMin)

            claveiglemin = 'iglemin-'+str(conIgleMin)

            valigleminNom = st.text_input(label=':blue[$ \\bold{Nombre}  $]', value=v[0].split(':')[1], key=claveiglemin+'nombre')
            valigleminDir = st.text_input(label=':blue[$ \\bold{Dirección}  $]', value=v[1].split(':')[1], key=claveiglemin+'direccion')
            valigleminNiv =  st.text_input(label=':blue[$ \\bold{Nivel \, Ministerial}  $]', value=v[2].split(':')[1], key=claveiglemin+'nivmin')
            valigleminDes = st.text_area(label=':blue[$ \\bold{Descripción}  $]', value = v[3].split(':')[1], key=claveiglemin+'desc')
            #v
            st.write('***')


    conIgleMin+=1

    st.write('')
    st.markdown('## ➕Nuevo Registro :  📝')

    nombreField1 = 'nombreIgleMin#'
    etinomfam1 = 'Nombre del Ministerio / Iglesia que preside actualmente'
    clavetxt = 'im1'
    valnewNombreField1 = newElemnt([nombreField1, 'texto', etinomfam1, clavetxt, '-'], conIgleMin, 'add')

    direccionField2 = 'direccionIgleMin#'
    etinomfam2 = 'Dirección de la Iglesia / Ministerio'
    clavedir = 'dir1'
    valnewDireccionField2 = newElemnt([direccionField2, 'texto', etinomfam2, clavedir, '-'], conIgleMin, 'add')

    nivelLiderField = 'nivelLiderIgleMin#'
    opcionesradio = ['-', 'Pastor principal', 'Líder', 'Asociado', 'Miembro', 'Otro']
    Etiqueta1 = 'Nivel Ministerial ó de Liderazgo (Cargo)'
    Etiqueta2 = 'Label o etiqueta secundaria'
    valnewNivelLider = newElemnt([nivelLiderField, 'radio', Etiqueta1, opcionesradio, Etiqueta2], conIgleMin, 'add') 

    describeIgleMinField = 'descripcionIgleMin#'
    etidescribeIgleMin = 'Breve descripción de la Iglesia / Ministerio que preside'
    valor = '-'
    valnewdescribeIgleMinField = newElemnt([describeIgleMinField, 'textarea', etidescribeIgleMin, valor], conIgleMin, 'add')

    # btn = st.button(label='Guardar', key='btn-iglemin201')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btn-iglemin201', use_container_width=True)
    if btn:
        #st.write('se guarda ')
        #st.write(st.session_state)
        st.write('***')
        st.write('conIgleMin = ', conIgleMin)
        nv=[]
        for conIgleMinS in range(1,int(conIgleMin)):
            'conParMinHoyS = ', conIgleMin
            k = 'ParMinHoy#'+str(conIgleMinS)
            v = []
            for elemento in st.session_state:
                if  elemento.startswith('ParMinHoy#'+str(conIgleMinS)):
                    #elemento, ' : ', st.session_state[elemento]
                    f2 = elemento.find(':')            
                    v.append(elemento[f2+1:] + ':' + str(st.session_state[elemento]))
            nv.append({k:v})
            st.write('***')
        #'nv0 = ', nv
        #st.stop()
        st.write('***')
        k='IgleMin#'+str(conIgleMin)
        v=[]
        for elemento in newvalea:   
            #elemento     
            if 'IgleMin#' in elemento:
                #'ele con IgleMin : ', elemento
                ele2 = elemento.replace(' --- ',' : ')
                ele3 = ele2.replace('-'+k,'')
                #ele3
                v.append(ele3)
        # v.append(k+'foto:'+st.session_state[k+'foto'])
        #'v = ', v
        nv.append({k:v})
        #'nv = ', nv
        #st.write(len(nv))
        for con in range(0, len(nv)):
            st.write('con = ', con)
            nnnv = ['No', 'Di', 'Ni', 'De']
            for k,v in nv[con].items():
                for ele in v:
                    # ele, '  ---  ', ele.split(':')
                    if 'nombreIgleMin' in ele.split(':')[0] :
                        nnnv[0]='Iglesia/Ministerio : '+str(ele[ele.find(':')+1: ]).lstrip()
                    elif 'direccionIgleMin'  in ele.split(':')[0]: 
                        nnnv[1]='Dirección de Iglesia/Ministerio : '+str(ele[ele.find(':')+1: ]).lstrip()
                    elif 'nivelLiderIgleMin' in ele.split(':')[0]: 
                        nnnv[2]='Nivel de participación/liderazgo : '+str(ele[ele.find(':')+1: ]).lstrip()
                    elif 'descripcionIgleMin' in ele.split(':')[0]: 
                        nnnv[3]='Descripción de la Iglesia/Ministerio que preside : '+str(ele[ele.find(':')+1: ]).lstrip()
                #st.write(k, '--> ', nnnv)
                registromin = {k:nnnv}
                'registromin = ', registromin
                
                actualiza = True
                len(registromin[k][0]), len(registromin[k][1]), len(registromin[k][2])
                if len(registromin[k][0])<10:
                    actualiza = False
                    st.toast('Campo nombre de Iglesia/Ministerio no puede quedar vacío')
                if len(registromin[k][3])<10:
                    actualiza = False
                    st.toast('Debe dar una breve Descripción de las principales tareas que realiza en Iglesia/Ministerio')
                actualiza
                
                if actualiza:
                    dbtest.update(registromin, key= rkey)
                    #st.stop()
        st.session_state['clave']=rkey
        switch_page('depaso1')       
        st.write('===================')
        

    
    st.write('***')


st.write('')
st.write('***')
st.write('')
imagenCer = photosys.get('testigo2.png')
#st.stop()
content = imagenCer.read()
st.image(content)

with st.expander(':orange[$\Large Testimonio $]'):
    st.info('ℹ️ 🙂Por favor comparte tu testimonio de salvación y llamado al ministerio ')
    try:
        v = reg['testimonio']
    except:
        v = []
    #v
    try:
        fec_conversion = st.date_input(label=':blue[$ Fecha \,de \, \\bold{Conversión}  $]',  min_value=datetime.date(1940,1,1), format='DD/MM/YYYY', value=datetime.datetime.strptime(v[0][17:], '%d/%m/%Y'))
    except:
        fec_conversion = st.date_input(label=':blue[$ Fecha \,de \, \\bold{Conversión}  $]',  min_value=datetime.date(1940,1,1), format='DD/MM/YYYY')
    try:
        fec_bautismo_agua = st.date_input(':blue[$ Fecha \, de\, Bautismo \, en\, agua  $]', min_value=datetime.date(1940,1,1), format='DD/MM/YYYY', value=datetime.datetime.strptime(v[1][24:], '%d/%m/%Y'))
    except:
        fec_bautismo_agua = st.date_input(':blue[$ Fecha \, de\, Bautismo \, en\, agua  $]', min_value=datetime.date(1940,1,1), format='DD/MM/YYYY')
    try:
        fec_bautismo_Espiritu = st.date_input(':blue[$ Fecha\, de\, Bautismo\, en\, \\newline el\, \\bold{Espiritu\, Santo}  $]',  min_value=datetime.date(1940,1,1), format='DD/MM/YYYY', value=datetime.datetime.strptime(v[2][27:], '%d/%m/%Y'))
    except:
        fec_bautismo_Espiritu = st.date_input(':blue[$ Fecha\, de\, Bautismo\, en\, \\newline el\, \\bold{Espiritu\, Santo}  $]',  min_value=datetime.date(1940,1,1), format='DD/MM/YYYY')
    try:
        testimonio = st.text_area(label=':blue[$ Compártenos\, tu\, testimonio\, de\, \\bold{salvación}  $]', value=v[3][25:])
    except:
        testimonio = st.text_area(label=':blue[$ Compártenos\, tu\, testimonio\, de\, \\bold{salvación}  $]')
    try:
        llamado = st.text_area(label=':blue[$ Compártenos\, tu\, testimonio\, acerca\, de\, tu\\newline \\bold{llamado\, ministerial.\,} \\newline \\scriptsize  ¿Cómo,\, cuándo\, y\, dónde\,  inició\, su\, ministerio? $]', value=v[4][36:])
    except:
        llamado = st.text_area(label=':blue[$ Compártenos\, tu\, testimonio\, acerca\, de\, tu\\newline \\bold{llamado\, ministerial.\,} \\newline \\scriptsize  ¿Cómo,\, cuándo\, y\, dónde\,  inició\, su\, ministerio? $]')
    st.write('---')
    guarda06 = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btntestimonio', use_container_width=True)
    if guarda06:
        st.write('---guardando Datos sobre su testimonio---')
        #st.write(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio, llamado)
        testimonio = ['fec conversión : '+fec_conversion.strftime('%d/%m/%Y'), 'fec bautismo en agua : '+fec_bautismo_agua.strftime('%d/%m/%Y'), 'fec bautismo en Espiritu : '+fec_bautismo_Espiritu.strftime('%d/%m/%Y'), 'testimonio de salvación : '+testimonio, 'testimonio del llamado ministerial : '+llamado]
        testimonio
        # clave

        # reg.update(testimonio, rkey)
        # dbtest.update({k:v}, key=rkey)
        dbtest.update({'testimonio':testimonio}, key=rkey)
        #st.rerun()
        st.session_state['clave']=rkey
        switch_page('depaso1')

        # 
        # update_reg_dattestimonio(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio, llamado)


st.write('')
st.write('***')
st.write('')
imagenCer = photosys.get('predicacion2.png')
#st.stop()
content = imagenCer.read()
st.image(content)

with st.expander(':orange[$\Large Trabajo\,\, ministerial$] :red[$\\bold(historial)$]📝'):


    st.info('ℹ️ 🙂En esta sección queremos nos hables sobre las diferentes 📋tareas o trabajos ministeriales que haz realizado✅ o realizas en la iglesia ó en cualquier organización ministerial. Tareas cómo 👨🏻‍🏫pastorear, 🎯dirigir👨🏽‍💼 y/o participar activamente en un ministerio, etc, que hayas ejecutado en 📆tiempos, lugares🌐 y hasta organizaciones diferentes. También pedimos referencias📝 con las cuáles se pueda verificar tu trabajo ministerial, tales como 🙋🏻‍♂️contactos personales, y también 🔗 direcciones electrónicas de fotos, videos, posts, sitios web, etc., relacionados')
    st.write('')
    st.write('')
    st.write('')

    conTraMin = '0'
    nombreu, clave = reg['nombreu'], reg['key']
    for k,v in reg.items():
        if 'TraMin#' in k:
            # k, v
            conTraMin = k.split('#')[1]
            claveTraMin = 'TraMin#'+str(conTraMin)+' : '
            st.markdown('#### 📌Registro #:  '+str(conTraMin))
            valTraMinNom = st.text_input(label=':blue[$ \\bold{Ministerio/Iglesia}  $]', value=v[0][20:], key=claveTraMin+'Ministerio/Iglesia')
            valTiempo = v[1].split(':')[1]
            valTiempoIni = int(valTiempo.split(',')[0].replace('(',''))
            valTiempoFin = int(valTiempo.split(',')[1].replace(')',''))
            valTraMinTiempo = st.slider(label=':blue[$ \\bold{Tiempo\, en\, el\, ministerio/iglesia}  $]', value=(valTiempoIni, valTiempoFin), min_value=valTiempoIni-10, max_value=valTiempoFin+10, key=claveTraMin+'Tiempo')
            valTraMinOrg = st.text_input(label=':blue[$ \\bold {Organización\, /\, Iglesia\, /\, Ministerio}  $]', value=v[2][14:], key=claveTraMin+'Organización')
            valTraMinDes = st.text_area(label=':blue[$ \\bold{Descripción\, del\, \\newline trabajo\, ministerial}  $]', value=v[3][13:], key=claveTraMin+'Descripción')
            valTraMinRef =  st.text_area(label=':blue[$ \\bold{Referencias }  $]', value=v[4][13:], key=claveTraMin+'Referencias')

            #st.write(v[5], ' * ', v[5].split(':')[1], len(v[5].split(':')[1]))
            #if v[5].split(':')[1] in [' -', '-', '', '---', ' --- ', '--- ', None]:
            if len(v[5].split(':')[1]) < 10:
                #contado = k.split('#')[1]
                st.session_state['TraMin#'+str(conTraMin)+'foto'] = '---'
                che2 = st.checkbox(label='Foto de referencia de trabajo ministerial', key='ch3'+str(k))
                if che2:
                    img_file_buffer = st.camera_input("Take a picture")
                    if img_file_buffer is not None: 
                        vali = random.randint(500,1000)
                        npic = 'fotoref : 201-'+clave+'-'+nombreu+'-fotoTraMin-'+str(vali)+'-#'+conTraMin+'v1.png'
                        with st.spinner('Espere un momento...se está guardando la foto'):
                            bytes_data = img_file_buffer.getvalue()
                            photosys.put(npic, bytes_data)
                        st.success('listo!!!')
                        v[5]=npic
                        st.session_state['TraMin#'+str(conTraMin)+'foto'] = npic
                        dbtest.update({k:v}, key=rkey)
            else:
                st.session_state['TraMin#'+str(conTraMin)+'foto'] = v[5]
                v[5]
                
                imagenCer = photosys.get(v[5])
                #st.stop()
                content = imagenCer.read()
                st.image(content)
                st.caption(v[5])
                cheact = st.checkbox(label='Actualizar foto de referencia de trabajo ministerial', key='ch7'+str(k))
                if cheact:
                    img_file_buffer = st.camera_input("Take a picture")
                    if img_file_buffer is not None: 
                        npic = v[5]
                        with st.spinner('Espere un momento...se está guardando la foto'):
                            bytes_data = img_file_buffer.getvalue()
                            photosys.put(npic, bytes_data)
                        st.success('listo!!!')
                        st.session_state['clave'] = rkey
                        switch_page('depaso1')
                #st.write('***')
            st.write('')
            st.write('')
            st.write('***')
            st.write('')
            st.write('')
    icontado = int(conTraMin)+1
    conTraMin = str(icontado)
    tm = 'TraMin#'+conTraMin
    vali = random.randint(500,1000)
    npic = 'fotoref : 201-'+clave+'-'+nombreu+'-fotoTraMin-'+str(vali)+'-#'+conTraMin+'v1.png'
    #npic = '201-123-pedropic-fotorc-'+str(vali)+'-#'+conTraMin+'v1.png'
    #st.write(tm)
    v=['-','-','-','-','-']

    st.markdown('## ➕Nuevo Registro :  📝')
    TraMinField1 = 'Ministerio/Iglesia-TraMin#'
    etiTraMin = ':blue[$ \\bold{Ministerio/Iglesia}  $]'
    claveTraMin = 'TraMin1'
    valnewTraMinField1 = newElemnt([TraMinField1, 'texto', etiTraMin, claveTraMin, '-'], conTraMin, 'add')

    tiempoTraMinField = 'Tiempo-TraMin#'
    etiquetaTiempoTraMin = ':blue[$ \\bold{Tiempo\, en\, el\, ministerio/iglesia. }  $]:orange[(Desde...hasta)]'
    minimo = 1980
    maximo = 2023
    desde = 1990
    hasta = 2000
    valnewtiempoTraMin = newElemnt([tiempoTraMinField, 'range slider', etiquetaTiempoTraMin, minimo, maximo, (desde, hasta)], conTraMin, 'add')

    orgTraMinField1 = 'Organización-TraMin#'
    etiorgTraMin = ':blue[$ \\bold {Organización\, /\, Iglesia\, /\, Ministerio}  $]'
    claveorgTraMin= 'orgTraMin1'
    valneworgTraMinField1 = newElemnt([orgTraMinField1, 'texto', etiorgTraMin, claveorgTraMin, '-'], conTraMin, 'add')

    describeTraMinField = 'Descripción-TraMin#'
    etidescribeTraMin = ':blue[$ \\bold{Descripción\, del\, \\newline trabajo\, ministerial}  $]'
    valor = '-'
    valnewdescribeTramMnField = newElemnt([describeTraMinField, 'textarea', etidescribeTraMin, valor], conTraMin, 'add')

    referenciaTraMinField = 'Referencias-TraMin#'
    claverefTraMin = 'referenciaTraMin1'
    etireferenciaTraMin = ':blue[$ \\bold{Referencias \,sobre \,el \,trabajo \,ministerial \, \, \, }  $]:orange[$ \\newline \\scriptsize Pueden\, ser\, enlaces\, de\, fotos\, y\, post\, en\, redes\, sociales\, y/o\, $]:orange[$ \\newline  \\scriptsize nombres\, y\, teléfonos\, de\, personas\, que\, testifiquen\, acerca\, de $]'
    valnewreferenciaTraMinField = newElemnt([referenciaTraMinField, 'textarea', etireferenciaTraMin,  '---'], conTraMin, 'add')

    che2 = st.checkbox(label='Foto de referencia de trabajo ministerial', key='ch3'+str(tm))

    if che2:
        k = tm
        #newvalea
        vnewtramin=[elem for elem in newvalea if 'TraMin#' in elem]
        #vnewtramin
        #valnewTraMinField1 
        try:    
            v0 = list(vnewtramin[0].items())[0]
            v0t = v0[0].split('-')[0] + ' : ' + str(v0[1])
        except: 
            v0 = vnewtramin[0]
            v0t = 'Ministerio/Iglesia : '+v0.split('---')[1]
        try:    
            v1 = list(vnewtramin[1].items())[0]
            v1t = v1[0].split('-')[0] + ' : ' + str(v1[1])
        except: 
            v1 = vnewtramin[1]
            v1t = 'Tiempo : ' +v1.split('---')[1]
        try:    
            v2 = list(vnewtramin[2].items())[0]
            v2t = v2[0].split('-')[0] + ' : ' + str(v2[1])
        except: 
            v2 = vnewtramin[2]
            v2t = 'Organización : '+v2.split('---')[1]
        try:    
            v3 = list(vnewtramin[3].items())[0]
            v3t = v3[0].split('-')[0] + ' : ' + str(v3[1])
        except: 
            v3 = vnewtramin[3]
            v3t = 'Descripción : '+v3.split('---')[1]
        try:    
            v4 = list(vnewtramin[4].items())[0]
            v4t = v4[0].split('-')[0] + ' : ' + str(v4[1])
        except: 
            v4 = vnewtramin[4]
            v4t = 'Referencias : ' +v4.split('---')[1]
        #v0t = v0[0].split('-')[0] + ' : ' + str(v0[1])
        #v1t = v1[0].split('-')[0] + ' : ' + str(v1[1])
        #v2t = v2[0].split('-')[0] + ' : ' + str(v2[1])
        #v3t = v3[0].split('-')[0] + ' : ' + str(v3[1])
        #v4t = v4[0].split('-')[0] + ' : ' + str(v4[1])
        v5t = npic
        st.session_state['TraMin#'+str(conTraMin)+'foto'] = npic

        'v#ts = ',v0t,v1t,v2t,v3t,v4t,v5t
        
        img_file_buffer = st.camera_input("Take a picture")
        if img_file_buffer is not None: 
            with st.spinner('Espere un momento...se está guardando la foto'):
                bytes_data = img_file_buffer.getvalue()
                photosys.put(npic, bytes_data)
            st.success('listo!!!')
            dbtest.update({k:[v0t, v1t, v2t, v3t, v4t, v5t]}, key=rkey)
            st.session_state['clave'] = rkey
            switch_page('depaso1')
    else: st.session_state['TraMin#'+str(conTraMin)+'foto'] = '-'
    st.write('')
    st.write('***')
    st.write('')
    st.write('')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btnTraMin', use_container_width=True)
    if btn:
        #st.write('se guarda ')
        st.write(st.session_state)
        st.write('***')
        st.write('conTraMin = ', conTraMin)
        nv=[]
        for conTraMinS in range(1,int(conTraMin)):
            'conTraMinS = ', conTraMinS
            k = 'TraMin#'+str(conTraMinS)
            v = []
            for elemento in st.session_state:
                if  elemento.startswith('TraMin#'+str(conTraMinS)):
                    elemento, ' : ', st.session_state[elemento]
                    f2 = elemento.find(':')            
                    v.append(elemento[f2+1:] + ':' + str(st.session_state[elemento]))
            nv.append({k:v})
            st.write('***')
        'nv0 = ', nv
        #st.stop()
        st.write('***')
        k='TraMin#'+str(conTraMin)
        v=[]
        for elemento in newvalea:   
            #elemento     
            ele2 = elemento.replace(' --- ',' : ')
            ele3 = ele2.replace('-'+k,'')
            #ele3
            v.append(ele3)
        v.append(k+'foto:'+st.session_state[k+'foto'])
        #'v = ', v
        nv.append({k:v})
        'nv = ', nv
        st.write(len(nv))
        for con in range(0, len(nv)):
            st.write('con = ', con)
            nnnv = ['M', 'T', 'O', 'D', 'R', 'F']
            for k,v in nv[con].items():
                for ele in v:
                    if ele.split(':')[0] in ' Ministerio/Iglesia ': 
                        nnnv[0]='Ministerio/Iglesia : '+str(ele[ele.find(':')+1: ]).lstrip()
                    elif ele.split(':')[0] in ' Tiempo ': 
                        nnnv[1]='Tiempo : '+str(ele[ele.find(':')+1: ]).lstrip()
                    elif ele.split(':')[0] in ' Organización ': 
                        nnnv[2]='Organización : '+str(ele[ele.find(':')+1: ]).lstrip()
                    elif ele.split(':')[0] in ' Descripción ': 
                        nnnv[3]='Descripción : '+str(ele[ele.find(':')+1: ]).lstrip()
                    elif ele.split(':')[0] in ' Referencias ': 
                        nnnv[4]='Referencias : '+str(ele[ele.find(':')+1: ]).lstrip()
                    else:
                        ele2 = ele[14:]
                        if len(ele2)>1:
                            nnnv[5]='fotoref : '+ele2[8:].lstrip()
                        else:
                            nnnv[5]='fotoref : --- '
                st.write(k, '--> ', nnnv)
                #dbtest.put(data={k:nnnv}, key=rkey)
                registromin = {k:nnnv}
                'registromin = ', registromin
                actualiza = True
                len(registromin[k][0]), len(registromin[k][2]), len(registromin[k][3])
                if len(registromin[k][0])<10:
                    actualiza = False
                    st.toast('Campo Ministerio/Iglesia no puede quedar vacío')
                if len(registromin[k][2])<10:
                    actualiza = False
                    st.toast('Debe llenar el Campo Organización')
                if len(registromin[k][3])<10:
                    actualiza = False
                    st.toast('Debe dar una breve Descripción del trabajo ministerial realizado')
                if actualiza:
                    dbtest.update(registromin, key= rkey)
                    #st.stop()
        st.session_state['clave']=rkey
        switch_page('depaso1')       
        st.write('===================')
            #

st.write('')
st.write('***')
st.write('')
imagenCer = photosys.get('colaboracion3.png')
#st.stop()
content = imagenCer.read()
st.image(content)

with st.expander(':orange[$\large  Participación\, actual\\newline en\, los\, ministerios\, de\, su\, iglesia $]'):
    #st.warning('ℹ️ 🙂 $\\Large Sección\, en\, construcción $')
    
    st.info('ℹ️ 🙂En esta sección queremos información de tu nivel de participación actual en los diferentes ministerios ó departamentos de tu iglesia. Por ejemplo, digamos que participas en el grupo o ministerio de alabanza porque tocas el piano, pero no tienes participación alguna en el departamento de damas, pero lideras a los diáconos.')
    st.caption('Por favor, trata de incluir todos los departamentos ó ministerios de tu congregación, aún cuando tu participación en alguno de ellos sea nula')
    st.write('***')
    st.write('')
    
    conMinA = 0
    listMinA = []
    MinAval = {}
    conParMinHoy = '0'
    nombreu, clave = reg['nombreu'], reg['key']
    for k,v in reg.items():
        if 'ParMinHoy#' in k:
            #k, v
            conParMinHoy = k.split('#')[1]
            claveParMinHoy = 'ParMinHoy#'+str(conParMinHoy)+' : '
            st.markdown('#### 📌Registro #:  '+str(conParMinHoy))
            valNombreParMinHoy = st.text_input(label=':blue[$ \\bold{Ministerio/Departamento}  $]', value=v[0][26:], key=claveParMinHoy+'Ministerio/Departamento')
            vaalNivelParMinHoy = st.select_slider(label=':blue[$ \\bold{Nivel \, de\, participación/relación\, en} $] :blue[$ \\bold{el\, ministerio/departamento}  $]', options=['ninguna', 'asisto', 'participo', 'líder', 'asesoro/superviso'], value=v[1][25:], key=claveParMinHoy+'NivelPar')
            valDescribeParMinHoy = st.text_area(label=':blue[$ \\bold{Descripción}  $]', value=v[2][14:], key=claveParMinHoy+'Describe')
            st.write('***')
            st.write('')
# =========================

    icontadopmh = int(conParMinHoy)+1
    conParMinHoy = str(icontadopmh)
    pmh = 'ParMinHoy#'+conParMinHoy

    v=['-','-','-','-','-']
    st.write('')
    st.markdown('## ➕Nuevo Registro :  📝')
    nombreMinAField = 'nombreParMinHoy#'
    etinomMinA = ':blue[$ \\bold{Ministerio/Departamento}  $]'
    claveMinA = 'MinA1'
    valnewnombreMinAField = newElemnt([nombreMinAField, 'texto', etinomMinA, claveMinA, '-'], conMinA, 'add')

    namepMinAField = 'nivelParMinHoy#'
    opcionesparticipacionMinA = ['ninguna', 'asisto', 'participo', 'líder', 'asesoro/superviso']
    etiquetapMinA = ':blue[$ \\bold{Nivel \, de\, participación/relación\, en} $] :blue[$ \\bold{el\, ministerio/departamento}  $]'
    valnewpMinA = newElemnt([namepMinAField, 'select slider', etiquetapMinA, opcionesparticipacionMinA], conMinA, 'add')

    describeparMinAField = 'describeParMinHoy#'
    etidescribeparMinA = ':blue[$ \\bold{Descripción}  $]'
    valor = '-'
    valnewdescribeparMinAField = newElemnt([describeparMinAField, 'textarea', etidescribeparMinA, valor], conMinA, 'add')

    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btnParMinHoy', use_container_width=True)
    if btn:
        #st.write('se guarda ')
        st.write(st.session_state)
        st.write('***')
        st.write('conParMinHoy = ', conParMinHoy)
        nv=[]
        for conParMinHoyS in range(1,int(conParMinHoy)):
            'conParMinHoyS = ', conParMinHoy
            k = 'ParMinHoy#'+str(conParMinHoyS)
            v = []
            for elemento in st.session_state:
                if  elemento.startswith('ParMinHoy#'+str(conParMinHoyS)):
                    elemento, ' : ', st.session_state[elemento]
                    f2 = elemento.find(':')            
                    v.append(elemento[f2+1:] + ':' + str(st.session_state[elemento]))
            nv.append({k:v})
            st.write('***')
        'nv0 = ', nv
        #st.stop()
        st.write('***')
        k='ParMinHoy#'+str(conParMinHoy)
        v=[]
        for elemento in newvalea:   
            #elemento     
            if 'ParMinHoy#' in elemento:
                'ele con ParMinHoy : ', elemento
                ele2 = elemento.replace(' --- ',' : ')
                ele3 = ele2.replace('-'+k,'')
                #ele3
                v.append(ele3)
        # v.append(k+'foto:'+st.session_state[k+'foto'])
        #'v = ', v
        nv.append({k:v})
        'nv = ', nv
        st.write(len(nv))
        for con in range(0, len(nv)):
            st.write('con = ', con)
            nnnv = ['N', 'L', 'D']
            for k,v in nv[con].items():
                for ele in v:
                    # ele, '  ---  ', ele.split(':')
                    if 'nombreParMinHoy' in ele.split(':')[0] :
                        nnnv[0]='Ministerio/Departamento : '+str(ele[ele.find(':')+1: ]).lstrip()
                    elif 'nivelParMinHoy'  in ele.split(':')[0]: 
                        nnnv[1]='Nivel de participación : '+str(ele[ele.find(':')+1: ]).lstrip()
                    elif 'describeParMinHoy' in ele.split(':')[0]: 
                        nnnv[2]='Descripción : '+str(ele[ele.find(':')+1: ]).lstrip()
                st.write(k, '--> ', nnnv)
                registromin = {k:nnnv}
                'registromin = ', registromin
                actualiza = True
                len(registromin[k][0]), len(registromin[k][1]), len(registromin[k][2])
                if len(registromin[k][0])<10:
                    actualiza = False
                    st.toast('Campo Ministerio no puede quedar vacío')
                if len(registromin[k][2])<10:
                    actualiza = False
                    st.toast('Debe dar una breve Descripción del trabajo ministerial realizado')
                actualiza
                if actualiza:
                    dbtest.update(registromin, key= rkey)
                    #st.stop()
        st.session_state['clave']=rkey
        switch_page('depaso1')       
        st.write('===================')
            #

    
st.write('')
st.write('***')
st.write('')
imagenCer = photosys.get('estudiosmin.png')
#st.stop()
content = imagenCer.read()
st.image(content)

with st.expander(':orange[$\Large Estudios\, eclesiásticos  $]'):
    #st.warning('ℹ️ 🙂 $\\Large Sección\, en\, construcción $')
    st.write('')
    st.info('ℹ️ 🙂Los estudios eclesiásticos se refieren  aquellos tomados en el contexto de la iglesia✝️ ó el 🛐ministerio. Incluye estudios,📜 cursos, y/o talleres 📓bíblicos, discipulares, sobre liderazgo,📚 teológicos, etc., en institutos o seminarios bíblicos, presenciales ó a👨🏻‍💻 distancia,🌐 en eventos tales como congresos🎇 o retiros, entre otros.')

    st.write('***')
    st.write('')
    conEstMin = '0'
    nombreu, clave = reg['nombreu'], reg['key']
    for k,v in reg.items():
        if 'EstMin#' in k:
            #k, v
            conEstMin = k.split('#')[1]
            claveEstMin = 'EstMin#'+str(conEstMin)+' : '
            #st.info('Registro #:  '+str(conEstMin)+'  👀  ', icon='📌')
            st.markdown('#### 📌Registro #:  '+str(conEstMin))
            valEstMinNom = st.text_input(label=':blue[$ \\bold{Nombre \,del \,curso/estudio \,eclesiastico}  $]', value=v[0][9:], key=claveEstMin+'Nombre')
            
            opcionesTipo = ['-', 'Bíblico', 'Discipular', 'Liderazgo', 'Teológico', 'Otra']
            if v[1][7:] not in opcionesTipo:
                opcionesTipo.append(v[1][7:])
            valEstMinTipo = st.radio(label=':blue[$ \\bold{Tipo \,de \,curso}  $]', options=opcionesTipo, key=claveEstMin+'Tipo', index=opcionesTipo.index(v[1][7:]), horizontal=True)
            
            valEstMinInst = st.text_input(label=':blue[$ \\bold {Institución\, /\, Iglesia\, /\, Ministerio}  $]', value=v[2][14:], key=claveEstMin+'Institución')

            valEstMinSede = st.text_input(label=':blue[$ \\bold {Sede\, /\, Lugar}  $]', value=v[3][6:], key=claveEstMin+'Sede')

            valEstMinModo = st.select_slider(label=':blue[$ \\bold{Modalidad \,de \,estudio}  $]', options=['presencial', 'en línea /a distancia', 'híbrido'], value=v[4][7:], key=claveEstMin+'Modo')

            valTiempo = v[5].split(':')[1]
            valTiempoIni = int(valTiempo.split(',')[0].replace('(',''))
            valTiempoFin = int(valTiempo.split(',')[1].replace(')',''))
            valEstMinTiempo = st.slider(label=':blue[$ \\bold{Tiempo}  $]', value=(valTiempoIni, valTiempoFin), min_value=valTiempoIni-3, max_value=valTiempoFin+3, key=claveEstMin+'Tiempo')

            valEstMinCert = st.text_input(label=':blue[$ \\bold {Certificado\, /\, Último \,  nivel \,alcanzado}  $]', value=v[6][20:], key=claveEstMin+'Certificado/Nivel')

            #valfotoref = st.caption(v[7])
            if len(v[8].split(':')[1]) < 10:
                #contado = k.split('#')[1]
                st.session_state['EstMin#'+str(conEstMin)+'foto'] = '---'
                che4 = st.checkbox(label='Foto del certificado de estudio ministerial', key='ch5'+str(k))
                if che4:
                    img_file_buffer = st.camera_input("Toma la foto")
                    if img_file_buffer is not None: 
                        vali = random.randint(2500,4000)
                        npic = 'Fotoref : 301-'+clave+'-'+nombreu+'-fotoEstMin-'+str(vali)+'-#'+conEstMin+'v1.png'
                        with st.spinner('Espere un momento...se está guardando la foto'):
                            bytes_data = img_file_buffer.getvalue()
                            photosys.put(npic, bytes_data)
                        st.success('listo!!!')
                        v[8]=npic
                        st.session_state['EstMin#'+str(conEstMin)+'foto'] = npic
                        dbtest.update({k:v}, key=rkey)
                        st.session_state['clave'] = rkey
                        switch_page('depaso1')
            else:
                st.session_state['EstMin#'+str(conEstMin)+'foto'] = v[8]
                #v[7]
                
                imagenCer = photosys.get(v[8])
                #st.stop()
                content = imagenCer.read()
                st.image(content)
                st.caption(v[7])
                cheact = st.checkbox(label='Actualizar foto referencia del estudio ministerial', key='ch9'+str(k))
                if cheact:
                    img_file_buffer = st.camera_input("Toma la foto")
                    if img_file_buffer is not None: 
                        npic = v[8]
                        with st.spinner('Espere un momento...se está guardando la foto'):
                            bytes_data = img_file_buffer.getvalue()
                            photosys.put(npic, bytes_data)
                        st.success('listo!!!')
                        st.session_state['clave'] = rkey
                        switch_page('depaso1')

            valEstMinDes = st.text_area(label=':blue[$ \\bold{Descripción\, del\, \\newline estudio\, ministerial}  $]', value=v[7][14:], key=claveEstMin+'Descripción')
            st.write('')
            st.write('')
            st.write('***')
            st.write('')
            st.write('')
            

    #st.stop()
    icontado = int(conEstMin)+1
    conEstMin = str(icontado)
    em = 'EstMin#'+conEstMin
    vali = random.randint(2500,4000)
    npic = 'fotoref : 301-'+clave+'-'+nombreu+'-fotoEstMin-'+str(vali)+'-#'+conEstMin+'v1.png'
    #npic = '201-123-pedropic-fotorc-'+str(vali)+'-#'+conTraMin+'v1.png'
    #st.write(tm)
    v=['-','-','-','-','-']

    #conEstMin+=1
    st.markdown('## ➕Nuevo Registro :  📝')
    #st.write(':red[$ \\bold{ ➕  \,\, Nuevo \,\, Registro \,\, 📝}  $]')
    nombreEBField = 'nombreEstMin#'
    etinomEB = ':blue[$ \\bold{Nombre \,del \,curso/estudio \,eclesiastico}  $]'
    clavetxt = 'nomEB1'
    valnewnombreEBField = newElemnt([nombreEBField, 'texto', etinomEB, clavetxt, '-'], conEstMin, 'add')

    tipoEBField = 'tipoEstMin#'
    opcionestipoEB = ['-', 'Bíblico', 'Discipular', 'Liderazgo', 'Teológico', 'Otra']
    Etiqueta1 = ':blue[$ \\bold{Tipo \,de \,\, curso}  $]'
    Etiqueta2 = 'Especifique el tipo de estudio'
    valnewtipoEB = newElemnt([tipoEBField, 'radio', Etiqueta1, opcionestipoEB, Etiqueta2], conEstMin, 'add')

    institutoEBField = 'institucionEstMin#'
    clavetxtiEB = 'iEB1'
    etiinstitutoEB = ':blue[$ \\bold {Institución\, /\, Iglesia\, /\, Ministerio}  $]'
    valnewinstitutoEBField = newElemnt([institutoEBField, 'texto', etiinstitutoEB, clavetxtiEB, '-'], conEstMin, 'add')

    sedeEBField = 'sedeEstMin#'
    clavetxtsEB = 'sEB1'
    etisedeEB = ':blue[$ \\bold {Lugar \,ó \,Sede \,del \, instituto}  $]'
    valnewsedeEBField = newElemnt([sedeEBField, 'texto', etisedeEB, clavetxtsEB, '-'], conEstMin, 'add')

    namemodoEBField = 'modoEstMin#'
    opcionesmodoEB = ['presencial', 'en línea /a distancia', 'híbrido']
    etiquetamodoEB = ':blue[$ \\bold{Modalidad \,de \,estudio}  $]'
    valnewmodoEB = newElemnt([namemodoEBField, 'select slider', etiquetamodoEB, opcionesmodoEB], conEstMin, 'add')

    tiempoEBField = 'tiempoEstMin#'
    etiquetaTiempoEB = ':blue[$ \\bold{Tiempo\, de\, estudio\, (Desde...Hasta)}  $]'
    minimo = 1980
    maximo = 2023
    desde = 1990
    hasta = 2000
    valnewtiempoEB = newElemnt([tiempoEBField, 'range slider', etiquetaTiempoEB, minimo, maximo, (desde, hasta)], conEstMin, 'add')

    certificadonivelEBField = 'certificadonivelEstMin#'
    clavecerEB = 'certEB1'
    eticertificadonivelEB = ':blue[$ \\bold {Certificado\, /\, Último \,  nivel \,alcanzado}  $]'
    valnewcertificadonivelEBField = newElemnt([certificadonivelEBField, 'texto', eticertificadonivelEB, clavecerEB, '-'], conEstMin, 'add')

    st.write('')
    
    describeEBField = 'describeEstMin#'
    etidescribeEB = ':blue[$ \\bold{Descripción\, del\, \\newline estudio\, ministerial}  $]'
    valor = '-'
    valnewdescribeEBField = newElemnt([describeEBField, 'textarea', etidescribeEB, valor], conEstMin, 'add')

    che3 = st.checkbox(label='Foto referencia del estudio ministerial', key='ch4'+str(em))

    if che3:
        #k = tm
        fieldsEstMin=[]
        # st.session_state
        for t in newvalea:
            if 'EstMin#'+str(conEstMin) in t:
                fieldsEstMin.append((t[ :t.find('EstMin')], t[t.find('---')+4 : ]))
        # fieldsEstMin
        li2=[x for (x,y) in fieldsEstMin]
        # li2
        tomarfoto = True
        try:
            li2.index('certificadonivel')
            li2.index('nombre')
        except:
            tomarfoto=False
        #'tomarfoto = ', tomarfoto
        if not tomarfoto: 
            st.toast('Campos Nombre y Certificados deben estar llenos para poder tomar la foto del certificado')
        else:
            vali = random.randint(2500,4000)
            npic = 'Fotoref : 301-'+clave+'-'+nombreu+'-fotoEstMin-'+str(vali)+'-#'+conEstMin+'v1.png'
            'npic = ', npic
            #v0=fieldsEstMin[li2.index('nombre')]
            v0t =  'Nombre : ' + fieldsEstMin[li2.index('nombre')][1]
            v1t =  'Tipo : ' + fieldsEstMin[li2.index('tipo')][1]
            v2t =  'Institución : ' + fieldsEstMin[li2.index('institucion')][1]
            v3t = 'Sede : ' + fieldsEstMin[li2.index('sede')][1]
            v4t =  'Modo : ' + fieldsEstMin[li2.index('modo')][1]
            v5t =  'Tiempo : ' + fieldsEstMin[li2.index('tiempo')][1]
            v6t =  'Certificado/Nivel : ' + fieldsEstMin[li2.index('certificadonivel')][1]
            try:
                v7t =  'Descripción : ' + fieldsEstMin[li2.index('describe')][1]
            except:
                v7t = 'Descripción :  ---'
            v8t =  npic

            v0t, v1t, v2t, v3t, v4t, v5t, v6t, v7t, v8t
    #         # dbtest.update({k:[v0t, v1t, v2t, v3t, v4t, v5t]}, key=rkey)

            img_file_buffer = st.camera_input("Take a picture")

            if img_file_buffer is not None: 
                with st.spinner('Espere un momento...se está guardando la foto'):
                    bytes_data = img_file_buffer.getvalue()
                    photosys.put(npic, bytes_data)
                st.success('listo!!!')
                kEstM = 'EstMin#'+str(conEstMin)
                # kEstM,'  ==> ',v0t, v1t, v2t, v3t, v4t, v5t, v6t, v7t, v8t, rkey
                #st.stop()
                dbtest.update({kEstM:[v0t, v1t, v2t, v3t, v4t, v5t, v6t, v7t, v8t]}, key=rkey)
                st.session_state['clave'] = rkey
                switch_page('depaso1')
    else: st.session_state['EstMin#'+str(conEstMin)+'foto'] = '-'
    st.write('')

    
    

    # btn = st.button(label='Guardar')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btnEstMin', use_container_width=True)
    if btn:
        #st.write(st.session_state)
        #st.write('conEstMin = ', conEstMin)
        nv=[]
        for conEstMinS in range(1,int(conEstMin)+1):
            'conEstMinS = ', conEstMinS
            k = 'EstMin#'+str(conEstMinS)
            v = []
            nvvv = ['-','-','-','-','-','-','-','-']
            for elemento in st.session_state:
                if 'EstMin#'+str(conEstMinS) in elemento:
                    #elemento, ' --- ', str(st.session_state[elemento])
                    if elemento.find(':')>6:
                        f2 = elemento.find(':')
                        elem2 = elemento[f2+1:].lstrip()
                    else:
                        f2 = elemento.find('-')
                        f3 = elemento.find('#')
                        elem1 = elemento[f2+1 : f3-6].lstrip()
                        elem2 = elem1.capitalize()
                        if elem2 == 'Certificadonivel': elem2='Certificado/Nivel'
                        if elem2 == 'Institucion': elem2='Institución'
                        if elem2 == 'Describe': elem2='Descripción'
                        if elem2 == '': elem2='Fotoref'
                        elem2, f2, f3
                    'elem2 = ', elem2, '***'
                    if elem2 in ['Nombre', 'Tipo', 'Institución', 'Sede', 'Modo',  'Tiempo', 'Certificado/Nivel', 'Descripción', 'Fotoref']:
                        #'encontrado'
                        v.append(elem2+' : '+str(st.session_state[elemento]))
                    if 'foto' in elem2: 
                        if len(st.session_state[elemento])>3:
                            v.append(st.session_state[elemento])
                        else: v.append('Fotoref : ---')
                    #'v = ', v
            nv.append({k:v})
            #st.write('***')
        'nv0 = ', nv
        st.write('***')

        registroemin=[]
        for it in nv:
            #it
            nvv=['-','-','-','-','-','-','-','-','-']
            for k,v in it.items():
                #'k = ',k, len(k), ' - ', len(v), v
                '---'
                if len(v)>0:
                    for ele in v:
                        #ele, ' * *  ', ele.split(':')[0], '  +*+  ', ele.split(':')[1]
                        if ele.split(':')[0] in ' Nombre ':
                            nvv[0]='Nombre : '+ele.split(':')[1].lstrip()
                        elif ele.split(':')[0] in ' Tipo ':
                            nvv[1]='Tipo : '+ele.split(':')[1].lstrip()
                        elif ele.split(':')[0] in ' Institución ':
                            nvv[2]='Institución : '+ele.split(':')[1].lstrip()
                        elif ele.split(':')[0] in ' Sede ':
                            nvv[3]='Sede : '+ele.split(':')[1].lstrip()
                        elif ele.split(':')[0] in ' Modo ':
                            nvv[4]='Modo : '+ele.split(':')[1].lstrip()
                        elif ele.split(':')[0] in ' Tiempo ':
                            nvv[5]='Tiempo : '+ele.split(':')[1].lstrip()
                        elif ele.split(':')[0] in ' Certificado/Nivel ':
                            nvv[6]='Certificado/Nivel : '+ele.split(':')[1].lstrip()
                        elif ele.split(':')[0] in ' Descripción ':
                            nvv[7]='Descripción : '+ele.split(':')[1].lstrip()
                        elif ele.split(':')[0] in ' Fotoref ':
                            try:
                                nvv[8]='Fotoref : '+ele.split(':')[2].lstrip()
                            except:
                                nvv[8]='Fotoref : '+ele.split(':')[1].lstrip()
                    'nvv[8] = ', nvv[8]
                    if nvv[8]=='-': nvv[8]='Fotoref : -'
                    registroemin.append({k : nvv})
                #k, '   :::   ', nvv
                #st.stop()

                actualiza = True
                # filtros de validacion -------------#
                if len(nvv)<8: actualiza=False
                if len(nvv[0]) < 12 : actualiza=False
                if len(nvv[2]) < 16 : actualiza=False
                if actualiza:
                    st.write(' Registro a grabar')
                    'k : ',k, 'v : ', nvv
                    dbtest.update({k:nvv}, key= rkey)
                else:
                    st.write('Registro invalido para grabar')
                    'k : ',k, 'v : ', nvv
                # continuar = False
                # btcontinuar = st.button('Continuar ??')
                # if btcontinuar:
                #     continuar = True
                # if not continuar: st.stop()
        #         if actualiza:
        #             dbtest.update(registroemin, key= rkey)
        # st.stop()
        st.session_state['clave']=rkey
        switch_page('depaso1')       
        # st.write('===================')
            #
        

