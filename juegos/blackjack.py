import random
from historial import registrar_en_historial

def blackjack(id_jugador, saldo):
    print("Bienvenido a Blackjack!")
    apuesta = float(input("Ingresa tu apuesta: "))
    if apuesta > saldo:
        print("No tienes suficiente saldo.")
        return saldo

    jugador = random.randint(15, 21)
    casa = random.randint(17, 21)
    print(f"Tu puntaje: {jugador} | Puntaje de la casa: {casa}")

    if jugador > casa:
        ganancia = apuesta * 2
        saldo += ganancia
        print("¡Ganaste!")
        registrar_en_historial(id_jugador, "Blackjack", "ganó", apuesta, ganancia)
    elif jugador == casa:
        print("Empate. Se devuelve la apuesta.")
        registrar_en_historial(id_jugador, "Blackjack", "empate", apuesta, apuesta)
    else:
        saldo -= apuesta
        print("Perdiste.")
        registrar_en_historial(id_jugador, "Blackjack", "perdió", apuesta, 0)

    return saldo
