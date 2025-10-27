from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import streamlit as st

# se conmfigura la pagina de la app

st.set_page_config(page_title="Chatbot Basico", page_icon="🙊​​​")
st.title("Hola, soy NikoiDev y uso Gemini")
st.markdown("este es un chatbot basico con langchain y gemini")

chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes previos

for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        continue

    role = "assistant" if isinstance(msg, AIMessage) else "user"

    with st.chat_message(role):
        st.markdown(msg.content)
    
# Cuadro de entrada de texto

pregunta = st.chat_input("Escribe tu mensaje...")

if pregunta:
    # Mostrar el mensaje del usuario
    with st.chat_message("user"):
        st.markdown(pregunta)
        # Agregar el mensaje al historial
        st.session_state.mensajes.append(HumanMessage(content=pregunta))
        # Generar respuesta
        respuesta = chat_model.invoke(st.session_state.mensajes)

        # Mostrar la respuesta del asistente
        with st.chat_message("assistant"):
            st.markdown(respuesta.content)
        # Agregar la respuesta al historial
        st.session_state.mensajes.append(respuesta)
