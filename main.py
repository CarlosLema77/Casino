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
from menuAlgoritmos import menuAlgoritmos  # si está en otro archivo, o copiar función directamente aquí

def menu():
    """
    Displays the main menu and handles user interactions.
    Allows players to register, update, or delete their data,
    play casino games, check history, and generate reports.
    """
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
        print("10. Ver jugador con más saldo")
        print("11. Ver jugador con más juegos ganados")
        print("12. Ver jugador que más ha apostado")
        print("13. Ver top 3 jugadores con más saldo y exportar reporte")
        print("14. Simular mejor ruta de apuestas (Backtracking)")
        print("15. Ver jugador con más juegos perdidos")
        print("16. Búsquedas y ordenamientos")

        opcion = input("Seleccione una opción (1–16): ").strip()

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
            mostrarHistorial(idJugador)
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
        elif opcion == "10":
            reporteSaldoMayor()
        elif opcion == "11":
            reporteMasVictorias()
        elif opcion == "12":
            reporteMayorApuestas()
        elif opcion == "13":
            reporteTop3Saldo()
        elif opcion == "14":
            try:
                saldo = float(input("Ingrese el saldo inicial del jugador: "))
                lista = input("Ingrese las apuestas posibles separadas por comas (ej: 10,20,30): ")
                apuestas = [float(x.strip()) for x in lista.split(",")]
                buscarMejorRuta(saldo, apuestas)
            except ValueError:
                print("Entrada no válida. Asegúrese de ingresar números correctamente.")
        elif opcion == "15":
            reporteMasDerrotas()
        elif opcion == "16":
            menuAlgoritmos()
        else:
            print("Opción no válida. Intente nuevamente.")

# Entry point of the program
if __name__ == "__main__":
    menu()
