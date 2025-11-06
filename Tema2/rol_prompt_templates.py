from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

plantilla_sistema = SystemMessagePromptTemplate.from_template(""" 
Eres un {rol} especializado en {especialidad}. Responde  de manera {tono}""")

plantilla_humano = HumanMessagePromptTemplate.from_template(
    " Mi pregunta sobre {tema} es: {pregunta}"
    )

chat_prompt = ChatPromptTemplate.from_messages([
    plantilla_sistema,
    plantilla_humano
])
mensajes = chat_prompt.format_messages(
    rol="historiador",
    especialidad="historia antigua",
    tono="formal y conciso",
    tema="Imperio Romano",
    pregunta="¿Cuál fue la causa principal de la caída del Imperio Romano?"
)

for m in mensajes:
    print(m.content)