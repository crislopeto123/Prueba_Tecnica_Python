import unittest
from unittest.mock import patch
from gestor_archivos.descargas_concurrentes import descargar_archivo, descargar_archivos_concurrentes


class TestDescargasConcurrentes(unittest.TestCase):
    def test_descargar_archivo(self):

        archivo = {'id': 1, 'url': 'http://mocked.url/archivo_prueba.pdf', 'nombre': 'archivo1.pdf', 'ruta': './pruebas/'}


        with patch('gestor_archivos.descargas_concurrentes.requests.get') as mock_requests:
            mock_requests.return_value.status_code = 200
            mock_requests.return_value.iter_content = lambda chunk_size: [b'dummy_data']


            with patch('gestor_archivos.descargas_concurrentes.open', unittest.mock.mock_open(), create=True):
                resultado = descargar_archivo(archivo)
                self.assertIsNone(resultado)

    def test_descargar_archivos_concurrentes(self):

        archivos_a_descargar = [
            {'id': 1, 'url': 'http://mocked.url/archivo_prueba1.pdf', 'nombre': 'archivo1.pdf', 'ruta': './pruebas/'},
            {'id': 2, 'url': 'http://mocked.url/archivo_prueba2.pdf', 'nombre': 'archivo2.pdf', 'ruta': './pruebas/'},
            {'id': 3, 'url': 'http://mocked.url/archivo_prueba3.pdf', 'nombre': 'archivo3.pdf', 'ruta': './pruebas/'}
        ]

        with patch('gestor_archivos.descargas_concurrentes.descargar_archivo', return_value=None) as mock_descargar:
            descargar_archivos_concurrentes(archivos_a_descargar)
            self.assertEqual(mock_descargar.call_count, len(archivos_a_descargar))


if __name__ == "__main__":
    unittest.main()
