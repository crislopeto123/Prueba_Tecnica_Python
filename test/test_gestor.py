import unittest
import pytest
from gestor_archivos.gestor import GestorArchivos

class TestGestorArchivos(unittest.TestCase):
    def setUp(self):

        self.gestor = GestorArchivos()
        self.archivo_prueba = "data/test_archivo.txt"

    def test_escribir_y_leer_archivo(self):
        contenido = "Este es un archivo de prueba."
        self.gestor.escribir_archivo(self.archivo_prueba, contenido)
        self.assertEqual(self.gestor.leer_archivo(self.archivo_prueba), contenido)

    def test_contar_palabras_unicas(self):
        contenido = "Hola Hola mundo"
        self.gestor.escribir_archivo(self.archivo_prueba, contenido)
        self.assertEqual(self.gestor.contar_palabras_unicas(self.archivo_prueba), 2)

    def test_buscar_palabra(self):
        contenido = "Hola mundo\nHola de nuevo"
        self.gestor.escribir_archivo(self.archivo_prueba, contenido)
        resultado = self.gestor.buscar_palabra(self.archivo_prueba, "Hola")
        self.assertEqual(len(resultado), 2)

    def tearDown(self):

        import os
        if os.path.exists(self.archivo_prueba):
            os.remove(self.archivo_prueba)

