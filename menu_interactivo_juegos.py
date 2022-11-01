import math
import random

menu = 0
while menu == 0:
    print("Hola!, Bienvenido.")
    print("Por favor, seleccione el número correspondiente al juego o actividad")
    print("1) Adivina el numero")
    print("2) ???")
    print("3) ???")
    print("4) ???")
    menu = int(input())

    while menu == 1:
        print("Bienvenido a Adivina el número")
        print("Tendrás que adivinar el numero generado aleatoriamente, o ingresado por el usuario")
        vidas = 5
        inputnumero = int(input("Por favor, ingrese 1 si desea que el numero sea aleatorio"
                                " 0 si desea ingresarlo "))
        if inputnumero == 1:
            print("El número se generará aleatoriamente")
            numero = random.randint(0, 100)
            print(numero)  # esto hay que borrarlo para que no revele el numero

        elif inputnumero == 0:
            print("El numero será elegido por el otro jugador")
            numero = int(input())
            # Agregamos la funcion para poder obtener los digitos del numero como ayuda

        if numero > 0:
            digits = int(math.log10(numero)) + 1
            print("El numero tiene", digits, "digitos!")
        else:
            if numero == 0:
                digits = 1
                print("El numero tiene", digits, "digitos!")

        if vidas == 5:
            print("Intentemoslo")
            numentrada = int(input())

        if numentrada == numero:
            print("Numero correcto!")
            print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0")
            del numentrada
            del numero
            menu = int(input())
        else:
            if numentrada != numero:
                vidas = vidas - 1

        while vidas > 0 and vidas < 5:
            vidas = vidas - 1
            print("Oh, una vida menos :( , prueba de nuevo")
            numentrada = int(input())

            if numentrada == numero:
                print("Numero correcto!")
                print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0")
                del numentrada
                del numero
                menu = int(input())
                break
            primerdigito = int(str(numero)[0])

            if vidas == 2 and digits == 1:
                print("Lo siento, no puedo revelarte la cantidad de digitos")
                print("Pero puedo decirte que tu numero se encuentra entre el 0 y el 9")

            if vidas == 2 and digits > 1:
                print("Veo que ya solo te quedan 2 intentos D:")
                print("Voy a darte una pista...")
                print("El numero empieza con", primerdigito)

            if vidas == 0:
                print("Lo siento! perdiste :(")
                print("El numero era",numero)
                print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0")
                menu = int(input())
