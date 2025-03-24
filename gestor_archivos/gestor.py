# gestor.py (ubicado en la carpeta gestor_archivos)

class GestorArchivos:
    """
    Clase para realizar operaciones básicas con archivos de texto.
    """

    def leer_archivo(self, ruta):

        try:
            with open(ruta, 'r', encoding='utf-8') as archivo:
                return archivo.read()
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
            return None
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
            return None

    def escribir_archivo(self, ruta, contenido):

        try:
            with open(ruta, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
            return None

    def contar_palabras_unicas(self, ruta):

        contenido = self.leer_archivo(ruta)
        if contenido:
            palabras = contenido.split()
            return len(set(palabras))
        return 0

    def buscar_palabra(self, ruta, palabra):

        contenido = self.leer_archivo(ruta)
        if contenido:
            lineas = contenido.split('\n')
            return [linea for linea in lineas if palabra in linea]
        return []
