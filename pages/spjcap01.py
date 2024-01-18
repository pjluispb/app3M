
import streamlit as st
import random
import time
from streamlit_extras.switch_page_button import switch_page

def inicializa():
    try:   #verifica y crea las var de session a usar como controladores
        #'controladores'
        st.session_state.ss1
        st.session_state.ss2
        st.session_state.ea1
        st.session_state.ea2
        st.session_state.bc1
        st.session_state.bc1B
        st.session_state.bc1C
        st.session_state.bc2
        st.session_state.bc21
        st.session_state.bc22b
        st.session_state.bc23b
        st.session_state.inicio

        '---'
    except:
        st.toast('iniciando')
        st.session_state.ss1 = []
        st.session_state.ss2 = []
        st.session_state.ea1 = ''
        st.session_state.ea2 = ''
        st.session_state.bc1 = 0
        st.session_state.bc1B = 0
        st.session_state.bc1C = 0
        st.session_state.bc2 = 0
        st.session_state.inicio = False
        st.session_state.bc21 = 0
        st.session_state.bc22b = 0
        st.session_state.bc23b = 0
    return
def cuq(ronda, seleccion):
    if seleccion==1: lista = lista_1
    if seleccion==2: lista = lista_2
    if ronda==1:
        if seleccion==1: st.session_state.selron = '11'
        if seleccion==2: st.session_state.selron = '21'
    if ronda==2:
        if seleccion==1: st.session_state.selron = '12'
        if seleccion==2: st.session_state.selron = '22'
    if ronda==3:
        if seleccion==1: st.session_state.selron = '13'
        if seleccion==2: st.session_state.selron = '23'
    q1 = 'q1-'+str(len(st.session_state.ss1))
    st.session_state.ss1.append(q1)
    lpre = random.sample(lista,4)
    pre1 = {'Q':lpre[0][0], 'ops':lpre[0][1],'ans':lpre[0][2]}
    pre2 = {'Q':lpre[1][0], 'ops':lpre[1][1],'ans':lpre[1][2]}
    pre3 = {'Q':lpre[2][0], 'ops':lpre[2][1],'ans':lpre[2][2]}
    pre4 = {'Q':lpre[3][0], 'ops':lpre[3][1],'ans':lpre[3][2]}
    if st.session_state.ea1=='':
        st.session_state.ea1 = 'preg cargadas'
    if st.session_state.ea1=='2da ronda de preg cargadas':
        st.session_state.ea1 = '2da ronda de preg cargadas'
    return(pre1,pre2,pre3,pre4)
def comparar_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        return None
    
    resultados = []
    for i in range(len(lista1)):
        if lista1[i] == lista2[i]:
            resultados.append(1)
        else:
            resultados.append(0)
    
    return resultados
       
