
![docker](https://user-images.githubusercontent.com/42939877/174486033-8dd2bd84-d0db-41fc-989c-bc8a147313f7.png)


# Docker
El objetivo general de este repositorio es realizar distintas aplicaciones con docker para ganar conocimiento con esta herramienta. Las aplicaciones que tenemos construidas son:

- Hello World!
- Docker mas Flask API
- Entrypoint-example with Python
- Docker Compose Example

## ¿Qué es docker y para qué sirve?

**Dependencias**. Es una forma de asegurar que nuestra app ejecute siempre con el mismo entorno de dependencias. 

**Aislación**. Esto crea una caja aislada que además permite evitar problemas con otras aplicaciones en la misma máquina. Por ejemplo podríamos tener 2 app ejecutando a la vez, en distintos containers una con python 2 y otra con python 3 sin problemas. 

**Fácil de Mover**. Podemos ejecutar un container en distintas máquinas y siempre ejecutaría sin errores. Muy bueno para etapas de desarrollo, donde puedo hacer la app en mi máquina y luego probarla en la máquina donde va a ser utilizada.

## ¿Cómo crear un Container?
El camino completo para crear un Docker Container es: 
- Dockerfile. Definimos un dockerfile con todas las dependencias necesarias para nuestra app.
- Docker Image. Creamos una imagen a partir del dockerfile construido anteriormente.
- Docker Container. Ejecutando un "docker run" de la imagen construida creamos un container de nuestra aplicación.

La imagen muestra el camino que describimos:


![docker2](https://user-images.githubusercontent.com/42939877/174488942-8bca63f9-0a36-461f-b4a5-295cae0524be.png)
