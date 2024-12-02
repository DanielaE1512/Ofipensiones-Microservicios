# Imagen base con Python
FROM python:3.8-slim

# Definir directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2 y otras librerías
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos del proyecto al contenedor
COPY . /app

# Actualizar pip a la última versión
RUN pip install --upgrade pip

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto por defecto para Django
EXPOSE 8000

# Comando de inicio del contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

