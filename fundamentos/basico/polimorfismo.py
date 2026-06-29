# Clase Base
class ItemBiblioteca:
    def __init__(self, titulo):
        self.titulo = titulo
        self.esta_prestado = False

    def prestar(self):
        self.esta_prestado = True
        print(f"Itme '{self.titulo}' prestado.")

    def devolver(self):
        self.esta_prestado = False
        print(f"Item '{self.titulo}' se ha devuelto.")

class Libro(ItemBiblioteca):
    def __init__(self, titulo, autor):
        super().__init__(titulo)
        self.autor = autor

class Revista(ItemBiblioteca):
    def __init__(self, titulo, numero_edicion):
        super().__init__(titulo)
        self.numero_edicion = numero_edicion

class Libro(ItemBiblioteca):
    def __init__(self, titulo, autor):
        super().__init__(titulo)
        self.autor = autor

class DVD(ItemBiblioteca):
    def __init__(self, titulo, director):
        super().__init__(titulo)
        self.director = director

    # Sobrescritura (Overrding) del metodo prestar
    def prestar(self):
        print(f"Vedificando si el DVD '{self.titulo}' tiene rayones...")
        return super().prestar()
    

items = [
    Libro("Libro A", "Autor A"),
    DVD("Pelicula B", "Director B")
]

for item in items:
    item.prestar()
    print("-" * 10)