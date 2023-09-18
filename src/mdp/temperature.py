import streamlit as st
import random
import pandas as pd
import time
import numpy as np

class ControlTemperatura:
    def __init__(self, initial_temperature, target_temperature, num_episodes):
        self.temperature = initial_temperature
        self.target_temperature = target_temperature
        self.num_episodes = num_episodes
        self.episode = 0
        self.episode_numbers = []
        self.temperatures = []
        self.rewards = []

    def transition(self, action):
        new_temperature = self.temperature + action + random.uniform(-1, 1)
        return new_temperature

    def reward(self):
        return -abs(self.temperature - self.target_temperature)

    def run_simulation(self):
        while self.episode < self.num_episodes:
            adjustment = 0.1 * (self.target_temperature - self.temperature)
            self.temperature = self.transition(adjustment)
            r = self.reward()

            self.episode_numbers.append(self.episode + 1)
            self.temperatures.append(self.temperature)
            self.rewards.append(r)

            self.episode += 1

    # Función para mostrar un gráfico usando una biblioteca específica
    def plot(self, data, x_label, y_label, title):
        st.subheader(title)
        st.line_chart(data.set_index(x_label), use_container_width=True)
        st.write(f"Eje X: {x_label}")
        st.write(f"Eje Y: {y_label}")

    def plot_rewards(self):
        df = pd.DataFrame({"Episodio": self.episode_numbers, "Recompensa": self.rewards})
        self.plot(df, "Episodio", "Recompensa", "Recompensas Acumuladas")

    def plot_temperature(self):
        df = pd.DataFrame({"Episodio": self.episode_numbers, "Temperatura (°C)": self.temperatures})
        self.plot(df, "Episodio", "Temperatura (°C)", "Evolución de la Temperatura")

def main():
    st.title("Simulación de Control de Temperatura")

    st.sidebar.header("Configuración del Experimento")

    initial_temperature = st.sidebar.slider("Temperatura Inicial (°C)", 0, 100, 20, help="Temperatura al comienzo del experimento.")
    target_temperature = st.sidebar.slider("Temperatura Objetivo (°C)", 0, 100, 25, help="Temperatura que se busca alcanzar.")
    num_episodes = st.sidebar.number_input("Número de Episodios", 1, 1000, 10, help="Cantidad de episodios en el experimento.")

    control = ControlTemperatura(initial_temperature, target_temperature, num_episodes)

    control.run_simulation()

    st.header("Resultados de la Simulación")
    st.write(f"Temperatura final: {control.temperature:.2f}°C")

    # Mostrar gráficos usando las funciones de orden superior
    control.plot_rewards()
    control.plot_temperature()

if __name__ == "__main__":
    main()
