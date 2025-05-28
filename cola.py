import json
import os

RUTA_COLAS = "data/colas.json"

def cargarColas():
    if not os.path.exists(RUTA_COLAS):
        return {"tragamonedas": [], "blackjack": []}
    with open(RUTA_COLAS, "r") as archivo:
        return json.load(archivo)

def guardarColas(colas):
    with open(RUTA_COLAS, "w") as archivo:
        json.dump(colas, archivo, indent=4)

def agregarACola(juego, idJugador):
    colas = cargarColas()
    if juego not in colas:
        colas[juego] = []
    colas[juego].append(idJugador)
    guardarColas(colas)
    print(f"Jugador {idJugador} agregado a la cola de {juego}.")

def atenderSiguiente(juego):
    colas = cargarColas()
    if juego in colas and colas[juego]:
        siguiente = colas[juego].pop(0)
        guardarColas(colas)
        print(f"Siguiente jugador para {juego}: {siguiente}")
        return siguiente
    else:
        print(f"No hay jugadores en la cola de {juego}.")
        return None
