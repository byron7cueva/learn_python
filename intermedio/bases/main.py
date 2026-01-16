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
def clean_text(text: str):
    # PEP 8: 4 espacios por indentacion, no tabs
    """Limpia y normaliza texto."""
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


# Argumentos dinamicos
def newsapi_client(api_key, query, timeout=30, retries=3):
    return f"NewsAPI: {query} con timeout {timeout}"


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con {timeout}"


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
