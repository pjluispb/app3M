
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
    
[':red[¿Qué ocurría con los niños en la Iglesia de los Hermanos en los países de Europa en 1708?]', ['Se les prohibía asistir a la iglesia', 'Eran bautizados automáticamente', 'No podían ser ciudadanos del Estado', 'Se les enseñaba a leer las Escrituras'], 'No podían ser ciudadanos del Estado'],

[':orange[¿Por qué los primeros miembros de la Iglesia comenzaron a preguntarse sobre el bautismo de los niños?]', ['Porque querían reformar la Iglesia oficial', 'Por el influjo de los pietistas y anabautistas', 'Por la presión del Estado', 'Por una disposición de la Iglesia oficial'], 'Por el influjo de los pietistas y anabautistas'],

[':red[¿Qué influencia tuvieron los pietistas en los primeros miembros de la Iglesia?]', ['Enfocaban el mensaje de la Iglesia en dogmas solamente', 'Promovían la participación laica en la Iglesia', 'Buscaban la reforma de la Iglesia desde afuera', 'Se oponían al estudio de las Escrituras'], 'Promovían la participación laica en la Iglesia'],

[':orange[¿Qué grupo insistía en el bautismo del creyente como evidencia de su propia decisión de haber aceptado a Cristo?]', ['Los pietistas', 'Los primeros miembros de la Iglesia', 'Los anabautistas', 'Los reformadores protestantes'], 'Los anabautistas'],

[':red[¿Qué decidieron hacer los primeros reformadores protestantes, incluyendo a Martín Lutero, en relación al bautismo?]', ['Continuar con la tradición de bautizar a los creyentes', 'Estudiar la posibilidad de bautizar al creyente', 'Oponerse al bautismo de los creyentes', 'Permitir el bautismo de los niños y los creyentes'], 'Continuar con la tradición de bautizar a los creyentes'],

[':orange[¿Qué sucedía con las personas que eran encontradas culpables del crimen de rebautizar en Suiza?]', ['Eran exiliadas del país', 'Eran ejecutadas con la pena de muerte', 'Eran multadas', 'Eran encarceladas por un tiempo determinado'], 'Eran ejecutadas con la pena de muerte'],

[':red[¿Por qué eran llamados "anabautistas"?]', ['Porque se oponían al bautismo', 'Porque querían reformar la Iglesia desde adentro', 'Porque insistían en el bautismo del creyente', 'Porque rechazaban la espiritualidad en la comunidad'], 'Porque insistían en el bautismo del creyente'],

[':orange[¿Qué enfocaban los pietistas en el mensaje de la Iglesia según el texto?]', ['La participación laica en la Iglesia', 'La espiritualidad y las necesidades diarias de la comunidad', 'La reforma de la Iglesia desde adentro', 'La promoción de dogmas solamente'], 'La espiritualidad y las necesidades diarias de la comunidad'],

[':red[¿Cuál era la disposición de la Iglesia oficial en relación al bautismo de los niños en 1708?]', ['Lo dejaba a decisión de los padres', 'Lo realizaba automáticamente', 'No lo permitía', 'Lo consideraba como un crimen'], 'Lo realizaba automáticamente'],

[':orange[¿Por qué se oponían violentamente al bautismo de los creyentes en Suiza?]', ['Porque consideraban que era una práctica anticristiana', 'Porque seguían la tradición existente', 'Porque los primeros reformadores protestantes así lo habían decidido', 'Porque consideraban que era un crimen que merecía la pena de muerte'], 'Porque consideraban que era un crimen que merecía la pena de muerte'],

[':red[¿Qué significa la palabra "bautismo" en griego según los primeros miembros de la Iglesia?]', ['Ser ungido con aceite', 'Ser sumergido', 'Ser bendecido', 'Ser purificado con agua'], 'Ser sumergido'],

[':orange[¿Qué práctica realizaba la Iglesia primitiva en relación al bautismo?]', ['Bautismo por aspersión', 'Bautismo por inmersión', 'Bautismo por unción', 'Bautismo por salpicadura'], 'Bautismo por inmersión'],

