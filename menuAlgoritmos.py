from algoritmos import (
    buscarJugadorNombre, BucarJugadoresID,
    ordenarBurbuja, ordenarSeccion, ordenarInsercion, mergeSort
)
from gestionJugadores import cargarJugadores

def menuAlgoritmos():
    while True:
        print("\n--- SUBMENÚ DE BÚSQUEDAS Y ORDENAMIENTO ---")
        print("1. Buscar jugador por nombre (lineal)")
        print("2. Buscar jugador por ID (binaria)")
        print("3. Ordenar por saldo (burbuja)")
        print("4. Ordenar por nombre (merge sort)")
        print("5. Ordenar por ID (inserción)")
        print("6. Ordenar por total apostado (selección)")
        print("7. Volver al menú principal")


        opcion = input("Seleccione una opción: ").strip()
        jugadores = cargarJugadores()

        if opcion == "1":
            nombre = input("Ingrese parte del nombre: ")
            buscarJugadorNombre(nombre)
        elif opcion == "2":
            id_buscado = input("Ingrese el ID exacto del jugador: ")
            BucarJugadoresID(id_buscado)
        elif opcion == "3":
            ordenarBurbuja(jugadores, 'saldo')
            print("\nJugadores ordenados por saldo:")
            for j in jugadores:
                print(f"{j['nombre']} - ${j['saldo']}")
        elif opcion == "4":
            ordenados = mergeSort(jugadores, 'nombre')
            print("\nJugadores ordenados por nombre:")
            for j in ordenados:
                print(f"{j['nombre']} - ID: {j['id']}")
        elif opcion == "5":
            ordenarInsercion(jugadores, 'id')
            print("\nJugadores ordenados por ID:")
            for j in jugadores:
                print(f"{j['id']} - {j['nombre']}")
        elif opcion == "6":
            ordenarSeccion(jugadores, 'totalApostado')
            print("\nJugadores ordenados por total apostado:")
            for j in jugadores:
                print(f"{j['nombre']} - Total apostado: ${j['totalApostado']}")
        elif opcion == "7":
            break
        else:
            print("Opción inválida.")
