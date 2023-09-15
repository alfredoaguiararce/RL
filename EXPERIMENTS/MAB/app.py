import numpy as np
import streamlit as st

class AnunciosMAB:
    def __init__(self, anuncios, tasas_de_clics, epsilon, num_pasos):
        """
        Inicializa el Multi-Armed Bandit (MAB) para la selección de anuncios.
        
        Args:
            anuncios (list): Lista de anuncios disponibles.
            tasas_de_clics (dict): Tasas de clics reales de cada anuncio.
            epsilon (float): Probabilidad de exploración.
            num_pasos (int): Número de pasos del experimento.
        """
        self.anuncios = anuncios
        self.tasas_de_clics = tasas_de_clics
        self.epsilon = epsilon
        self.num_pasos = num_pasos

        # Inicializa estimaciones de recompensa y conteos de selección
        self.estimaciones_recompensa = {ad: 0.0 for ad in anuncios}
        self.conteos_seleccion = {ad: 0 for ad in anuncios}
        self.recompensas_acumuladas = []

    def seleccionar_anuncio(self):
        """
        Selecciona un anuncio según la estrategia epsilon-greedy.
        
        Returns:
            str: El anuncio seleccionado.
        """
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.anuncios)
        else:
            return max(self.estimaciones_recompensa, key=lambda x: self.estimaciones_recompensa[x])

    def simular_experimento(self):
        """
        Simula el experimento MAB para la selección de anuncios.
        """
        for paso in range(self.num_pasos):
            anuncio_seleccionado = self.seleccionar_anuncio()
            tasa_de_clics = np.random.normal(self.tasas_de_clics[anuncio_seleccionado], 0.05)

            # Actualiza estimaciones de recompensa y conteos
            self.conteos_seleccion[anuncio_seleccionado] += 1
            self.estimaciones_recompensa[anuncio_seleccionado] += (tasa_de_clics - self.estimaciones_recompensa[anuncio_seleccionado]) / self.conteos_seleccion[anuncio_seleccionado]

            self.recompensas_acumuladas.append(tasa_de_clics)

    def obtener_mejor_anuncio(self):
        """
        Obtiene el mejor anuncio basado en las estimaciones de recompensa finales.
        
        Returns:
            str: El mejor anuncio.
        """
        anuncio_mejor = max(self.estimaciones_recompensa, key=lambda x: self.estimaciones_recompensa[x])
        return anuncio_mejor
    

# Crear una función principal para la aplicación Streamlit
def main():
    st.title("Simulación de Multi-Armed Bandit para Selección de Anuncios")
    
    st.sidebar.header("Configuración de Parámetros")
    
    # Definir los parámetros iniciales
    anuncios = ["Anuncio A", "Anuncio B", "Anuncio C", "Anuncio D"]
    tasas_de_clics = {
        "Anuncio A": st.sidebar.slider("Tasa de Clics Anuncio A", 0.0, 1.0, 0.2),
        "Anuncio B": st.sidebar.slider("Tasa de Clics Anuncio B", 0.0, 1.0, 0.15),
        "Anuncio C": st.sidebar.slider("Tasa de Clics Anuncio C", 0.0, 1.0, 0.1),
        "Anuncio D": st.sidebar.slider("Tasa de Clics Anuncio D", 0.0, 1.0, 0.25)
    }

    st.sidebar.header("Parámetros de Simulación")
    
    # Configurar la barra lateral para ajustar los parámetros
    epsilon = st.sidebar.slider("Valor de Epsilon MAB 1", 0.0, 1.0, 0.1)
    epsilon_2 = st.sidebar.slider("Valor de Epsilon MAB 2", 0.0, 1.0, 0.01)
    num_pasos = st.sidebar.slider("Número de Pasos", 100, 2000, 1000)

    # Agregar un divisor
    st.sidebar.markdown("---")

    # Configurar y ejecutar el experimento MAB para la selección de anuncios (MAB 1)
    mab = AnunciosMAB(anuncios, tasas_de_clics, epsilon, num_pasos)
    mab.simular_experimento()

    # Configurar y ejecutar el experimento MAB para la selección de anuncios (MAB 2)
    mab_2 = AnunciosMAB(anuncios, tasas_de_clics, epsilon_2, num_pasos)
    mab_2.simular_experimento()

    # Mostrar resultados
    st.header("Resultados de la Simulación")
    st.write(f"Mejor anuncio (basado en estimaciones finales - MAB 1): {mab.obtener_mejor_anuncio()}")
    st.write(f"Mejor anuncio (basado en estimaciones finales - MAB 2): {mab_2.obtener_mejor_anuncio()}")

    # Agregar una descripción a la gráfica de recompensas acumuladas
    st.subheader("Recompensas Acumuladas")
    st.write("Este gráfico muestra cómo evolucionan las recompensas acumuladas a lo largo del tiempo durante la simulación del Multi-Armed Bandit (MAB) para la selección de anuncios. Representa la acumulación de recompensas a medida que se toman decisiones en el MAB durante el experimento.")

    # Mostrar gráfico de recompensas acumuladas de ambos MABs y agregar un título
    st.line_chart({f"epsilon : {epsilon}": mab.recompensas_acumuladas, f"epsilon : {epsilon_2}": mab_2.recompensas_acumuladas}, use_container_width=True)
    st.write("Eje X: Pasos del Experimento")
    st.write("Eje Y: Recompensas Acumuladas")

if __name__ == "__main__":
    main()