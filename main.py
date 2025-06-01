from gestionJugadores import registrarJugador, consultarJugador, modificarJugador, eliminarJugador
from historial import mostrar_historial
from cola import agregarACola, atenderSiguiente
from juegos.tragamonedas import tragamonedas
from juegos.blackjack import blackjack

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar jugador")
        print("2. Consultar jugador")
        print("3. Modificar jugador")
        print("4. Eliminar jugador")
        print("5. Ver historial")
        print("6. Agregar jugador a cola")
        print("7. Jugar Tragamonedas")
        print("8. Jugar Blackjack")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarJugador()
        elif opcion == "2":
            consultarJugador()
        elif opcion == "3":
            modificarJugador()
        elif opcion == "4":
            eliminarJugador()
        elif opcion == "5":
            idJugador = input("Ingrese ID del jugador: ")
            mostrar_historial(idJugador)
        elif opcion == "6":
            juego = input("Ingrese el nombre del juego (tragamonedas / blackjack): ").lower()
            idJugador = input("Ingrese el ID del jugador: ")
            agregarACola(juego, idJugador)
        elif opcion == "7":
            jugador = atenderSiguiente("tragamonedas")
            if jugador:
                tragamonedas(jugador)
        elif opcion == "8":
            jugador = atenderSiguiente("blackjack")
            if jugador:
                blackjack(jugador)
        elif opcion == "9":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
