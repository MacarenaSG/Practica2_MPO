
import os
import datetime

from colorama import Fore, Style, init
init(autoreset=True)
#autoreset=True hace que los colores se restauren automáticamente después de cada línea.

HISTORIAL = []
# Aquí se guardarán los comandos que el usuario use

def mostrar_menu():
    #Muestra las opciones disponibles del programa.
    print("\n================ MENÚ PRINCIPAL ================")
    print("1) Listar contenido del directorio actual")
    print("2) Crear un nuevo directorio")
    print("3) Crear un archivo de texto")
    print("4) Escribir texto en un archivo existente (añadir al final)")
    print("5) Eliminar un archivo o directorio")
    print("6) Mostrar información de un archivo o directorio")
    print("7) Ir al directorio padre")
    print("8) Renombrar un archivo o directorio")
    print("9) Mostrar el tamaño total de los archivos del directorio actual")
    print("10) Historial de comandos")
    print("11) Comentarios para Jordi")
    print("12) Salir")
    print("================================================")


def mostrar_ruta_actual():
    #Muestra la ruta del directorio actual para que el usuario se sitúe.
    ruta_directorio_actual = os.getcwd()
    print(f"\nRuta actual: {ruta_directorio_actual}")


def listar_contenido():
    #Lista archivos y carpetas del directorio actual indicando su tipo.
    try:
        elementos = os.listdir(os.getcwd())
        if not elementos:
            print("El directorio está vacío.")
            HISTORIAL.append("Listar contenido (vacío)")
            return
        print("\nContenido del directorio actual:")
        for nombre_elemento in elementos:
            ruta_elemento = os.path.join(os.getcwd(), nombre_elemento)
            if os.path.isdir(ruta_elemento):
                tipo = "CARPETA"
                color = Fore.BLUE + Style.BRIGHT
            else:
                tipo = "ARCHIVO"
                color = Fore.MAGENTA
            print(f"- {color}{nombre_elemento}{Style.RESET_ALL}  ->  {tipo}")
        HISTORIAL.append("Listar contenido")
    except PermissionError:
        print("No tienes permisos para listar este directorio.")
    except FileNotFoundError:
        print("El directorio actual no existe o no se puede acceder.")
    except OSError as error_del_sistema_operativo:
        print(f"Ocurrió un error al listar el contenido: {error_del_sistema_operativo}")

def crear_directorio():
    #Crea una nueva carpeta con el nombre indicado por el usuario.
    nombre_directorio = input("Escribe el nombre del nuevo directorio: ").strip()
    if not nombre_directorio:
        print("El nombre no puede estar vacío.")
        return
    ruta_nueva = os.path.join(os.getcwd(), nombre_directorio)
    if os.path.exists(ruta_nueva):
        print("Ya existe un archivo o directorio con ese nombre.")
        return
    try:
        os.mkdir(ruta_nueva)
        print(f"Directorio creado: {ruta_nueva}")
        HISTORIAL.append(f"Crear directorio -> {nombre_directorio}")
    except PermissionError:
        print("No tienes permisos para crear el directorio en esta ubicación.")
    except FileNotFoundError:
        print("La ruta indicada no existe.")
    except OSError as error_del_sistema_operativo:
        print(f"No se pudo crear el directorio: {error_del_sistema_operativo}")

def crear_archivo():
    #Crea un archivo de texto y permite escribir contenido inicial.
    nombre_archivo = input("Escribe el nombre del archivo (por ejemplo, notas.txt): ").strip()
    if not nombre_archivo:
        print("El nombre no puede estar vacío.")
        return
    ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
    if os.path.exists(ruta_archivo):
        print("Ya existe un archivo o directorio con ese nombre.")
        return
    try:
        contenido_inicial = input("Escribe el contenido inicial (puede estar vacío): ")
        with open(ruta_archivo, mode="w", encoding="utf-8") as archivo_de_texto:
            archivo_de_texto.write(contenido_inicial)
        print(f"Archivo creado: {ruta_archivo}")
        HISTORIAL.append(f"Crear archivo -> {nombre_archivo}")
    except PermissionError:
        print("No tienes permisos para crear o escribir en este archivo.")
    except FileNotFoundError:
        print("La ruta indicada no existe.")
    except OSError as error_del_sistema_operativo:
        print(f"No se pudo crear el archivo: {error_del_sistema_operativo}")

