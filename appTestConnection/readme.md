![speedd](https://user-images.githubusercontent.com/42939877/175611520-2757e76d-fabc-4aaa-b431-20edbd731214.jpg)



# appTestConnection
La idea de este repo es crear un contenedor que ejecute nuestra appTestConnection creada en el [repo de python](https://github.com/Leonardo1133/Python/tree/main/appSpeed) para poder ejecutarla de forma aislada de nuestro sistema y tambien para que pueda ser usada en distintos entornos gracias a las ventajas que tiene docker.

### Step 1: Dockerfile create
Creamos un Dockerfile para construir la imagen que finalmente utilizaremos para ejecutar nuestro contenedor. Dockerfile tendra todas las dependencias necesarias como Python, Pandas y speedtest.

