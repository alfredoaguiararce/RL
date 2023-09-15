import numpy as np
import matplotlib.pyplot as plt

# Configuración del problema de los 10-armed bandit
num_bandits = 10  # Número de brazos
num_steps = 1000  # Número de pasos en el experimento
num_experiments = 1000  # Número de experimentos

# Crear los valores de acción verdaderos (valores verdaderos de cada brazo)
true_action_values = np.random.normal(0, 1, num_bandits)

# Función para seleccionar una acción basada en la estrategia epsilon-greedy
def epsilon_greedy(Q, epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(len(Q))  # Exploración aleatoria
    else:
        return np.argmax(Q)  # Explotación del mejor valor estimado

# Función para simular un experimento
def run_experiment(Q_true, epsilon):
    rewards = []
    Q_estimates = np.zeros(num_bandits)

    for step in range(num_steps):
        action = epsilon_greedy(Q_estimates, epsilon)
        reward = np.random.normal(Q_true[action], 1)
        rewards.append(reward)

        # Actualizar estimaciones de valor de acción (Regla de actualización incremental)
        Q_estimates[action] += (reward - Q_estimates[action]) / (action + 1)

        # Imprimir los datos de esta iteración
        print(f'Experimento: {step + 1}, Acción seleccionada: {action}, Recompensa: {reward}')

    return rewards

# Ejecutar múltiples experimentos
avg_rewards_epsilon_greedy = np.zeros(num_steps)
avg_rewards_greedy = np.zeros(num_steps)

for experiment in range(num_experiments):
    rewards_epsilon_greedy = run_experiment(true_action_values, epsilon=0.1)
    rewards_greedy = run_experiment(true_action_values, epsilon=0.0)
    
    avg_rewards_epsilon_greedy += np.array(rewards_epsilon_greedy) / num_experiments
    avg_rewards_greedy += np.array(rewards_greedy) / num_experiments

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(avg_rewards_epsilon_greedy, label="epsilon-greedy (epsilon=0.1)")
plt.plot(avg_rewards_greedy, label="greedy (epsilon=0.0)")
plt.xlabel("Pasos")
plt.ylabel("Recompensa Promedio")
plt.legend()
plt.title("Comparación entre epsilon-greedy y greedy")
plt.show()
