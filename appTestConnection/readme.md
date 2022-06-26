![speedd](https://user-images.githubusercontent.com/42939877/175611520-2757e76d-fabc-4aaa-b431-20edbd731214.jpg)



# appTestConnection
La idea de este repo es crear un contenedor que ejecute nuestra appTestConnection creada en el [repo de python](https://github.com/Leonardo1133/Python/tree/main/appSpeed) para poder ejecutarla de forma aislada de nuestro sistema y tambien para que pueda ser usada en distintos entornos gracias a las ventajas que tiene docker.

### Step 1: Dockerfile
Creamos un Dockerfile para construir la imagen que finalmente utilizaremos para ejecutar nuestro contenedor. Dockerfile tendra todas las dependencias necesarias como Python, Pandas y speedtest.

### Step 2: Docker Build
Ya creado el Dockerfile con las dependencias, el paso siguiente es construir la imagen de docker con el siguiente comando:

`sudo docker build -t app-test-connection .`

- Usamos `docker build` para construir la imagen a partir del Dockerfile.
- Parametro `-t`
- `app-test-connection` es el nombre que elegimos para nuestra imagen docker.

### Step 3: Docker Run
Teniendo la imagen de docker construida a partir del Dockerfile, podemos ejecutarla para crear un contenedor con la app en funcionamiento. Con el siguiente comando:

`docker run -it -v /home/leo/dev/repos/docker/appSpeed/:/usr/src/app app-test-connection appTestConnection.py`

- Usamos `docker run` para ejecutar el contenedor a partir de la imagen
- Parametro `-it` para que una vez corriendo se pueda interactuar con el mismo.
- Parametro `-v` para asociar un directorio local con uno propio del contenedor.
- Especificamos el nombre de la imagen: `app-test-connection`.
- Indicamos el script de python que queremos ejecutar: `appTestConnection.py`.

### Result
Finalmente tenemos un file CSV con los datos de conexion listos para ser analizados, incluso podemos crear algun modelo de machine learning para predicciones de nuestra conexion.

![dockerrun](https://user-images.githubusercontent.com/42939877/175822728-a40433f1-2c0f-4c26-9aa7-26ea9ca7fea5.png)

Nota: Algo que agregue es que el CSV resultante generado dentro del contenedor se replicado en nuestra maquina local. Esta es otra ventaja que aprovechamos de los volumenes compartidos.
