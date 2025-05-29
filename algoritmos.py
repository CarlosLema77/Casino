import json
import os 
from gestionJugadores import cargarJugadores

def buscarJugadorNombre(nombre.lower()):

    tempA [] 

    cont = 0 #initialize the counter

    """Searches for a player by their name."""

    jugadores = cargarJugadores() #load the players from the json file

    """If the name is not found, it returns an empty list."""
    
    for jugador in jugadores:
        temp = jugador['nombre'].lower()
        for letra in nombre:
            for letra2 in temp:
                if letra == letra2:
                    cont = cont + 1
                if cont == 3:
w


