from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

pregunta = "¿Qué es la inteligencia artificial?"
print("Pregunta: ", pregunta)

respuesta = llm.invoke(pregunta)
print("Respuesta: ", respuesta.content)