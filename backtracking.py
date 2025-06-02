def buscarMejorRuta(saldo_inicial, apuestas_posibles):
    """
    Uses backtracking to find the best sequence of bets that maximizes profit
    without the player's balance ever reaching zero.
    
    Parameters:
        saldo_inicial (float): The player's starting balance.
        apuestas_posibles (list of float): The set of allowed bet values.
    """
    mejor_ruta = []        # Best sequence of bets found so far
    max_ganancia = 0       # Highest profit achieved so far

    def backtrack(saldo_actual, camino_actual, ganancia_actual):
        nonlocal mejor_ruta, max_ganancia

        # Update best route if this path has a higher total gain
        if ganancia_actual > max_ganancia:
            max_ganancia = ganancia_actual
            mejor_ruta = camino_actual.copy()

        # Explore each possible bet from the current state
        for apuesta in apuestas_posibles:
            if saldo_actual >= apuesta:
                # Simulate winning the bet: gain 50% of the bet amount
                ganancia = apuesta * 0.5
                nuevo_saldo = saldo_actual - apuesta + ganancia

                # Choose this bet and continue exploring
                camino_actual.append(apuesta)
                backtrack(nuevo_saldo, camino_actual, ganancia_actual + ganancia)

                # Undo the last choice (backtrack)
                camino_actual.pop()

    # Start recursive exploration from the initial balance and empty path
    backtrack(saldo_inicial, [], 0)

    # Output the best result found
    print("\nMejor ruta de apuestas encontrada:")
    print("Secuencia:", mejor_ruta)
    print(f"Ganancia total: ${round(max_ganancia, 2)}")
