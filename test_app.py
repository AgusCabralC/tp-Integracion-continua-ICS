import unittest
from app import app

class TestMiAplicacionWeb(unittest.TestCase):

    def setUp(self):
        # Crea un cliente de pruebas para simular peticiones web sin necesidad de encender el servidor real
        self.cliente = app.test_client()

    def test_home_status(self):
        # Simula entrar a la raiz de la pagina ('/') y verifica que el codigo de estado web sea 200 (OK)
        respuesta = self.cliente.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_home_contenido(self):
        # Verifica que el texto que muestra la pagina contenga el mensaje que configuramos
        respuesta = self.cliente.get('/')
        self.assertIn("Hola, bienvenido al TP", respuesta.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()