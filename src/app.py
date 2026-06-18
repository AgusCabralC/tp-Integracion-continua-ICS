from flask import Flask, jsonify, request, render_template
import datetime

app = Flask(__name__)

# NUEVA RUTA: Sirve la interfaz visual con el boton
@app.route('/', methods=['GET'])
def pagina_principal():
    return render_template('index.html')

# NUESTRO ENDPOINT: Procesa la logica de fondo (intacta para la IC)
@app.route('/es-navidad', methods=['GET'])
def consultar_navidad():
    if request.args:
        return jsonify({"error": "Peticion invalida. No se admiten parametros."}), 400
        
    hoy = datetime.datetime.now()
    if hoy.month == 12 and hoy.day == 25:
        es_navidad = True
    else:
        es_navidad = False
        
    return jsonify({"es_navidad": es_navidad}), 200

if __name__ == '__main__':
    app.run(debug=True)