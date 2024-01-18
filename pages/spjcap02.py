
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
    [':red[¿Cuál es el enfoque central del grupo mencionado en el video?]', ['La ley del Antiguo Testamento', 'Las enseñanzas acumuladas por la iglesia', 'Leyes espirituales respecto a la salvación', 'Jesús'], 'Jesús'],

    [':orange[Según el video, ¿quién debería ser el Señor de nuestras vidas?]', ['Pablo', 'La iglesia', 'Jesús', 'La ley del Antiguo Testamento'], 'Jesús'],

    [':red[¿Cómo se transforman las personas, según el video?]', ['A través de la acumulación de enseñanzas espirituales', 'Siguiendo la ley del Antiguo Testamento', 'Al encontrarnos con Jesús', 'Mediante la obediencia a las leyes de la iglesia'], 'Al encontrarnos con Jesús'],

    [':orange[¿En qué libro de la Biblia se hace referencia a Jesús como el principio y el fin?]', ['Mateo', 'Juan', 'Apocalipsis', 'Hechos'], 'Apocalipsis'],

    [':red[¿Cuál es la comparación que se hace entre Jesús y las estrellas en el cielo?]', ['Jesús brinda guía como las estrellas en el cielo', 'Las enseñanzas de Jesús son tan numerosas como las estrellas', 'La autoridad de Jesús es como la de las estrellas', 'La presencia de Jesús es tan visible como las estrellas'], 'Jesús brinda guía como las estrellas en el cielo'],

    [':red[¿Con qué compara el video a Jesús para brindar guía en tiempos oscuros?]', ['Una brújula', 'Mapa', 'Antorcha', 'Linterna'], 'Una brújula'],

    [':orange[Según el video, ¿qué simboliza la sangre de Jesús?]', ['Impureza', 'Perdón', 'Sentencia', 'Miedo'], 'Perdón'],

    [':red[¿Qué sabe la ciencia médica sobre la sangre, como se menciona en el video?]', ['Es fuente de impurezas', 'Es un símbolo de vida', 'Produce impurezas', 'Purifica el cuerpo'], 'Purifica el cuerpo'],

    [':orange[Según el vídeo, ¿dónde encontramos el perdón y la vida nueva?]', ['A los pies de la iglesia', 'En el altar del templo', 'Al pie de la cruz', 'En las enseñanzas de Pablo'], 'Al pie de la cruz'],

    [':orange[¿Qué se describe como la extensión del amor de Dios por nosotros en el video?]', ['Las enseñanzas de la iglesia', 'La sangre de Jesús en la cruz', 'La ley del Antiguo Testamento', 'Las leyes espirituales de la salvación'], 'La sangre de Jesús en la cruz'],

    [':red[¿Qué creen los miembros de la iglesia de los hermanos sobre Jesús?]', ['Solo es el Señor', 'Solo es el Salvador', 'Es el Señor y Salvador', 'No creen en Jesús'], 'Es el Señor y Salvado'],

    [':red[¿Cómo han recibido los miembros de la iglesia la salvación según el pasaje bíblico en Efesios 2:8 y 9?]', ['Por sus méritos', 'Por medio de la fe', 'Por sus obras', 'Por la bondad de otros'], 'Por medio de la fe'],

    [':orange[¿Quién nos ha creado según el versículo de Efesios 2:10?]', ['Nosotros mismos', 'Dios', 'Jesús', 'La iglesia de los hermanos'], 'Dios'],

    [':red[¿Cuál fue la base de las creencias de la iglesia de los hermanos, según el historiador Floyd Mallott?]', ['La imitación de Cristo', 'La adoración de Jesús como la segunda persona de la Trinidad', 'El estudio de la historia de la iglesia', 'La organización de la iglesia'], 'La imitación de Cristo'],

    [':orange[¿Qué hizo Francisco de Asís con sus riquezas?]', ['Las conservó', 'Las donó', 'Las invirtió', 'Las perdió'], 'Las donó'],

    [':red[¿Qué aportó Pedro Waldo a la iglesia de los hermanos?]', ['Teorías del Nuevo Testamento', 'Organización eclesiástica', 'Actitud práctica y devota', 'Doctrina de la inspiración'], 'Actitud práctica y devota'],

    [':orange[¿Cómo practicaban la fe Bernardo, Francisco y Waldo?]', ['Siguiendo la teoría del Nuevo Testamento', 'Aceptando la imagen de Jesús y del cristianismo primitivo', 'Rechazando la fe cristiana', 'Ignorando la cultura y la nación'], 'Aceptando la imagen de Jesús y del cristianismo primitivo'],

    [':orange[¿Qué convicciones gemelas forman la base de la fe de la iglesia de los hermanos?]', ['La fe en la teología', 'La fe en la cultura', 'Aceptar a Jesús como Señor y Salvador', 'No tienen convicciones'], 'Aceptar a Jesús como Señor y Salvador'],

    [':red[¿Qué preocupación guía a la iglesia de los hermanos en su relación con los demás?]', ['Cómo acumular riquezas', 'Cómo ejercer poder', 'Cómo vivir y relacionarse con los demás', 'No tienen preocupaciones'], 'Cómo vivir y relacionarse con los demás'],

    [':orange[¿En qué se basa la fe evangélica de la iglesia de los hermanos?]', ['Solo en la ley del Antiguo Testamento', 'Solo en las enseñanzas acumuladas de la iglesia', 'En Jesús como Señor y Salvador', 'En un grupo de leyes espirituales sobre el plan de salvación'], 'En Jesús como Señor y Salvador'],
    # Agrega más preguntas aquí
]
lista_2 = [
    [':red[¿Qué representa la Biblia para los miembros de la iglesia según el video?]', ['Un libro de historia', 'La carta de amor de Dios a la humanidad', 'Un manual de instrucciones', 'Un libro de poesía'], 'La carta de amor de Dios a la humanidad'],

    [':red[¿Por qué es importante la Biblia en relación con Jesús según el video?]', ['Nos da un trasfondo sobre la vida de Jesús', 'Es el único medio para conocer a Jesús', 'Fue escrita por Jesús', 'No tiene relación con Jesús'], 'Nos da un trasfondo sobre la vida de Jesús'],

    [':orange[¿Dónde empieza el tema de la vida de Jesús según el video?]', ['En los primeros pasajes de Génesis', 'En el Nuevo Testamento', 'En el libro de los Salmos', 'En el Antiguo Pacto'], 'En el Nuevo Testamento'],

    [':orange[¿Por qué es importante el Nuevo Testamento según el video?]', ['Porque contiene profecías sobre Jesús', 'Porque fue escrito cerca de la época de Jesús', 'No es importante', 'Porque complementa al Antiguo Testamento'], 'Porque fue escrito cerca de la época de Jesús'],

    [':red[¿Qué frase relacionada con la Biblia le gustaba citar a Carlos Seigler según el video?]', ['Lo que es nuevo está escondido en lo viejo', 'Lo nuevo siempre es mejor', 'No hay nada nuevo bajo el sol', 'La Biblia es un libro sagrado'], 'Lo que es nuevo está escondido en lo viejo'],

    [':orange[¿Qué actividad realizaron los primeros miembros de la iglesia muchos años antes de que el movimiento de la escuela dominical comenzara a expandirse?]', ['Estudios de teología', 'Estudios bíblicos serios', 'Actividades caritativas', 'Oración en grupo'], 'Estudios bíblicos serios'],

    [':red[¿En qué momento del día se llevan a cabo los estudios bíblicos en la conferencia anual de la denominación mencionada en el video?]', ['Tarde en la noche', 'Bien temprano en la mañana', 'Durante el almuerzo', 'En la tarde'], 'Bien temprano en la mañana'],

    [':orange[¿Qué tipo de estudio bíblico enfatiza la naturaleza del pacto de fe según el video?]', ['Estudio histórico', 'Estudio teológico', 'Estudio interpersonal', 'Estudio lingüístico'], 'Estudio interpersonal'],

    [':orange[¿Qué motiva a las personas que estudian en el programa de tres años llamado el pueblo del pacto a practicar lo que han aprendido?]', ['Sanciones legales', 'Promesas unos a otros y a Dios', 'Amenazas de expulsión', 'No hay motivación mencionada'], 'Promesas unos a otros y a Dios'],

    [':red[¿Qué enfatiza el programa de estudio bíblico del pueblo del pacto según el video?]', ['La historia de la iglesia', 'La naturaleza del pacto de fe, nuestras necesidades y nuestro mundo', 'La profecía bíblica', 'El estudio de los salmos'], 'La naturaleza del pacto de fe, nuestras necesidades y nuestro mundo'],

    [':red[¿Qué discuten algunos cristianos en relación con la infalibilidad de las escrituras según el video?]', ['La autoría de la Biblia', 'Las diferencias entre versiones de la Biblia', 'Si las palabras escritas en la Biblia son infalibles', 'El origen alemán de la Biblia'], 'La autoría de la Biblia'],

    [':orange[¿Por qué evita la iglesia de los hermanos los debates sobre la infalibilidad de las escrituras según el video?]', ['Por sus raíces alemanas', 'Porque consideran la Biblia como la palabra de Dios', 'Porque prefieren no discutir temas religiosos', 'Porque no le dan importancia a la Biblia'], 'Porque prefieren no discutir temas religiosos'],

    [':red[¿En qué se basaban los miembros de la iglesia de los hermanos para su dedicación a la paz y su rechazo a las guerras según el video?]', ['En la interpretación metafórica de la Biblia', 'En su lectura literal del sermón de la montaña', 'En las enseñanzas del Antiguo Testamento', 'En las tradiciones de la iglesia'], 'En su lectura literal del sermón de la montaña'],

    [':orange[¿Cómo aprendieron los miembros de la iglesia de los hermanos a buscar el mensaje divino según el video?]', ['A través de manuscritos originales', 'Leyendo frases y palabras individuales', 'Sin prestar atención a las traducciones', 'Sin fijarse en frases y palabras individuales'], 'Leyendo frases y palabras individuales'],

    [':red[¿A quién se refiere Jesús en el pasaje citado en el video: "Ustedes estudian las Escrituras con mucho cuidado porque esperan encontrar en ellas la vida eterna"?]', ['A los discípulos', 'A los fariseos', 'A los escribas', 'A sus seguidores'], 'A los fariseos'],

    [':orange[¿Quién es Jesús según el video citado en el pasaje: "Jesús es el camino, la verdad y la vida"?]', ['Un profeta', 'Un líder político', 'El alfa y la omega', 'El camino, la verdad y la vida'], 'El camino, la verdad y la vida'],

    [':red[¿Por qué fueron perseguidos los miembros de la Iglesia según el video?]', ['Por no creer en Dios', 'Por su dedicación a la paz', 'Por creer en algo diferente', 'Por su origen alemán'], 'Por su dedicación a la paz'],

    [':orange[¿Qué libertad agradecen muchos miembros de la Iglesia según el video?]', ['La libertad de expresión', 'La libertad de culto', 'La libertad para alcanzar una fe significativa', 'La libertad política'], 'La libertad de expresión'],

    [':red[¿Cómo deben ser leídos los evangelios según la perspectiva mencionada en el video?]', ['A la luz de los profetas del Antiguo Testamento', 'A la luz de la historia de la iglesia', 'A la luz de las enseñanzas del Nuevo Testamento', 'A la luz de Cristo, su mente y su espíritu'], 'A la luz de Cristo, su mente y su espíritu'],

    [':orange[¿Cuál es el punto de vista propuesto para leer las distintas partes de la Biblia según el video?]', ['Leyendo cada parte de forma aislada', 'Leyendo el Antiguo Testamento sin referencia al Nuevo Testamento', 'Leyendo cada parte a la luz de las enseñanzas del Nuevo Testamento', 'No hay un punto de vista propuesto'], 'Leyendo cada parte a la luz de las enseñanzas del Nuevo Testamento'],


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
    st.markdown("## CAPÍTULO 2 ")
    st.markdown("## Reunidos alrededor de la Palabra")
    st.markdown("""
                En el capítulo "Reunidos alrededor de la Palabra", el autor --un miembro de la iglesia-- describe las principales convicciones de la iglesia de los Hermanos, centrándose en su enfoque en Jesús, la Biblia y la práctica de la fe.

                Jesús

                La Iglesia de los Hermanos cree que Jesús es el centro de su fe. Es el Señor y el Salvador, y es el modelo que los miembros de la iglesia buscan seguir. El autor describe a Jesús como una brújula que guía a los miembros de la iglesia a través de la vida.

                La Biblia

                La Iglesia de los Hermanos cree que la Biblia es la Palabra de Dios. Es la autoridad suprema para la vida y la fe de los miembros de la iglesia. El autor afirma que la Biblia es importante porque nos da información sobre Jesús y nos ayuda a entender su mensaje.

                La práctica de la fe

                La Iglesia de los Hermanos cree que la fe debe ser vivida. Los miembros de la iglesia están comprometidos a vivir de acuerdo con las enseñanzas de Jesús. Esto incluye la práctica de la paz, la no violencia y la sencillez.

                Algunos puntos clave del escrito

                La Iglesia de los Hermanos cree que Jesús es el Señor y el Salvador.
                La Biblia es la Palabra de Dios y la autoridad suprema para la vida y la fe de los miembros de la iglesia.
                La fe debe ser vivida de acuerdo con las enseñanzas de Jesús.

                Algunos aspectos interesantes del escrito

                El autor destaca la importancia de la imitación de Cristo en la fe de la Iglesia de los Hermanos.
                El autor describe la experiencia de persecución que sufrieron los primeros miembros de la iglesia.
                El autor afirma que la Iglesia de los Hermanos es una iglesia inclusiva que respeta la libertad de expresión.

                """)

ph01.info('ph01')
with ph01.container():
    video_link = "https://youtu.be/gTvcV_vuLr8"
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
        video_link02 = 'https://youtu.be/PFBN8XELvg8'
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
            st.write('Esta semana lea el Evangelio de Mateo. Tome nota de lo que usted cree que Dios quisiera que se haga si se toma a Cristo seriamente. ')
            algoXhacer = st.text_area(label='Compártenos algunas notas de lo que usted cree que Dios quisiera que se haga si se toma a Cristo seriamente:')
            st.write('***')
            st.subheader('Algunos pasajes para estudio')
            st.write('Más allá de la página sagrad :orange[Juan 5:37-40]')
            st.write('Jesús mismo es la Palabra :orange[Juan 1]')
            st.write('Procure la salvación :orange[Filipenses 2:12-13]')
            st.write('Toda escritura es de ayuda :orange[2 Timoteo 3:16,17]')
            st.write('Ser como los bereanos :orange[Hechos 17:10 y 11]')
            st.write('La Palabra de Dios en los corazones :orange[Jeremías 31:31-34]')
            estudiobib = st.text_area(label='Escriba un pequeño estudio o reflexión basado en uno de los pasajes anteriores')
            st.write('***')
            st.subheader('Preguntas para el diálogo')
            ppd01 = st.text_area(label='Tome prestada las Biblias de dos personas que subrayan los pasajes que más le gustan. Pida que su pastor le provea de las Biblias de dos personas que sean bastante distintas a su manera de ver las cosas, aunque sean cristianos fieles. Compare las partes que cada uno ha subrayado. En algunos casos, donde termina el subrayado de uno, empieza el del otro. ¿Qué es lo que muestra esto sobre nuestra disposición de obedecer a Dios?')
            ppd02 = st.text_area(label='Comparte tu opinión acerca de cómo Bernardo de Clarebox, Francisco de Asís y Pedro Waldo, representan importantes valores enseñados por la iglesia de Los Hermanos')
            ppd03 = st.text_area(label='Algunos grupos discuten si uno va al cielo inmediatamente después que uno muere o si solo va al final de los tiempos. Ellos discuten sobre la frase de Jesús: "Yo te digo que hoy mismo estarás conmigo en el paraíso" Lucas 23:43. El propio Jesús evitó esta clase de discusiones. Lea Mateo 22:23-33, Marcos 12:18-27 y Lucas 20:27-38. Jesús dijo que Dios es fiel. Dios es el Señor sobre la vida y la muerte. ¿Cuál es tu opinión al respecto?')
            ppd04 = st.text_area(label='La vida después de la muerte será buena porque acá o allá estamos en las manos amantes del creador. ¿Podemos nosotros estar satisfechos con Jesús? ')
            ppd05 = st.text_area(label='¿O debemos saber más de lo que él pensó que seríamos capaces de entender? Lea y dialogue sobre lo que Jesús quiso decir en Mateo 22:23-35')
            ppd06 = st.text_area(label='Algunos años atrás cuando una nueva versión de la Biblia apareció en los Estados Unidos, Revised Standard Version. Revised Standard Version. En algunas áreas hubo gente que tomó copias de esta versión y las quemó porque traducía a Isaías 7:14 como una "joven" y no como a una "virgen". Los miembros de la iglesia leyeron sus Biblias en alemán y no encontraron razón para tales actitudes porque usaba la palabra "doncella". Por esto, rehusaron participar en los actos de quemar Biblias. El espíritu de la iglesia es conservador porque entienden que lo más importante no son los pequeños detalles, pero sí, el mensaje que Dios tiene para nosotros. ¿Recuerdas algún caso similar en tu vida o ministerio? ¿Cómo se resolvió?')
            ppd07 = st.text_area(label='¿Hay en la iglesia la disposición de aceptar diferentes puntos de vista?  ')
            ppd08 = st.text_area(label='¿Hay libertad para que cada uno tenga su propia opinión? ')
            butform = st.form_submit_button('Enviar/Actualizar respuestas de aplicación para evaluación', use_container_width=True)
        

regresar = st.button('volver', use_container_width=True, key='volver2')
if regresar: switch_page('interface') 