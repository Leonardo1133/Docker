
![docker](https://user-images.githubusercontent.com/42939877/174486033-8dd2bd84-d0db-41fc-989c-bc8a147313f7.png)


# Docker
Docker es una herramienta que te permite ejecutar y desarrollar una aplicacion siempre en un mismo entorno. Esto quiere decir que todas las dependencias que la app va a requerir van a estar siempre en el contenedor. Y vamos a poder mover el contenedor entre una maquina y otra y esas dependencias siempre estaran ahi adentro. Esto es una ventaja porque puedo compartir esta app con otras personas o con otros ambientes y seguira funcionando igual.

Algunas caracteristicas:

**Aislación**. Esto crea una caja aislada que además permite evitar problemas con otras aplicaciones en la misma máquina. Por ejemplo podríamos tener 2 app ejecutando a la vez, en distintos containers una con python 2 y otra con python 3 sin problemas. 

**Fácil de Mover**. Podemos ejecutar un container en distintas máquinas y siempre ejecutaría sin errores. Muy bueno para etapas de desarrollo, donde puedo hacer la app en mi máquina y luego probarla en la máquina donde va a ser utilizada.

**Dependencias**. Es una forma de asegurar que nuestra app ejecute siempre con el mismo entorno de dependencias. 

## ¿Cómo crear un Container?
El camino completo para crear un Docker Container es: 
- Dockerfile. Definimos un dockerfile con todas las dependencias necesarias para nuestra app.
- Docker Image. Creamos una imagen a partir del dockerfile construido anteriormente.
- Docker Container. Ejecutando un "docker run" de la imagen construida creamos un container de nuestra aplicación.

La imagen muestra el camino que describimos:


![docker2](https://user-images.githubusercontent.com/42939877/174488942-8bca63f9-0a36-461f-b4a5-295cae0524be.png)

## ¿Qué es Dockerfile?
A Dockerfile es un documento de texto que contiene todos los comandos que un usuario podría llamar en la línea de comando para ensamblar una imagen.
Docker puede crear imágenes automáticamente leyendo las instrucciones de un archivo Dockerfile.


## ¿Qué es Docker Compose?

Docker Compose es una herramienta para definir y ejecutar aplicaciones Docker de varios contenedores. Con Compose, utiliza un archivo YAML para configurar los servicios de su aplicación. Luego, con un solo comando, crea e inicia todos los servicios desde su configuración. 

![docker-compose-1](https://user-images.githubusercontent.com/42939877/176027816-d5d8ee42-8fb6-4481-874d-63f69439dcdd.png)

