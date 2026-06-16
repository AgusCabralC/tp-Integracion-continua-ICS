import unittest
from unittest.mock import patch
import datetime
import json
from src.app import app

class PruebasBotonNavidad(unittest.TestCase):
    def setUp(self):
        # Levantamos el navegador falso para las pruebas de IC
        self.navegador_prueba = app.test_client()

    def test_caso_comun_no_es_navidad(self):
        """Filtro: Verifica que un día común devuelva False"""
        fecha_falsa = datetime.datetime(2026, 6, 15)
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = fecha_falsa
            
            respuesta = self.navegador_prueba.get('/es-navidad')
            datos = json.loads(respuesta.data)
            
            self.assertEqual(respuesta.status_code, 200) # Filtro estructural
            self.assertIsInstance(datos["es_navidad"], bool) # Filtro de tipo
            self.assertFalse(datos["es_navidad"]) # Lógica de negocio

    def test_caso_borde_si_es_navidad(self):
        """Filtro: Verifica que el 25/12 devuelva True obligatoriamente"""
        fecha_navidad = datetime.datetime(2026, 12, 25)
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = fecha_navidad
            
            respuesta = self.navegador_prueba.get('/es-navidad')
            datos = json.loads(respuesta.data)
            
            self.assertEqual(respuesta.status_code, 200)
            self.assertTrue(datos["es_navidad"]) # Lógica de negocio

    def test_rechazo_usuario_erroneo(self):
        """Filtro: Comprueba que la app controle y rechace basura del usuario"""
        respuesta = self.navegador_prueba.get('/es-navidad?hack=123')
        self.assertEqual(respuesta.status_code, 400) # Valida el código de rechazo