import json
import os

def cargarJugadores():
    """
    Loads the list of players from the JSON file.
    If the file does not exist, returns an empty list.
    """
    ruta = "data/jugadores.json"
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r") as archivo:
        return json.load(archivo)


def guardarJugadores(listaJugadores):
    """
    Saves the list of players to the JSON file with indentation.
    """
    ruta = "data/jugadores.json"
    with open(ruta, "w") as archivo:
        json.dump(listaJugadores, archivo, indent=4)


def registrarJugador():
    """
    Registers a new player by asking for name, unique ID, and initial balance.
    Ensures ID is unique and balance is not negative.
    Then saves the player to the JSON file.
    """
    jugadores = cargarJugadores()

    nombre = input("Ingrese el nombre del jugador: ")
    id_unico = input("Ingrese el ID único del jugador: ")
    saldo_inicial = float(input("Ingrese el saldo inicial del jugador: "))

    for jugador in jugadores:
        if jugador['id'] == id_unico:
            print("El ID ya está en uso. Intente nuevamente.")
            return

    if saldo_inicial < 0:
        print("El saldo inicial no puede ser negativo.")
        return

    nuevo_jugador = {
        "nombre": nombre,
        "id": id_unico,
        "saldo": saldo_inicial,
        "historial": [],
        "juegosGanados": 0,
        "juegosPerdidos": 0,
        "totalApostado": 0
    }

    jugadores.append(nuevo_jugador)
    guardarJugadores(jugadores)
    print(f"Jugador {nombre} registrado con éxito.")


def consultarJugador():
    """
    Looks up a player by their ID and displays their information.
    """
    jugadores = cargarJugadores()
    id_unico = input("Ingrese el ID único del jugador a consultar: ")

    for jugador in jugadores:
        if jugador['id'] == id_unico:
            print(f"Jugador encontrado: {jugador['nombre']}, \n ID: {jugador['id']}, \n Saldo: {jugador['saldo']}")
            return

    print("Jugador no encontrado.")


def modificarJugador():
    """
    Allows updating a player's name and/or balance.
    Validates non-negative balance and saves changes to file.
    """
    jugadores = cargarJugadores()
    id_unico = input("Ingrese el ID único del jugador a modificar: ")

    for jugador in jugadores:
        if jugador['id'] == id_unico:
            print(f"Jugador encontrado: {jugador['nombre']}, \n ID: {jugador['id']}, \n Saldo: {jugador['saldo']}")

            cambio = int(input("Desea modificar el nombre y/o el saldo del jugador? (1: Nombre, 2: Saldo, 3: Ambos): "))

            if cambio == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre del jugador: ")
                jugador["nombre"] = nuevo_nombre

            elif cambio == 2:
                nuevo_saldo = float(input("Ingrese el nuevo saldo del jugador: "))
                if nuevo_saldo < 0:
                    print("El saldo no puede ser negativo.")
                    return
                jugador["saldo"] = nuevo_saldo

            elif cambio == 3:
                nuevo_nombre = input("Ingrese el nuevo nombre del jugador: ")
                nuevo_saldo = float(input("Ingrese el nuevo saldo del jugador: "))
                if nuevo_saldo < 0:
                    print("El saldo no puede ser negativo.")
                    return
                jugador["nombre"] = nuevo_nombre
                jugador["saldo"] = nuevo_saldo

            else:
                print("Opción no válida.")
                return

            guardarJugadores(jugadores)
            print(f"Jugador {jugador['nombre']} modificado con éxito.")
            return

    print("Jugador no encontrado.")


def eliminarJugador():
    """
    Deletes a player from the system by their unique ID.
    Asks for confirmation before deleting.
    """
    jugadores = cargarJugadores()
    id_unico = input("Ingrese el ID único del jugador a eliminar: ")

    for jugador in jugadores:
        if jugador['id'] == id_unico:
            print(f"Jugador encontrado: {jugador['nombre']}, \n ID: {jugador['id']}, \n Saldo: {jugador['saldo']}")
            confirmacion = input("¿Está seguro de que desea eliminar este jugador? (s/n): ")

            if confirmacion.lower() == 's':
                jugadores.remove(jugador)
                guardarJugadores(jugadores)
                print(f"Jugador {jugador['nombre']} eliminado con éxito.")
                return
            else:
                print("Eliminación cancelada.")
                return

    print("Jugador no encontrado.")
