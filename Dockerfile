# Usa la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios (requerimientos y la aplicación)
COPY requirements.txt .
COPY app/ ./app

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Expone el puerto 8000 para la aplicación FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI con Gunicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
