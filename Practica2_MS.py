
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
    print("7) Comentarios para Jordi")
    print("8) Salir")
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




def main():
    #Bucle principal del programa. Muestra la ruta y el menú hasta que el usuario salga.
    while True:
        mostrar_ruta_actual()
        mostrar_menu()
        opcion_elegida = input("Elige una opción (1 al 8): ").strip()
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
            notas_jordi()
        elif opcion_elegida == "8":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 8.")

main()