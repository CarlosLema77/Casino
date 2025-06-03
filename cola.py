import json
import os

RUTA_COLAS = "data/colas.json"

def cargarColas():
    """
    Loads the current game queues from the JSON file.
    If the file doesn't exist, returns a default dictionary with empty queues.
    """
    if not os.path.exists(RUTA_COLAS):
        return {"tragamonedas": [], "blackjack": []}
    with open(RUTA_COLAS, "r") as archivo:
        return json.load(archivo)

def guardarColas(colas):
    """
    Saves the current state of the queues to the JSON file.
    """
    with open(RUTA_COLAS, "w") as archivo:
        json.dump(colas, archivo, indent=4)

def agregarACola(juego, idJugador):
    """
    Adds a player to the queue for the specified game.
    
    Parameters:
        juego (str): The name of the game ("tragamonedas" or "blackjack").
        idJugador (str): The player's unique ID to add to the queue.
    """

    if juego.lower() != "blackjack" and juego.lower() != "tragamonedas":
        print("Ese juego no existe. ")
        return

    colas = cargarColas()

    # Create the queue if it doesn't exist yet
    if juego not in colas:
        colas[juego] = []

    # Add player to the queue
    colas[juego].append(idJugador)
    guardarColas(colas)
    print(f"Player {idJugador} added to the {juego} queue.")

def atenderSiguiente(juego):
    """
    Removes and returns the next player in the queue for the specified game.
    If the queue is empty, returns None and notifies the user.

    Parameters:
        juego (str): The name of the game queue to attend.

    Returns:
        str or None: The ID of the next player, or None if the queue is empty.
    """
    colas = cargarColas()

    if juego in colas and colas[juego]:
        siguiente = colas[juego].pop(0)
        guardarColas(colas)
        print(f"Next player for {juego}: {siguiente}")
        return siguiente
    else:
        print(f"No players in the {juego} queue.")
        return None
