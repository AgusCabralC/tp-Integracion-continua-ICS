import unittest
from app import servidor_tp  # Importamos nuestro servidor con el nuevo nombre

class PruebasDeMiServidor(unittest.TestCase):

    def setUp(self):
        # Creamos un navegador falso para testear las rutas sin prender el servidor real
        self.navegadorprueba = servidor_tp.test_client()

    def test_verificar_conexion_exitosa(self):
        # Entramos a la pagina principal y chequeamos que responda con un codigo 200 
        respuestaweb = self.navegadorprueba.get('/')
        self.assertEqual(respuestaweb.status_code, 200)

    def test_verificar_contenido_del_texto(self):
        # Valido que el texto en pantalla contenga las palabras clave que puse en app.py
        respuestaweb = self.navegadorprueba.get('/')
        texto_recibido = respuestaweb.data.decode('utf-8')
        self.assertIn("Servidor de Gestión", texto_recibido)

if __name__ == '__main__':
    unittest.main()