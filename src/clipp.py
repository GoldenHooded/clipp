#!/usr/bin/env python3
import argparse
import shutil
import json
import os
import readline

# Colores ANSI
BLUE = "\033[34m"
GREY = "\033[90m"
RESET = "\033[0m"

# Archivo para guardar los datos
DATA_DIR = os.path.expanduser("~/.local/share/clipp")
DATA_FILE = os.path.join(DATA_DIR, "clipp_data.json")

# Crear el directorio si no existe
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Cargar lista desde el archivo JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Guardar lista en el archivo JSON
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(strings, f, indent=4)

# Obtener el tamaño de la terminal
def get_terminal_width():
    return shutil.get_terminal_size((80, 20)).columns

# Función para autocompletar comandos
def completer(text, state):
    commands = ['add', 'list', 'ls', 'ex', 'execute', 'remove', 'rm', 'clear']
    matches = [cmd for cmd in commands if cmd.startswith(text)]
    return matches[state] if state < len(matches) else None

# Configurar autocompletado
readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

# Crear un parser para los argumentos
parser = argparse.ArgumentParser(description="Aplicación Clipp.")

# Añadir comandos y opciones
subparsers = parser.add_subparsers(dest="command")

# Subparser para el comando 'add'
add_parser = subparsers.add_parser("add")
add_parser.add_argument("cmd", help="Comando que deseas añadir")
add_parser.add_argument("description", nargs="?", help="Descripción del comando (opcional)")

# Subparser para el comando 'list' o 'ls'
list_parser = subparsers.add_parser("list", aliases=["ls"])
list_parser.add_argument("-d", "--description", action="store_true", help="Muestra las descripciones")
list_parser.add_argument("-n", "--index", action="store_true", help="Muestra los índices")

# Subparser para el comando 'ex' o 'execute'
ex_parser = subparsers.add_parser("ex", aliases=["execute"])
ex_parser.add_argument("index", type=int, help="Índice del comando a ejecutar")
ex_parser.add_argument("extra", nargs="?", help="Argumento adicional para añadir al comando (opcional)")

# Subparser para el comando 'remove' o 'rm'
remove_parser = subparsers.add_parser("remove", aliases=["rm"])
remove_parser.add_argument("index", type=int, help="Índice del comando a remover")

# Subparser para el comando 'clear'
clear_parser = subparsers.add_parser("clear")

# Parsear los argumentos
args = parser.parse_args()

# Cargar los datos al iniciar
strings = load_data()

# Lógica para añadir un string con o sin descripción
def add_string():
    if args.cmd:
        description = args.description if args.description else ""
        strings.append({"command": args.cmd, "description": description})
        save_data()
        print(f"Comando añadido: {args.cmd} con descripción: {description}")

# Lógica de los comandos
if args.command == "add":
    add_string()

elif args.command in ["list", "ls"]:
    if not strings:
        print("La lista está vacía.")
    else:
        show_descriptions = args.description
        show_indices = args.index

        terminal_width = get_terminal_width()

        # Calcular el ancho de las columnas si la lista no está vacía
        max_index_len = len(str(len(strings) - 1)) if show_indices else 0
        max_command_len = max(len(item["command"]) for item in strings)
        description_column_start = max_index_len + max_command_len + 5  # Espacio entre columnas

        for index, item in enumerate(strings):
            command_str = item["command"]
            description_str = item["description"]

            # Mostrar índice en azul si se pide
            if show_indices:
                print(f"{BLUE}{str(index).rjust(max_index_len)}{RESET}: ", end="")

            # Mostrar el string del comando alineado
            print(command_str.ljust(max_command_len), end="")

            # Mostrar descripción en gris si se pide
            if show_descriptions:
                # Calcular el espacio restante para la descripción
                available_width = terminal_width - description_column_start
                description_str = description_str[:available_width]
                print(f" {GREY}{description_str}{RESET}")
            else:
                print()

# Lógica para ejecutar un comando por índice
elif args.command in ["ex", "execute"]:
    index = args.index
    command_to_execute = strings[index]["command"]
    if args.extra:
        command_to_execute += " " + args.extra
    print(f"Ejecutando: {command_to_execute}")
    os.system(command_to_execute)

# Lógica para remover un comando por índice
elif args.command in ["remove", "rm"]:
    index = args.index
    removed = strings.pop(index)
    save_data()
    print(f"Comando removido: {removed['command']}")

# Lógica para limpiar la lista
elif args.command == "clear":
    strings.clear()
    save_data()
    print("Lista de comandos limpiada.")