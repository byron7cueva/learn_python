# f-strings fue agregado en la version 3.6
# Literal string
# En nuevas versines de Python han mejorado el formateo del texto y hace que corra mas rapido

from datetime import datetime

name = "Ana"
year = 2020
text = f"Hola {name}"
print(text)

# Con format no es muy entendible cuando se pasa muchas variables
text_format = "Hola {}".format(name)

# Se puede hacer funciones matematicas
text_calc = f"Hola, tu edad es {2026 - year} años"
print(text_calc)


# Se puede llamar a funciones
text_func = f"Hola {name.upper()}"
print(text_func)


# Podemos realizar condiciones
age = 20
text_if = f"Hola {name}, eres {'mayor' if age >= 18 else 'menor'} de edad"
print(text_if)

# Modificadores de formato
bank_balance = 12000000
# Separador de miles
text = f"Tu saldo en la cuenta bancaria es: {bank_balance:,}"
print(text)

stock_price = 1.405
# Solo tome un valo decimal
text = f"El valor del stock es: {stock_price:.1f}"
print(text)

# Agrear ceros a la izquierda
user_id = 1
# Lo maximo de caracteres que puede tener es 4 digitos
# Si excede el valor del formateador se va mostrar como esta el valor, ya que no aplica en ese caso
text = f"Su id es: {user_id:04d}"
print(text)

# Formatear en una table
product = "Laptop"
price = 1000

# < alineado a la izquierda
# > aliniado a la derecha
text = f"Product: {product:<15} | Precio: {price:>10}"
print(f"{text}\n{text}")


# Fechas
date = datetime(2024, 12, 5, 10, 10)
# Por defecto la fecha imprime en formato ISO al no aplicar el formato
text = f"La fecha completa es {date: %A %d de %B de %Y a las %I:%M %p}"
print(text)

user = "ana"
items = ["A", "B", "C"]
print(f"debug: usuario={user}, total_items={len(items)}, items={items}")