lista_1 = [
    [':orange[¿En qué año Alejandro Mack descendió a las aguas del río Eder?]', ['1608', '1708', '1808', '1908'], '1708'],
    [':orange[¿Cuántas personas fueron bautizadas junto con Alejandro Mack?]', ['4', '6', '8', '10'], '8'],
    [':red[¿Cuál era la ocupación del padre de Alejandro Mack?]', ['Molinero', 'Maestro', 'Carpintero', 'Agricultor'], 'Molinero'],
    [':red[¿En qué estado de Estados Unidos terminó Alejandro Mack como refugiado religioso?]', ['Nueva York', 'Florida', 'Pensilvania', 'California'], 'Pensilvania'],
    [':orange[¿Por qué se estaban matando y torturando mutuamente las diferentes iglesias?]', ['Por problemas económicos', 'Por problemas políticos', 'Por problemas religiosos', 'Por problemas territoriales'], 'Por problemas religiosos'],
    [':red[¿Qué norma de fe y manera de vivir tomaron como base los miembros del grupo original?]', ['El Antiguo Testamento', 'El Corán', 'El Nuevo Testamento', 'El Libro de Mormón'], 'El Nuevo Testamento'],
    [':orange[¿Qué afirmaron los miembros del grupo original sobre su credo?]', ['No tenían credo', 'Tenían un credo formal', 'No creían en ningún credo', 'Creían en varios credos'], 'No tenían credo'],
    [':red[¿Qué era repulsivo para los miembros de la comunidad de fe?]', ['La violencia religiosa', 'La falta de fe', 'La falta de estudios bíblicos', 'La falta de adoración'], 'La violencia religiosa'],
    [':orange[¿Qué era muy importante para los miembros de la comunidad de fe?]', ['La política', 'La economía', 'La adoración', 'La educación'], 'La educación'],
    [':red[¿Qué deseaban los miembros de la comunidad de fe que viviera en ellos?]', ['La palabra de Jesucristo', 'El espíritu de la comunidad', 'La doctrina de la Iglesia', 'El amor al prójimo'], 'La palabra de Jesucristo'],
    # Agrega más preguntas aquí
]
lista_2 = [
    [':orange[¿En qué pasaje bíblico se encuentra la advertencia de Jesús a aquellos que iban a seguirle?]', ['Mateo 9:9', 'Marcos 1:16-18', 'Lucas 14:25-33', 'Mateo 7:21-22'], 'Lucas 14:25-33'],
    [':red[¿Qué obra de Godfrey Arnold fue estudiada y apreciada por Alejandro Mack y los primeros líderes?]', ['La Historia Imparcial de la Iglesia y las Herejías', 'El Libro de Mormón', 'El Corán', 'La Biblia'], 'La Historia Imparcial de la Iglesia y las Herejías'],
    [':orange[¿Qué significa originalmente la palabra "hereje"?]', ['Escoger', 'Creer', 'Difamar', 'Seguir'], 'Escoger'],
    [':red[¿Qué perdieron los primeros miembros de la Iglesia de los Hermanos debido a su fe en Cristo?]', ['Sus hogares', 'Sus propiedades', 'La división familiar', 'Todas las anteriores'], 'Todas las anteriores'],
    [':orange[¿Qué pasaje bíblico menciona que los seguidores de Jesús deben calcular el costo de seguirle?', ['Mateo 9:9', 'Marcos 1:16-18', 'Lucas 14:25-33', 'Mateo 7:21-22'], 'Lucas 14:25-33'],
    [':red[¿Qué se espera de los cristianos según Mateo 7:21-22?]', ['Que digan sí al llamado de Cristo', 'Que estudien las Escrituras', 'Que obedezcan a los líderes de la Iglesia', 'Que crean en un credo formal'], 'Que digan sí al llamado de Cristo'],
    [':orange[¿Qué nos guía y fortalece según el texto?]', ['El Espíritu Santo de Dios', 'La comunidad de la fe', 'Las Escrituras', 'Los líderes de la Iglesia'], 'El Espíritu Santo de Dios'],
    [':red[¿Qué aclara el Nuevo Testamento acerca de los cristianos?]', ['Que nacen en una familia de cristianos', 'Que deben seguir un credo formal', 'Que deben ser miembros de una iglesia establecida', 'Que deben estudiar la historia de la Iglesia'], 'Que nacen en una familia de cristianos'],
    [':orange[¿Qué se menciona como importante para sobrevivir como cristianos?]', ['El compañerismo de la Iglesia', 'La sencillez en la vestimenta', 'El estudio profundo de las Escrituras', 'La obediencia a los líderes religiosos'], 'El compañerismo de la Iglesia'],
    [':red[¿Qué se espera de los cristianos según 1ra Corintios 3:1-2?]', ['Que crezcan y aprendan mutuamente', 'Que se alimenten con comida para niños', 'Que sigan las enseñanzas de Godfrey Arnold', 'Que estudien la historia de la Iglesia'], 'Que crezcan y aprendan mutuamente'],
    [':orange[¿Cuál es el objetivo principal de los miembros de la Iglesia de los Hermanos?]', ['Regresar a Jesús y dejarlo ser el Señor y Salvador en su vida personal', 'Mantener la vestimenta simple de los menonitas y cuáqueros', 'Buscar la voluntad de Dios solo en el área de la adoración', 'No tener diferencias en teología y formas de adoración'], 'Regresar a Jesús y dejarlo ser el Señor y Salvador en su vida personal'],
    [':red[¿Cuál fue la razón por la cual los primeros miembros de la Iglesia de los Hermanos decidieron usar una vestimenta simple?]', ['Para destacarse en la sociedad', 'Como testimonio de la sencillez enseñada por Jesús', 'Por influencia de otras denominaciones religiosas', 'Por imposición de la Iglesia institucional'], 'Como testimonio de la sencillez enseñada por Jesús'],
    [':orange[¿Cuál es una de las convicciones profundas que une a los miembros de la Iglesia de los Hermanos?]', ['La búsqueda de la voluntad de Dios en todas las áreas de la vida', 'La adhesión a un credo formal', 'La uniformidad en la vestimenta y forma de adoración', 'La obediencia a los líderes religiosos'], 'La búsqueda de la voluntad de Dios en todas las áreas de la vida'],
    [':red[¿Qué se espera de los seguidores de Jesús según el texto?]', ['Que busquen la voluntad de Dios en todas las áreas de sus vidas', 'Que sigan un credo formal establecido por la Iglesia', 'Que se vistan de manera sencilla como los menonitas y cuáqueros', 'Que se adhieran a una teología específica'], 'Que busquen la voluntad de Dios en todas las áreas de sus vidas'],
    [':orange[¿A quién pertenece el mundo según el texto?]', ['A los seguidores de Jesús', 'A la Iglesia institucional', 'A Dios', 'A todas las personas por igual'], 'A Dios'],
    # Agrega más preguntas aquí
]