def escribir_en_archivo():
    #Abre un archivo existente y añade texto al final.
    nombre_archivo = input("Escribe el nombre del archivo existente: ").strip()
    if not nombre_archivo:
        print("El nombre no puede estar vacío.")
        return
    ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
    if not os.path.exists(ruta_archivo):
        print("El archivo no existe.")
        return
    if os.path.isdir(ruta_archivo):
        print("Has indicado una carpeta. Debes indicar un archivo de texto.")
        return
    try:
        nuevo_texto = input("Escribe el texto que quieres añadir al final: ")
        with open(ruta_archivo, mode="a", encoding="utf-8") as archivo_de_texto:
            archivo_de_texto.write("\n" + nuevo_texto)
        print("Texto añadido correctamente.")
        HISTORIAL.append(f"Escribir en archivo -> {nombre_archivo}")
    except PermissionError:
        print("No tienes permisos para escribir en este archivo.")
    except FileNotFoundError:
        print("El archivo no existe o la ruta no es válida.")
    except OSError as error_del_sistema_operativo:
        print(f"No se pudo escribir en el archivo: {error_del_sistema_operativo}")

def eliminar_elemento():
    #Elimina un archivo o una carpeta vacía indicada por el usuario.
    nombre_elemento = input("Escribe el nombre del archivo o directorio a eliminar: ").strip()
    if not nombre_elemento:
        print("El nombre no puede estar vacío.")
        return
    ruta_elemento = os.path.join(os.getcwd(), nombre_elemento)
    if not os.path.exists(ruta_elemento):
        print("No existe un archivo o directorio con ese nombre.")
        return
    try:
        if os.path.isdir(ruta_elemento):
            # os.rmdir solo elimina directorios vacíos.
            os.rmdir(ruta_elemento)
            print("Carpeta eliminada correctamente (debe estar vacía).")
            HISTORIAL.append(f"Eliminar carpeta -> {nombre_elemento}")
        else:
            os.remove(ruta_elemento)
            print("Archivo eliminado correctamente.")
            HISTORIAL.append(f"Eliminar archivo -> {nombre_elemento}")
    except PermissionError:
        print("No tienes permisos para eliminar este elemento.")
    except OSError as error_del_sistema_operativo:
        # Por ejemplo, directorio no vacío u otros problemas del sistema.
        print(f"No se pudo eliminar el elemento: {error_del_sistema_operativo}")


def mostrar_informacion():
    #Muestra el tamaño, la fecha de modificación y el tipo (archivo o carpeta).
    nombre_elemento = input("Escribe el nombre del archivo o directorio: ").strip()
    if not nombre_elemento:
        print("El nombre no puede estar vacío.")
        return

    ruta_elemento = os.path.join(os.getcwd(), nombre_elemento)

    if not os.path.exists(ruta_elemento):
        print("No existe un archivo o directorio con ese nombre.")
        return

    try:
        # Obtenemos el tamaño del archivo en bytes
        tamanio_en_bytes = os.path.getsize(ruta_elemento)

        # Obtenemos la última modificación
        modificacion = os.path.getmtime(ruta_elemento)

        # Convertimos modificacion a formato legible (año-mes-día hora:minutos:segundos)
        fecha_modificacion = datetime.datetime.fromtimestamp(modificacion).strftime("%Y-%m-%d %H:%M:%S")

        # También obtenemos la hora actual, usando datetime.datetime.now()
        ahora = datetime.datetime.now()
        hora_actual = ahora.strftime("%Y-%m-%d %H:%M:%S")

        # Comprobamos si es archivo o carpeta
        if os.path.isdir(ruta_elemento):
            tipo_elemento = "CARPETA"
        else:
            tipo_elemento = "ARCHIVO"

        # Mostramos toda la información
        print("\n--- Información del elemento ---")
        print(f"Nombre: {nombre_elemento}")
        print(f"Ruta: {ruta_elemento}")
        print(f"Tipo: {tipo_elemento}")
        print(f"Tamaño (bytes): {tamanio_en_bytes}")
        print(f"Fecha de última modificación: {fecha_modificacion}")
        print(f"Hora actual del sistema: {hora_actual}")

        HISTORIAL.append(f"Mostrar información -> {nombre_elemento}")

        #Si es un archivo, mostramos su contenido
        if os.path.isfile(ruta_elemento):
            print("\n--- Contenido del archivo ---")
            try:
                with open(ruta_elemento, "r", encoding="utf-8") as archivo:
                    contenido = archivo.read()
                    if contenido.strip() == "":
                        print("(El archivo está vacío)")
                    else:
                        print(contenido)
            except UnicodeDecodeError:
                print("(El archivo no es de texto o tiene un formato que no se puede leer)")
            except Exception as error:
                print(f"(No se pudo leer el contenido del archivo: {error})")

    except PermissionError:
        print("No tienes permisos para leer la información de este elemento.")
    except OSError as error_del_sistema_operativo:
        print(f"No se pudo obtener la información: {error_del_sistema_operativo}")

