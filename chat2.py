import streamlit as st

# Título del chatbot
st.title('El Instituto Superior de Formación Técnica Nº 12')

# Menú de opciones
opcion = st.selectbox(
    "Selecciona una opción:", 
    [
        "Técnicaturas", 
        "Instituto",  
        "Encuesta personal", 
        "Test vocacional", 
        "Ingreso"
    ], 
    key='menu_opcion'
)

# Lógica para la opción de Técnicaturas
if opcion == "Técnicaturas":
    st.subheader("Información sobre Técnicaturas")
    tecnicatura = st.selectbox(
        "Elige la tecnicatura que te interesa:", 
        [
            "Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos", 
            "Tecnicatura Superior en Análisis de Sistemas", 
            "Tecnicatura Superior en Desarrollo de Software", 
            "Tecnicatura Superior en Administración Contable", 
            "Tecnicatura Superior en Administración Financiera", 
            "Tecnicatura Superior en Higiene y Seguridad en el Trabajo", 
            "Tecnicatura Superior en Ceremonial y Protocolo", 
            "Certificación Superior en Salud y Seguridad Ocupacional en el Trabajo"
        ],
        key='tecnicatura_opcion'
    )
    
    if tecnicatura == "Tecnicatura Superior en Administración Financiera":
        st.write(f"Has seleccionado {tecnicatura}. Aquí tienes información relevante sobre esta tecnicatura.")
        
        # Información específica sobre Administración Financiera
        st.subheader("Preguntas y Respuestas sobre Administración Financiera")
        
        preguntas_respuestas = {
            "1. ¿Cuál es la carga horaria total de la Tecnicatura Superior en Administración Financiera?":
            "La carga horaria total es de 1824 horas reloj, distribuidas a lo largo de 32 semanas anuales durante un período de 3 años.",
            
            "2. ¿Cómo se distribuyen las horas entre los diferentes campos formativos?":
            "La distribución es la siguiente:\n"
            "● Formación General: 192 horas (11%)\n"
            "● Formación de Fundamento: 416 horas (23%)\n"
            "● Formación Específica: 736 horas (40%)\n"
            "● Prácticas Profesionalizantes: 480 horas (26%).",
            
            "3. ¿Qué materias son correlativas para el segundo año de la carrera?":
            "Algunas materias correlativas incluyen:\n"
            "● Contabilidad de Gestión (debe tener aprobado Principios de Contabilidad)\n"
            "● Matemática Financiera (debe tener aprobado Fundamentos de Matemática)\n"
            "● Práctica Profesionalizante 2 (debe tener aprobado Práctica Profesionalizante 1).",
            
            "4. ¿Qué son las prácticas profesionalizantes y cómo se organizan?":
            "Las prácticas profesionalizantes son experiencias que permiten a los estudiantes aplicar los conocimientos adquiridos en un entorno laboral real. Deben ser organizadas, implementadas y evaluadas por la institución educativa, bajo el control de la respectiva Jurisdicción.",
            
            "5. ¿Cuántas horas de prácticas profesionalizantes se realizan en cada año de la carrera?":
            "La cantidad de horas de prácticas profesionalizantes es la siguiente:\n"
            "● Primer año: 96 horas\n"
            "● Segundo año: 128 horas\n"
            "● Tercer año: 256 horas.",
            
            "6. ¿Qué habilidades se desarrollan a través de las prácticas profesionalizantes?":
            "Las prácticas profesionalizantes permiten desarrollar habilidades como el trabajo en equipo, la resolución de problemas y promueven una visión global e integrada de la formación.",
            
            "7. ¿Qué enfoque se debe considerar en la planificación de las prácticas profesionalizantes?":
            "En la planificación de las prácticas profesionalizantes se debe incluir un enfoque de género que garantice la equidad en el acceso a estas instancias de aprendizaje.",
            
            "8. ¿Cuáles son los objetivos específicos de la Tecnicatura Superior en Administración Financiera?":
            "Los objetivos específicos son:\n"
            "● Formar profesionales capaces de comprender y gestionar la complejidad de las organizaciones sociales.\n"
            "● Proporcionar herramientas y conocimientos para intervenir de manera crítica en las organizaciones.\n"
            "● Desarrollar competencias técnicas en administración, finanzas y contabilidad.\n"
            "● Promover la creación de proyectos innovadores.",
            
            "9. ¿Qué tipo de salidas laborales ofrece esta carrera?":
            "La Tecnicatura ofrece salidas laborales como:\n"
            "● Administrador financiero en empresas.\n"
            "● Asesor en gestión financiera.\n"
            "● Analista de costos y presupuestos.",
            
            "10. ¿Cuáles son los requisitos de ingreso para esta tecnicatura?":
            "Los requisitos incluyen:\n"
            "● Título de educación secundaria completo.\n"
            "● A veces se requiere examen de ingreso o entrevista personal.",
            
            "11. ¿Hay equivalencias con otras carreras?":
            "Sí, contempla equivalencias con otras carreras, especialmente aquellas de educación secundaria técnica."
        }

        # Usar expander para preguntas y respuestas
        for pregunta, respuesta in preguntas_respuestas.items():
            with st.expander(pregunta):
                st.write(respuesta)

                

    # Información adicional
    st.write("En esta sección puedes incluir información sobre materias, salida laboral, etc.")
    st.write("Test de orientación para identificar si esta tecnicatura es adecuada para ti.")

