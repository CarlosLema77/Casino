import random
from gestionJugadores import cargarJugadores, guardarJugadores
from historial import historialJugador

# Simulates a slot machine game for a given player ID
def tragamonedas(id_jugador):
    """
    Simulates a slot machine game for the given player ID.
    Uses randomness to determine the outcome.
    Updates balance, history and statistics.
    """
    jugadores = cargarJugadores()
    jugador = next((j for j in jugadores if j['id'] == id_jugador), None)

    if not jugador:
         # Player not found
        print("Jugador no encontrado.")
        return

    print("🎰 ¡Bienvenido a la Tragamonedas!")
    print(f"Saldo actual: ${jugador['saldo']}")

    # Ask the player to enter their bet
    try:
        apuesta = float(input("Ingresa tu apuesta: "))
    except ValueError:
         # Invalid input
        print("Apuesta inválida.")
        return

    if apuesta <= 0:
        # Bet must be positive
        print("La apuesta debe ser mayor que cero.")
        return
    if apuesta > jugador['saldo']:
        # Insufficient balance
        print("No tienes suficiente saldo.")
        return

    # Register total amount bet
    jugador['totalApostado'] += apuesta

    # Generate random outcome (brute force)
    resultado = [random.randint(1, 3) for _ in range(3)]
    print("Resultado:", resultado)

    if resultado[0] == resultado[1] == resultado[2]:
        # Player wins (all three symbols match)
        ganancia = apuesta * 3
        jugador['saldo'] += ganancia
        jugador['juegosGanados'] += 1
        print(f"¡Ganaste ${ganancia}!")
        actividad = f"Jugó Tragamonedas - GANÓ ${ganancia} con apuesta de ${apuesta}"
    else:
        # Player loses
        jugador['saldo'] -= apuesta
        jugador['juegosPerdidos'] += 1
        print("Perdiste esta vez.")
        actividad = f"Jugó Tragamonedas - PERDIÓ ${apuesta}"

    # Update player history and save changes
    historialJugador(jugador['id'], actividad, jugadores)
    guardarJugadores(jugadores)


