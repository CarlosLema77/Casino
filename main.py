from gestionJugadores import registrarJugador, consultarJugador, modificarJugador, eliminarJugador
from historial import mostrarHistorial
from cola import agregarACola, atenderJugador
from juegos import tragamonedas, blackjack

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar jugador")
        print("2. Consultar jugador")
        print("3. Modificar jugador")
        print("4. Eliminar jugador")
        print("5. Ver historial")
        print("6. Agregar jugador a cola")
        print("7. Atender tragamonedas")
        print("8. Atender blackjack")
        print("0. Salir")

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
            idJugador = input("ID del jugador: ")
            mostrarHistorial(idJugador)
        elif opcion == "6":
            juego = input("Nombre del juego (tragamonedas/blackjack): ").lower()
            idJugador = input("ID del jugador: ")
            agregarACola(juego, idJugador)
        elif opcion == "7":
            idJugador = atenderJugador("tragamonedas")
            if idJugador:
                tragamonedas(idJugador)
        elif opcion == "8":
            idJugador = atenderJugador("blackjack")
            if idJugador:
                blackjack(idJugador)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
