import json
import os

def cargarJugadores():
    ruta = "data/jugadores.json"
    if not os.path.exists(ruta):
        return [] #if the file does not exist, return an empty list
    with open(ruta, "r") as archivo:
        return json.load(archivo) #load the players from the json file

def guardarJugadores(listaJugadores):
    ruta = "data/jugadores.json"
    with open(ruta, "w") as archivo:
        json.dump(listaJugadores, archivo, indent=4) #save the players to the json file

def registrarJugador():
    """Registers a new player by asking for their name, ID, and initial balance.
    Validates unique ID and non-negative balance. Saves to jugadores.json."""
    jugadores = cargarJugadores() #load the players from the json file

    nombre = input("Ingrese el nombre del jugador: ") #ask for the player's name
    id_unico = input("Ingrese el ID único del jugador: ") #ask for the player's unique ID
    saldo_inicial = float(input("Ingrese el saldo inicial del jugador: ")) #ask for the player's initial balance

    # Validation
    for jugador in jugadores:
        if jugador['id'] == id_unico:
            print("El ID ya está en uso. Intente nuevamente.")
            return
    if saldo_inicial < 0:
        print("El saldo inicial no puede ser negativo.")
        return
    
    nuevo_jugador = {
        "nombre": nombre,
        "id": id_unico,
        "saldo": saldo_inicial,
        "historial": [],
        "juegosGanados": 0,
        "juegosPerdidos": 0,
        "totalApostado": 0
    } #create a new player dictionary with the player's information
    jugadores.append(nuevo_jugador)
    guardarJugadores(jugadores) #save the players to the json file
    print(f"Jugador {nombre} registrado con éxito.")

def consultarJugador():

    """Finds a player by their unique ID and displays their information.
    Loads players from jugadores.json."""

    jugadores=cargarJugadores() #load the players from the json file"""

    id_unico = input("Ingrese el ID único del jugador a consultar: ")#ask for the player's unique ID

    for jugador in jugadores:
        if jugador['id'] == id_unico:
            print(f"Jugador encontrado: {jugador['nombre']}, \n ID: {jugador['id']}, \n Saldo: {jugador['saldo']}")
            return
    print("Jugador no encontrado.")

def modificarJugador():

    """Modifies a player's name and/or balance by their unique ID."""

    jugadores=cargarJugadores() #load the players from the json file"""

    """Finds a player by their unique ID and displays their information."""

    id_unico = input("Ingrese el ID único del jugador a modificar: ") #ask for the player's unique ID

    """Validates unique ID and non-negative balance."""

    for jugador in jugadores:
        if jugador['id'] == id_unico:
            print(f"Jugador encontrado: {jugador['nombre']}, \n ID: {jugador['id']}, \n Saldo: {jugador['saldo']}")
            
            """# Ask for the new name and/or balance"""

            cambio = int(input("Desea modificar el nombre y/o el saldo del jugador? (1: Nombre, 2: Saldo, 3: Ambos): "))
            
            if cambio == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre del jugador: ")
                jugador["nombre"] = nuevo_nombre
            elif cambio == 2:
                nuevo_saldo = float(input("Ingrese el nuevo saldo del jugador: "))
                if nuevo_saldo < 0:
                    print("El saldo no puede ser negativo.")
                    return
                jugador["saldo"] = nuevo_saldo
            elif cambio == 3:
                nuevo_nombre = input("Ingrese el nuevo nombre del jugador: ")
                nuevo_saldo = float(input("Ingrese el nuevo saldo del jugador: "))
                if nuevo_saldo < 0:
                    print("El saldo no puede ser negativo.")
                    return
                jugador["nombre"] = nuevo_nombre
                jugador["saldo"] = nuevo_saldo
            else:
                print("Opción no válida.")
                return
            guardarJugadores(jugadores) #save the players to the json file
            print(f"Jugador {jugador['nombre']} modificado con éxito.")
            return
    
    print("Jugador no encontrado.")

def eliminarJugador():

    """Deletes a player by their unique ID."""

    jugadores = cargarJugadores() #load the players from the json file

    id_unico = input("Ingrese el ID único del jugador a eliminar: ") #ask for the player's unique ID

    for jugador in jugadores:
        if jugador['id'] == id_unico:
            print(f"Jugador encontrado: {jugador['nombre']}, \n ID: {jugador['id']}, \n Saldo: {jugador['saldo']}")
            confirmacion = input("¿Está seguro de que desea eliminar este jugador? (s/n): ")#ask for confirmation
            
            if confirmacion.lower() == 's': #confirm if the user wants to delete the player
                print(f"Jugador {jugador['nombre']} eliminado con éxito.")
                jugadores.remove(jugador) #remove the player from the list 
                guardarJugadores(jugadores) #save the players to the json file
                break
            
            else: #if the user does not want to delete the player
                print("Eliminación cancelada.")
                return
    
    print("Jugador no encontrado.")
    
            
   
    