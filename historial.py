import json
from datetime import datetime

HISTORIAL_PATH = "data/historial.json"

def registrar_en_historial(id_jugador, juego, resultado, apuesta, ganancia):
    nuevo_registro = {
        "id": id_jugador,
        "juego": juego,
        "resultado": resultado,
        "apuesta": apuesta,
        "ganancia": ganancia,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(HISTORIAL_PATH, "r", encoding="utf-8") as f:
            historial = json.load(f)
    except FileNotFoundError:
        historial = []

    historial.append(nuevo_registro)

    with open(HISTORIAL_PATH, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=4)


def mostrar_historial():
    try:
        with open(HISTORIAL_PATH, "r", encoding="utf-8") as f:
            historial = json.load(f)
        for entrada in historial:
            print(f"{entrada['fecha']} - {entrada['id']} jugó {entrada['juego']}: {entrada['resultado']}, apostó {entrada['apuesta']} y ganó {entrada['ganancia']}")
    except FileNotFoundError:
        print("No hay historial registrado.")