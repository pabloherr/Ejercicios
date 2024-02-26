def inv_cadena(cadena):
    new_cadena = []
    for i in range(len(cadena)):
        new_cadena.append(cadena[-1])
        cadena = cadena[:-1]
    new_cadena = "".join(new_cadena)
    print(new_cadena)

inv_cadena("Hola Mundo")