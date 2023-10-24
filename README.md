# Block de Notas

## Instalación

Para instalar este proyecto, asegúrate de tener Python y Flask instalados en tu sistema. Luego, sigue estos pasos:

1. Clona este repositorio en tu máquina local.

```shell
git clone https://github.com/tu-usuario/block-de-notas.git
```

2. Accede al directorio del proyecto.

```shell
cd block-de-notas
```

3. Instala las dependencias necesarias desde el archivo `requirements.txt` utilizando pip.

```shell
pip install -r requirements.txt
```

4. Opcionalmente, si deseas visualizar la base de datos, puedes utilizar la extensión de Visual Studio Code llamada "SQLite Viewer". 

## Uso

Para ejecutar el proyecto, utiliza el siguiente comando:

```shell
flask run
```

Esto iniciará la aplicación en `localhost:5000`. Si deseas cambiar el puerto, puedes hacerlo proporcionando la opción `--port` seguida del número de puerto deseado.

Ejemplo: 

```shell
flask run --port 8080
```

Si necesitas activar el modo de depuración, agrega la opción `--debug` al comando:

```shell
flask run --debug
```

Nota: No se recomienda ejecutar el proyecto directamente con el comando `python3`. Usar `flask run` es la forma correcta de iniciar la aplicación.