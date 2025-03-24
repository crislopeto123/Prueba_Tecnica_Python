import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def descargar_archivo(archivo):
    try:
        ruta_completa = os.path.join(archivo['ruta'], archivo['nombre'])
        os.makedirs(archivo['ruta'], exist_ok=True)

        print(f"\nIniciando la descarga del archivo: {archivo['nombre']} desde {archivo['url']} a {ruta_completa}")
        respuesta = requests.get(archivo['url'], stream=True)
        respuesta.raise_for_status()
        with open(ruta_completa, 'wb') as archivo_local:
            for chunk in respuesta.iter_content(chunk_size=8192):
                archivo_local.write(chunk)
        print(f"Archivo descargado exitosamente: {ruta_completa}")
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP al descargar el archivo {archivo['nombre']}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error general al descargar el archivo {archivo['nombre']}: {e}")


def descargar_archivos_concurrentes(archivos):
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(descargar_archivo, archivo): archivo for archivo in archivos}
        for future in as_completed(futures):
            archivo = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"Error al descargar el archivo {archivo['nombre']}: {e}")