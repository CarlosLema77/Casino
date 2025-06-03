import json
import os 
from gestionJugadores import cargarJugadores

def buscarJugadorNombre(nombre):
    """
    Searches for players whose names contain the given text (case-insensitive).
    Prints all matching players.
    """
    bandera = False
    jugadores = cargarJugadores()  # Load players from the JSON file

    print("Jugador Encontrado:")

    for jugador in jugadores:
        if nombre.lower() in jugador['nombre'].lower():
            bandera = True
            print(f"ID: {jugador['id']}, Nombre: {jugador['nombre']}, Saldo: {jugador['saldo']}")

    if not bandera:
        print("Jugador NO encontrado o no existe")    


def BucarJugadoresID(idBuscado):
    """
    Performs a binary search to find a player by their unique ID.
    Assumes the player list is already sorted by ID.
    """
    jugadores = cargarJugadores()
    jugadoresOrdenados = ordenarJugadoresPorID(jugadores)

    init = 0
    fin = len(jugadoresOrdenados) - 1

    while init <= fin:
        medio = (init + fin) // 2
        jugadorActual = jugadoresOrdenados[medio]

        if jugadorActual['id'] == idBuscado:
            print("Jugador Encontrado:")
            print(f"Nombre: {jugadorActual['nombre']}, ID: {jugadorActual['id']}, Saldo: {jugadorActual['saldo']}")
            return
        elif idBuscado < jugadorActual['id']:
            fin = medio - 1
        else:
            init = medio + 1  # <- Este era un error en tu versión: antes decía `fin = medio + 1`
    
    print("Jugador NO encontrado.")


def ordenarJugadoresPorID(jugadores):
    """
    Returns a new list of players sorted by their 'id' field.
    """
    return sorted(jugadores, key=lambda jugador: jugador['id'])


def ordenarBurbuja(jugadores, clave):
    """
    Sorts the list of players using the Bubble Sort algorithm.
    Sorts in ascending order based on the given field (clave).
    """
    n = len(jugadores)
    for i in range(n):
        for j in range(0, n - i - 1):
            if jugadores[j][clave] < jugadores[j + 1][clave]:
                jugadores[j], jugadores[j + 1] = jugadores[j + 1], jugadores[j]


def ordenarSeccion(jugadores, clave):
    """
    Sorts the list of players using the Selection Sort algorithm.
    Sorts in ascending order based on the given field (clave).
    """
    n = len(jugadores)
    for i in range(n):
        indiceMenor = i
        for j in range(i + 1, n):
            if jugadores[j][clave] > jugadores[indiceMenor][clave]:
                indiceMenor = j

        if indiceMenor != i:
            jugadores[i], jugadores[indiceMenor] = jugadores[indiceMenor], jugadores[i]


def ordenarInsercion(jugadores, clave):
    """
    Sorts the list of players using the Insertion Sort algorithm.
    Sorts in ascending order based on the given field (clave).
    """
    n = len(jugadores)
    for i in range(1, n):
        jugadorActual = jugadores[i]
        j = i - 1

        while j >= 0 and jugadores[j][clave] > jugadorActual[clave]:
            jugadores[j + 1] = jugadores[j]
            j -= 1

        jugadores[j + 1] = jugadorActual


def mergeSort(jugadores, clave):
    """
    Sorts the list of players using the Merge Sort algorithm.
    Returns a new sorted list based on the given field (clave).
    """
    if len(jugadores) <= 1:
        return jugadores

    mitad = len(jugadores) // 2
    izquierda = mergeSort(jugadores[:mitad], clave)
    derecha = mergeSort(jugadores[mitad:], clave)

    i = 0
    j = 0
    resultado = []

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][clave] < derecha[j][clave]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
