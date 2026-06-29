import logging

# Configuracion basica para guardar los logs en un archivo
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def my_function(data):
    logging.info(f"Funcion iniciada con los datos: {data}")
    try:
        result = data / 2
        logging.info(f"Calculo exitoso. Resultado {result}")
        return result
    except TypeError:
        logging.error("Error los datos de entrada no heran numeros", exc_info=True)
        return None
    
my_function("texto")