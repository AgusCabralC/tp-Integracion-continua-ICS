import unittest
from unittest.mock import patch
import datetime
import json
from src.app import app

class PruebasBotonNavidad(unittest.TestCase):
    def setUp(self):
        # Interfaz falsa para las pruebas de IC
        self.navegador_prueba = app.test_client() #instancio el test_client de Flask para simular peticiones a la app

    def test_caso_comun_no_es_navidad(self):
        # Verifica que un día común devuelva False
        fecha_falsa = datetime.datetime(2026, 6, 15)
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = fecha_falsa # Hago mocking con unittest por Github Actions
            respuesta = self.navegador_prueba.get('/es-navidad')
            datos = json.loads(respuesta.data)
            
            self.assertEqual(respuesta.status_code, 200) # Todo Ok online
            self.assertIsInstance(datos["es_navidad"], bool) # Si mandaron un Boolean
            self.assertFalse(datos["es_navidad"]) # Es correcto que devuelva False en un día común

    def test_caso_borde_si_es_navidad(self):
        #Verifica que el 25/12 devuelva True obligatoriamente
        fecha_navidad = datetime.datetime(2026, 12, 25)
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = fecha_navidad
            
            respuesta = self.navegador_prueba.get('/es-navidad')
            datos = json.loads(respuesta.data)
            
            self.assertEqual(respuesta.status_code, 200)
            self.assertTrue(datos["es_navidad"]) 

    def test_rechazo_usuario_erroneo(self):
        #verifica que el usuario no escriba parametros en la URL, y que el sistema los rechace
        respuesta = self.navegador_prueba.get('/es-navidad?hack=123')
        self.assertEqual(respuesta.status_code, 400) # Valida el código de rechazo