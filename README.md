# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción:
Este reto consiste en procesar información de transacciones bancarias mediante el desarrollo de una aplicación de línea de comandos(CLI) y que al final genere un reporte resumen.El proposito del reto es evaluar la capacidad de procesar datos, analizarlos y presentar los resultados de manera clara.

## Instrucciones de ejecucción:
### Requisitos previos:
  Tener instalado **Python 3.8 o superior**
  De no tenerlo puede descargalo desde [python.org](https://www.python.org/downloads/).

### Instalación de dependencias:
  En la terminal ejecutar el codigo:
  pip isntall pandas
  ![Captura de Pantalla](https://drive.google.com/uc?id=1tFpBgIr2svo4I0BGR8LdlqxHp8aK2anx)
  
### Ejecutar aplicación:

## Enfoque y solucción:
### Lógica implementada:
  1. El programa lee el archivo CSV con los datos de las transacciones
  2. Verificamos los tipos de transacciones
  3. Verificamos la cantidad de datos
  4. Agrupamos y sumamos los montos por el tipo de transacción; al final, se restan para obtener el balance final
  5. Mediante el comando `max()` obtenemos el monto mas alto y con el comando `idxmax()` obtenemos el ID de la transacción
  6. Agrupamos por tipo de transacción y contamos el número de transacciones por tipo
  7. Generamos el reporte de transacciones

### Diseño:
El diseño del programa fue sencillo y se centró en la eficiencia y la claridad del código. A continuación, se describen las decisiones clave tomadas durante el desarrollo:

  1. **Uso de pandas**: Elegí **pandas** como la librería principal para procesar el archivo CSV. Pandas es muy eficiente para manejar datos en forma de tablas y proporciona funciones rápidas para leer archivos CSV y filtrar datos. Además, ofrece un rendimiento sólido cuando se trabaja con archivos relativamente grandes.
  2. **Lectura del CSV**: Utilicé la función `pandas.read_csv()` para leer el archivo CSV, lo que permite cargar los datos en un **DataFrame**. Un DataFrame facilita la manipulación de datos y la ejecución de operaciones como la suma, el filtrado y el conteo.
  3. **Procesamiento de los Datos**: Tras cargar el archivo CSV en un DataFrame, utilicé las capacidades de pandas para filtrar las transacciones de tipo "Crédito" y "Débito", calcular el balance final y encontrar la transacción con el monto más alto. Las transacciones se procesan en tiempo lineal (O(n)), lo que significa que el rendimiento es óptimo incluso con archivos grandes.
  4. **Manejo de Errores**: Se ha implementado un manejo básico de errores para asegurar que el archivo CSV exista y esté bien formado. Si el archivo no está en el formato correcto o contiene datos incorrectos, el programa genera un mensaje de error explicativo.
  5. **Salida en la Terminal**: La salida del programa se presenta en la terminal, donde se muestra de manera clara y legible el balance final, la transacción de mayor monto y el conteo de transacciones.

#### Decisiones de Diseño

- **Simplicidad**: La solución fue diseñada para ser simple y fácil de entender. Opté por un diseño claro con funciones pequeñas y enfocadas en una tarea, lo que hace que el código sea fácil de mantener y modificar.
  
- **Escalabilidad**: Aunque el programa se diseñó para archivos CSV pequeños, su estructura es lo suficientemente flexible como para manejar archivos más grandes si es necesario. **Pandas** optimiza el procesamiento de archivos grandes debido a su eficiencia.

- **Interfaz de Línea de Comandos (CLI)**: La interfaz de línea de comandos se eligió por su simplicidad y facilidad de uso. No se requiere ninguna interfaz gráfica, lo que permite que el programa sea fácilmente ejecutado en servidores o en sistemas sin un entorno gráfico.

## Estructura del Proyecto:Archivos y carpetas principales
La estructura del proyecto es simple y está organizada de manera que sea fácil de entender y mantener. A continuación se describen los archivos del proyecto:

  - **`analysis.py`**: Este es el archivo principal donde se encuentra la lógica del programa. Contiene las funciones que procesan el archivo CSV y generan el reporte final, que incluye el balance final, la transacción de mayor monto y el conteo de transacciones.
  - **`data.csv`**: Carpeta que contiene los archivos CSV con las transacciones bancarias. En este ejemplo, el archivo se llama `transacciones.csv`. Si tienes más archivos CSV, puedes agregarlos en esta carpeta.
  - **`README.md`**: Documento que contiene la introducción del proyecto, las instrucciones de ejecucción, el enfoque y diseño utilizado.

---

5. **README del Proyecto:**  
   Incluye un archivo `README.md` con la siguiente estructura:

   - **Introducción:** Breve descripción del reto y su propósito.
   - **Instrucciones de Ejecución:** Cómo instalar dependencias y ejecutar la aplicación.
   - **Enfoque y Solución:** Lógica implementada y decisiones de diseño.
   - **Estructura del Proyecto:** Archivos y carpetas principales.