nombreu = st.session_state['nombreu']
claveu = st.session_state['claveu']

try:         #inicializa var de session
    if st.session_state.inicio==True:
        inicializa()
except:
    st.session_state.inicio=True
    inicializa()
try:         #inicializa contenedores phs
    ph0 = st.empty()
    ph01 = st.empty()
    ph01b = st.empty()
    ph1 = st.empty()
    ph12 = st.empty()
    ph1B = st.empty()
    ph1B2 = st.empty()
    ph1B3 = st.empty()
    ph1C = st.empty()
    ph1C2 = st.empty()

    ph02 = st.empty()
    ph02b = st.empty()
    ph2 = st.empty()
    ph21 = st.empty()
    ph21b = st.empty()
    ph22 = st.empty()
    ph22b = st.empty()
    ph22c = st.empty()
    ph23 = st.empty()
    ph23b = st.empty()

    ph03 = st.empty()
    ph31 = st.empty()
    ph31b = st.empty()
    ph32 = st.empty()
    ph32b = st.empty()
    ph33 = st.empty()
    ph33b = st.empty()
    ph34 = st.empty()

    ph04 = st.empty()
except:
    'error configurando phs'
ph0.info('ph0')
with ph0.container():
    regresar = st.button('volver', use_container_width=True, key='volver1')
    if regresar: switch_page('interface')
    st.markdown(':green[ $ \\bold {Hola \,\,\,' + nombreu + '}$]')
    st.title('Siguiendo las pisadas de Jesús')
    st.markdown("---")
    st.markdown("## CAPÍTULO 1 ")
    st.markdown("## Calculando el costo")
    st.markdown("""
    La Iglesia de los Hermanos es una denominación cristiana anabautista fundada en Alemania en 1708. Los Hermanos creen en la importancia de la Biblia, el discipulado, la sencillez y el pacifismo.

    Los Hermanos creen que el seguimiento de Jesús es una decisión que debe tomarse con seriedad. Jesús mismo advirtió a sus discípulos que el camino de la fe puede ser difícil. Por eso, los Hermanos creen que es importante "calcular el costo" antes de seguir a Jesús.

    Los Hermanos creen que la Iglesia es una comunidad de personas que se apoyan mutuamente en el seguimiento de Jesús. La Iglesia no es una institución, sino un grupo de creyentes que se reúnen para adorar a Dios, estudiar la Biblia y servir a los demás.

    Los Hermanos están unidos por una serie de convicciones profundas, una de las cuales es el intento de regresar a Jesús y dejarlo ser el Señor y Salvador de sus vidas.
    """)

ph01.info('ph01')
with ph01.container():
    video_link = "https://youtu.be/8eBimSwergs"
    st.video(video_link)

