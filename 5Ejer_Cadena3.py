def cuenta(cadena, letra_busc):
    contador = 0
    for letra in cadena:
        if letra == letra_busc:
            contador = contador + 1
    print("El numero de letras", letra_busc, "es: ", contador)


cadena = input("Ingrese una palabra: ")
letra_busc = input("Letra a buscar: ")
cuenta(cadena, letra_busc)