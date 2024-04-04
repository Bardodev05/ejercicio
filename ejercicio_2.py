#le pedimos al usuario una frase ( o varias)
frase = input("decime una frase y te calculo cuanto tardarias en hacerlo si tuvieras que decirmelo: ")

#creamos una lista con todas las palabras de la frase ( separa cada vez que hat un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len para ver la cantidad de elementos que hay en la lista
cantidad_de_palablas = len(palabras_separadas)

#en caso de que diga mas de 120 parablas le mandamos un mensaje
if cantidad_de_palablas > 120 :
    print("para flaco tampoco te pedi una historia de tu vida")

#calculamos cuanto tardarias en decrilo
print(f"dijiste {cantidad_de_palablas} palabras,y tardarias {cantidad_de_palablas / 2} segundos en decirlo")
print(f"yudy lo diria en {cantidad_de_palablas * 100 // 2 * 1.3 / 100} segundos")