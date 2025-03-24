import os
from base_datos.operaciones_db import insertar_empleado, consultar_por_departamento, calcular_salario_promedio
from gestor_archivos.gestor import GestorArchivos
from gestor_archivos.descargas_concurrentes import descargar_archivo, descargar_archivos_concurrentes
import optimizacion.optimizacion as optimizado
import optimizacion.original as original


def salir():
    print("Saliendo...")


def main():
    while True:
        print('\n')
        print('''---Prueba Técnica ---

       1. Ejercicio 1: Programación Orientada a Objetos (Gestor de archivos)
       2. Ejercicio 2: Concurrencia y Paralelismo (Descarga de archivos)
       3. Ejercicio 3: Base de Datos y ORM (Gestión de empleados)
       4. Ejercicio 4: Optimización de Código
       5. Salir

    ''')

        print('Seleccione alguna opción:')
        opc = input()

        if opc == '1':
            print("Seleccionó \nEjercicio 1: Programación Orientada a Objetos (Gestor de archivos)")

            gestor = GestorArchivos()
            ruta = r"C:\Users\lopez\OneDrive\Documentos\Prueba_Tecnica\Python\archivo1.txt"
            contenido = "Tres tristes tigres.\nComian pollo en tres tristes platos.\nTres tristes gallos.\nComian maiz en tres tristes platos."

            # Intentar escribir en el archivo
            gestor.escribir_archivo(ruta, contenido)

            # Intentar leer el archivo
            print("\nLeyendo el archivo...")
            contenido_archivo = gestor.leer_archivo(ruta)

            if contenido_archivo is None:
                print("No se pudo leer el archivo. Verifica la ruta o los permisos.")
            else:
                print("\nContenido del archivo:")
                print(contenido_archivo)
                print('------')
                print("Palabras únicas:")
                print(gestor.contar_palabras_unicas(ruta))
                print('------')
                print("Buscar palabra 'tres':")
                lineas_encontradas = gestor.buscar_palabra(ruta, "tres")
                print(lineas_encontradas)

            input("\nPresiona Enter para volver al menú...")

        elif opc == '2':
            print("Seleccionó \nEjercicio 2: Concurrencia y Paralelismo (Descarga de archivos)")

            ruta_destino = input("Por favor, ingresa la ruta donde deseas guardar los archivos: ")
            if not os.path.exists(ruta_destino):
                os.makedirs(ruta_destino)

            archivos_a_descargar = [
                {'id': 1, 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
                 'nombre': 'archivo1.pdf', 'ruta': ruta_destino},
                {'id': 2, 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
                 'nombre': 'archivo2.pdf', 'ruta': ruta_destino},
                {'id': 3, 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
                 'nombre': 'archivo3.pdf', 'ruta': ruta_destino}
            ]

            print("\nDescargando un solo archivo:")
            descargar_archivo(archivos_a_descargar[0])

            print("\nDescargando múltiples archivos de forma concurrente:")
            descargar_archivos_concurrentes(archivos_a_descargar)

            input("\nPresiona Enter para volver al menú...")

        elif opc == '3':
            print("Seleccionó \nEjercicio 3: Base de Datos y ORM (Gestión de empleados)")

            while True:
                print('''
    Gestión de Empleados:
    1. Insertar un nuevo empleado
    2. Consultar empleados por departamento
    3. Calcular salario promedio por departamento
    4. Volver al menú principal
                ''')

                sub_opc = input("Seleccione una opción: ")

                if sub_opc == '1':
                    nombre = input("Ingrese el nombre del empleado: ")
                    salario = float(input("Ingrese el salario del empleado: "))
                    departamento = input("Ingrese el departamento del empleado: ")
                    insertar_empleado(nombre, salario, departamento)
                    input("\nPresiona Enter para continuar...")

                elif sub_opc == '2':
                    departamento = input("Ingrese el nombre del departamento: ")
                    consultar_por_departamento(departamento)
                    input("\nPresiona Enter para continuar...")

                elif sub_opc == '3':
                    departamento = input("Ingrese el nombre del departamento: ")
                    calcular_salario_promedio(departamento)
                    input("\nPresiona Enter para continuar...")

                elif sub_opc == '4':
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción inválida, por favor seleccione una opción válida.")

        elif opc == '4':
            print("Seleccionó \nEjercicio 4: Optimización de Código")

            while True:
                print('''
                Optimizacion de codigo
                1. Codigo Optimizado
                2. Codigo Original
                3. Volver al menú principal
                            ''')

                sub_opc = input("Seleccione una opción: ")

                if sub_opc == '1':

                    print("Seleccionó Código Optimizado")
                    datos = [1, 2, 3, 4, 5]
                    resultado = optimizado.procesar_datos(datos)
                    print("Resultado con código optimizado:", resultado)


                elif sub_opc == '2':

                    print("Seleccionó Código Original")
                    datos = [1, 2, 3, 4, 5]
                    resultado = original.procesar_datos_original(datos)
                    print("Resultado con código original:", resultado)



                elif sub_opc == '3':
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción inválida, por favor seleccione una opción válida.")

        elif opc == '5':
            print("Seleccionó la opción: Salir")
            salir()
            break

        else:
            print("Opción inválida, por favor seleccione una opción válida.")


if __name__ == "__main__":
    main()
