from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route('/es-navidad', methods=['GET'])
def consultar_navidad():
    # 1. Si el usuario manda parámetros extraños en la URL, los rechazamos (Control de usuario erróneo)
    if request.args:
        return jsonify({"error": "Peticion invalida. No se admiten parametros."}), 400
        
    # 2. Obtenemos la fecha actual del servidor
    hoy = datetime.datetime.now()
    
    # 3. Verificamos si es 25 de Diciembre (Mes 12, Día 25)
    if hoy.month == 12 and hoy.day == 25:
        es_navidad = True
    else:
        es_navidad = False
        
    # 4. Devolvemos la respuesta en estructura JSON limpia
    return jsonify({"es_navidad": es_navidad}), 200

if __name__ == '__main__':
    app.run(debug=True)