# Lógica para la opción de Instituto
elif opcion == "Instituto":
    st.subheader("Información sobre el Instituto")
    info = st.selectbox("Elige la información que buscas:", 
                        ["Documentación", "Programas de estudio", "Inscripción", "Instagram/Facebook"],
                        key='info_opcion')
    
    if info == "Documentación":
        st.write("Documentación necesaria para inscripción: DNI, título secundario, formulario completo, etc.")
    elif info == "Programas de estudio":
        st.write("Aquí encontrarás el plan de estudios de cada tecnicatura.")
    elif info == "Inscripción":
        st.write("Inscripción abierta desde marzo a julio. Para más detalles, consulta la página web.")
    elif info == "Instagram/Facebook":
        st.write("Síguenos en nuestras redes sociales para estar al tanto de las novedades.")


elif opcion == "Encuesta personal":
    st.subheader("Encuesta personal")

    # Formulario de encuesta
    with st.form("Formulario de Encuesta"):
        # Datos personales
        st.header("Datos Personales")
        nombre = st.text_input("Nombre", key='nombre_input')
        apellido = st.text_input("Apellido", key='apellido_input')
        fecha_nacimiento = st.date_input("Fecha de Nacimiento", key='fecha_nacimiento_input')
        dni = st.text_input("DNI", key='dni_input')
        cuil = st.text_input("CUIL", key='cuil_input')
        nacionalidad = st.text_input("Nacionalidad", key='nacionalidad_input')
        tiene_hijos = st.radio("¿Tiene hijos?", ("Sí", "No"), key='tiene_hijos_radio')
        
        # Domicilio
        st.header("Domicilio")
        calle = st.text_input("Calle", key='calle_input')
        numero = st.text_input("Nº", key='numero_input')
        codigo_postal = st.text_input("Código Postal", key='codigo_postal_input')
        provincia = st.text_input("Provincia", key='provincia_input')
        localidad = st.text_input("Localidad", key='localidad_input')
        telefono = st.text_input("Número de Teléfono", key='telefono_input')
        correo = st.text_input("Correo Electrónico", key='correo_input')

        # Información de salud
        st.header("Información de Salud")
        padece_condicion = st.radio("¿Padece o ha padecido alguna condición de salud?", ("Sí", "No"), key='padece_condicion_radio')
        condicion_cual = st.text_input("¿Cuál?", key='condicion_cual_input') if padece_condicion == "Sí" else ""
        alergia_grave = st.radio("¿Padece o ha padecido algún tipo de alergia grave?", ("Sí", "No"), key='alergia_grave_radio')
        alergia_cual = st.text_input("¿Cuál?", key='alergia_cual_input') if alergia_grave == "Sí" else ""
        medicacion = st.radio("¿Recibe de manera habitual algún tipo de medicación?", ("Sí", "No"), key='medicacion_radio')
        operacion = st.radio("¿Tuvo alguna operación?", ("Sí", "No"), key='operacion_radio')
        motivo_operacion = st.text_input("En caso afirmativo, ¿por qué motivo?", key='motivo_operacion_input') if operacion == "Sí" else ""
        obra_social = st.radio("¿Posee obra social?", ("Sí", "No"), key='obra_social_radio')
        obra_social_nombre = st.text_input("Obra Social", key='obra_social_nombre_input') if obra_social == "Sí" else ""
        numero_afiliado = st.text_input("Nº Afiliado", key='numero_afiliado_input') if obra_social == "Sí" else ""

        # Estudios cursados
        st.header("Estudios Cursados")
        secundaria_completo = st.radio("¿Tiene secundaria completa?", ("Sí", "No"), key='secundaria_completo_radio')
        instituto_titulo = st.text_input("Instituto que emite el título", key='instituto_titulo_input') if secundaria_completo == "Sí" else ""
        otros_estudios = st.text_area("Otros estudios superiores realizados", key='otros_estudios_text_area')

        # Botón para enviar el formulario
        enviado = st.form_submit_button("Enviar")

        if enviado:
            # Configurar el servidor SMTP
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_user = 'tu_email@gmail.com'  # Cambia a tu correo electrónico
            smtp_password = 'tu_contraseña'  # Cambia a tu contraseña

            # Crear el mensaje
            mensaje = MIMEMultipart()
            mensaje['From'] = smtp_user
            mensaje['To'] = 'bibliotecaidoce@gmail.com'
            mensaje['Subject'] = Header('Formulario de Encuesta Personal', 'utf-8')

            cuerpo = f"""
            Datos Personales:
            Nombre: {nombre}
            Apellido: {apellido}
            Fecha de Nacimiento: {fecha_nacimiento}
            DNI: {dni}
            CUIL: {cuil}
            Nacionalidad: {nacionalidad}
            ¿Tiene hijos?: {tiene_hijos}

            Domicilio:
            Calle: {calle}
            Nº: {numero}
            Código Postal: {codigo_postal}
            Provincia: {provincia}
            Localidad: {localidad}
            Número de Teléfono: {telefono}
            Correo Electrónico: {correo}

            Información de Salud:
            ¿Padece o ha padecido alguna condición de salud?: {padece_condicion}
            ¿Cuál?: {condicion_cual}
            ¿Padece o ha padecido algún tipo de alergia grave?: {alergia_grave}
            ¿Cuál?: {alergia_cual}
            ¿Recibe de manera habitual algún tipo de medicación?: {medicacion}
            ¿Tuvo alguna operación?: {operacion}
            En caso afirmativo, ¿por qué motivo?: {motivo_operacion}
            ¿Posee obra social?: {obra_social}
            Obra Social: {obra_social_nombre}
            Nº Afiliado: {numero_afiliado}

            Estudios Cursados:
            ¿Tiene secundaria completa?: {secundaria_completo}
            Instituto que emite el título: {instituto_titulo}
            Otros estudios superiores realizados: {otros_estudios}
            """
            # Usar UTF-8 para el cuerpo del mensaje
            mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

            # Enviar el mensaje
            try:
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_user, smtp_password)
                    server.send_message(mensaje)
                st.success("Formulario enviado correctamente.")
            except Exception as e:
                st.error(f"No se pudo enviar el formulario. Error: {e}")


