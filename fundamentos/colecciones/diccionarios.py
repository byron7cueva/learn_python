# Diccionarios
# Coleccion de pares clave y valor (Ordenado a partir de Python 3.7)

auto = {
    "marca": "Renault",
    "modelo": "Clio",
    "ano": 2025
}

print(auto)

# Tomar informacion
print(auto["marca"])
print(auto.get("marca"))

# Obtener las claves o valores
print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("Marca es una de las propiedades de este diccionario")

# Modificar un valor
auto["ano"] = 2020
print(auto)

# Agregar una propiedad
auto["color"] = "verde"
print(auto)

# Hacer modificaciones y agregar propiedades
auto.update({"ano": 2022, "puertas": 4})
print(auto)

# Recorrer
for key in auto:
    print(key)

for key in auto.keys():
    print(key)

for value in auto.values():
    print(value)

print("==========")
for k,v in auto.items():
    print(k,v)

# Eliminar
auto.pop("puertas")
print(auto)

# Elimina la ultima propiedad
auto.popitem()
print(auto)

# Vaciar el diccionario
auto.clear()
print(auto)

# Diccionarios aninados
familia = {
    "hijo1": {"nombre": "Luis", "edad": 19},
    "hijo2": {"nombre": "Pedro", "edad": 20},
    "hijo3": {"nombre": "Juan", "edad": 21}
}
print(familia)

print(familia["hijo1"]["nombre"])
print(familia.get("hijo1").get("nombre"))