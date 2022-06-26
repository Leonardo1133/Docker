# Desde una imagen oficial de python, construimos nuestra imagen custom
FROM python

# Agregamos dependencias: pandas y speedtest
RUN python -m pip install --upgrade pip && pip install pandas && pip install speedtest-cli 

# indicamos donde estara la app en python
WORKDIR /usr/src/app

# Copiamos todos los archivos al directorio de trabajo.
COPY . .

# Indicamos cual es el script .py que se ejecutara al iniciar el contenedor
CMD ["appSpeed.py"]

# Indicamos el comando que aplicara al iniciar el contenedor
ENTRYPOINT ["python3"]