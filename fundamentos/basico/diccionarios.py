# Diccionario
# Almacenamiento de datos en pares "clave=valor".
# Son ideales para rerpresentar objetos del mundo real.
# Se definen usando llaves {}

student = {
    "name": "Carlos",
    "age": 28,
    "course": "Master en IA",
    "isActive": True
}

# Se accede a sus valores a traves de sus claves
print(student['name'])

# Para iterar sobre un diccionario, usamos el m'etodo .iterms(),
# que nos devuelve la clave y el valor en cada iteracion
print("\n Detalles del estudiante:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")