[':red[¿Qué querían representar los primeros miembros de la Iglesia al regresar a la práctica del Nuevo Testamento bautizando por inmersión a los creyentes?]', ['Estar completamente fuera de la voluntad de Dios', 'Estar completamente dentro de la voluntad de Dios', 'Estar parcialmente dentro de la voluntad de Dios', 'No representar nada en específico'], 'Estar completamente dentro de la voluntad de Dios'],

[':orange[¿Qué rechazaron los primeros miembros de la Iglesia de Los Hermanos en relación al sacramento del bautismo?]', ['La idea de que es un rito sin importancia', 'La idea de que es un rito mágico', 'La idea de que es un rito exclusivo para los sacerdotes', 'La idea de que es un rito reservado para los niños'], 'La idea de que es un rito sin importancia'],

[':red[¿Qué representan el bautismo y la Santa Cena según el video?]', ['Símbolos exteriores de una realidad que está sucediendo en el exterior', 'Símbolos exteriores de una realidad que está sucediendo en el interior', 'Símbolos de poderes mágicos', 'Símbolos de obediencia a la Iglesia'], 'Símbolos exteriores de una realidad que está sucediendo en el interior'],

[':orange[¿Qué representa el bautismo según el video en relación a la vida pasada?]', ['Representa la aceptación por parte de la familia', 'Representa un compromiso de dar toda la vida a Dios', 'Representa la limpieza de nuestro pasado', 'Representa una aspirina espiritual'], 'Representa la limpieza de nuestro pasado'],

[':red[¿Qué representa la imposición de manos después del bautismo según el texto?]', ['La aceptación por parte de la familia', 'La apertura de nuestro corazón para recibir el Espíritu Santo', 'El compromiso de dar toda la vida a Dios', 'La limpieza de nuestro pasado'], 'La apertura de nuestro corazón para recibir el Espíritu Santo'],

[':orange[¿Qué dice el Antiguo Testamento en el libro de Ezequiel en relación a la responsabilidad de cada individuo?]', ['Los hijos son castigados por los pecados de los padres', 'Los padres son castigados por los pecados de los hijos', 'Todos tienen que presentarse delante de Dios solos', 'Nadie tiene que presentarse delante de Dios solo'], 'Todos tienen que presentarse delante de Dios solos'],

[':red[¿Qué querían los primeros miembros de la Iglesia al simbolizar públicamente su decisión a través del bautismo?]', ['Ser abandonados por Dios', 'Dar a conocer su decisión de dedicar sus vidas a Dios', 'Ser considerados como miembros parciales de la familia', 'Negar su compromiso con Dios'], 'Dar a conocer su decisión de dedicar sus vidas a Dios'],

