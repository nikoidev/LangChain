import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, AIMessage
import streamlit as st
from langchain.prompts import PromptTemplate

# Cargar variables de entorno desde el archivo .env
# Esto permite mantener las API keys seguras y fuera del código
load_dotenv()

# Configuración de la página de Streamlit
st.set_page_config(page_title="Chatbot Básico", page_icon="🤖")
st.title("🤖 Chatbot Básico con LangChain")
st.markdown("Este es un *chatbot de ejemplo* construido con LangChain + Streamlit. ¡Escribe tu mensaje abajo para comenzar!")

# Sidebar para configuración del chatbot
with st.sidebar:
    st.header("⚙️ Configuración")
    
    # Control de temperatura: valores más altos = respuestas más creativas
    # valores más bajos = respuestas más deterministas y precisas
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    
    # Selector de modelo (puedes agregar más modelos aquí)
    model_name = st.selectbox("Modelo", ["gemini-2.5-flash", "gemini-pro"])
    
    # Botón para limpiar el historial de conversación
    if st.button("🗑️ Nueva conversación"):
        st.session_state.mensajes = []
        st.rerun()

# Inicializar el modelo de chat con las configuraciones seleccionadas
# La API key se obtiene de forma segura desde las variables de entorno
try:
    chat_model = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
except Exception as e:
    st.error(f"❌ Error al inicializar el modelo: {str(e)}")
    st.info("Verifica que tu API Key de Google esté configurada en el archivo .env")
    st.stop()

# Inicializar el estado de sesión para almacenar el historial de mensajes
# st.session_state persiste los datos entre reruns de Streamlit
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Crear el template de prompt que define el comportamiento del chatbot
prompt_template = PromptTemplate(
    input_variables=["mensaje", "historial"],
    template="""Eres un asistente útil y amigable llamado ChatBot Pro. 

Historial de conversación:
{historial}

Responde de manera clara y concisa a la siguiente pregunta: {mensaje}"""
)

# Crear cadena usando LCEL (LangChain Expression Language)
# El operador | conecta el prompt template con el modelo de chat
cadena = prompt_template | chat_model

# Mostrar todos los mensajes previos de la conversación

for msg in st.session_state.mensajes:
    # Determinar si el mensaje es del asistente o del usuario
    role = "assistant" if isinstance(msg, AIMessage) else "user"
    
    # Renderizar el mensaje con el icono correspondiente
    with st.chat_message(role):
        st.markdown(msg.content)

# Cuadro de entrada de texto para nuevos mensajes
pregunta = st.chat_input("Escribe tu mensaje...")

if pregunta:
    # Mostrar el mensaje del usuario inmediatamente
    with st.chat_message("user"):
        st.markdown(pregunta)

    try:
        # Formatear el historial como texto legible para el modelo
        # Limitamos a los últimos 10 mensajes para no exceder límites de tokens
        historial_texto = "\n".join([
            f"{'Usuario' if isinstance(msg, HumanMessage) else 'Asistente'}: {msg.content}"
            for msg in st.session_state.mensajes[-10:]
        ]) if st.session_state.mensajes else "No hay historial previo."
        
        # Generar y mostrar la respuesta del asistente con streaming
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            # Streaming: mostrar la respuesta token por token en tiempo real
            for chunk in cadena.stream({
                "mensaje": pregunta,
                "historial": historial_texto
            }):
                full_response += chunk.content
                # El símbolo ▌ simula un cursor parpadeante mientras se escribe
                response_placeholder.markdown(full_response + "▌")
            
            # Mostrar la respuesta completa sin el cursor
            response_placeholder.markdown(full_response)
        
        # Guardar ambos mensajes (usuario y asistente) en el historial
        st.session_state.mensajes.append(HumanMessage(content=pregunta))
        st.session_state.mensajes.append(AIMessage(content=full_response))
        
    except Exception as e:
        st.error(f"❌ Error al generar respuesta: {str(e)}")
        st.info("💡 Verifica que tu API Key de Google Gemini esté configurada correctamente en el archivo .env")