import streamlit as st
import random

# Definición de estados, acciones y recompensas
states = [(0, 0), (0, 1), (1, 0), (1, 1)]
actions = [0, 1]  # Salida 0 o 1
rewards = {(0, 0, 0): 1, (0, 1, 0): 0, (1, 0, 0): 0, (1, 1, 1): 1}  # Recompensas

# Parámetros de SARSA (con controles)
alpha = st.slider("Tasa de Aprendizaje (alpha)", min_value=0.0, max_value=1.0, step=0.01, value=0.1)
gamma = st.slider("Factor de Descuento (gamma)", min_value=0.0, max_value=1.0, step=0.01, value=0.9)
epsilon = st.slider("Probabilidad de Exploración (epsilon)", min_value=0.0, max_value=1.0, step=0.01, value=0.1)

# Inicialización de la tabla Q
Q = {}
for state in states:
    for action in actions:
        Q[(state, action)] = 0.0

# Función epsilon-greedy para selección de acciones
def epsilon_greedy(state):
    if random.random() < epsilon:
        return random.choice(actions)
    else:
        return max(actions, key=lambda a: Q[(state, a)])

# Función para entrenar al agente
def entrenar_agente(alpha, gamma, epsilon, num_episodes):
    rewards_history = []

    for _ in range(num_episodes):
        state = random.choice(states)  # Estado inicial aleatorio
        action = epsilon_greedy(state)
        episode_reward = 0

        while True:
            next_state = random.choice(states)  # Estado siguiente aleatorio
            next_action = epsilon_greedy(next_state)
            reward = rewards.get((state[0], state[1], action), 0)

            # Actualización de Q usando la ecuación SARSA
            Q[(state, action)] = Q[(state, action)] + alpha * (reward + gamma * Q[(next_state, next_action)] - Q[(state, action)])

            episode_reward += reward

            if state == (1, 1):
                break  # Fin del episodio

            state = next_state
            action = next_action

        rewards_history.append(episode_reward)

    return rewards_history

# Evaluación de la política aprendida
def evaluar_agente(Q):
    correct = 0
    total = 0

    for state in states:
        action = max(actions, key=lambda a: Q[(state, a)])
        if action == state[0] and state[0] == state[1]:
            correct += 1
        total += 1

    precision = correct / total * 100
    return precision

# Crear la aplicación Streamlit
st.title("Aprendizaje de la Compuerta Lógica AND con SARSA")

# Agregar botón para ejecutar la simulación
if st.button("Ejecutar Simulación"):
    # Obtener el número de episodios de entrenamiento ingresado
    num_episodes = st.number_input("Número de Episodios de Entrenamiento", min_value=1, value=1000)
    
    # Entrenar al agente y obtener las recompensas históricas
    rewards_history = entrenar_agente(alpha, gamma, epsilon, num_episodes)
    
    # Evaluar la política aprendida
    precision = evaluar_agente(Q)

    # Mostrar resultados finales
    st.subheader("Resultados Finales")
    st.write(f"Se necesitaron {num_episodes} episodios para alcanzar una eficiencia del {precision:.2f}%.")

    # Gráfico de Precisión
    st.subheader("Precisión en la Compuerta AND")
    st.write(f"Precisión: {precision:.2f}%")

    # Gráfico de Recompensas
    st.subheader("Recompensas a lo largo del Entrenamiento")
    st.line_chart(rewards_history)

    # Mostrar la política aprendida
    st.subheader("Política Aprendida")
    st.write("La política aprendida se muestra a continuación:")
    st.write(Q)
