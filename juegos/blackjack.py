import random
from gestionJugadores import cargarJugadores, guardarJugadores
from historial import historialJugador

def repartir_carta():
    """
    Returns a random card between 1 and 11 (as in simplified Blackjack).
    """
    return random.randint(1, 11)

def jugar_turno(puntaje_actual):
    """
    Recursive function that simulates the player's turn.
    Uses implicit stack calls to accumulate cards until the player stops or busts.
    """
    print(f"Tu puntaje actual es: {puntaje_actual}")

    if puntaje_actual > 21:
        print("Te pasaste de 21. Pierdes.")
        return puntaje_actual

    decision = input("¿Deseas otra carta? (s/n): ").lower()
    if decision == 's':
        nueva = repartir_carta()
        print(f"Recibiste un {nueva}")
        return jugar_turno(puntaje_actual + nueva)
    else:
        print(f"Te plantaste con {puntaje_actual}")
        return puntaje_actual

def blackjack(id_jugador):
    """
    Recursively simulates a Blackjack game for the given player ID.
    Updates balance, history and statistics.
    """
    jugadores = cargarJugadores()
    jugador = next((j for j in jugadores if j['id'] == id_jugador), None)

    if not jugador:
        print("Jugador no encontrado.")
        return

    print("🃏 ¡Bienvenido a Blackjack (versión recursiva)!")
    print(f"Saldo actual: ${jugador['saldo']}")

    try:
        apuesta = float(input("Ingresa tu apuesta: "))
    except ValueError:
        print("Apuesta inválida.")
        return

    if apuesta <= 0:
        print("La apuesta debe ser mayor que cero.")
        return
    if apuesta > jugador['saldo']:
        print("No tienes suficiente saldo.")
        return

    # Registrar cantidad apostada
    jugador['totalApostado'] += apuesta

    # Inicio del juego recursivo
    puntaje_jugador = jugar_turno(repartir_carta() + repartir_carta())
    puntaje_casa = random.randint(17, 21)
    print(f"Puntaje de la casa: {puntaje_casa}")

    if puntaje_jugador > 21:
        jugador['saldo'] -= apuesta
        jugador['juegosPerdidos'] += 1
        print("Perdiste la partida.")
        actividad = f"Jugó Blackjack (recursivo) - PERDIÓ ${apuesta}"
    elif puntaje_casa > 21 or puntaje_jugador > puntaje_casa:
        ganancia = apuesta * 2
        jugador['saldo'] += ganancia
        jugador['juegosGanados'] += 1
        print(f"¡Ganaste ${ganancia}!")
        actividad = f"Jugó Blackjack (recursivo) - GANÓ ${ganancia} con apuesta de ${apuesta}"
    elif puntaje_jugador == puntaje_casa:
        print("Empate. Se devuelve la apuesta.")
        actividad = f"Jugó Blackjack (recursivo) - EMPATÓ. Apuesta devuelta ${apuesta}"
    else:
        jugador['saldo'] -= apuesta
        jugador['juegosPerdidos'] += 1
        print("Perdiste contra la casa.")
        actividad = f"Jugó Blackjack (recursivo) - PERDIÓ ${apuesta}"

    historialJugador(jugador['id'], actividad, jugadores)
    guardarJugadores(jugadores)
