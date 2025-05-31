import json
import os 
from gestionJugadores import cargarJugadores

def buscarJugadorNombre(nombre):

    bandera = False

    """Searches for a player by their name."""

    jugadores = cargarJugadores() #load the players from the json file

    """If the name is not found, it returns an empty list."""
    
    print("Jugador Encontrado: ")

    for jugador in jugadores:

        if nombre.lower() in jugador['nombre'].lower():
            bandera = True
            print(f"ID: {jugador['id']}, Nombre: {jugador['nombre']}, Saldo: {jugador['saldo']}")
            

    if not bandera:
        print("Jugador NO encontrado o no existe")    


"""
    Performs binary search to find a player by their unique ID.
    Requires the player list to be sorted by ID.
"""
def BucarJugadoresID (idBuscado):

    jugadores = cargarJugadores()
    jugadoresOrdenados = ordenarJugadoresPorID(jugadores)

    init = 0
    fin = len(jugadoresOrdenados)-1

    while init <= fin :
        medio = (init + fin)//2

        jugadorActual = jugadoresOrdenados[medio]

        if jugadorActual['id'] == idBuscado:
            print("Jugador Encontrado: ")
            print(f"Nombre: {jugadorActual['nombre']}, ID: {jugadorActual['id']}, Saldo: {jugadorActual['saldo']}")
            return
        
        elif idBuscado < jugadorActual['id']:
            fin = medio - 1
        else:
            fin = medio + 1
    print("Jugador NO encontrado. ")



"""
    Returns a new list of players sorted by their 'id' field.
"""
def ordenarJugadoresPorID(jugadores):
    """
    Returns a new list of players sorted by their 'id' field.
    """
    return sorted(jugadores, key=lambda jugador: jugador['id'])

def ordenarBurbuja(jugadores, clave):
    """
    Ordena la lista de jugadores por el campo dado (clave) usando Bubble Sort.
    """
    n = len(jugadores)
    for i in range(n):
        for j in range(0, n - i - 1):
            if jugadores[j][clave] > jugadores[j + 1][clave]:
                jugadores[j], jugadores[j + 1] = jugadores[j + 1], jugadores[j]


def ordenarSeccion(jugadores, clave):

    n = len(jugadores)
    for i in range(n):
        indiceMenor = i
        for j in range(i+1,n):
            if jugadores[j][clave] < jugadores[indiceMenor][clave]:
                indiceMenor = j
            
        if indiceMenor != i :
            jugadores[i],jugadores[indiceMenor] = jugadores[indiceMenor],jugadores[i]

def ordenarInsercion(jugadores, clave):
    
    n = len(jugadores)
    for i in range(1, n):
        jugadorActual = jugadores[i]
        j = i - 1

        while j >= 0 and jugadores[j][clave] > jugadorActual[clave]:
            jugadores[j+1] = jugadores[j]
            j -= 1

        jugadores[j+1] = jugadorActual
            
        



      
            


                
            

