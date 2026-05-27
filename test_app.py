import unittest
from app import saludar, sumar

class TestMiApp(unittest.TestCase):

    def test_saludar(self):
        self.assertEqual(saludar(), "Hola Mundo")

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

if __name__ == '__main__':
    unittest.main()