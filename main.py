from gestionJugadores import registrarJugador, consultarJugador, modificarJugador, eliminarJugador
from historial import mostrarHistorial
from cola import agregarACola, atenderSiguiente
from juegos.tragamonedas import jugarTragamonedas
from juegos.blackjack import jugarBlackjack

def menu():
    """
    Displays the main menu and handles user interactions.
    Allows players to register, view/edit their info, access game queues,
    and play Tragamonedas or Blackjack when it's their turn.
    """
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Register player")
        print("2. View player information")
        print("3. Modify player")
        print("4. Delete player")
        print("5. View player history")
        print("6. Add player to game queue")
        print("7. Play Tragamonedas")
        print("8. Play Blackjack")
        print("9. Exit")

        opcion = input("Select an option (1–9): ").strip()

        if opcion == "1":
            # Register a new player
            registrarJugador()

        elif opcion == "2":
            # View a player's information
            consultarJugador()

        elif opcion == "3":
            # Modify a player's name or balance
            modificarJugador()

        elif opcion == "4":
            # Delete a player from the system
            eliminarJugador()

        elif opcion == "5":
            # Show the player's activity history
            idJugador = input("Enter the player's ID: ").strip()
            mostrarHistorial(idJugador)

        elif opcion == "6":
            # Add a player to the queue for a game
            juego = input("Enter game name (tragamonedas / blackjack): ").strip().lower()
            if juego not in ["tragamonedas", "blackjack"]:
                print("Invalid game name. Please try again.")
                continue
            idJugador = input("Enter the player's ID: ").strip()
            agregarACola(juego, idJugador)

        elif opcion == "7":
            # Serve next player in Tragamonedas queue and start game
            jugador = atenderSiguiente("tragamonedas")
            if jugador:
                jugarTragamonedas(jugador)

        elif opcion == "8":
            # Serve next player in Blackjack queue and start game
            jugador = atenderSiguiente("blackjack")
            if jugador:
                jugarBlackjack(jugador)

        elif opcion == "9":
            # Exit the program
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid option. Please select a number from 1 to 9.")

if __name__ == "__main__":
    menu()
