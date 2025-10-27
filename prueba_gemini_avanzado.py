from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

plantilla = PromptTemplate(
    input_variables= ["nombre"],
    template= "Saluda al usuario con su nombre. \n Nombre del usuario: {nombre}"

)

chain = plantilla | chat  

resultado = chain.invoke({"nombre":"NikoiDev"})
print("Resultado es: ", resultado.content)