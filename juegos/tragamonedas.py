import random
from historial import registrar_en_historial

def tragamonedas(id_jugador, saldo):
    print("Bienvenido a la Tragamonedas!")
    apuesta = float(input("Ingresa tu apuesta: "))
    if apuesta > saldo:
        print("No tienes suficiente saldo.")
        return saldo

    resultado = [random.randint(1, 3) for _ in range(3)]
    print("Resultado:", resultado)

    if resultado[0] == resultado[1] == resultado[2]:
        ganancia = apuesta * 3
        saldo += ganancia
        print("¡Ganaste! Ganaste:", ganancia)
        registrar_en_historial(id_jugador, "Tragamonedas", "ganó", apuesta, ganancia)
    else:
        saldo -= apuesta
        print("Perdiste esta vez.")
        registrar_en_historial(id_jugador, "Tragamonedas", "perdió", apuesta, 0)

    return saldo
