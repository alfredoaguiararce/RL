# Documentación del Repositorio de Experimentos de Reinforcement Learning

# **Introducción**

Este repositorio contiene una serie de experimentos de Reinforcement Learning diseñados para ayudarte a comprender y desarrollar algoritmos de aprendizaje por refuerzo. A continuación, se detalla cómo configurar el entorno y las dependencias necesarias para ejecutar estos experimentos.

## **Requisitos del Sistema**

Antes de comenzar, asegúrate de que tu sistema cumple con los siguientes requisitos:

- **Sistema Operativo:** Este repositorio se ha probado en el sistema operativo Windows
- **Python:** Se requiere Python 3. o superior.

## **Instalación de Dependencias**

Para instalar las dependencias necesarias, utilizamos un archivo **`requirements.txt`**. Sigue estos pasos:

1. **Clona el repositorio:**
    
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```
    
2. **Crea un entorno virtual (opcional pero recomendado):**
    
    ```bash
    python -m venv venv
    source venv/bin/activate   # En sistemas Unix/Linux
    ```
    
    O en Windows:
    
    ```
    venv\Scripts\activate
    ```
    
3. **Instala las dependencias utilizando pip:**
    
    ```
    pip install -r requirements.txt
    ```
    
    Esto instalará todas las bibliotecas y paquetes necesarios para ejecutar los experimentos de Reinforcement Learning en tu entorno virtual.
    
4. **Verifica la instalación:**
    
    Para asegurarte de que todo se haya instalado correctamente, puedes ejecutar un script de prueba o comenzar a trabajar en tus experimentos.
    

## **Estructura del Repositorio**

- **/src:** Contiene el código fuente de los experimentos de Reinforcement Learning separado por algoritmos.
- **/scripts:** Puede contener pequeñas practicas basadas en fuentes que se han consultado (sin referencia por el momento).
- **/notebooks:** Tendrá Jupyter notebooks que explicaran y demostraran los experimentos.

## **Ejecución de los Experimentos**

Para ejecutar las simulaciones una vez instaladas las dependencias se puede ejecutar el siguiente comando : 

```bash
streamlit run src/[sub_directorio]/[nombre_del_archivo].py
```

## **Contacto**

Si tienes preguntas, problemas o sugerencias relacionadas con este repositorio, no dudes en ponerte en contacto con el autor a través de [alfredoaguiararce@gmail.com](mailto:alfredoaguiararce@gmail.com).