if st.session_state.ea2 == '':
    if st.session_state.ea1 == '':
        st.session_state.p1,st.session_state.p2,st.session_state.p3, st.session_state.p4 = cuq(1,1)    # crea/carga las preguntas iniciales
    if st.session_state.selron=='11':
        with ph1.container():
            with st.form('Formulario-11'):
                st.write('Formulario-11')
                #'SESSION :', st.session_state
                st.caption('Las siguientes son preguntas de comprensión del video anterior. Para poder continuar al siguiente video, es necesario tener un porcentaje de aciertos superior al 75% (esto es 3 respuestas correctas sobre 4). Recomendación: Mirar y escuchar el video con atención antes de contestar y dar clic al botón EVALUAR.')
                pr1 = st.radio(label=st.session_state.p1['Q'], options=st.session_state.p1['ops'])
                pr2 = st.radio(label=st.session_state.p2['Q'], options=st.session_state.p2['ops'])
                pr3 = st.radio(label=st.session_state.p3['Q'], options=st.session_state.p3['ops'])
                pr4 = st.radio(label=st.session_state.p4['Q'], options=st.session_state.p4['ops'])
                bsub1 = st.form_submit_button('$$ \\Large {👉Evaluar 01👈} $$', use_container_width=True)
                if bsub1:
                    # '***'
                    # st.write('pr1 =',pr1,'  pr2 =',pr2,'   pr3 =',pr3, '   pr4 =',pr4)
                    st.session_state.bc1=1
                    #---------
                    sumA=0
                    gooda = [st.session_state.p1['ans'], st.session_state.p2['ans'], st.session_state.p3['ans'], st.session_state.p4['ans']]
                    st.session_state.resp_u = [pr1, pr2, pr3, pr4]
                    compara = comparar_listas(gooda, st.session_state.resp_u)
                    porcen = [val*int(100/len(compara)) for val in compara]
                    #'compara = ', compara, 'porcen = ', porcen
                    for p in porcen: sumA+=p
                    # 'sumA = ', sumA
                    with st.spinner('espera un momento...'):
                            time.sleep(2)
                    #'SESSION :', st.session_state
                    if sumA>=75:
                        #st.session_state.selron='21'
                        st.session_state.ea2 = 'N2H'
                        st.session_state.ea1=''
                    else:
                        st.session_state.ea1='fallo01'   
        if  st.session_state.ea1=='fallo01':
            ph1.empty()
            st.toast('$$\\large{Repreguntando}$$')
            st.session_state.p1,st.session_state.p2,st.session_state.p3,st.session_state.p4 = cuq(2,1)
    
    if st.session_state.selron=='12':
        ph1.empty()
        with ph12.container():
            with st.chat_message('user'):
                st.warning('Primera ronda de preguntas fallida')
                st.caption('ph12')
                # st.success('video☝ visto👀 y revisado🤩     ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️ ')
                st.write('⚠️ tuviste :red[menos] del :orange[75%] de aciertos en tus respuestas🤦‍♂️')
                st.write('A continuación 👇 tienes una 2️⃣:orange[segunda oportunidad.] Revisa👀 con cuidado el video anterior☝ antes de contestar')
        
        with ph1B.container():

            with st.form('Formulario-12'):
                st.write('Formulario-12')
                #st.session_state
                pr1 = st.radio(label=st.session_state.p1['Q'], options=st.session_state.p1['ops'], horizontal=True)
                pr2 = st.radio(label=st.session_state.p2['Q'], options=st.session_state.p2['ops'], horizontal=True)
                pr3 = st.radio(label=st.session_state.p3['Q'], options=st.session_state.p3['ops'], horizontal=True)
                pr4 = st.radio(label=st.session_state.p4['Q'], options=st.session_state.p4['ops'], horizontal=True)
                bsub2 = st.form_submit_button('$$ \\Large {👉Evaluar 02👈} $$', use_container_width=True)
                
                #'SESSION :', st.session_state
                if bsub2:
                    #'***'
                    # st.write('pr1 =',pr1,'  pr2 =',pr2,'   pr3 =',pr3, '   pr4 =',pr4)
                    st.session_state.bc1B=1
                    #---------
                    sumA=0
                    gooda = [st.session_state.p1['ans'], st.session_state.p2['ans'], st.session_state.p3['ans'], st.session_state.p4['ans']]
                    st.session_state.resp_u = [pr1, pr2, pr3, pr4]
                    compara = comparar_listas(gooda, st.session_state.resp_u)
                    porcen = [val*int(100/len(compara)) for val in compara]
                    #'compara = ', compara, 'porcen = ', porcen
                    for p in porcen: sumA+=p
                    'sumA = ', sumA
                    with st.spinner('Espere un momento...'):
                            time.sleep(2)
                    #'SESSION :', st.session_state
                    if sumA>=75:
                        #st.session_state.selron='21'
                        #ph1.success('Seguimos al siguiente nivel desde Formulario 1')
                        st.toast('$$\\large{Pasamos al siguiente video}$$')
                        st.session_state.ea2 = 'N2H'
                        st.session_state.ea1=''
                    else:
                        st.toast('$$\\large{Repreguntando}$$')
                        st.session_state.ea1='fallo02' 
                    #'SESSION :', st.session_state
            ph1B2 = st.empty()
            
        if  st.session_state.ea1=='fallo02':

            ph12.empty()
            ph1B.empty()
            ph1B2.empty()
            ph1B3.empty()
            ph1C.empty()
            st.toast('$$\\large{Repreguntando}$$')
            st.session_state.p1,st.session_state.p2,st.session_state.p3,st.session_state.p4 = cuq(3,1)

                
    if st.session_state.selron=='13':
        #ph1B.warning('Segunda ronda de preguntas fallida')
        ph12.empty()
        ph1B.empty()
        ph1B2.empty()
        # ph1B3 = st.info('')
        ph1C.empty()
        with ph1B3.container():
            with st.chat_message('user'):
                st.caption('ph1B3')
                st.error('Segunda ronda de preguntas fallida')
                # st.success('video☝ visto👀 y revisado🤩     ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️ ')
                st.write('⚠️⚠️⚠️ haz tenido :red[menos] del :orange[75%] de aciertos en tus respuestas🤦‍♂️ en 2 rondas de preguntas ⚠️⚠️⚠️')
                st.write('A continuación 👇 tienes una última oportunidad. Revisa👀 con cuidado el video anterior☝ antes de contestar')
                st.warning('🛑Si :red[NO] aciertas en todas las respuestas a continuación👇, el sistema te sacará↗️ del módulo para vuelvas a empezar🛑')

        with ph1C.container():
            with st.form('Formulario-13'):
                st.caption('Formulario-13 .......................................................ph1C')
                #st.session_state
                pr1 = st.radio(label=st.session_state.p1['Q'], options=st.session_state.p1['ops'], horizontal=True)
                pr2 = st.radio(label=st.session_state.p2['Q'], options=st.session_state.p2['ops'], horizontal=True)
                pr3 = st.radio(label=st.session_state.p3['Q'], options=st.session_state.p3['ops'], horizontal=True)
                pr4 = st.radio(label=st.session_state.p4['Q'], options=st.session_state.p4['ops'], horizontal=True)
                #bsub3 = st.form_submit_button('Submit preguntas 01B')
                bsub3 = st.form_submit_button('$$ \\Large {👉Evaluar 03👈} $$', use_container_width=True)
                #'SESSION :', st.session_state
                if bsub3:
                    # '***'
                    # st.write('pr1 =',pr1,'  pr2 =',pr2,'   pr3 =',pr3,'   pr4 =',pr4)
                    st.session_state.bc1C=1
                    #'SESSION :', st.session_state
                    #---------
                    sumA=0
                    gooda = [st.session_state.p1['ans'], st.session_state.p2['ans'], st.session_state.p3['ans'], st.session_state.p4['ans']]
                    st.session_state.resp_u = [pr1, pr2, pr3, pr4]
                    compara = comparar_listas(gooda, st.session_state.resp_u)
                    porcen = [val*int(100/len(compara)) for val in compara]
                    #'compara = ', compara, 'porcen = ', porcen
                    for p in porcen: sumA+=p
                    #'sumA = ', sumA
                    with st.spinner('Espere un momento...'):
                            time.sleep(2)
                    'SESSION :', st.session_state
                    if sumA>=75:
                        #st.session_state.selron='21'
                        ph1.success('Seguimos al siguiente nivel desde Formulario 1')
                        st.toast('$$\\large{Pasamos al siguiente video}$$')
                        st.session_state.ea2 = 'N2H'
                        st.session_state.ea1=''
                    else:
                        st.toast('$$\\large{3ra \,ronda \,de}$$')
                        st.toast('$$\\large{de\, preguntas}$$')
                        st.toast('$$\\large{fallido}$$')
                        st.toast('$$\\large{Saliendo\,del}$$')
                        st.toast('$$\\large{módulo\,actual}$$')
                        #st.session_state.ea1='3ra ronda de preg cargadas' 
                        for key in st.session_state.keys():
                            del st.session_state[key]
                        switch_page('bard01')
                    #'SESSION :', st.session_state
            ph1C2 = st.empty()


