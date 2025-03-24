import unittest
from optimizacion.optimizacion import procesar_datos

class TestOptimizacion(unittest.TestCase):
    def test_procesar_datos(self):
        datos = [1, 2, 3, 4, 5]
        esperado = [3, 4, 9, 8, 15]
        resultado = procesar_datos(datos)
        self.assertEqual(resultado, esperado)

if __name__ == "__main__":
    unittest.main()
