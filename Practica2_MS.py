
import os
import datetime

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
    print("8) Comentarios para Jordi")
    print("9) Salir")
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
            return
        print("\nContenido del directorio actual:")
        for nombre_elemento in elementos:
            ruta_elemento = os.path.join(os.getcwd(), nombre_elemento)
            if os.path.isdir(ruta_elemento):
                tipo = "CARPETA"
            else:
                tipo = "ARCHIVO"
            print(f"- {nombre_elemento}  ->  {tipo}")
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
            archivo_de_texto.write(nuevo_texto)
        print("Texto añadido correctamente.")
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
        else:
            os.remove(ruta_elemento)
            print("Archivo eliminado correctamente.")
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

def main():
    #Bucle principal del programa. Muestra la ruta y el menú hasta que el usuario salga.
    while True:
        mostrar_ruta_actual()
        mostrar_menu()
        opcion_elegida = input("Elige una opción (1 al 9): ").strip()
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
            notas_jordi()
        elif opcion_elegida == "9":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 9.")

main()