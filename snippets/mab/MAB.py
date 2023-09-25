import numpy as np

# Número de brazos (acciones)
num_brazos = 3

# Valores verdaderos de las recompensas medias de los brazos (desconocidos para el agente)
recompensas_verdaderas = [0.3, 0.5, 0.7]

# Función para simular la selección de un brazo y obtener una recompensa estocástica
def seleccionar_brazo(brazo):
    recompensa_promedio = recompensas_verdaderas[brazo]
    recompensa = np.random.normal(recompensa_promedio, 0.1)  # Simulamos una recompensa con ruido
    return recompensa

# Implementación de la estrategia Epsilon-Greedy
def epsilon_greedy(epsilon, valores_q):
    if np.random.rand() < epsilon:
        # Exploración: elige un brazo aleatorio
        return np.random.choice(num_brazos)
    else:
        # Explotación: elige el brazo con el valor Q más alto
        return np.argmax(valores_q)

# Parámetros
epsilon = 0.1  # Tasa de exploración (ajusta esto para cambiar la cantidad de exploración)
num_pasos = 1000  # Número de pasos o intentos

# Inicializar valores Q para cada brazo
valores_q = np.zeros(num_brazos)

# Contadores para seguimiento
brazos_seleccionados = np.zeros(num_brazos)
recompensas_acumuladas = 0

# Ciclo principal de interacción
for paso in range(num_pasos):
    # Seleccionar un brazo utilizando la estrategia Epsilon-Greedy
    brazo_elegido = epsilon_greedy(epsilon, valores_q)
    
    # Registrar el brazo seleccionado
    brazos_seleccionados[brazo_elegido] += 1
    
    # Simular la obtención de una recompensa al seleccionar el brazo
    recompensa = seleccionar_brazo(brazo_elegido)
    
    # Actualizar el valor Q del brazo seleccionado (Regla de actualización Q-Learning)
    valores_q[brazo_elegido] += (1 / brazos_seleccionados[brazo_elegido]) * (recompensa - valores_q[brazo_elegido])
    
    # Acumular recompensas
    recompensas_acumuladas += recompensa

# Resultados
print("Valores Q finales:")
print(valores_q)
print("Brazo óptimo (mejor acción):")
print(np.argmax(valores_q))
print("Recompensas acumuladas:")
print(recompensas_acumuladas)
