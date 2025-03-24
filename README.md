# Prueba Técnica: Buenas Prácticas de Programación en Python

Este proyecto aborda una serie de ejercicios técnicos avanzados utilizando Python, siguiendo buenas prácticas de programación, pruebas unitarias, y un flujo de trabajo profesional con Git.

---

## Instalación y Ejecución

### 1. **Requisitos previos**
   - Asegúrate de tener **Python 3.10** o una versión superior instalada en tu sistema. Verifica la instalación con:
     ```bash
     python --version
     ```

### 2. **Clonar el repositorio**
   - Clona este repositorio en tu máquina local y accede al directorio del proyecto:
     ```bash
     git clone https://github.com/crislopeto123/Prueba_Tecnica_Python.git
     cd Prueba_Tecnica_Python
     ```

### 3. **Configurar un entorno virtual**
   - Crea y activa un entorno virtual:
     ```bash
     python -m venv venv
     ```
     - **Sistemas UNIX/Mac:**
       ```bash
       source venv/bin/activate
       ```
     - **Windows:**
       ```bash
       venv\Scripts\activate
       ```

### 4. **Instalar dependencias**
   - Instala las dependencias necesarias desde el archivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

### 5. **Ejecutar el proyecto**
   - Inicia el programa ejecutando:
     ```bash
     python main.py
     ```

---

## Funcionalidades del Programa

Al iniciar el proyecto, se desplegará un menú interactivo que permite acceder a las siguientes funcionalidades:

### **1. Gestión de Archivos (Ejercicio 1)**
- Crear y escribir contenido en un archivo `archivo1.txt`.
- Leer el archivo para mostrar su contenido.
- Realizar análisis, como:
  - Contar palabras únicas.
  - Buscar y mostrar líneas que contengan la palabra "tres".

### **2. Descargas Concurrentes (Ejercicio 2)**
- Descargar archivos de forma individual o concurrente utilizando `ThreadPoolExecutor`.
- Especificar una ruta donde guardar los archivos descargados.

### **3. Gestión de Base de Datos (Ejercicio 3)**
- Operaciones con una base de datos SQLite (`empleados.db`):
  - Insertar nuevos empleados.
  - Consultar empleados por departamento.
  - Calcular el salario promedio de un departamento.

### **4. Optimización de Código (Ejercicio 4)**
- Comparar resultados entre el código original y el código optimizado:
  - **Código original:** Iterativo, utiliza métodos tradicionales.
  - **Código optimizado:** Basado en comprensión de listas para mayor eficiencia.

### **5. Salir**
- Finalizar el programa.

---

## Estructura del Proyecto

- **`base_datos/`:** Módulos para gestión y operaciones con bases de datos (SQLAlchemy).
- **`gestor_archivos/`:** Funciones para manejo de archivos y descargas concurrentes.
- **`optimizacion/`:** Implementaciones del código original y su versión optimizada.
- **`tests/`:** Pruebas unitarias para validar cada módulo.
- **`main.py`:** Punto de entrada principal del programa.

---

## Ejercicio 4: Explicación de Optimización

### Código Optimizado: 
Se mejora el rendimiento del código original utilizando comprensión de listas en lugar de iteración basada en índices. Esto reduce la complejidad y mejora la legibilidad.
#### Cambios realizados: 
1. **Iteración simplificada:** Se reemplaza `range(len(datos))` por un bucle directo sobre los elementos (`for x in datos`). 
2. **Uso de comprensión de listas:** Combina la construcción de la lista y la lógica de cálculo en una sola línea.

#### Ejemplo de Ejecución: 

```python datos = [1, 2, 3, 4, 5] resultado = optimizado.procesar_datos(datos) print(resultado) # Salida: [3, 4, 9, 8, 15]
---

## Ejecución de Pruebas

Este proyecto incluye pruebas unitarias para garantizar la funcionalidad de cada módulo. Para ejecutar las pruebas:

1. Abre una terminal en el directorio principal del proyecto.
2. Ejecuta el siguiente comando:
   ```bash
   pytest
3. deberia salir este resultado
4. 
   ============================= test session starts =============================
platform win32 -- Python 3.10, pytest-7.2.0
rootdir: C:\Users\lopez\Prueba_Tecnica_Python
collected 9 items

test/test_base_datos.py ...                                                    [ 33%]
test/test_gestor_archivos.py ...                                               [ 66%]
test/test_descargas.py ..                                                      [ 88%]
test/test_optimizacion.py .                                                    [100%]

============================= 9 passed in 2.15s ================================