# Sección de Test vocacional
elif opcion == "Test vocacional":
    st.subheader("Test vocacional")

    # Definición de preguntas y opciones
    preguntas = {
        "¿Cómo te sientes trabajando con tecnología y sistemas?": [
            "Me encanta descubrir cómo los dispositivos se conectan e interactúan entre sí.",
            "Me interesa analizar y resolver problemas complejos de sistemas informáticos.",
            "Disfruto desarrollando software y creando nuevas aplicaciones.",
            "No tengo mucho interés en la tecnología, prefiero enfocarme en aspectos financieros o administrativos.",
            "Me interesa asegurarme de que los procesos en el trabajo sean seguros y eficientes.",
            "Prefiero trabajar en un entorno donde se gestionen eventos y ceremonias.",
            "Estoy más interesado en temas de contabilidad y finanzas.",
            "Me gustaría trabajar en la protección y seguridad de los empleados en ambientes de salud."
        ],
        "¿Qué tipo de tareas disfrutas más?": [
            "Diseñar y gestionar redes y sistemas integrados.",
            "Analizar datos y mejorar la eficiencia de los sistemas.",
            "Programar y desarrollar aplicaciones o software.",
            "Llevar a cabo tareas relacionadas con la contabilidad y la gestión de recursos financieros.",
            "Asegurar un entorno de trabajo seguro y saludable.",
            "Organizar y coordinar eventos y protocolos.",
            "Administrar y controlar aspectos financieros en una organización.",
            "Trabajar en la prevención y seguridad en entornos de salud."
        ],
        "¿Cuál de estas actividades te atrae más?": [
            "Trabajar con sistemas de Internet de las Cosas y dispositivos inteligentes.",
            "Resolver problemas técnicos y mejorar el rendimiento de los sistemas.",
            "Desarrollar programas y aplicaciones de software.",
            "Gestionar la contabilidad y los libros financieros de una empresa.",
            "Implementar y supervisar medidas de seguridad en el lugar de trabajo.",
            "Coordinar eventos y asegurarse de que se cumplan los protocolos adecuados.",
            "Planificar y controlar el flujo financiero y los presupuestos.",
            "Asegurar el cumplimiento de las normativas de salud y seguridad en el entorno laboral."
        ],
        "¿Qué habilidades te gustaría desarrollar más?": [
            "Programación y diseño de sistemas integrados.",
            "Análisis de sistemas y resolución de problemas técnicos.",
            "Desarrollo y mantenimiento de aplicaciones de software.",
            "Contabilidad y administración financiera.",
            "Implementación de medidas de seguridad y protocolos de prevención.",
            "Organización y planificación de eventos y ceremonias.",
            "Control y planificación financiera.",
            "Gestión de seguridad y salud en el entorno laboral."
        ],
        "¿Cómo te imaginas tu entorno de trabajo ideal?": [
            "En un entorno dinámico, trabajando con tecnología avanzada y sistemas inteligentes.",
            "En un lugar donde pueda analizar y mejorar la tecnología y los sistemas existentes.",
            "En una oficina de desarrollo, creando y programando nuevas aplicaciones.",
            "En una oficina de contabilidad, gestionando y analizando información financiera.",
            "En un entorno enfocado en la seguridad, implementando y supervisando normas de prevención.",
            "En un entorno relacionado con la organización de eventos y protocolo.",
            "En una oficina financiera, manejando presupuestos y planes financieros.",
            "En un entorno de salud, asegurando la protección y bienestar de los trabajadores."
        ],
        "¿Cuál es tu principal motivación para elegir una carrera?": [
            "Trabajar con tecnología avanzada y sistemas innovadores.",
            "Resolver problemas complejos y mejorar sistemas tecnológicos.",
            "Crear y desarrollar nuevas aplicaciones y software.",
            "Gestionar finanzas y contabilidad de manera efectiva.",
            "Asegurar un entorno laboral seguro y saludable.",
            "Coordinar eventos y garantizar el cumplimiento de protocolos.",
            "Planificar y controlar aspectos financieros en una empresa.",
            "Garantizar la seguridad y salud en el entorno laboral."
        ]
    }

    respuestas = {pregunta: st.selectbox(pregunta, opciones, key=f'respuesta_{pregunta}') for pregunta, opciones in preguntas.items()}
    
    if st.button("Finalizar Test"):
        # Definir descripciones para cada carrera
        descripciones = {
            "Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos": "Se centra en el diseño y gestión de redes y sistemas integrados que utilizan Internet de las Cosas (IoT) y dispositivos embebidos.",
            "Tecnicatura Superior en Análisis de Sistemas": "Se enfoca en el análisis, diseño y mejora de sistemas informáticos, con un enfoque en la resolución de problemas técnicos.",
            "Tecnicatura Superior en Desarrollo de Software": "Está orientada a la creación, desarrollo y mantenimiento de aplicaciones y software para diversas plataformas.",
            "Tecnicatura Superior en Administración Contable": "Aborda la gestión contable y administrativa de una empresa, incluyendo la preparación de informes financieros y auditoría.",
            "Tecnicatura Superior en Administración Financiera": "Se dedica a la planificación, gestión y control de recursos financieros dentro de una organización.",
            "Tecnicatura Superior en Higiene y Seguridad en el Trabajo": "Se especializa en implementar y supervisar políticas y medidas de seguridad para garantizar un entorno de trabajo seguro y saludable.",
            "Tecnicatura Superior en Ceremonial y Protocolo": "Enfocada en la organización y coordinación de eventos, ceremonias y protocolos, garantizando su correcta ejecución.",
            "Certificación Superior en Salud y Seguridad Ocupacional en el Trabajo en los Establecimientos de Salud": "Se centra en la protección y seguridad de los empleados en el entorno de salud, asegurando el cumplimiento de normativas y protocolos."
        }

        # Definir la lógica para asignar puntos a cada carrera
        puntuaciones = {
            "Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos": 0,
            "Tecnicatura Superior en Análisis de Sistemas": 0,
            "Tecnicatura Superior en Desarrollo de Software": 0,
            "Tecnicatura Superior en Administración Contable": 0,
            "Tecnicatura Superior en Administración Financiera": 0,
            "Tecnicatura Superior en Higiene y Seguridad en el Trabajo": 0,
            "Tecnicatura Superior en Ceremonial y Protocolo": 0,
            "Certificación Superior en Salud y Seguridad Ocupacional en el Trabajo en los Establecimientos de Salud": 0
        }

        # Mapear respuestas a carreras
        respuestas_carrera = {
            "Me encanta descubrir cómo los dispositivos se conectan e interactúan entre sí.": "Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos",
            "Me interesa analizar y resolver problemas complejos de sistemas informáticos.": "Tecnicatura Superior en Análisis de Sistemas",
            "Disfruto desarrollando software y creando nuevas aplicaciones.": "Tecnicatura Superior en Desarrollo de Software",
            "No tengo mucho interés en la tecnología, prefiero enfocarme en aspectos financieros o administrativos.": ["Tecnicatura Superior en Administración Contable", "Tecnicatura Superior en Administración Financiera"],
            "Me interesa asegurarme de que los procesos en el trabajo sean seguros y eficientes.": ["Tecnicatura Superior en Higiene y Seguridad en el Trabajo", "Certificación Superior en Salud y Seguridad Ocupacional en el Trabajo en los Establecimientos de Salud"],
            "Prefiero trabajar en un entorno donde se gestionen eventos y ceremonias.": "Tecnicatura Superior en Ceremonial y Protocolo",
            "Estoy más interesado en temas de contabilidad y finanzas.": ["Tecnicatura Superior en Administración Contable", "Tecnicatura Superior en Administración Financiera"],
            "Me gustaría trabajar en la protección y seguridad de los empleados en ambientes de salud.": "Certificación Superior en Salud y Seguridad Ocupacional en el Trabajo en los Establecimientos de Salud"
        }

        # Asignar puntos a cada carrera según las respuestas
        for pregunta, respuesta in respuestas.items():
            if respuesta in respuestas_carrera:
                carreras = respuestas_carrera[respuesta]
                if isinstance(carreras, list):
                    for carrera in carreras:
                        puntuaciones[carrera] += 1
                else:
                    puntuaciones[carreras] += 1
        
        # Ordenar carreras por puntuación
        carreras_ordenadas = sorted(puntuaciones.items(), key=lambda x: x[1], reverse=True)
        
        # Mostrar las 3 principales recomendaciones
        st.write("Basado en tus respuestas, aquí tienes las 3 carreras que podrían ser más adecuadas para ti:")

        for carrera, _ in carreras_ordenadas[:3]:
            st.write(f"**{carrera}:** {descripciones[carrera]}")


