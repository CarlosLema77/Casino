from gestionJugadores import cargarJugadores

def reporteSaldoMayor():
    """
    Finds and displays the player with the highest balance.
    """
    jugadores = cargarJugadores()
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    # Initialize with the first player
    mayorSaldo = jugadores[0]
    # Iterate to find the player with the highest balance
    for i in range(1, len(jugadores)):
        if jugadores[i]['saldo'] > mayorSaldo['saldo']:
            mayorSaldo = jugadores[i]

    print("\nJugador con más saldo:")
    print(f"Nombre: {mayorSaldo['nombre']}")
    print(f"ID: {mayorSaldo['id']}")
    print(f"Saldo: ${mayorSaldo['saldo']}")


def reporteMasVictorias():
    """
    Finds and displays the player with the most games won.
    """
    jugadores = cargarJugadores()
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    # Start by assuming the first player has the most victories
    masVictorias = jugadores[0]
    for i in range(1, len(jugadores)):
        if jugadores[i]['juegosGanados'] > masVictorias['juegosGanados']:
            masVictorias = jugadores[i]

    print("\nJugador con más juegos ganados:")
    print(f"Nombre: {masVictorias['nombre']}")
    print(f"ID: {masVictorias['id']}")
    print(f"Juegos ganados: {masVictorias['juegosGanados']}")


def reporteMasDerrotas():
    """
    Finds and displays the player with the most games lost.
    """
    jugadores = cargarJugadores()
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    # Start with the first player as the one with most losses
    masDerrotas = jugadores[0]
    for i in range(1, len(jugadores)):
        if jugadores[i]['juegosPerdidos'] > masDerrotas['juegosPerdidos']:
            masDerrotas = jugadores[i]

    print("\nJugador con más juegos perdidos:")
    print(f"Nombre: {masDerrotas['nombre']}")
    print(f"ID: {masDerrotas['id']}")
    print(f"Juegos perdidos: {masDerrotas['juegosPerdidos']}")


def reporteMayorApuestas():
    """
    Finds and displays the player who has bet the most in total.
    """
    jugadores = cargarJugadores()
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    # Initialize with the first player as the one who has bet the most
    masApostado = jugadores[0]
    for i in range(1, len(jugadores)):
        if jugadores[i]['totalApostado'] > masApostado['totalApostado']:
            masApostado = jugadores[i]

    print("\nJugador que más ha apostado:")
    print(f"Nombre: {masApostado['nombre']}")
    print(f"ID: {masApostado['id']}")
    print(f"Total apostado: ${masApostado['totalApostado']}")


def reporteTop3Saldo():
    """
    Sorts players by balance and displays the top 3.
    Also exports the results to a text file.
    """
    jugadores = cargarJugadores()
    if not jugadores or len(jugadores) < 3:
        print("No hay suficientes jugadores registrados.")
        return

    # Bubble sort to arrange players in descending order by balance
    for i in range(len(jugadores)):
        for j in range(len(jugadores) - i - 1):
            if jugadores[j]['saldo'] < jugadores[j + 1]['saldo']:
                jugadores[j], jugadores[j + 1] = jugadores[j + 1], jugadores[j]

    # Take the first three players as the top 3
    top3 = [jugadores[0], jugadores[1], jugadores[2]]

    print("\nTop 3 jugadores con más saldo:")
    for i in range(3):
        print(f"\nTop {i + 1}:")
        print(f"Nombre: {top3[i]['nombre']}")
        print(f"ID: {top3[i]['id']}")
        print(f"Saldo: ${top3[i]['saldo']}")

    # Export the report to a text file
    exportarReporteTop3Saldo(top3)


def exportarReporteTop3Saldo(top3):
    """
    Exports the top 3 highest-balance players to a text file.
    """
    try:
        with open("top3_saldo.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Top 3 jugadores con más saldo:\n")
            for i, jugador in enumerate(top3):
                archivo.write(f"\nTop {i + 1}:\n")
                archivo.write(f"Nombre: {jugador['nombre']}\n")
                archivo.write(f"ID: {jugador['id']}\n")
                archivo.write(f"Saldo: ${jugador['saldo']}\n")
        print("\nReporte exportado a 'top3_saldo.txt'")
    except Exception as e:
        print("Error al exportar el archivo:", e)
