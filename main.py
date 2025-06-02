from gestionJugadores import registrarJugador, consultarJugador, modificarJugador, eliminarJugador
from historial import mostrarHistorial
from cola import agregarACola, atenderSiguiente
from juegos.Tragamonedas01 import tragamonedas
from juegos.blackjack import blackjack
from reportes import (
    reporteSaldoMayor,
    reporteMasVictorias,
    reporteMayorApuestas,
    reporteTop3Saldo,
    reporteMasDerrotas
)
from backtracking import buscarMejorRuta
from menuAlgoritmos import menuAlgoritmos  # if located in another file, or copy the function here directly

# Displays the main menu and handles user interactions
def menu():
    """
    Displays the main menu and handles user interactions.
    Allows players to register, update, or delete their data,
    play casino games, check history, and generate reports.
    """
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar jugador") # Register player
        print("2. Consultar jugador") # Consult player info
        print("3. Modificar jugador") # Modify player data
        print("4. Eliminar jugador") # Delete player
        print("5. Ver historial") # View history
        print("6. Agregar jugador a cola") # Add player to game queue
        print("7. Jugar Tragamonedas") # Play Slot Machine
        print("8. Jugar Blackjack") # Play Blackjack
        print("9. Salir") # Exit the program
        print("10. Ver jugador con más saldo") # View player with highest balance
        print("11. Ver jugador con más juegos ganados") # View player with most wins
        print("12. Ver jugador que más ha apostado") # View player who has bet the most
        print("13. Ver top 3 jugadores con más saldo y exportar reporte") # View top 3 players with highest balance and export report
        print("14. Simular mejor ruta de apuestas (Backtracking)") # Simulate best betting route using backtracking
        print("15. Ver jugador con más juegos perdidos") # View player with most losses
        print("16. Búsquedas y ordenamientos") # Search and sorting algorithms menu

        opcion = input("Seleccione una opción (1–16): ").strip() # Get user input for menu option
        # Handle user input and call corresponding functions
        if opcion == "1": 
            registrarJugador() # Register a new player
        elif opcion == "2":
            consultarJugador() # Consult player information
        elif opcion == "3":
            modificarJugador() # Modify player data
        elif opcion == "4":
            eliminarJugador() # Delete a player
        elif opcion == "5":
            idJugador = input("Ingrese ID del jugador: ") # Get player ID to view history
            mostrarHistorial(idJugador) # Show player's game history
        elif opcion == "6":
            juego = input("Ingrese el nombre del juego (tragamonedas / blackjack): ").lower() # Get game name to add player to queue
            idJugador = input("Ingrese el ID del jugador: ") # Get player ID to add to queue
            agregarACola(juego, idJugador) # Add player to the specified game queue
        elif opcion == "7":
            jugador = atenderSiguiente("tragamonedas") # Get the next player in the slot machine queue
            if jugador:
                tragamonedas(jugador) # Play the slot machine game for the next player
        elif opcion == "8":
            jugador = atenderSiguiente("blackjack") # Get the next player in the Blackjack queue
            if jugador:
                blackjack(jugador) # Play the Blackjack game for the next player
        elif opcion == "9":
            print("Gracias por usar el sistema.") # Exit the program
            break
        elif opcion == "10":
            reporteSaldoMayor() # Generate report for player with highest balance
        elif opcion == "11":
            reporteMasVictorias() # Generate report for player with most wins
        elif opcion == "12":
            reporteMayorApuestas() # Generate report for player who has bet the most
        elif opcion == "13":
            reporteTop3Saldo() # Generate report for top 3 players with highest balance
        elif opcion == "14":
            try:
                saldo = float(input("Ingrese el saldo inicial del jugador: ")) # Get initial balance for betting simulation
                lista = input("Ingrese las apuestas posibles separadas por comas (ej: 10,20,30): ") # Get possible bets from user
                apuestas = [float(x.strip()) for x in lista.split(",")] # Convert input string to list of floats
                buscarMejorRuta(saldo, apuestas) # Simulate best betting route using backtracking
            except ValueError:
                print("Entrada no válida. Asegúrese de ingresar números correctamente.") # Handle invalid input for betting simulation
        elif opcion == "15":
            reporteMasDerrotas() # Generate report for player with most losses
        elif opcion == "16":
            menuAlgoritmos() # Display the algorithms menu for search and sorting
        else:
            print("Opción no válida. Intente nuevamente.") # Handle invalid menu option

# Entry point of the program
if __name__ == "__main__":
    menu()
