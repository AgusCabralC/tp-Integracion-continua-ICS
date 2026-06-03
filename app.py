from flask import Flask

# Creo el servidor web
servidor_tp = Flask(__name__)

@servidor_tp.route('/')
def pagina_principal():
    # Mensaje que se va a mostrar en la pantalla
    return "Servidor de Gestión anda correctamente"

if __name__ == "__main__":
    #puerto que ocupo
    servidor_tp.run(host='0.0.0.0', port=5000)