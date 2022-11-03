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
        dificultadjuego1 = int(input("Por favor, ingrese la dificultad del juego, sea 1, 2 o 3: "))
        if dificultadjuego1 == 1:
            vidas = 7
        if dificultadjuego1 == 2:
            vidas = 6
        if dificultadjuego1 == 3:
            vidas = 5
        print("Tendrás que adivinar el numero generado aleatoriamente, o ingresado por el usuario ")
        print(vidas)  # borrar
        inputnumero = int(input("Por favor, ingrese 1 si desea que el numero sea aleatorio"
                                " 0 si desea ingresarlo "))
        print("Oh no!, un invader se metió en el programa ;)")
        print("      ____       ")
        print("     /___/\_                   ")
        print("    _\   \/_/\__                ")
        print("  __\       \/_/\               ")
        print("  \   __    __ \ \               ")
        print(" __\  \_\   \_\ \ \   __      ")
        print("\_\/_\__\/\__\/\__\/_\_\/   ")
        print("   \_\/_/\       /_\_\/  ")
        print("      \_\/       \_\/  ")
        print("Hay una probabilidad de que el invader te quite o agregue una vida!")


        if inputnumero == 1:
            print("El número se generará aleatoriamente ")
            if dificultadjuego1 == 1:
                numero = random.randint(0, 100)
            if dificultadjuego1 == 2:
                numero = random.randint(0, 500)
            if dificultadjuego1 == 3:
                numero = random.randint(0, 1000)
            print(numero)  # borrar

        elif inputnumero == 0:
            numero = int(input("El numero será elegido por el otro jugador"))
            if dificultadjuego1 == 1 and numero > 100:
                print("La dificultad fue seteada en nivel 1, el numero no puede superar el 100: ")
            if dificultadjuego1 == 2 and numero > 500 or numero < 100:
                print("La dificultad fue seteada en nivel 2, el numero no puede ser menor que 100 ni mayor que 500: ")
            if dificultadjuego1 == 3 and numero < 1000:
                print("La dificultad fue seteada en nivel 3, el numero no puede ser menor que 100 ni mayor que 1000: ")
            numero = int(input())
            # Agregamos la funcion para poder obtener los digitos del numero como ayuda

        if numero > 0:
            digits = int(math.log10(numero)) + 1
            print("El numero tiene", digits, "digitos!")
        else:
            if numero == 0:
                digits = 1
                print("El numero tiene", digits, "digitos!")

        if vidas <= 7 and vidas >= 5:
            print("Intentemoslo")
            numentrada = int(input())

        if numentrada == numero:
            print("Numero correcto!")
            print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: ")
            del numentrada
            del numero
            menu = int(input())
        else:
            if numentrada != numero:
                vidas = vidas - 1

        while vidas > 0 and vidas < 7:
            vidas = vidas - 1
            print("Oh, una vida menos :( , prueba de nuevo")
            numentrada = int(input())

            if numentrada == numero:
                print("Numero correcto!")
                print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: ")
                del numentrada
                del numero
                menu = int(input())
                break
            primerdigito = int(str(numero)[0])

            if vidas == 5 and dificultadjuego1 == 3:
                print("Ya perdiste 2 vidas!")
                print("Voy a ayudarte un poco...")
                print()

            if vidas == 2 and digits == 1:
                print("Lo siento, no puedo revelarte la cantidad de digitos")
                print("Pero puedo decirte que tu numero se encuentra entre el 0 y el 9")

            if vidas == 2 and digits > 1:
                print("Veo que ya solo te quedan 2 intentos D:")
                print("Voy a darte una pista...")
                print("El numero empieza con", primerdigito)

            if vidas == 0:
                print("Lo siento! perdiste :(")
                print("El numero era", numero)
                print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: ")
                menu = int(input())
