# 🛠️ Comandos Útiles para el Proyecto

Guía rápida de comandos para trabajar con este proyecto de LangChain.

---

## 🚀 Iniciar el Proyecto

### Ejecutar el Chatbot de Streamlit
```bash
# Activar el entorno virtual y ejecutar
pipenv shell
streamlit run streamlit_chatbot.py
```

### Ejecutar Scripts de Prueba
```bash
# Ejemplo básico de Gemini
pipenv run python prueba_gemini.py

# Ejemplo con PromptTemplate
pipenv run python prueba_gemini_avanzado.py

# Ejemplo con OpenAI
pipenv run python prueba_openai.py
```

---

## 📦 Gestión de Dependencias

### Instalar Todas las Dependencias
```bash
pipenv install
```

### Instalar una Nueva Dependencia
```bash
pipenv install nombre-paquete
```

### Instalar una Versión Específica
```bash
pipenv install langchain==0.3.0
```

### Actualizar Dependencias
```bash
pipenv update
```

### Ver Dependencias Instaladas
```bash
pipenv graph
```

### Desinstalar un Paquete
```bash
pipenv uninstall nombre-paquete
```

---

## 🔧 Gestión del Entorno Virtual

### Activar el Entorno Virtual
```bash
pipenv shell
```

### Salir del Entorno Virtual
```bash
exit
```

### Ver Información del Entorno
```bash
pipenv --venv
```

### Ver Dónde está Python
```bash
pipenv run which python
```

---

## 🔑 Configuración de Variables de Entorno

### Ver Variables de Entorno
```bash
# En PowerShell
Get-Content .env

# Usando Python
pipenv run python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('GOOGLE_API_KEY'))"
```

### Verificar que la API Key Funciona
```bash
pipenv run python prueba_gemini.py
```

---

## 📊 Streamlit - Comandos Avanzados

### Ejecutar en un Puerto Específico
```bash
streamlit run streamlit_chatbot.py --server.port 8080
```

### Ejecutar sin Abrir el Navegador
```bash
streamlit run streamlit_chatbot.py --server.headless true
```

### Ver Configuración de Streamlit
```bash
streamlit config show
```

### Limpiar Caché de Streamlit
```bash
streamlit cache clear
```

---

## 🔍 Depuración y Testing

### Ver Errores en Detalle
```bash
# Ejecutar con modo verbose
pipenv run python prueba_gemini.py -v
```

### Verificar Sintaxis sin Ejecutar
```bash
python -m py_compile streamlit_chatbot.py
```

---

## 📝 Git - Comandos Útiles

### Ver Estado del Repositorio
```bash
git status
```

### Agregar Cambios
```bash
git add .
```

### Commit de Cambios
```bash
git commit -m "Descripción del cambio"
```

### Ver Historial
```bash
git log --oneline
```

### Verificar que .env NO está en Git
```bash
git status --ignored
```

---

## 🧹 Limpieza del Proyecto

### Limpiar Archivos de Caché de Python
```bash
# En PowerShell
Remove-Item -Recurse -Force __pycache__
Remove-Item -Recurse -Force *.pyc
```

### Limpiar Caché de Streamlit
```bash
Remove-Item -Recurse -Force .streamlit
```

---

## 📊 Información del Sistema

### Ver Versión de Python
```bash
python --version
```

### Ver Versiones de Paquetes
```bash
pipenv run pip list
```

### Ver Info del Sistema
```bash
# En PowerShell
Get-ComputerInfo | Select-Object OsName, OsVersion
```

---

## 🔄 Actualización de Código

### Aplicar Mejoras de Código (si las hay)
```bash
# Reformatear código con black (opcional)
pipenv install --dev black
pipenv run black streamlit_chatbot.py
```

### Linting con flake8 (opcional)
```bash
pipenv install --dev flake8
pipenv run flake8 streamlit_chatbot.py
```

---

## 🚨 Solución de Problemas Comunes

### Problema: ModuleNotFoundError
**Solución:**
```bash
# Asegúrate de ejecutar con pipenv run
pipenv run python tu_script.py
```

### Problema: API Key no funciona
**Solución:**
```bash
# Verifica que el archivo .env existe
Get-Content .env

# Verifica que load_dotenv() está en tu código
# Reinicia el terminal después de cambiar .env
```

### Problema: Streamlit no se abre en el navegador
**Solución:**
```bash
# Abre manualmente en: http://localhost:8501
```

### Problema: Puerto ocupado
**Solución:**
```bash
# Usa un puerto diferente
streamlit run streamlit_chatbot.py --server.port 8502
```

---

## 📚 Comandos de Aprendizaje

### Abrir Documentación de LangChain
```bash
# En PowerShell, abre el navegador
Start-Process "https://python.langchain.com/docs/get_started/introduction"
```

### Experimentar con Python REPL
```bash
pipenv run python
>>> from langchain_google_genai import ChatGoogleGenerativeAI
>>> llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
>>> print(llm.invoke("Hola"))
>>> exit()
```

---

## 🎯 Atajos Rápidos

```bash
# Todo en uno: instalar y ejecutar
pipenv install && pipenv run streamlit run streamlit_chatbot.py

# Actualizar y ejecutar
pipenv update && pipenv run streamlit run streamlit_chatbot.py

# Limpiar y ejecutar
Remove-Item -Recurse -Force __pycache__; pipenv run streamlit run streamlit_chatbot.py
```

---

## 💡 Tips Profesionales

### 1. Crear un Alias (PowerShell)
Agrega a tu perfil de PowerShell (`$PROFILE`):
```powershell
function Start-Chatbot {
    Set-Location "C:\Users\arann\Desktop\nikoidev\LangChain"
    pipenv run streamlit run streamlit_chatbot.py
}
Set-Alias chatbot Start-Chatbot
```

Luego solo escribe:
```bash
chatbot
```

### 2. Script de Inicio Rápido
Crea un archivo `start.ps1`:
```powershell
Write-Host "🚀 Iniciando Chatbot LangChain..." -ForegroundColor Green
pipenv run streamlit run streamlit_chatbot.py
```

Ejecuta:
```bash
.\start.ps1
```

---

## 📋 Checklist de Comandos Esenciales

Comandos que deberías conocer:

- [ ] `pipenv install` - Instalar dependencias
- [ ] `pipenv shell` - Activar entorno
- [ ] `pipenv run streamlit run streamlit_chatbot.py` - Ejecutar app
- [ ] `pipenv run python prueba_gemini.py` - Probar scripts
- [ ] `git status` - Ver estado de Git
- [ ] `streamlit cache clear` - Limpiar caché

---

**Última actualización:** 27 de octubre de 2025  
**Mantén este archivo a mano para consultas rápidas!** 📖