[':orange[¿Qué representa el bautismo y la imposición de manos después del bautismo en relación a la comunidad religiosa?]', ['La exclusión de los nuevos miembros de la comunidad', 'La aceptación por parte de la familia al nuevo miembro como hijo completo', 'La imposición de una carga adicional a los nuevos miembros', 'La separación de los nuevos miembros de la comunidad'], 'La aceptación por parte de la familia al nuevo miembro como hijo completo'],
# Agrega más preguntas aquí
]
lista_2 = [
[':red[¿Cuántas preguntas se hacen durante el bautismo según el texto?]', ['Dos preguntas', 'Tres preguntas', 'Cuatro preguntas', 'Cinco preguntas'], 'Tres preguntas'],

[':red[¿Qué se le pregunta a la persona durante el bautismo en relación a Jesús?]', ['¿Crees que Jesús es un profeta?', '¿Crees que Jesús es el Hijo de Dios?', '¿Crees que Jesús es un maestro sabio?', '¿Crees que Jesús es un líder político?'], '¿Crees que Jesús es el Hijo de Dios?'],

[':red[¿Qué se le pregunta a la persona durante el bautismo en relación al pecado y a vivir de acuerdo al ejemplo de Jesús?]', ['¿Prometes seguir tus propios deseos?', '¿Dejas voluntariamente el pecado y buscas vivir de acuerdo al ejemplo de Jesús?', '¿Te comprometes a seguir las normas sociales establecidas?', '¿Te comprometes a vivir como te plazca sin restricciones?'], '¿Dejas voluntariamente el pecado y buscas vivir de acuerdo al ejemplo de Jesús?'],

[':red[¿Qué se le pregunta a la persona durante el bautismo en relación a la iglesia?]', ['¿Prometes ser fiel a tus amigos?', '¿Prometes ser fiel a la iglesia y sostenerla con tus oraciones, asistencia, dones y finanzas?', '¿Prometes ser fiel a tus propios intereses?', '¿Prometes no asistir a la iglesia?'], '¿Prometes ser fiel a la iglesia y sostenerla con tus oraciones, asistencia, dones y finanzas?'],

[':red[¿Qué forma se utiliza al bautizar a la persona de acuerdo al texto?]', ['Forma tradicional', 'Forma moderna', 'Forma que Jesús usó en la Gran Comisión', 'Forma que el pastor elige en el momento'], 'Forma que Jesús usó en la Gran Comisión'],

[':red[¿Qué siente el creyente al ser bautizado, según el video?]', ['Tristeza y arrepentimiento', 'Gran liberación, desaparición de cargas y un nuevo gozo', 'Confusión y miedo', 'Nada en particular'], 'Gran liberación, desaparición de cargas y un nuevo gozo'],

[':red[¿Qué representa la imposición de manos después del bautismo según el texto?]', ['Un antiguo símbolo de ser lleno del Espíritu Santo', 'Un gesto de aprobación de la congregación', 'Un símbolo de aceptación en la comunidad', 'Una práctica obsoleta sin significado real'], 'Un antiguo símbolo de ser lleno del Espíritu Santo'],

[':red[¿Qué simboliza la entrada al agua y el bautismo según el texto?]', ['La llegada a una nueva etapa de la vida', 'La muerte de la vieja naturaleza', 'La purificación espiritual', 'Nada en particular'], 'La muerte de la vieja naturaleza'],

[':red[¿Qué requisito tiene la Iglesia de los Hermanos para recibir nuevos miembros de otras congregaciones cristianas?]', ['Requiere que sean rebautizados', 'No requiere rebautismo si están satisfechos con su primer bautismo', 'No acepta miembros de otras congregaciones', 'Exige una confirmación adicional de la fe'], 'No requiere rebautismo si están satisfechos con su primer bautismo'],

[':red[¿Cómo describe la Iglesia de los Hermanos su práctica de bautizar a los creyentes?]', ['Bautiza a los creyentes con aspersión', 'Bautiza a los creyentes con inmersión trina', 'No practica el bautismo', 'Bautiza a los creyentes con inmersión única'], 'Bautiza a los creyentes con inmersión trina'],

[':red[¿Dónde insistían muchos de los primeros miembros de la Iglesia en que se hiciera el bautismo?]', ['En fuentes termales', 'En riachuelos', 'En piscinas', 'En el mar'], 'En riachuelos'],

[':red[¿Cuándo ocurrieron los primeros bautismos en los Estados Unidos, según el video?]', ['25 de diciembre de 1623', '25 de diciembre de 1723', '25 de diciembre de 1823', '25 de diciembre de 1923'], '25 de diciembre de 1723'],

[':red[¿Qué tenían que hacer los miembros de las Iglesias en aquellos tiempos para llevar a cabo el bautismo, según el video?]', ['Romper el hielo', 'Construir un bautisterio', 'Viajar al mar', 'Llevar a cabo el bautismo en la primavera'], 'Romper el hielo'],

[':red[¿Qué representaba el bautismo para los anabautistas desde el principio, según el texto?]', ['Un acto simbólico sin mayor significado', 'Una disposición de seguir a Cristo incondicionalmente, incluso si significaba sufrimiento', 'Un simple ritual de iniciación', 'Una actividad social sin implicaciones espirituales'], 'Una disposición de seguir a Cristo incondicionalmente, incluso si significaba sufrimiento'],

[':red[¿Qué representa el bautismo según la escritura mencionada en el video?]', ['Una nueva vida', 'Una obligación', 'Una tradición', 'Un castigo'], 'Una nueva vida'],

[':red[¿Qué se menciona como la consecuencia de bautizarnos, según el video?]', ['Enfrentar la vida solos', 'Ir con Dios de una nueva forma y tener una familia de hermanos en la fe', 'No tener ninguna responsabilidad', 'Perder la conexión con la comunidad de fe'], 'Ir con Dios de una nueva forma y tener una familia de hermanos en la fe'],

[':red[¿Qué hacen los miembros de la iglesia en lugar de bautizar a los infantes, según el video?]', ['Los bautizan en el templo', 'Los llevan al mar para bautizarlos', 'Los traen para dedicarlos al Señor', 'No realizan ninguna ceremonia'], 'Los traen para dedicarlos al Señor'],

[':red[¿Cuándo puede llevarse a cabo la ceremonia de presentación de niños, según el video?]', ['Solo una vez al año', 'Cerca de la Navidad o en el día de las madres, por lo menos dos veces al año o en otras ocasiones a petición de los padres', 'Sólo en primavera', 'Durante el verano'], 'Cerca de la Navidad o en el día de las madres, por lo menos dos veces al año o en otras ocasiones a petición de los padres'],

[':red[¿Qué se les pide a los padres durante la ceremonia de presentación de niños, según el video?]', ['Renovar su pasaporte', 'Renovar su dedicación a Dios y su compromiso con la iglesia para usar los recursos que ésta provee para criar a sus hijos', 'No se les pide nada en particular', 'Abandonar su fe'], 'Renovar su dedicación a Dios y su compromiso con la iglesia para usar los recursos que ésta provee para criar a sus hijos'],

[':red[¿Qué se le pide a la congregación durante la ceremonia de presentación de niños?]', ['Afirmar que están dispuestos a apoyar a los padres con la oración y el compañerismo espiritual', 'No se les pide nada en particular', 'Que abandonen la iglesia', 'Que se queden en silencio durante la ceremonia'], 'Afirmar que están dispuestos a apoyar a los padres con la oración y el compañerismo espiritual'],


    # Agrega más preguntas aquí
]

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
    st.title('Siguiendo las pisadas de Jesús')
    st.markdown("---")
    st.markdown("## CAPÍTULO 3 ")
    st.markdown("## El Bautismo del Creyente")
    st.markdown("""
                En este capítulo se describe la práctica del bautismo en la Iglesia de los Hermanos. Comienza con una explicació sobre que la Iglesia de los Hermanos cree que el bautismo es un acto de compromiso personal con Cristo, y que debe ser realizado por adultos que han hecho una decisión consciente de seguir a Jesús.

                Luego se discute la historia del bautismo en la Iglesia de los Hermanos. Se señala que los primeros miembros de la iglesia se basaron en las enseñanzas de los anabaptistas, un grupo de cristianos que creían en el bautismo del creyente. Los anabaptistas fueron perseguidos por sus creencias, y algunos incluso fueron ejecutados por rebautizarse.

                Se explican los requisitos para el bautismo en la Iglesia de los Hermanos. Los candidatos al bautismo deben responder afirmativamente a tres preguntas:

                ¿Crees que Jesús es el Hijo de Dios y que él trajo a la tierra el Evangelio salvador?
                ¿Dejas voluntariamente el pecado y con la ayuda de Dios buscas vivir de acuerdo al ejemplo y enseñanza de Jesús?
                ¿Prometes ser fiel a la iglesia? ¿Prometes sostenerla con tus oraciones, asistencia, dones y finanzas?
                Si el candidato responde afirmativamente a estas preguntas, el pastor lo bautiza por inmersión trina en el nombre del Padre, del Hijo y del Espíritu Santo.

                Se concluye señalando que el bautismo es una señal de la nueva vida que Cristo ofrece a todos los que creen en él. El bautismo es un acto de fe y compromiso, y es un paso importante en el camino de la discipulado cristiano.

                Algunos puntos clave son:

                La Iglesia de los Hermanos cree que el bautismo es un acto de compromiso personal con Cristo.
                Los primeros miembros de la Iglesia de los Hermanos se basaron en las enseñanzas de los anabaptistas.
                Los requisitos para el bautismo en la Iglesia de los Hermanos incluyen responder afirmativamente a tres preguntas.
                El bautismo es una señal de la nueva vida que Cristo ofrece a todos los que creen en él.

                La dedicación de los infantes

                La Iglesia de los Hermanos no bautiza a los infantes. En lugar de ello, los padres llevan a sus hijos a la iglesia para dedicarlos a Dios. Esta ceremonia se basa en los ejemplos bíblicos de Ana, que dedicó a su hijo Samuel al Señor, y de María y José, que llevaron a Jesús al templo para presentarlo.

                Significado de la dedicación de los infantes

                La dedicación de los infantes es una manera de expresar la fe de los padres en que sus hijos serán criados en el conocimiento y el amor de Dios. Es también una oportunidad para que la iglesia apoye a los padres en su tarea de criar a sus hijos.

                Conclusiones

                El bautismo es un acto importante en la fe de la Iglesia de los Hermanos. Representa un compromiso con Dios y con la iglesia. La Iglesia de los Hermanos practica el bautismo por inmersión y no bautiza a los infantes. En lugar de ello, los padres llevan a sus hijos a la iglesia para dedicarlos a Dios.

                """)

