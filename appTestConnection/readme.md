![speedd](https://user-images.githubusercontent.com/42939877/175611520-2757e76d-fabc-4aaa-b431-20edbd731214.jpg)



# appTestConnection
La idea de este repo es crear un contenedor que ejecute nuestra appTestConnection creada en el [repo de python](https://github.com/Leonardo1133/Python/tree/main/appSpeed) para poder ejecutarla de forma aislada de nuestro sistema y tambien para que pueda ser usada en distintos entornos gracias a las ventajas que tiene docker.

### Step 1: Dockerfile
Creamos un Dockerfile para construir la imagen que finalmente utilizaremos para ejecutar nuestro contenedor. Dockerfile tendra todas las dependencias necesarias como Python, Pandas y speedtest.

### Step 2: Docker Build
Ya creado el Dockerfile con las dependencias, el paso siguiente es construir la imagen de docker con el siguiente comando:

`sudo docker build -t app-speed .`

### Step 3: Docker Run
Teniendo la imagen de docker construida a partir del Dockerfile, podemos ejecutarla para crear un contenedor con la app en funcionamiento. Con el siguiente comando:

`docker run -it -v /home/leo/dev/repos/docker/appSpeed/:/usr/src/app app-speed appTestConnection.py`

- Usamos `docker run` para ejecutar el contenedor a partir de la imagen
- Parametro `-it` para que una vez corriendo se pueda interactuar con el mismo.
- Parametro `-v` para asociar un directorio local con uno propio del contenedor.
