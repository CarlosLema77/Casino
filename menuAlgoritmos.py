from algoritmos import (
    buscarJugadorNombre, BucarJugadoresID,
    ordenarBurbuja, ordenarSeccion, ordenarInsercion, mergeSort
)
from gestionJugadores import cargarJugadores

# Displays the submenu for searching and sorting players
def menuAlgoritmos():
    while True:
        print("\n--- SUBMENÚ DE BÚSQUEDAS Y ORDENAMIENTO ---") # Display submenu title
        print("1. Buscar jugador por nombre (lineal)") # Search player by name using linear search
        print("2. Buscar jugador por ID (binaria)") # Search player by ID using binary search
        print("3. Ordenar por saldo (burbuja)") # Sort players by balance using bubble sort
        print("4. Ordenar por nombre (merge sort)") # Sort players by name using merge sort
        print("5. Ordenar por ID (inserción)") # Sort players by ID using insertion sort
        print("6. Ordenar por total apostado (selección)") # Sort players by total bet using selection sort
        print("7. Volver al menú principal") # Return to the main menu


        opcion = input("Seleccione una opción: ").strip() # Get user input for submenu option
        jugadores = cargarJugadores() # Load players from file

        if opcion == "1":
            nombre = input("Ingrese parte del nombre: ") # Get part of the name to search for players
            buscarJugadorNombre(nombre) # Search players by name
        elif opcion == "2":
            id_buscado = input("Ingrese el ID exacto del jugador: ") # Get exact ID to search for a player
            BucarJugadoresID(id_buscado) # Search player by ID using binary search
        elif opcion == "3":
            ordenarBurbuja(jugadores, 'saldo') # Sort players by balance using bubble sort
            print("\nJugadores ordenados por saldo:") 
            for j in jugadores:
                print(f"{j['nombre']} - ${j['saldo']}") 
        elif opcion == "4":
            ordenados = mergeSort(jugadores, 'nombre') # Sort players by name using merge sort
            print("\nJugadores ordenados por nombre:") 
            for j in ordenados:
                print(f"{j['nombre']} - ID: {j['id']}") 
        elif opcion == "5":
            ordenarInsercion(jugadores, 'id') # Sort players by ID using insertion sort
            print("\nJugadores ordenados por ID:") 
            for j in jugadores:
                print(f"{j['id']} - {j['nombre']}") 
        elif opcion == "6":
            ordenarSeccion(jugadores, 'totalApostado') # Sort players by total bet using selection sort
            print("\nJugadores ordenados por total apostado:") 
            for j in jugadores:
                print(f"{j['nombre']} - Total apostado: ${j['totalApostado']}") 
        elif opcion == "7":
            break
        else:
            print("Opción inválida.") # Invalid option, prompt again
