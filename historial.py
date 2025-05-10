import json
import os
from gestionJugadores import cargarJugadores, guardarJugadores

def historialJugador(idJugador, actividad):
    """Records an activity in the player's history.
    If the history is full (10 activities), the oldest one is removed."""
    
    jugadores = cargarJugadores() #load the players from the json file

    for jugador in jugadores:

        if jugador['id'] == idJugador:
            if len(jugador['historial']) == 10: #check if the history is empty
                jugador['historial'].pop()

            jugador['historial'].insert(0,actividad) #insert the activity at the beginning of the history
            guardarJugadores(jugadores)
            print(f"Actividad registrada en el historial del jugador {jugador['nombre']}.")
            return
    print("Jugador no encontrado.")
                    
def mostrarHistorial(idJugador):

    """Displays the player's history."""

    jugadores = cargarJugadores()  # Load the players from the JSON file

    for jugador in jugadores:

        """Check if the player ID matches the given ID"""

        if jugador['id'] == idJugador:
            print(f"Historial del jugador {jugador['nombre']}:")
            
            if not jugador['historial']: # Check if the history is empty
                print("El historial está vacío.")
                return
            else:
                print(f"{len(jugador['historial'])} actividades registradas:")
                for actividad in jugador['historial']: 
                    print(actividad)
                return

    print("Jugador no encontrado.")

