# ---------------------------------------------------------
#    JUEGO NIM – Minimax
#    MAX = Computadora
#    MIN = Humano
# ---------------------------------------------------------
# Movimientos posibles cada turno
# ----------------------------------
def legal_moves(stones):
    moves = []
    for m in [1, 2, 3]:
        if stones - m >= 0:
            moves.append(m)
    return moves
# ----------------------------------
# Estado terminal: no quedan piedras
# ----------------------------------
def terminal(stones):
    return stones == 0
# ----------------------------------
# Función de utilidad:
#   Si MAX no puede jugar → pierde → -1
#   Si MIN no puede jugar → pierde → +1
# ----------------------------------
def utility(stones, maximizing):
    if maximizing:
        return -1
    else:
        return 1

# ----------------------------------
# ALGORITMO MINIMAX
# ----------------------------------
def minimax(stones, maximizing):

    # Caso base
    if terminal(stones):
        return utility(stones, maximizing)

    # Turno de MAX (computadora)
    if maximizing:
        best_value = float('-inf')
        for move in legal_moves(stones):
            value = minimax(stones - move, False)
            best_value = max(best_value, value)
        return best_value

    # Turno de MIN (humano)
    else:
        best_value = float('inf')
        for move in legal_moves(stones):
            value = minimax(stones - move, True)
            best_value = min(best_value, value)
        return best_value

# ----------------------------------
# Mejor jugada para la computadora
# ----------------------------------
def best_move(stones):
    best_value = float('-inf')
    chosen_move = None

    for move in legal_moves(stones):
        value = minimax(stones - move, False)
        if value > best_value:
            best_value = value
            chosen_move = move

    return chosen_move

# ----------------------------------
# DEMO DE JUEGO
# ----------------------------------
if __name__ == "__main__":

    stones = 10   # número inicial de piedras
    turno_max = False   # False = empieza humano, True = computadora

    print("JUEGO NIM – Hay", stones, "piedras")
    print("Gana el jugador que deja al rival sin movimientos.\n")

    while not terminal(stones):
        print("Piedras restantes:", stones)

        # -------------------------------------
        # Turno del humano (MIN)
        # -------------------------------------
        human = int(input("Tu jugada (1-3): "))
        while human not in legal_moves(stones):
            human = int(input("Movimiento inválido. Elige 1, 2 o 3: "))

        stones -= human
        turno_max = True   # luego de humano, turno de MAX

        if terminal(stones):
            break

        # -------------------------------------
        # Turno de la computadora (MAX)
        # -------------------------------------
        print("Piedras restantes:", stones) # Pequeño añadido visual para claridad
        cpu = best_move(stones)
        print("La computadora toma", cpu, "\n")

        stones -= cpu
        turno_max = False   # luego de MAX, turno de MIN

    print("\nPiedras restantes:", stones)
    print("\nResultado:")

    # turno_max indica a quién le tocaba mover
    if turno_max:
        print("Gana el humano!")
    else:
        print("Gana la computadora!")