if st.session_state.ea2 == 'N2H':
    st.toast('cargando 2do video')
    ph1.empty()
    ph12.empty()
    ph1B.empty()
    ph1B2.empty()
    ph1B3.empty()
    ph1C.empty()
    ph1C2.empty()
    with ph01b.container():
        with st.chat_message('user'):
            st.success('video☝ visto👀 y revisado🤩     ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️ ')
    
    if st.session_state.ea1 == '':
        st.session_state.p1,st.session_state.p2,st.session_state.p3,st.session_state.p4 = cuq(1,2)
        
    with ph02.container():
        video_link02 = 'https://youtu.be/9MHtPnYC-eA'
        st.video(video_link02)
        ph02b.info('Despúes de ver👀 el video anterior☝, contesta las siguientes👇 preguntas de comprensión🤔💭 para avanzar➡️ a la siguiente actividad')

    if st.session_state.selron=='21':  
        ph21 = st.empty()
        ph21.write('***')

        with ph21.container():
            with st.form('Formulario-21'):
                st.write('Formulario-21')
                pr1 = st.radio(label=st.session_state.p1['Q'], options=st.session_state.p1['ops'], horizontal=True)
                pr2 = st.radio(label=st.session_state.p2['Q'], options=st.session_state.p2['ops'], horizontal=True)
                pr3 = st.radio(label=st.session_state.p3['Q'], options=st.session_state.p3['ops'], horizontal=True)
                pr4 = st.radio(label=st.session_state.p4['Q'], options=st.session_state.p4['ops'], horizontal=True)
                #'SESSION :', st.session_state
                #bsub21 = st.form_submit_button('Submit preguntas 21')
                bsub21 = st.form_submit_button('$$ \\large {👉Evaluar \,Form21👈} $$', use_container_width=True)
                if bsub21:
                    #'***'
                    #st.write('pr1 =',pr1,'  pr2 =',pr2,'   pr3 =',pr3, 'pr4 =',pr4)
                    st.session_state.bc21=1
                    #'SESSION :', st.session_state
                    #---------
                    sumA=0
                    gooda = [st.session_state.p1['ans'], st.session_state.p2['ans'], st.session_state.p3['ans'], st.session_state.p4['ans']]
                    st.session_state.resp_u = [pr1, pr2, pr3, pr4]
                    compara = comparar_listas(gooda, st.session_state.resp_u)
                    porcen = [val*int(100/len(compara)) for val in compara]
                    #'compara = ', compara, 'porcen = ', porcen
                    for p in porcen: sumA+=p
                    #'sumA = ', sumA
                    with st.spinner('Espere un momento...'):
                            time.sleep(2)
                    #'SESSION :', st.session_state
                    if sumA>=75:
                        #st.session_state.selron='21'
                        # ph1.success('Seguimos al siguiente nivel desde Formulario 21')
                        st.toast('$$\\large{Pasamos}$$')
                        st.toast('$$\\large{a la }$$')
                        st.toast('$$\\large{siguiente }$$')
                        st.toast('$$\\large{actividad}$$')
                        st.session_state.ea2 = 'N3H'
                        st.session_state.ea1=''
                    else:
                        st.toast('$$\\large{Repreguntando}$$')
                        st.session_state.ea1='fallo021' 

        if  st.session_state.ea1=='fallo021':
            ph21.empty()
            st.toast('$$\\large{Repreguntando}$$')
            st.session_state.p1,st.session_state.p2,st.session_state.p3,st.session_state.p4 = cuq(2,2)

    if st.session_state.selron=='22':
        ph22.empty()
        ph02b.empty()
        #ph1.empty()
        with ph21b.container():
            with st.chat_message('user'):
                st.warning('Primera ronda de preguntas fallida')
                st.caption('ph21b')
                # st.success('video☝ visto👀 y revisado🤩     ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️ ')
                st.write('⚠️ tuviste :red[menos] del :orange[75%] de aciertos en tus respuestas🤦‍♂️')
                st.write('A continuación 👇 tienes una 2️⃣:orange[segunda oportunidad.] Revisa👀 con cuidado el video anterior☝ antes de contestar')
        with ph22.container():
            with st.form('Formulario-22'):
                st.write('Formulario-22')
                #st.session_state
                pr1 = st.radio(label=st.session_state.p1['Q'], options=st.session_state.p1['ops'], horizontal=True)
                pr2 = st.radio(label=st.session_state.p2['Q'], options=st.session_state.p2['ops'], horizontal=True)
                pr3 = st.radio(label=st.session_state.p3['Q'], options=st.session_state.p3['ops'], horizontal=True)
                pr4 = st.radio(label=st.session_state.p4['Q'], options=st.session_state.p4['ops'], horizontal=True)
                #bsub22 = st.form_submit_button('Submit preguntas 22')
                bsub22 = st.form_submit_button('$$ \\Large {👉Evaluar 22👈} $$', use_container_width=True)
                
                if bsub22:
                    st.session_state.bc22b=1
                    sumA=0
                    gooda = [st.session_state.p1['ans'], st.session_state.p2['ans'], st.session_state.p3['ans'], st.session_state.p4['ans']]
                    st.session_state.resp_u = [pr1, pr2, pr3, pr4]
                    compara = comparar_listas(gooda, st.session_state.resp_u)
                    porcen = [val*int(100/len(compara)) for val in compara]
                    #'compara = ', compara, 'porcen = ', porcen
                    for p in porcen: sumA+=p
                    #'sumA = ', sumA
                    with st.spinner('Espere un momento...'):
                            time.sleep(2)
                    #'SESSION :', st.session_state
                    if sumA>=75:
                        st.toast('$$\\large{Pasamos}$$')
                        st.toast('$$\\large{a la }$$')
                        st.toast('$$\\large{siguiente }$$')
                        st.toast('$$\\large{actividad}$$')
                        st.session_state.ea2 = 'N3H'
                        st.session_state.ea1=''
                    else:
                        st.toast('$$\\large{Repreguntando}$$')
                        st.session_state.ea1='fallo022' 
            ph22b = st.empty()

        if  st.session_state.ea1=='fallo022':
            ph22b = st.empty()
            st.toast('$$\\large{Repreguntando}$$')
            st.session_state.p1,st.session_state.p2,st.session_state.p3,st.session_state.p4 = cuq(3,2)
                #st.write('SESSION = ',st.session_state)

    if st.session_state.selron=='23':
        #ph22.warning('Segunda ronda de preguntas fallida')
        ph22.empty()
        ph22b.empty()
        ph02b.empty()
        ph21b.empty()
        with ph22c.container():
            with st.chat_message('user'):
                st.caption('ph22c')
                st.error('Segunda ronda de preguntas fallida')
                # st.success('video☝ visto👀 y revisado🤩     ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️ ')
                st.write('⚠️⚠️⚠️ haz tenido :red[menos] del :orange[75%] de aciertos en tus respuestas🤦‍♂️ en 2 rondas de preguntas ⚠️⚠️⚠️')
                st.write('A continuación 👇 tienes una última oportunidad. Revisa👀 con cuidado el video anterior☝ antes de contestar')
                st.warning('🛑Si :red[NO] aciertas en todas las respuestas a continuación👇, el sistema te sacará↗️ del módulo para que vuelvas a empezar🛑')


        with ph23.container():
            with st.form('Formulario-23'):
                st.caption('Formulario-23 .......................................................ph23')
                #st.session_state
                pr1 = st.radio(label=st.session_state.p1['Q'], options=st.session_state.p1['ops'], horizontal=True)
                pr2 = st.radio(label=st.session_state.p2['Q'], options=st.session_state.p2['ops'], horizontal=True)
                pr3 = st.radio(label=st.session_state.p3['Q'], options=st.session_state.p3['ops'], horizontal=True)
                pr4 = st.radio(label=st.session_state.p4['Q'], options=st.session_state.p4['ops'], horizontal=True)
                #bsub3 = st.form_submit_button('Submit preguntas 01B')
                bsub23 = st.form_submit_button('$$ \\Large {👉Evaluar 023👈} $$', use_container_width=True)
                #'SESSION :', st.session_state
                if bsub23:
                    # '***'
                    # st.write('pr1 =',pr1,'  pr2 =',pr2,'   pr3 =',pr3,'   pr4 =',pr4)
                    #st.session_state.bc1C=1
                    #'SESSION :', st.session_state
                    #---------
                    sumA=0
                    gooda = [st.session_state.p1['ans'], st.session_state.p2['ans'], st.session_state.p3['ans'], st.session_state.p4['ans']]
                    st.session_state.resp_u = [pr1, pr2, pr3, pr4]
                    compara = comparar_listas(gooda, st.session_state.resp_u)
                    porcen = [val*int(100/len(compara)) for val in compara]
                    #'compara = ', compara, 'porcen = ', porcen
                    for p in porcen: sumA+=p
                    #'sumA = ', sumA
                    with st.spinner('Espere un momento...'):
                            time.sleep(2)
                    #'SESSION :', st.session_state
                    if sumA>=75:
                        #st.session_state.selron='21'
                        #ph1.success('Seguimos al siguiente nivel desde Formulario 1')
                        st.toast('$$\\large{Pasamos al siguiente video}$$')
                        st.session_state.ea2 = 'N3H'
                        st.session_state.ea1=''
                    else:
                        st.toast('$$\\large{3ra \,ronda \,de}$$')
                        st.toast('$$\\large{de\, preguntas}$$')
                        st.toast('$$\\large{fallido}$$')
                        st.toast('$$\\large{Saliendo\,del}$$')
                        st.toast('$$\\large{módulo\,actual}$$')
                        #st.session_state.ea1='3ra ronda de preg cargadas' 
                        for key in st.session_state.keys():
                            del st.session_state[key]
                        switch_page('bard01')
                    #'SESSION :', st.session_state
            ph23b = st.empty()


