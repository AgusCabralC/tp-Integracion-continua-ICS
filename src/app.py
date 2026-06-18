from flask import Flask, jsonify, request, render_template
import datetime

app = Flask(__name__)

# Interfaz visual con el boton
@app.route('/', methods=['GET'])
def pagina_principal():
    return render_template('index.html')

# El ENDPOINT que devuelve si es navidad o no
@app.route('/es-navidad', methods=['GET']) #Mapeo la url especifica
def consultar_navidad():
    if request.args: #lo ocupo por si alguien intenta entrar con parametros /es-navidad?hack=123, el sistema lo rechaza
        return jsonify({"error": "Peticion invalida. No se admiten parametros."}), 400
        
    hoy = datetime.datetime.now()  #    hoy = datetime.datetime(2026, 12, 25)
    if hoy.month == 12 and hoy.day == 25:
        es_navidad = True
    else:
        es_navidad = False
        
    return jsonify({"es_navidad": es_navidad}), 200

if __name__ == '__main__':
    app.run(debug=True)