import random
from historial import historialJugador
from gestionJugadores import cargarJugadores, guardarJugadores

def valorMano(mano):
    total = 0
    ases = 0
    for carta in mano:
        if carta == "A":
            ases += 1
            total += 11
        elif carta in ["J", "Q", "K"]:
            total += 10
        else:
            total += int(carta)
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

def jugarBlackjack(idJugador):
    jugadores = cargarJugadores()
    for jugador in jugadores:
        if jugador["id"] == idJugador:
            apuesta = 2000
            if jugador["saldo"] < apuesta:
                print("Saldo insuficiente.")
                return

            jugador["saldo"] -= apuesta
            jugador["totalApostado"] += apuesta

            mazo = [str(x) for x in list(range(2, 11))] + ["J", "Q", "K", "A"]
            mano_jugador = [random.choice(mazo) for _ in range(2)]
            mano_crupier = [random.choice(mazo) for _ in range(2)]

            print("Tu mano:", mano_jugador)
            print("Mano del crupier:", [mano_crupier[0], "?"])

            while valorMano(mano_jugador) < 17:
                mano_jugador.append(random.choice(mazo))
                print("Nueva carta:", mano_jugador[-1])

            while valorMano(mano_crupier) < 17:
                mano_crupier.append(random.choice(mazo))

            puntos_jugador = valorMano(mano_jugador)
            puntos_crupier = valorMano(mano_crupier)

            print(f"Tu mano: {mano_jugador} ({puntos_jugador})")
            print(f"Crupier: {mano_crupier} ({puntos_crupier})")

            if puntos_jugador > 21 or (puntos_crupier <= 21 and puntos_crupier >= puntos_jugador):
                jugador["juegosPerdidos"] += 1
                historialJugador(idJugador, f"Perdió en Blackjack (-{apuesta})")
                print("Perdiste.")
            else:
                premio = 4000
                jugador["saldo"] += premio
                jugador["juegosGanados"] += 1
                historialJugador(idJugador, f"Ganó en Blackjack (+{premio})")
                print("Ganaste.")

            guardarJugadores(jugadores)
            return
    print("Jugador no encontrado.")
