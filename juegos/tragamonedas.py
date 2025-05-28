import random
from historial import historialJugador
from gestionJugadores import cargarJugadores, guardarJugadores

def jugarTragamonedas(idJugador):
    jugadores = cargarJugadores()
    for jugador in jugadores:
        if jugador["id"] == idJugador:
            apuesta = 1000
            if jugador["saldo"] < apuesta:
                print("Saldo insuficiente para jugar.")
                return

            jugador["saldo"] -= apuesta
            jugador["totalApostado"] += apuesta

            resultado = [random.choice(["🍒", "🍋", "🔔", "⭐", "🍀"]) for _ in range(3)]
            print("Resultado:", " ".join(resultado))

            if resultado.count(resultado[0]) == 3:
                premio = 5000
                jugador["saldo"] += premio
                jugador["juegosGanados"] += 1
                historialJugador(idJugador, f"Ganó en tragamonedas: {' '.join(resultado)} (+{premio})")
                print("¡Felicidades! Ganaste.")
            else:
                jugador["juegosPerdidos"] += 1
                historialJugador(idJugador, f"Perdió en tragamonedas: {' '.join(resultado)} (-{apuesta})")
                print("Sigue intentando.")

            guardarJugadores(jugadores)
            return
    print("Jugador no encontrado.")
