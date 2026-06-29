# Clase
# Una clase define la estructura general que tendra todos los objetos creados a partir.
# de ella.

# Definicion de clase
# Se debe utilizar PascalCase
class Book:
    # pass indica que la clase esta vacia intencionalmente
    pass

# Insranciacion
book_1 = Book()
book_2 = Book()

# Los objetos son distintos en la memoria del ordenador
print(book_1)
print(book_2)


class OtherBook:
    # Definiendo el constructor con __init__
    # Siempre recibe self, la cual es la referencia a la instancia especifica.
    # Siempre self debe ser el primer parametro del metodo de una clase
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_loan = False

    def loan(self):
        if self.is_loan:
            print(f"Error: '{self.title}' ya esta prestado")
        else:
            self.is_loan = True
            print(f"'{self,self.title}' ha sido prestado")

    def return_book(self):
        if not self.is_loan:
            print(f"Error: '{self.title}' no estaba prestado")
        else:
            self.is_loan = False
            print(f"'{self,self.title}' ha sido devuelto")
            

book_1 = OtherBook("Titulo1", "Auto1")
book_2 = OtherBook("Titulo2", "Autor2")
print(book_1.title)
print(book_1.author)

book_1.loan()
print(book_1)
book_1.return_book()
print(book_1)