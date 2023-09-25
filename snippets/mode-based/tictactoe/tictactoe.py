import numpy as np

# Espacio de estados (configuraciones del tablero)
S = [np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),  # Estado inicial
     np.array([[1, 0, -1], [0, 0, 0], [0, 0, 0]])]  # Ejemplo de un estado
     # ... otros estados ...]
# Agregar más estados al espacio de estados
S.append(np.array([[1, -1, 0], [0, 0, 0], [0, 0, 0]]))  # Otro ejemplo de estado
S.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]]))  # Otro ejemplo de estado
# Agregar más estados aquí...


# Espacio de acciones (posiciones en el tablero)
A = [(i, j) for i in range(3) for j in range(3)]

# Modelo de transición (determinista)
def transition(s, a):
    s_prime = s.copy()
    if s[a] == 0:  # Verificar si la casilla está vacía
        s_prime[a] = 1  # "X" toma la casilla
    return s_prime

# Función de recompensa
def reward(s):
    # Definir la función de recompensa en función de los resultados del juego
    if check_win(s, 1):  # "X" gana
        return 1
    elif check_win(s, -1):  # "O" gana
        return -1
    elif is_full(s):  # Empate
        return 0
    else:
        return 0.5  # Juego en curso

# Verificar si un jugador ha ganado
def check_win(board, player):
    # Verificar filas, columnas y diagonales
    for i in range(3):
        if all(board[i, :] == player) or all(board[:, i] == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Verificar si el tablero está lleno
def is_full(board):
    return np.all(board != 0)

# Algoritmo de Q-learning
# Algoritmo de Q-learning
def q_learning(S, A, transition, reward, alpha=0.1, gamma=0.9, num_episodes=1000):
    Q = {}  # Inicializar la función Q como un diccionario vacío

    for _ in range(num_episodes):
        s = S[0]  # Estado inicial
        while not is_terminal(s):
            s_bytes = s.tobytes()  # Convertir el estado en bytes
            if s_bytes not in Q:
                Q[s_bytes] = np.zeros(len(A))  # Inicializar Q(s, a) para cada acción

            # Seleccionar una acción utilizando una política ε-greedy
            epsilon = 0.1
            if np.random.rand() < epsilon:
                a = np.random.choice(len(A))
            else:
                a = np.argmax(Q[s_bytes])

            s_prime = transition(s, A[a])  # Obtener el siguiente estado
            r = reward(s_prime)  # Obtener la recompensa
            if s_prime.tobytes() not in Q:
                Q[s_prime.tobytes()] = np.zeros(len(A))  # Inicializar Q(s', a) si aún no existe
            Q[s_bytes][a] += alpha * (r + gamma * np.max(Q[s_prime.tobytes()]) - Q[s_bytes][a])

            s = s_prime  # Avanzar al siguiente estado

    return Q


# Función para verificar si un estado es terminal
def is_terminal(s):
    return check_win(s, 1) or check_win(s, -1) or is_full(s)

# Entrenar al agente
Q_values = q_learning(S, A, transition, reward)

# Evaluar la política óptima aprendida
def evaluate_policy(Q, S):
    policy = {}
    for s in S:
        if s.tobytes() in Q:
            policy[s.tobytes()] = np.argmax(Q[s.tobytes()])
        else:
            policy[s.tobytes()] = None
    return policy

optimal_policy = evaluate_policy(Q_values, S)

# Mostrar la política óptima
for s, action in optimal_policy.items():
    if action is not None:
        print(f"Estado: {np.array(s).tolist()}\nAcción óptima: {A[action]}\n")


# Función para mostrar el tablero
def print_board(board):
    symbols = [' ', 'X', 'O']
    for row in board:
        print(" | ".join([symbols[cell] for cell in row]))
        print("-" * 9)

# Función para que el jugador humano realice un movimiento
def player_move(board):
    while True:
        try:
            row = int(input("Fila (0-2): "))
            col = int(input("Columna (0-2): "))
            if board[row][col] == 0:
                return (row, col)
            else:
                print("Esa casilla ya está ocupada. Intenta de nuevo.")
        except (ValueError, IndexError):
            print("Entrada no válida. Ingresa números del 0 al 2.")

# Función para que el modelo realice un movimiento
def model_move(board, Q):
    s_bytes = board.tobytes()
    
    # Obtener las casillas vacías en el tablero
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

    if len(empty_cells) == 0:
        # No hay casillas vacías, no se puede realizar un movimiento
        return None
    
    if s_bytes in Q:
        # El estado está en Q, elige la mejor acción entre las casillas vacías
        valid_actions = [A.index(cell) for cell in empty_cells]
        q_values = [Q[s_bytes][a] for a in valid_actions]
        action = valid_actions[np.argmax(q_values)]
    else:
        # Si el estado no está en Q o no hay suficientes datos para tomar una decisión,
        # elige una acción aleatoria entre las casillas vacías
        action = np.random.choice(len(empty_cells))
    
    return empty_cells[action]


# Función para actualizar la función Q del modelo durante el juego
def update_q_values(Q, s, a, r, s_prime, alpha=0.1, gamma=0.9):
    s_bytes = s.tobytes()
    s_prime_bytes = s_prime.tobytes()
    
    if s_bytes not in Q:
        Q[s_bytes] = np.zeros(len(A))  # Inicializar Q(s, a) si es un estado nuevo
    
    if s_prime_bytes not in Q:
        Q[s_prime_bytes] = np.zeros(len(A))  # Inicializar Q(s', a) si es un estado nuevo
    
    # Actualizar Q(s, a) usando Q-learning
    Q[s_bytes][a] += alpha * (r + gamma * np.max(Q[s_prime_bytes]) - Q[s_bytes][a])

# Función principal del juego
def play_game(Q):
    board = np.zeros((3, 3), dtype=int)
    player_turn = True

    while True:
        print_board(board)
        if player_turn:
            print("Tu turno:")
            move = player_move(board)
        else:
            print("Turno del modelo:")
            s = board.copy()
            s_bytes = s.tobytes()
            if s_bytes in Q:
                action = np.argmax(Q[s_bytes])
            else:
                action = np.random.choice(len(A))
            move = A[action]

        row, col = move
        board[row][col] = 1 if player_turn else -1

        if check_win(board, 1):
            print_board(board)
            print("¡Has ganado!")
            break
        elif check_win(board, -1):
            print_board(board)
            print("El modelo ha ganado.")
            break
        elif is_full(board):
            print_board(board)
            print("Empate.")
            break

        if not player_turn:
            # Si el modelo jugó, actualiza sus Q-values
            s_prime = board.copy()
            update_q_values(Q, s, action, reward(s_prime), s_prime)

        player_turn = not player_turn
# Jugar el juego
play_game(Q_values)





