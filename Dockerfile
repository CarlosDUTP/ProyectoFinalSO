# Utiliza una imagen de Python como base
FROM python:3

# Instala Flask y las dependencias necesarias para las gráficas
RUN pip install --no-cache-dir Flask matplotlib pandas

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios (app.py y la carpeta templates) al contenedor
COPY app.py /app/
COPY templates /app/templates

# Expone el puerto en el que se ejecuta la aplicación web (el mismo especificado en tu código Python)
EXPOSE 8000

# Ejecuta la aplicación web
CMD ["python", "app.py"]
