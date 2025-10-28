# 🤖 Proyecto de Aprendizaje: LangChain con Python

Este es un proyecto educativo para aprender los fundamentos de **LangChain**, una biblioteca poderosa para construir aplicaciones con modelos de lenguaje (LLMs).

## 📚 Contenido del Proyecto

### Archivos de Práctica

1. **`prueba_gemini.py`** - Introducción básica
   - Uso simple de Google Gemini AI
   - Invocación directa del modelo
   - Conceptos: LLM básico

2. **`prueba_gemini_avanzado.py`** - Prompt Templates
   - Implementación de `PromptTemplate`
   - Uso de LCEL (LangChain Expression Language)
   - Conceptos: Templates, Chains

3. **`prueba_openai.py`** - Integración con OpenAI
   - Uso de ChatGPT (gpt-4o-mini)
   - Comparación con Gemini

4. **`streamlit_chatbot.py`** - Aplicación Completa 🎯
   - Chatbot interactivo con interfaz web
   - Streaming en tiempo real
   - Gestión de historial de conversación
   - Configuración dinámica (temperatura, modelo)

## 🚀 Instalación y Configuración

### 1. Requisitos Previos
- Python 3.13+
- Pipenv instalado

### 2. Instalar Dependencias

```bash
# Instalar todas las dependencias del proyecto
pipenv install
```

### 3. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto (o copia `.env.example`):

```bash
# Google Gemini API Key
GOOGLE_API_KEY=tu_google_api_key_aqui

# OpenAI API Key (opcional)
OPENAI_API_KEY=tu_openai_api_key_aqui
```

**📌 Cómo obtener una API Key:**
- **Google Gemini**: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
- **OpenAI**: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### 4. Ejecutar el Chatbot

```bash
# Activar el entorno virtual
pipenv shell

# Ejecutar la aplicación Streamlit
streamlit run streamlit_chatbot.py
```

## 🎓 Conceptos Aprendidos

### 1. **LLMs (Large Language Models)**
Modelos de lenguaje que pueden generar texto basándose en prompts.

### 2. **Prompt Templates**
Plantillas reutilizables para formatear instrucciones al modelo.

```python
template = PromptTemplate(
    input_variables=["nombre"],
    template="Saluda al usuario: {nombre}"
)
```

### 3. **LCEL (LangChain Expression Language)**
Sintaxis moderna para crear cadenas (chains) usando el operador `|`.

```python
chain = prompt_template | chat_model
```

### 4. **Streaming**
Recibir respuestas token por token en tiempo real para mejor UX.

```python
for chunk in chain.stream(input_data):
    print(chunk.content)
```

### 5. **Session State (Streamlit)**
Persistencia de datos entre reruns de la aplicación.

```python
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
```

## 📦 Dependencias Principales

- **`langchain`** (0.3.*) - Framework principal
- **`langchain-google-genai`** - Integración con Google Gemini
- **`langchain-openai`** - Integración con OpenAI
- **`streamlit`** - Framework para crear la interfaz web
- **`python-dotenv`** - Gestión de variables de entorno

## 🔧 Características del Chatbot

✅ Interfaz web moderna con Streamlit  
✅ Streaming de respuestas en tiempo real  
✅ Historial de conversación persistente  
✅ Configuración dinámica de temperatura  
✅ Selector de modelos  
✅ Botón para limpiar conversación  
✅ Manejo de errores robusto  
✅ API keys seguras con variables de entorno  

## 📖 Próximos Pasos para Aprender

1. **Memory Management**: Implementar `ConversationBufferMemory`
2. **RAG (Retrieval Augmented Generation)**: Conectar documentos y bases de datos vectoriales
3. **Agents**: Crear agentes que usen herramientas
4. **Custom Chains**: Cadenas más complejas con múltiples pasos
5. **Testing**: Agregar tests unitarios

## 🤝 Contribuciones

Este es un proyecto de aprendizaje personal. Siéntete libre de usarlo como referencia.

## 📝 Notas

- El código sigue buenas prácticas de seguridad (API keys en `.env`)
- Comentarios en inglés en el código
- Documentación en español
- Variables y funciones en inglés

## 🔒 Seguridad

⚠️ **IMPORTANTE**: Nunca subas tu archivo `.env` a Git. Asegúrate de que esté en tu `.gitignore`.

---

**Desarrollado con fines educativos** 🎓

