from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()


class AnalisisTexto(BaseModel):
    resumen: str = Field (description="Resumen conciso del texto proporcionado")
    sentimiento: str = Field (description="Sentimiento predominante del texto: positivo, negativo o neutral")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6, google_api_key=os.getenv("GOOGLE_API_KEY" ))

structured_llm = llm.with_structured_output(AnalisisTexto)

texto = """me encanta la arepa con queso, es mi comida favorita. Siempre me hace sentir feliz y satisfecho."""
resultado = structured_llm.invoke(f"Analiza el siguiente texto y proporciona un resumen y el sentimiento predominante:\n\n{texto}")
print("\n Este es el resultado:",resultado)
print("\n Resumen:",resultado.resumen)
print("\n Sentimiento:",resultado.sentimiento)

