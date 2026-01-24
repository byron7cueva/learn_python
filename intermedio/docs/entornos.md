# Entornos

Nos permite urilizar diferentes versiones del mismo paquete.

En Python existe los Virtual Environments and Pakages.

Documentacion: https://docs.python.org/3/tutorial/venv.html

* Permiten tener una carpeta extra en el computador con una version de Python.
* Se debe instalar las dependencias despues de habilitar esa version de Python virtualizada.
* Python da un escript para habilitar el entorno.
* Cuando se crea un entorno virtual nuevo se crea sin paquetes intalasdos. Para instalar utilizamos una dependencia llamada pip.
* Para compartir las dependencias de un proyecto se usa requirements.txt. Es un archivo de texto con la lista de las dependenicas y las versiones.
* La carpeta del entorno virtual nunca debe ser subida al repositorio.


Saber donde esta instalado Python

```shell
which python
```

## Crear el entorno virtual

```shell
python -m venv nombre
```

## Habilitar el entorno

```shell
source news_env/bin/activate
```

## Desactivar el entorno vitual
```shell
deactivate
```

## Utilidades:

* Pagina para buscar dependencias: pypi.org

## Instalar dependencias

```shell
pip install ruff

# Listar las dependencias
pip list

#Obtener la lista en formatos de requirements.txt
pip freeze

# Instalar todas las dependencias
pip install -r requirements.txt

# Desinstalar una dependencia
pip uninstall ruff
```