import streamlit as st
import streamlit.components.v1 as components

# Si el usuario selecciona "Ingreso", mostrar el chat
if opcion == "Ingreso":
    st.subheader("Ingreso")
    st.title("Asistente Virtual - Nova")

    # HTML y CSS para simular un chat estilo WhatsApp
    html_code = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            .chat-container {
                width: 100%;
                max-width: 600px;
                margin: auto;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                background-color: #f8f9fa;
            }
            .chat-box {
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                height: 400px;
                overflow-y: auto;
                background-color: #e5ddd5;
            }
            .message {
                display: inline-block;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 10px;
                max-width: 70%;
                font-size: 14px;
            }
            .user-message {
                background-color: #dcf8c6;
                align-self: flex-end;
                margin-left: auto;
            }
            .bot-message {
                background-color: #fff;
                align-self: flex-start;
                margin-right: auto;
            }
            #chat-log {
                display: flex;
                flex-direction: column;
            }
            .chat-input {
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="chat-container">
            <div class="chat-box">
                <div id="chat-log"></div>
            </div>
            <form id="chat-form" class="chat-input">
                <input type="text" id="user-message" placeholder="Escribe tu mensaje aquí..." class="form-control">
                <button type="submit" class="btn btn-primary mt-2">Enviar</button>
            </form>
        </div>

        <script>
            var firstMessage = true;

            document.getElementById('chat-form').onsubmit = function (e) {
                e.preventDefault();
                var message = document.getElementById('user-message').value;

                // Mostrar el mensaje del usuario
                var chatLog = document.getElementById('chat-log');
                var userMessageDiv = document.createElement("div");
                userMessageDiv.className = "message user-message";
                userMessageDiv.innerHTML = `<strong>Tú:</strong> ${message}`;
                chatLog.appendChild(userMessageDiv);

                // Respuesta de Nova
                var response;
                if (firstMessage && isGreeting(message)) {
                    response = "¡Buen día! Soy Nova, tu asistente virtual. ¿En qué puedo ayudarte hoy?";
                    firstMessage = false;
                } else if (firstMessage) {
                    response = "Por favor, salúdame para que podamos comenzar.";
                } else {
                    response = getResponse(message);
                }

                // Mostrar la respuesta de Nova
                var botMessageDiv = document.createElement("div");
                botMessageDiv.className = "message bot-message";
                botMessageDiv.innerHTML = `<strong>Nova:</strong> ${response}`;
                chatLog.appendChild(botMessageDiv);

                // Limpiar input
                document.getElementById('user-message').value = '';  

                // Scroll automático al final del chat
                chatLog.scrollTop = chatLog.scrollHeight;
            };

            function isGreeting(message) {
                const greetings = ["hola", "buen día", "buenas tardes", "buenas noches", "hey", "saludos"];
                var lowerMessage = message.toLowerCase();
                return greetings.some(greeting => lowerMessage.includes(greeting));
            }

            function getResponse(message) {
                const responses = [
                    { pattern: /requisitos.*(ingresar|inscripción)/i, response: "Los requisitos para ingresar son: DNI, certificado de estudios y completar el formulario de inscripción." },
                    { pattern: /fecha.*límite/i, response: "La fecha límite para inscribirse es el 8 de marzo." },
                    { pattern: /horario/i, response: "El horario de inscripción es de 9 a 18 horas." },
                    { pattern: /documentos/i, response: "Necesitas presentar tu DNI y un certificado de estudios." },
                    { pattern: /ayuda|asistencia/i, response: "Estoy aquí para ayudarte. ¿Cuál es tu pregunta?" },
                    { pattern: /dirección.*instituto|calle del instituto/i, response: "La dirección del instituto es Avda. 7 Nro. 2149 esq. 76. Espero que te haya ayudado esta información." },
                    { pattern: /contacto|teléfono/i, response: "Puedes contactarnos al teléfono: 123-456-7890." },
                    { pattern: /programas|cursos/i, response: "Ofrecemos una variedad de programas y cursos. ¿Te gustaría saber más sobre alguno en particular?" },
                    { pattern: /gracias/i, response: "¡De nada! Si tienes más preguntas, no dudes en preguntar." },
                ];

                for (const { pattern, response } of responses) {
                    if (pattern.test(message)) {
                        return response;
                    }
                }
                return "Lo siento, no tengo información sobre eso.";
            }
        </script>
    </body>
    </html>
    """

    # Renderizar el HTML personalizado en Streamlit
    components.html(html_code, height=600)
