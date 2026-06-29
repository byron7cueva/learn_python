# Lista
languages = ["Python","Javascript","Java"]

print(languages[0])

#Indices negativos acceden desde el final
print(languages[-1])

# Agregar un nuevo elemento
languages.append("Go");

# Eliminar un elemento
languages.remove("Java")

print(languages)

for language in languages:
    print(language)