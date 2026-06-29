# Manejo de Errores (Try/Except)
# Intentamos try ejecutar codigo y capturamos except errores especificos si ocurren

# Ejemplo de entrada invelida
age_str = input("Introduce tu edad: ")

try:
    age_int = int(age_str)
    print(f"Tu edad es {age_int}")
except ValueError:
    print("Error: No se ingreso un velo numerico valido.")

print("Fin")