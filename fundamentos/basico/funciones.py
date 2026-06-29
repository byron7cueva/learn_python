def greet(name):
    message = f"Hola {name}. Bienvenido al curso!"
    return message

result = greet("Luis")
print(result)

# Definir parametros con valore por defecto
def calculate_tax(base_price, rate=0.21):
    tax = base_price + rate
    return tax

print(calculate_tax(1000))

print(calculate_tax(1000, 0.10))