ph01.info('ph01')
with ph01.container():
    video_link = "https://youtu.be/W-PPO36y-Dc"
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
                    'sumA = ', sumA
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
                st.write('⚠️ tuviste :red[menos] del :orange[75%] de aciertos en tus respuestas🤦‍♂️'+sumA)
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
                    'sumA = ', sumA
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
        video_link02 = 'https://youtu.be/0QJB7rCGDlk'
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
                    'sumA = ', sumA
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
                    'sumA = ', sumA
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
                    'sumA = ', sumA
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
            st.write('Pida perdón a alguien a quien usted haya ofendido y haga lo necesario para que la reconciliación se efectúe. ')
            # algoXhacer = st.text_area(label='Compártenos algunas notas de lo que usted cree que Dios quisiera que se haga si se toma a Cristo seriamente:')
            st.write('***')
            st.subheader('Algunos pasajes para estudio')
            st.write('La Gran Comisión :orange[Mateo 28:18-20]')
            st.write('¿Qué debemos hacer? :orange[Hechos 2:37-38]')
            st.write('Bautismo por inmersión :orange[Hechos 8:26-40]')
            st.write('Significado del bautismo :orange[Romanos 6:1-11]')
            st.write('Jesús bendice a los niñoss :orange[Mateo 19:13-15, Marcos 10 13-16 y Lucas 18:15-17]')

            estudiobib = st.text_area(label='Escriba un pequeño estudio o reflexión basado en uno de los pasajes anteriores')
            st.write('***')
            st.subheader('Preguntas para el diálogo')
            ppd01 = st.text_area(label='El bautismo de adultos comparado con el bautismo de infantes es algo que debe considerarse hoy. ¿sí o no?. ')
            ppd02 = st.text_area(label='¿Los infantes que no fueron bautizados serán condenados por esto?')
            ppd03 = st.text_area(label='¿Cuál es la diferencia entre sacramento y ordenanza?')
            ppd04 = st.text_area(label='¿Cuál es la diferencia en la vida de las personas al ser bautizados?  ')
            
            butform = st.form_submit_button('Enviar/Actualizar respuestas de aplicación para evaluación', use_container_width=True)
        

        