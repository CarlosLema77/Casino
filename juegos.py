import random
from historial import historialJugador
from gestionJugadores import cargarJugadores, guardarJugadores

def tragamonedas(idJugador):
    jugadores = cargarJugadores()
    jugador = next((j for j in jugadores if j['id'] == idJugador), None)
    if not jugador:
        print("Jugador no encontrado.")
        return

    apuesta = float(input("Ingrese su apuesta para tragamonedas: "))
    if apuesta > jugador['saldo'] or apuesta <= 0:
        print("Apuesta inválida.")
        return

    jugador['totalApostado'] += apuesta
    jugador['saldo'] -= apuesta

    opciones = ['🍒', '🔔', '7️⃣']
    resultado = [random.choice(opciones) for _ in range(3)]
    print("Resultado:", ' | '.join(resultado))

    if resultado.count(resultado[0]) == 3:
        ganancia = apuesta * 10
        jugador['saldo'] += ganancia
        jugador['juegosGanados'] += 1
        historialJugador(idJugador, f"Ganó {ganancia} en tragamonedas.")
    else:
        jugador['juegosPerdidos'] += 1
        historialJugador(idJugador, f"Perdió {apuesta} en tragamonedas.")

    guardarJugadores(jugadores)

def blackjack(idJugador):
    jugadores = cargarJugadores()
    jugador = next((j for j in jugadores if j['id'] == idJugador), None)
    if not jugador:
        print("Jugador no encontrado.")
        return

    apuesta = float(input("Ingrese su apuesta para blackjack: "))
    if apuesta > jugador['saldo'] or apuesta <= 0:
        print("Apuesta inválida.")
        return

    def sacarCarta():
        return random.randint(1, 11)  # As simple 1-11

    def turnoJugador(pila, total=0):
        if total >= 21:
            return total
        eleccion = input(f"Total actual: {total}. ¿Pedir carta? (s/n): ").lower()
        if eleccion == 's':
            carta = sacarCarta()
            pila.append(carta)
            return turnoJugador(pila, total + carta)
        else:
            return total

    jugador['saldo'] -= apuesta
    jugador['totalApostado'] += apuesta

    pilaJugador = []
    totalJugador = turnoJugador(pilaJugador)

    totalCrupier = random.randint(16, 21)

    print(f"Tu total: {totalJugador} | Crupier: {totalCrupier}")

    if totalJugador > 21 or (totalCrupier <= 21 and totalCrupier >= totalJugador):
        jugador['juegosPerdidos'] += 1
        historialJugador(idJugador, f"Perdió {apuesta} en blackjack.")
    else:
        ganancia = apuesta * 2
        jugador['saldo'] += ganancia
        jugador['juegosGanados'] += 1
        historialJugador(idJugador, f"Ganó {ganancia} en blackjack.")

    guardarJugadores(jugadores)

