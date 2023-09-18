# Documentación del Multi-Armed Bandit para Selección de Anuncios

Este documento proporciona una explicación detallada del código implementado en Python para simular un Multi-Armed Bandit (MAB) utilizado en la selección de anuncios en una plataforma de publicidad en línea.

## Clase `AnunciosMAB`

La clase `AnunciosMAB` es la piedra angular del sistema MAB y se encarga de realizar la selección de anuncios y gestionar las estimaciones de recompensa.

### Método `__init__`

Este método inicializa el MAB con los siguientes parámetros:
- `anuncios` (lista): Una lista de los anuncios disponibles.
- `tasas_de_clics` (diccionario): Las tasas de clics reales de cada anuncio.
- `epsilon` (float): La probabilidad de exploración, que determina cuánta exploración frente a explotación se realizará.
- `num_pasos` (int): El número de pasos del experimento MAB.

### Método `seleccionar_anuncio`

Este método se encarga de seleccionar un anuncio según la estrategia epsilon-greedy. Puede elegir explorar aleatoriamente con probabilidad `epsilon` o explotar el anuncio con la estimación de recompensa más alta.

### Método `simular_experimento`

Este método simula el experimento MAB para la selección de anuncios. En cada paso, se selecciona un anuncio, se simula la tasa de clics y se actualizan las estimaciones de recompensa y los conteos de selección.

### Método `obtener_mejor_anuncio`

Este método devuelve el mejor anuncio basado en las estimaciones de recompensa finales.

## Uso del MAB

En el código principal, se configuran los parámetros del MAB, como la lista de anuncios y las tasas de clics reales. Luego, se crea una instancia de la clase `AnunciosMAB` y se ejecuta el experimento MAB utilizando el método `simular_experimento`. Finalmente, se obtiene y muestra el mejor anuncio utilizando el método `obtener_mejor_anuncio`.

Este enfoque orientado a objetos permite una gestión clara y modular del MAB para la selección de anuncios y facilita la comprensión y extensión del código en aplicaciones de optimización publicitaria en línea.