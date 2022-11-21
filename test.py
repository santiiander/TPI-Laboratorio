while vidas != 2:

    print("Intentemoslo")
    numentrada = int(input())

    if numentrada == numero:
        print("Numero correcto!")
        print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: ")
        menu = int(input())
        break
    else:
        if numentrada != numero:
            vidas -= 1

    while vidas > 0 and vidas < 7 and numentrada != numero:
        vidas -= 1
        print("Oh, una vida menos :( , prueba de nuevo")
        numentrada = int(input())

        if vidas == 2 and digits == 1:
            print("Lo siento, no puedo revelarte la cantidad de digitos")
            print("Pero puedo decirte que tu numero se encuentra entre el 0 y el 9")

        if vidas == 2 and digits > 1:
            print("Veo que ya solo te quedan 2 intentos D:")
            print("Voy a darte una pista...")
            print("El numero empieza con", primerdigito)

        if numentrada == numero:
            print("Numero correcto!")
            print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: ")
            menu = int(input())
            break
        primerdigito = int(str(numero)[0])

    if vidas == 0:
        print("Lo siento! perdiste :(")
        print("El numero era", numero)
        print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: ")
        menu = int(input())
        break