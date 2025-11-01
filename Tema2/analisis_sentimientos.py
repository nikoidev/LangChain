from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Configuración del modelo con rate limit handling
# Gemini Free Tier: 10 requests/min
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    max_retries=2  # Reducir reintentos para evitar esperas largas
)


# Preprocesador: limpia espacios y limita a 500 caracteres
def preprocess_text(text):
    """Limpia el texto eliminando espacios extras y limitando longitud"""
    return text.strip()[:500]

preprocessor = RunnableLambda(preprocess_text)

# Generación de resumen
def generate_summary(text):
    """Genera un resumen conciso del texto"""
    prompt = f"Resume en una sola oración: {text}"
    response = llm.invoke(prompt)
    return response.content

summary_brach = RunnableLambda(generate_summary)

# Análisis de sentimiento con formato JSON
def analyze_sentiment(text):
    """Analiza el sentimiento y devuelve resultado estructurado"""
    prompt = f"""Analiza el sentimiento del siguiente texto.
    Responde ÚNICAMENTE en formato JSON válido, sin markdown, sin backticks, solo el JSON puro:
    {{"sentimiento": "positivo|negativo|neutro", "razon": "justificación breve"}}
    
    Texto: {text}"""
    
    response = llm.invoke(prompt)
    content = response.content.strip()
    
    try:
        # Limpiar markdown si viene con ```json
        if content.startswith("```"):
            # Extraer solo el JSON entre los backticks
            lines = content.split("\n")
            content = "\n".join(lines[1:-1])  # Quitar primera y última línea
        
        return json.loads(content)
    except json.JSONDecodeError as e:
        # Si hay error, mostrar debug para diagnosticar
        print(f"ERROR - Error parseando JSON: {e}")
        print(f"DEBUG - Contenido recibido: {content}")
        return {"sentimiento": "neutro", "razon": "Error en análisis"}
    
sentiment_branch = RunnableLambda(analyze_sentiment)

# Combinación de resultados
def merge_results(data):
    """Combina los resultados de ambas ramas en un formato unificado"""
    return {
        "resumen": data["resumen"],
        "sentimiento": data["sentimiento_data"]["sentimiento"],
        "razon": data["sentimiento_data"]["razon"]
    }

merger = RunnableLambda(merge_results)

parallel_analysis = RunnableParallel({
    "resumen": summary_brach,
    "sentimiento_data": sentiment_branch
})

# Cadena completa
chain = preprocessor | parallel_analysis | merger

reviews = [
    "Este producto es excelente, me encanta el sabor y la calidad del producto.", 
    "Este producto es muy malo. No me ha gustadoo para nada"
    # Comentados para no exceder el rate limit de Gemini (10 req/min)
    # "Este producto es bueno, pero no es excelente", 
    # "Este producto es mas o menos. No me ha gustadoo"
]

# invoke() se usa para un solo texto
# batch() se usa para procesar múltiples textos en paralelo
print("\n⏳ Procesando", len(reviews), "textos...")
print("💡 Cada texto genera 2 llamadas a la API (resumen + sentimiento en paralelo)")
print("⚠️  Gemini Free Tier: 10 requests/minuto\n")

try:
    resultados = chain.batch(reviews)
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\n💡 Si excediste el rate limit, espera 60 segundos y vuelve a intentar.")
    exit(1)

# Mostrar resultados formateados
print("\n" + "="*70)
print("ANALISIS DE SENTIMIENTOS Y RESUMEN - MULTIPLES TEXTOS")
print("="*70)

for i, (texto, resultado) in enumerate(zip(reviews, resultados), 1):
    print(f"\n[{i}] TEXTO ORIGINAL:")
    print(f"    {texto}")
    print(f"\n    Resumen:     {resultado['resumen']}")
    print(f"    Sentimiento: {resultado['sentimiento'].upper()}")
    print(f"    Razon:       {resultado['razon']}")
    print("-" * 70)

print("="*70 + "\n")
# Nota: Asegúrate de tener la variable de entorno GOOGLE_API_KEY configurada
# para que el script funcione correctamente.