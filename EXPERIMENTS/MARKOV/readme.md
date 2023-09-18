# Markov decision process

Esta documentación describe una simulación de control de temperatura desarrollada en Python utilizando la biblioteca Streamlit. La simulación se basa en un modelo simplificado de control de temperatura donde se ajusta la temperatura inicial para que se acerque a una temperatura objetivo a lo largo de varios episodios.

## **Objetivo**

El objetivo de la simulación es ilustrar los conceptos de control y aprendizaje por refuerzo mediante la toma de decisiones basada en recompensas para controlar la temperatura.

## **Parámetros de Configuración**

La simulación permite configurar los siguientes parámetros:

- **Temperatura Inicial (°C)**: La temperatura al comienzo del experimento.
- **Temperatura Objetivo (°C)**: La temperatura que se busca alcanzar.
- **Número de Episodios**: La cantidad de episodios en la simulación.

## **Modelo de Transición de la Temperatura**

En cada episodio, la temperatura actual se ajusta utilizando la siguiente fórmula:

$Nueva Temperatura = Temperatura Actual + Acción + Ruido$

- **Nueva Temperatura**: La temperatura resultante después de aplicar la acción y el ruido.
- **Temperatura Actual**: La temperatura en el paso anterior.
- **Acción**: Un valor que representa el ajuste controlado por el algoritmo.
- **Ruido**: Un valor aleatorio que simula cambios naturales o fluctuaciones en la temperatura.

## **Recompensa**

La recompensa se calcula como la diferencia absoluta entre la temperatura actual y la temperatura objetivo. Cuanto más cerca esté la temperatura actual de la temperatura objetivo, mayor será la recompensa. La fórmula es:

$Recompensa = -|Temperatura Actual - Temperatura Objetivo|$

## **Simulación**

La simulación se realiza a lo largo de varios episodios:

- **Número de Episodios**: La simulación se ejecuta durante un número específico de episodios determinados por el usuario.
- **Toma de Decisiones**: En cada episodio, se toma una decisión (acción) para ajustar la temperatura actual hacia la temperatura objetivo.
- **Almacenamiento de Resultados**: Se almacenan datos relevantes en listas, como la temperatura actual, las recompensas y el número de episodio, para su posterior visualización.

## **Gráficos**

La simulación utiliza gráficos de líneas para visualizar los datos acumulados durante la simulación:

- **Gráfico de Recompensas Acumuladas**: Muestra cómo evolucionan las recompensas acumuladas a lo largo del tiempo durante la simulación del control de temperatura.
- **Gráfico de Evolución de la Temperatura**: Muestra cómo evoluciona la temperatura en tiempo real durante la simulación del control de temperatura.

## **Funciones de Graficación**

Las funciones de graficación utilizadas aceptan datos, etiquetas de ejes y títulos como argumentos para mostrar gráficos interactivos.

### ****Control de Temperatura como un Procesos de Decision de Markov(MDP)****

> Un proceso de decisión de Markov (MDP) es un marco matemático utilizado para modelar situaciones en las que un agente toma decisiones secuenciales en un entorno incierto. Aquí está cómo podemos interpretar la simulación de control de temperatura como un MDP:
> 

### **Estados (States):**

- **Estado**: En este caso, el estado representa la temperatura actual del sistema en grados Celsius. El rango de temperaturas posibles define el espacio de estados.

### **Acciones (Actions):**

- **Acción**: Cada acción representa un ajuste controlado de la temperatura actual en un episodio. La acción es una cantidad que se suma a la temperatura actual para intentar acercarla a la temperatura objetivo.

### **Transiciones (Transitions):**

- **Transición de Estado**: El proceso de transición de estado ocurre cuando se toma una acción. La nueva temperatura (estado siguiente) se calcula mediante la ecuación :

$S(t+1) = S(t) + A(t) + Ruido$

Donde:

- $S(t+1)$: Nuevo estado (temperatura) en el siguiente paso.
- $S(t)$: Estado actual (temperatura) en el paso actual.
- $A(t)$: Acción tomada en el paso actual.
- $Ruido$: Valor aleatorio que simula cambios naturales o fluctuaciones en la temperatura.

### **Recompensas (Rewards):**

- **Recompensa**: La recompensa en cada estado se calcula como la diferencia absoluta entre la temperatura actual y la temperatura objetivo. Cuanto más cerca esté la temperatura actual de la temperatura objetivo, mayor será la recompensa.

$R = -|S - Objetivo|$

Donde:

- $R$: Recompensa en el estado actual.
- $S$: Temperatura actual en el estado actual.
- $Objetivo$: Temperatura objetivo deseada.

### **Política (Policy):**

- **Política**: La política en este MDP es la estrategia que el agente sigue para seleccionar acciones en cada estado. En este caso, la política podría ser un algoritmo que determine cómo ajustar la temperatura en función de la diferencia entre la temperatura actual y la temperatura objetivo.

### **Objetivo:**

- **Objetivo**: El objetivo del agente en este MDP es maximizar la suma acumulativa de recompensas a lo largo de los episodios. En otras palabras, el agente intenta controlar la temperatura de manera efectiva para mantenerla cerca de la temperatura objetivo y, por lo tanto, obtener recompensas más altas.

### **Aprendizaje y Control:**

- **Aprendizaje por Refuerzo**: La simulación de control de temperatura se puede ver como un problema de aprendizaje por refuerzo, donde el agente aprende a tomar decisiones óptimas a lo largo del tiempo para maximizar las recompensas acumuladas.
- **Exploración vs. Explotación**: El agente puede enfrentar el dilema de exploración vs. explotación, donde decide entre explorar nuevas acciones (ajustes) o explotar acciones conocidas basadas en su política.

En resumen, la simulación de control de temperatura se puede interpretar como un MDP en el que el agente (controlador) toma decisiones secuenciales (acciones) para ajustar la temperatura actual del sistema (estado) y maximizar las recompensas acumuladas. 

Estas fórmulas reflejan las dinámicas fundamentales de la simulación del control de temperatura como un MDP. El objetivo del agente es tomar decisiones secuenciales para ajustar la temperatura actual y maximizar las recompensas acumuladas a lo largo de los episodios, utilizando la política adecuada.