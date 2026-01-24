# main.py - Todo el codigo va estar en un archivo
"""
Sistema de analisis de noticias con APIs multiples
"""

# Imports organizados segun PEP 8
# PEP 8: Import estandar primero, luego de terceros, luego locales

# PEP 8: Configuracion centralizada - contantes en Mayusculas con guines bajos.

API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para strings
# No dice que tipo de comillas pero es mejor que en todo el proyecto se aplique
# La misma convencion.


# PEP 8: Utilidades comunes del proyecto - funciones en snake_case
# PEP 8: 4 espacios por indentacion, no tabs
def clean_text(text: str) -> str:
    """Limpia y normaliza texto removiendo espacios y convirtiendo a minusculas

    Esta funcion toma una cadena de texto y realiza operaciones de limpieza
    basicas para normalizar el contenido. Elimina espacion en blanco al inicio
    y final, y convierte todo el texto a minusculas para facilitar comparacion y
    procesamiento posterior

    Args:
        text (str): La cadena de texto que se desea limpiar y normalizar.

    Returns:
        str: EL texto limpio y normalizado.

    Raises:
        TypeError: Si el parametro text no es de tipo str.

    Examples:
        >>> clean_text("   HOLA MUNDO   ")
        'hola mundo'

        >>> clean_text("Python Programming")
        'python programming'
    """
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble lineas en blanco entre funciones para separar logicamente
def validate_api_key(api_key: str):
    """Valida que la API key tenga formato correcto"""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas despues de las utilidades
def fetch_news_from_api(api_name: str, query: str):
    """Obtener noticias de un API especifica"""
    pass


def process_article_data(raw_data):
    """Procesa datos crudos de articulo."""
    pass


# Longitud de la linea: Maximo 88 caracteres (Black default)
# Identacion: 4 espacions, nunca tabs
# Nombres descriptivos: snake_case para funciones y variables
# Imports ordenados: estandar -> terceros -> locales
# Lineas en blanco: Separar funciones y clases logicamente
# Comillas consistentes: Usar comillas dobles para strings


# Por lo general se utiliza como nombre al argumeto como args
def ejemplo_args(*args):
    print(f"TODOS {args}")
    print(type(args))


ejemplo_args("Este", "parametro", "aca")
ejemplo_args("Hola", "Mundo")
ejemplo_args()


# El orden de los argumentos si importa, porque son posicionales
def ejemplo_args2(api_key, *args):
    print(f"api_key: {api_key}")
    print(f"args: {args}")


print("======")
ejemplo_args2("Este", "parametro", "aca")


# kwargs
# Es similar a args con la diferencia que se pasa clave y valos y se define con **
# Genera un diccionario
def ejemplo_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)


ejemplo_kwargs(api_key="DEMO", query="Noticias de Python", timeout=30, retries=3)
ejemplo_kwargs(
    api_key="DEMO_GUARDIAN",
    section="Sports",
    from_date="2020-10-20",
    timeout=30,
    retries=3,
)

API_KEY = "911167fe64aa4e969d3250d2aadb0473"
BASE_URL = "https://newsapi.org/v2/everything"

import json
import urllib.error
import urllib.parse
import urllib.request


class NewsSystemError(Exception):
    """Error general de la app"""

    pass


class APIKeyError(NewsSystemError):
    """Error cuando la API Key es invalida"""

    pass


# Argumentos dinamicos
def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)  # Json en string transforma en diccionario
            """
            print(
                f"Response data: {data[:100]}..."
            )  # Implrimiendo los primeros 100 caracteres
        """
    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrio un error no se pudo conectar con la API")
    return f"NewsAPI: {query} con timeout {timeout}"


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con {timeout}"


# El orden siempre importa
# Primero los obligatorios, luego los opcionales
def fetch_news(api_name, *args, **kwargs):
    """
    Funcion flexible para conectar con la API
    """

    base_config = {"timeout": 30, "retries": 3}

    # Copiar propiedades del otro diccionario **bas_config
    config = {**base_config, **kwargs}

    api_clients = {"newsapi": newsapi_client, "guardian": guardian_client}

    client = api_clients[api_name]

    # Pasar los  parametros con todos los campops desglozados **config
    return client(*args, **config)


try:
    response_data = fetch_news("newsapi", api_key=API_KEY, query="Python")
    for article in response_data["articles"]:
        print(article["title"])
except APIKeyError as e:
    print(e)

# Python es un lenguaje dinamicamente tipado
# El Typing fue agregado en la version 3.5
# Type Hints: Estiquetas que no fuerzan el contenido
# No se puede usar para nombres de archivos con los mismos nombres de las palabras claves de python
