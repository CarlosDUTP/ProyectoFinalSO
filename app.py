from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Lista para almacenar las respuestas de la encuesta
respuestas = {
    'Python': 0,
    'JavaScript': 0,
    'Java': 0,
    'C#': 0
}

# Función para cargar los resultados desde el archivo resultados.json
def cargar_resultados():
    if os.path.exists('resultados.json'):
        with open('resultados.json', 'r') as file:
            resultados_cargados = json.load(file)

        # Combinar los resultados cargados con el diccionario respuestas
        for lenguaje, votos in resultados_cargados.items():
            if lenguaje in respuestas:
                respuestas[lenguaje] = votos

    return respuestas

# Función para guardar los resultados en el archivo resultados.json
def guardar_resultados(resultados):
    with open('resultados.json', 'w') as file:
        json.dump(resultados, file)

# Ruta para mostrar la encuesta
@app.route('/')
def index():
    return render_template('encuesta.html')

# Ruta para procesar la encuesta
@app.route('/encuesta', methods=['POST'])
def encuesta():
    lenguaje = request.form['lenguaje']
    if lenguaje in respuestas:
        respuestas[lenguaje] += 1

    guardar_resultados(respuestas)

    return render_template('resultado.html', respuestas=respuestas)

# Ruta para obtener los datos de los resultados en formato JSON
@app.route('/datos', methods=['GET'])
def obtener_datos():
    return jsonify(respuestas)

if __name__ == '__main__':
    respuestas = cargar_resultados()  # Cargar los resultados al iniciar la aplicación
    app.run(host='0.0.0.0', port=8000)
