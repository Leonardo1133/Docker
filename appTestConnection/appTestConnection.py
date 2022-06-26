# Importamos la libreria
import speedtest
import datetime
import time
import pandas as pd


# Creamos el Pandas dataframe con las columnas que queremos
df = pd.DataFrame(columns=['datetime', 'download_speed','upload_speed', 'ping'])

# ---- Hacemos un bucle para monitorear la conexion durante el dia
for sample in range(0, 1000):

    print(sample)

    # tomamos muestras cada 1 min (mas el tiempo de los procesos download() y upload() test)
    time.sleep(1)

    # Fecha y hora actual
    t = datetime.datetime.now()

    # Creamos una instancia de Speedtest
    st = speedtest.Speedtest()

    # Test de velocidad de descarga con el metodo "download". 
    d_st = st.download()

    # Test de velocidad de descarga con el metodo "upload". 
    u_st = st.upload()

    # Hacemos un ping
    st.get_servers([])
    ping = st.results.ping

    # Creamos un diccionario con los datos para agregarlos al pandas dataframe 
    speed_data = {'datetime':t ,'download_speed':d_st, 'upload_speed':u_st, 'ping':ping}

    # agregar datos al dataframe
    df = df.append(speed_data, ignore_index=True)
    df.to_csv('/usr/src/app/data.csv')
