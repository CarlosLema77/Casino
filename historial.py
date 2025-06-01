import json
import os
from gestionJugadores import cargarJugadores, guardarJugadores

def historialJugador(idJugador, actividad):
    """
    Adds a new activity to the player's individual history (as a stack).
    Keeps only the 10 most recent entries.
    Updates the 'jugadores.json' file.
    """
    jugadores = cargarJugadores()  # Load the players from the JSON file

    for jugador in jugadores:
        if jugador['id'] == idJugador:
            # If the history already has 10 entries, remove the oldest (first in)
            if len(jugador['historial']) == 10:
                jugador['historial'].pop(0)

            # Add the new activity to the end (acts as top of the stack)
            jugador['historial'].append(actividad)
            guardarJugadores(jugadores)
            print(f"Actividad registrada en el historial del jugador {jugador['nombre']}.")
            return

    print("Jugador no encontrado.")

def mostrarHistorial(idJugador):
    """
    Displays the activity history of a specific player by ID.
    Shows the most recent activities (up to 10).
    """
    jugadores = cargarJugadores()

    for jugador in jugadores:
        if jugador['id'] == idJugador:
            print(f"Historial del jugador {jugador['nombre']}:")
            if len(jugador['historial']) == 0:
                print("El historial está vacío.")
                return
            else:
                for actividad in jugador['historial']:
                    print(actividad)
                return

    print("Jugador no encontrado.")
