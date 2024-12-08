# Utiliza una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir websockets

# Expone el puerto para el servidor WebSocket
EXPOSE 8765

# Comando para ejecutar el servidor
CMD ["python", "server.py"]
