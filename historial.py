import json
import os
from gestionJugadores import cargarJugadores

def historialJugador(idJugador, actividad, jugadores=None):
    """
    Adds an activity to the player's history.
    - If 'jugadores' is passed, modifies that list (preferred).
    - If not, loads the player list from file (read-only).
    This version does NOT save anything by itself.
    """
    if jugadores is None:
        jugadores = cargarJugadores()

    for jugador in jugadores:
        if jugador['id'] == idJugador:
            if 'historial' not in jugador or not isinstance(jugador['historial'], list):
                jugador['historial'] = []
            if len(jugador['historial']) >= 10:
                jugador['historial'].pop(0)
            jugador['historial'].append(actividad)
            print(f"[DEBUG] Historial actualizado: {actividad}")
            return

    print("Jugador no encontrado al actualizar historial.")

def mostrarHistorial(idJugador):
    """
    Displays the activity history of a specific player by ID.
    """
    jugadores = cargarJugadores()

    for jugador in jugadores:
        if jugador['id'] == idJugador:
            print(f"Historial del jugador {jugador['nombre']}:")
            if not jugador.get('historial'):
                print("El historial está vacío.")
                return
            for actividad in jugador['historial']:
                print(actividad)
            return

    print("Jugador no encontrado.")
