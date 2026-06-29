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


libro = Libro("Dune", "Frank Herbert")
revista = Revista("Wired", 305)

libro.prestar()
revista.prestar()