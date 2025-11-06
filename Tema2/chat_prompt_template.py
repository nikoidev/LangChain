from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un traductor del español al ingles muy precico."),
    ("human", "{text}")
])

mensajes = chat_prompt.format_messages(text="Hola, ¿cómo estás?")

for m in mensajes:
    print(f"{type(m)}: {m.content}")
