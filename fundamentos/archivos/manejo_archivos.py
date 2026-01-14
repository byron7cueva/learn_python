# open(nombre, modo)

# R (read) lectura
# W (write) escritura
# X (Crear archivo)

try:
    f = open("archivo.txt", "r")
    # Leer una linea
    print(f.readline())
    # cerrar
    f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo")

# with se encarga de abrir y cerrar
try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")

# w sobre escribe todo lo que ha estado en el archivo
try:
    with open("archivo.txt", "w", encoding="utf-8") as f:
        f.write("Hola mundo desde el with")
    
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")

# a escribe a continuacion pero despues de lo que estaba antes
try:
    with open("archivo.txt", "a", encoding="utf-8") as f:
        f.write("\n") # Agregando un salto de linea
        f.write("Hola mundo desde el with")
    
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")


try:
    with open("archivo2.txt", "r", encoding="utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    open("archivo2.txt", "x")
    print("No se ha encontrado el archivo")


