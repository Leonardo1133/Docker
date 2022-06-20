## Creamos una aplicacion "hello World" donde aplicamos algunos conceptos importantes de docker como ser:

- **Dockerfile**. Permite construir una imagen custom, con todos los requerimientos.
- **Imagenes preconstruidas de docker hub**. Podemos descargar imagenes creadas por la comunidad con todo lo necesario para nuestra app, y con las mejores practicas de diseño.
- **Comandos Importantes**. Aprendemos los comandos mas importantes de docker para iniciar con el uso de esta herramienta.
- **Volumenes**. Usamos volumenes para vincular los files del contenedor con los que estan fuera, ubicados nuestra maquina.

## Para crear la APP: "Hello World", seguimos los siguientes pasos:

### Step 1: **APP Code**
Creamos el codigo fuente, es un index.php para imprimir el hello world.

### Step 2: **Create Dockerfile**
La primera linea de codigo es el FROM que hace referencia a una imagen que normalmente trae un SO (ejemplo alpine, ubuntu, etc) preinstalado y algunas depedencias. Una buena practica es usar imagenes oficiales en docker-hub.

Buscamos en docker-hub si hay alguna imagen con php y apache preinstalados y encontramos "php:7.4.1-apache-buster" imagen oficial de php.

### Step 3: **Docker Build**
Construir la imagen ejecutando el siguiente comando: "docker build -t hola-php ."

![Captura de pantalla de 2022-06-19 19-52-19](https://user-images.githubusercontent.com/42939877/174503347-56425e5a-6ef4-4eaa-82b6-3d7b31ca1fb6.png)

### Step 4: **Docker Run**
Crear el contenedor con "docker run -p 80:80 hola-php"
Podemos ver que el LOG nos dice la direccion ip: http://172.17.0.2/ donde esta el output de nuestra app php.

![docker_run](https://user-images.githubusercontent.com/42939877/174502810-d610346f-0beb-4728-aaee-c8a583899d1b.png)

Visitando la direccion http podemos visualizar la salida del **Hello World!**

![web](https://user-images.githubusercontent.com/42939877/174504376-92daab08-1a26-4c2a-b121-4154f4fef5d1.png)

### Step 5: Volumes
Los Volumenes permiten entre otras cosas, vincular un directorio entre el contenedor y el host. Esto nos permite editar el index.php y ver reflejados los cambios automaticamente en la web sin tener que reconstruir el contenedor.

Ejecutamos: "sudo docker run -p 80:80 -v /home/leo/dev/repos/docker/hello_world/src/:/var/www/html hola-php". Esto va montar el directorio local "/src" dentro del contenedor "/var/www/html":

![vol](https://user-images.githubusercontent.com/42939877/174504987-38cf2735-2ed9-4a03-8d28-822277e055ac.png)

Dejando activo el contenedor actual y abriendo otra terminal, modificamos el index.php y nos dirigimos al navegador web para hacer un check de los cambios:

![Edit_vol](https://user-images.githubusercontent.com/42939877/174505238-4f1ded29-7f58-43b8-84a3-c36c4d0501cc.png)





![web_edit](https://user-images.githubusercontent.com/42939877/174505248-af878054-bff3-487a-9bb4-31278b89c593.png)
