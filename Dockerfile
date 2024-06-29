# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instalar python-dotenv para manejar variables de entorno desde un archivo .env
RUN pip install python-dotenv

# Copiar el contenido del directorio actual al directorio de trabajo en la imagen
COPY . .

# Copiar el archivo .env
COPY .env .

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
