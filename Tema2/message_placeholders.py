from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente util que mantiene el contexto de la conversacion."),
    MessagesPlaceholder(variable_name="historial"),
    ("human", "{pregunta_actual}")
])




#Simulamos un historial de conversación

historial_conversacion = [
    HumanMessage(content="¿cual es la capital de Venezuela?"),
    AIMessage(content="La capital de Venezuela es Caracas."),
    HumanMessage(content="¿y cuantos habitantes tiene?"),
    AIMessage(content="Venezuela tiene aproximadamente 28 millones de habitantes.")
]

mensajes = chat_prompt.format_messages(
    historial=historial_conversacion,
    pregunta_actual="¿Cual es la moneda oficial de Venezuela?"
)

for m in mensajes:
    print(m.content)