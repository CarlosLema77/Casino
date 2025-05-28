import json
import os
from gestionJugadores import cargarJugadores

RUTA_COLAS = "data/colas.json"

def cargarCola(nombreJuego):
    if not os.path.exists(RUTA_COLAS):
        return {}
    with open(RUTA_COLAS, "r") as archivo:
        colas = json.load(archivo)
    return colas.get(nombreJuego, [])

def guardarCola(nombreJuego, cola):
    if os.path.exists(RUTA_COLAS):
        with open(RUTA_COLAS, "r") as archivo:
            colas = json.load(archivo)
    else:
        colas = {}

    colas[nombreJuego] = cola
    with open(RUTA_COLAS, "w") as archivo:
        json.dump(colas, archivo, indent=4)

def agregarACola(nombreJuego, idJugador):
    jugadores = cargarJugadores()
    if not any(j['id'] == idJugador for j in jugadores):
        print("Jugador no encontrado.")
        return

    cola = cargarCola(nombreJuego)
    if idJugador in cola:
        print("El jugador ya está en la cola.")
        return
    cola.append(idJugador)
    guardarCola(nombreJuego, cola)
    print(f"Jugador {idJugador} agregado a la cola de {nombreJuego}.")

def atenderJugador(nombreJuego):
    cola = cargarCola(nombreJuego)
    if not cola:
        print(f"No hay jugadores en la cola de {nombreJuego}.")
        return None
    idJugador = cola.pop(0)
    guardarCola(nombreJuego, cola)
    print(f"Atendiendo jugador {idJugador} en {nombreJuego}.")
    return idJugador