def ir_directorio_padre():
    #Permite moverse al directorio padre (uno hacia atrás).
    ruta_actual = os.getcwd()
    ruta_padre = os.path.dirname(ruta_actual)

    if ruta_padre == ruta_actual:
        print("Ya estás en el directorio raíz. No puedes subir más.")
    else:
        os.chdir(ruta_padre)
        print(f"Te has movido al directorio: {ruta_padre}")
        HISTORIAL.append(f"Ir al directorio padre -> {ruta_padre}")

def renombrar_elemento():
    #Permite renombrar un archivo o una carpeta en el directorio actual.
    nombre_actual = input("Escribe el nombre ACTUAL del archivo o directorio: ").strip()
    if not nombre_actual:
        print("El nombre actual no puede estar vacío.")
        return

    nuevo_nombre = input("Escribe el NUEVO nombre: ").strip()
    if not nuevo_nombre:
        print("El nuevo nombre no puede estar vacío.")
        return

    ruta_actual = os.path.join(os.getcwd(), nombre_actual)
    ruta_nueva = os.path.join(os.getcwd(), nuevo_nombre)

    # Validaciones
    if not os.path.exists(ruta_actual):
        print("No existe un archivo o directorio con ese nombre actual.")
        return

    if os.path.exists(ruta_nueva):
        print("Ya existe un archivo o directorio con el nuevo nombre.")
        return

    if nombre_actual == nuevo_nombre:
        print("El nombre actual y el nuevo nombre son iguales. No hay nada que cambiar.")
        return

    # Intento de renombrado
    try:
        os.rename(ruta_actual, ruta_nueva)
        print(f"Se ha renombrado correctamente a: {nuevo_nombre}")
        HISTORIAL.append(f"Renombrar -> {nombre_actual} -> {nuevo_nombre}")
    except PermissionError:
        print("No tienes permisos para renombrar este elemento.")
    except FileNotFoundError:
        # Por si el origen desaparece entre la comprobación y el renombrado
        print("El elemento a renombrar ya no existe.")
    except OSError as error_del_sistema_operativo:
        print(f"No se pudo renombrar: {error_del_sistema_operativo}")

def mostrar_tamano_total():
    # Obtener la ruta actual
    ruta_actual = os.getcwd()

    # Listar los elementos de la carpeta actual
    elementos = os.listdir(ruta_actual)

    # Variable para acumular el tamaño total
    tamano_total = 0

    # Recorrer todos los elementos
    for nombre in elementos:
        ruta_completa = os.path.join(ruta_actual, nombre)

        # Solo contar los archivos (no carpetas)
        if os.path.isfile(ruta_completa):
            tamano_total += os.path.getsize(ruta_completa)

    # Mostrar el resultado en diferentes unidades
    print("\n--- TAMAÑO TOTAL DE LOS ARCHIVOS ---")
    print(f"Total en bytes: {tamano_total}")
    print(f"En kilobytes (KB): {tamano_total / 1024:.2f}")
    print(f"En megabytes (MB): {tamano_total / (1024 * 1024):.2f}")

def mostrar_historial():
    #Muestra todos los comandos que el usuario ha ejecutado en esta sesión.
    if not HISTORIAL:
        print("Aún no has ejecutado ningún comando.")
    else:
        print("\n--- HISTORIAL DE COMANDOS ---")
        for numero, comando in enumerate(HISTORIAL, start=1):
            print(f"{numero}. {comando}")

