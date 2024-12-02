FROM python:3.8.10-alpine3.13

WORKDIR /app

# Instalar dependencias del sistema
RUN apk update && apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev

# Copiar la aplicación Django al directorio de trabajo
COPY . /app

# Configurar variables de entorno
ENV DB_Realacional_HOST=10.128.0.82

# Actualizar pip para evitar problemas de instalación
RUN pip install --upgrade pip

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Definir el punto de entrada
ENTRYPOINT ["sh", "init.sh"]