if st.session_state.ea2 == 'N3H':
    ph21.empty()
    ph21b.empty()
    ph22.empty()
    ph22c.empty()
    ph34.empty()
    ph23.empty()
    with ph34.container():
        with st.chat_message('user'):
            st.success('video☝ visto👀 y revisado🤩     ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️  ✔️ ')
    with ph04.container():
        st.header('Sección de tareas o preguntas de aplicación y evaluación')
        with st.form('Formulario de aplicación y evaluación'):
            st.caption('''
                    
                    Las siguientes preguntas tienen la intención de que el usuario muestre reflexión y aplicación personal de la materia vista en el video.
                    Sus respuestas serán evaluadas por el comité de Educación Cristiana de Asigleh. 
                    Por tanto, trate de que sus respuestas sean lo más claro posible.
                    
                    ''')
            st.write('***')
            st.subheader('Algo que hacer')
            st.write('Esta semana haz algo que ejercite tu fe, arriésguese a ser criticado, o perder algo, por el costo de seguir a Cristo')
            algoXhacer = st.text_area(label='Cuéntanos sobre lo que hiciste por amor a Cristo que tuvo un alto costo para ti:')
            st.write('***')
            st.subheader('Algunos pasajes para estudio')
            st.write('Siguiendo sus pisadas :orange[1 Pedro 2:21]')
            st.write('Calculando el precio :orange[Lucas 14:25-33]')
            st.write('No solamente con nuestros labios :orange[Mateo 7:21-29]')
            st.write('Siendo parte de un cuerpo :orange[Romanos 12:3-8]')
            st.write('Comenzando como niños, pero... :orange[1 Corintios 3:1-9]')
            st.write('Ven, sígueme :orange[Mateo 4:18-22]')
            estudiobib = st.text_area(label='Escriba un pequeño estudio o reflexión basado en uno de los pasajes anteriores')
            st.write('***')
            st.subheader('Preguntas para discusión')
            ppd01 = st.text_area(label='Haz un contraste entre la fe que empieza con una dependencia exclusiva en Jesucristo y la fe basada en las palabras de un credo')
            ppd02 = st.text_area(label='Hay cosas en la vida en la que seguir a Cristo tiene su precio. Haz una lista de estas cosas')
            ppd03 = st.text_area(label='En tu vida cristiana, puedes hacer una lista de nuevas áreas de creencias o prácticas que han sido desarrolladas por tu decisión de seguir a Cristo')
            ppd04 = st.text_area(label='¿Por qué pertenecer a una comunidad de fe es importante?')
            butform = st.form_submit_button('Enviar/Actualizar respuestas de aplicación para evaluación', use_container_width=True)
        
regresar = st.button('volver', use_container_width=True, key='volver2')
if regresar: switch_page('interface')
        