def notas_jordi():
    while True:
        print("\n---APARTADOS EXTRAS: Comentarios y dificultades---")
        print("1 - Escritura y Comprobación de Errores ")
        print("2 - Directorio padre")
        print("3 - Uso de Colorama")
        print("4 - Renombrar elementos")
        print("5 - Mostar tamaño total de los archivos")
        print("6 - Historial de comandos")
        print("7 - Volver al Menu Principal")

        opcion = input("Selecciona una opción:")

        if opcion == "1":
            print("\nEscritura y Comprobación de Errores:\n")
            print("Uno de los aspectos que más me ha costado ha sido la parte del manejo de errores con las excepciones PermissionError, FileNotFoundError y OSError.")
            print("Entendía la teoría de para qué servía cada una, pero me resultó complicado aplicarlas correctamente en el código para que el programa no se cerrara al producirse un fallo. ")
            print("Además, al probar el proyecto en la consola, no siempre pude comprobar si realmente se generaban estos errores.")
            print("Puesto que en mi entorno no se daban las situaciones necesarias (por ejemplo, intentar acceder a carpetas sin permisos o rutas inexistentes).")
            print("Aun así, los añadí para asegurar que el programa sea más robusto y preparado ante posibles problemas reales.")
            print("Usé las siguientes referencias para poder aplicarlo")
            print("https://docs.python.org/3/library/exceptions.html")
            print("https://realpython.com/ref/builtin-exceptions/permissionerror/")
            print("https://labex.io/tutorials/python-how-to-handle-filenotfounderror-in-python-421944")

        elif opcion == "2":
            print("\nDirectorio padre:\n")
            print("Otra parte en la que me ha surgido muchas dudas ha sido la de permitir volver al directorio padre.")
            print("Al principio me costaba entender cómo funcionaba la relación entre las rutas en el sistema de archivos y qué significaba exactamente el “directorio padre”. ")
            print("También tuve que aprender cómo usar correctamente las funciones os.getcwd() y os.path.dirname() para cambiar de carpeta sin provocar errores. ")
            print("Aunque finalmente conseguí que funcionara, fue un apartado que requirió varias pruebas y consultas para comprenderlo bien.")
            print("Usé la siguiente referencia para poder aplicarlo")
            print("https://docs.python.org/3/library/os.path.html")

        elif opcion == "3":
            print("\nUso de Colorama:\n")
            print("Este apartado me ha resultado super facil de entender y aplicar.")
            print("Me ha llecado tan solo unos pocos minutos escribir el código, ya que intarlar colorama desde consola a sido muy sencillo")
            print("Las bibliografias que he utilizado han sido las siguietnes.")
            print("https://thelinuxcode.com/colorama-python/")
            print("https://www.geeksforgeeks.org/python/introduction-to-python-colorama/ ")


        elif opcion == "4":
            print("\nRenombrar elementos\n")
            print("En este apartado lo que más trabajo me ha costado ha sido hacer funcionar correctamente las validaciones para evitar errores.")
            print("Al principio, el programa se detenía si el archivo no existía o si ya había otro con el mismo nombre, por lo que tuve que aprender a usar comprobaciones con os.path.exists() y manejar las excepciones adecuadas.")
            print("Para ello, usé las siguientes referencias y la IA para lograr escribir las validacioens correctamente y poder hacer funcinar el código. ")
            print("https://www.tutorialspoint.com/python/python_renaming_and_delete_files.htm")
            print("https://www.geeksforgeeks.org/python/python-os-rename-method/")
            print("https://docs.python.org/3/library/os.html")

        elif opcion == "5":
            print("\nMostar tamaño total de los archivos\n")
            print("Este apartado me ha resultado bastante sencillo de realizar, ya que la referencia “How to calculate a directory size using Python?” explica el proceso de forma muy clara y visual.")
            print("Gracias a los ejemplos mostrados en esa guía, pude entender fácilmente cómo recorrer los archivos del directorio actual y sumar sus tamaños usando os.path.getsize()")
            print("https://www.geeksforgeeks.org/python/how-to-get-size-of-folder-using-python/")
            print("https://www.delftstack.com/api/python/python-os-path-getsize/")
            print("https://www.tutorialspoint.com/How-to-calculate-a-directory-size-using-Python")

        elif opcion == "6":
            print("\nHistorial de comandos\n")
            print("La implementación del historial de comandos ha sido relativamente sencilla.")
            print("Sin embargo, la mayor dificultad ha estado en colocar correctamente las líneas que añadían los registros del historial dentro del código, especialmente para evitar que los return impidieran que se guardara el comando antes de que la función terminara")
            print("Tuve que probar varias posiciones hasta conseguir que todos los comandos se registraran sin causar errores ni interferir con el funcionamiento del programa.")
            print("Usando las siguientes referencias y la IA conseguí escribir el código en el sitio adecuado para que pudiese quedar todo registrado. ")
            print("https://dnmtechs.com/viewing-command-history-in-interactive-python/")
            print("https://cmd2.readthedocs.io/en/latest/features/history/")

        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def main():
    #Bucle principal del programa. Muestra la ruta y el menú hasta que el usuario salga.
    while True:
        mostrar_ruta_actual()
        mostrar_menu()
        opcion_elegida = input("Elige una opción (1 al 12): ").strip()
        if opcion_elegida == "1":
            listar_contenido()
        elif opcion_elegida == "2":
            crear_directorio()
        elif opcion_elegida == "3":
            crear_archivo()
        elif opcion_elegida == "4":
            escribir_en_archivo()
        elif opcion_elegida == "5":
            eliminar_elemento()
        elif opcion_elegida == "6":
            mostrar_informacion()
        elif opcion_elegida == "7":
            ir_directorio_padre()
        elif opcion_elegida == "8":
            renombrar_elemento()
        elif opcion_elegida == "9":
            mostrar_tamano_total()
        elif opcion_elegida == "10":
            mostrar_historial()
        elif opcion_elegida == "11":
            notas_jordi()
        elif opcion_elegida == "12":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 12.")

main()