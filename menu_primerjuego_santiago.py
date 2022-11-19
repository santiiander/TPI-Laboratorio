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
        contadorproblema = 0
        randominvader=0
        probabilidadinvader = random.randint(1, 2)
        print("Bienvenido a Adivina el número")
        dificultadjuego1 = int(input("Por favor, ingrese la dificultad del juego, sea 1, 2 o 3: "))

        if dificultadjuego1 == 1:
            vidas = 7
        elif dificultadjuego1 == 2:
            vidas = 6
        elif dificultadjuego1 == 3:
            vidas = 5

        print("Tendrás que adivinar el numero generado aleatoriamente, o ingresado por el usuario ")

        inputnumero = int(input("Por favor, ingrese 1 si desea que el numero sea aleatorio, 0 si desea ingresarlo "))
        if probabilidadinvader == 1:

            print("Oh no!, un invader se metió en el programa ;)")
            print("      ____       ")
            print('     /___/\_                   ')
            print("    _\   \/_/\__                ")
            print("  __\       \/_/\               ")
            print("  \   __    __ \ \               ")
            print(" __\  \_\   \_\ \ \   __      ")
            print("\_\/_\__\/\__\/\__\/_\_\/   ")
            print("   \_\/_/\       /_\_\/  ")
            print("      \_\/       \_\/  ")

            print("Hay una probabilidad de que el invader te quite o agregue una vida!")
            randominvader = random.randint(1, 2)

        if inputnumero == 1:
            print("El número se generará aleatoriamente ")
            if dificultadjuego1 == 1:
                numero = random.randint(0, 100)  # Dificultad 1 = 7 vidas
            if dificultadjuego1 == 2:
                numero = random.randint(0, 500)  # Dificultad 2 = 6 vidas
            if dificultadjuego1 == 3:
                numero = random.randint(0, 1000)  # Dificultad 3 = 5 vidas

        else:
            numero = int(input("El numero será elegido por el otro jugador: "))
            if dificultadjuego1 == 1 and numero > 100:
                print("La dificultad fue seteada en nivel 1, el numero no puede superar el 100: ")
            if dificultadjuego1 == 2 and 100 > numero < 500:
                print("La dificultad fue seteada en nivel 2, el numero no puede ser menor que 100 ni mayor que 500: ")
            if dificultadjuego1 == 3 and 500 > numero > 1000:
                print("La dificultad fue seteada en nivel 3, el numero no puede ser menor que 100 ni mayor que 1000: ")


        if numero > 0:
            digits = int(math.log10(numero)) + 1
            print("El numero tiene", digits, "digitos!")
        else:
            if numero == 0:
                digits = 1
                print("El numero tiene", digits, "digitos!")

        while vidas != 2:  # arreglar error de dificultad y esta linea
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

            while vidas > 0 and vidas < 7 and numentrada != numero and randominvader != 2:
                vidas -= 1
                print("Oh, una vida menos :( , prueba de nuevo")
                numentrada = int(input())

                if numentrada == numero:
                    print("Numero correcto!")
                    print("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: ")
                    menu = int(input())
                    break
                primerdigito = int(str(numero)[0])

            while vidas == 3 and contadorproblema==0:
                    if probabilidadinvader == 1:

                        if randominvader == 1:
                            vidas -= 1
                            print(
                            "El invader se metió en el código y te robó 1 vida! 💔 ")

                        else:
                            vidas += 1
                            contadorproblema+=1
                            print("El invader se metió en el código y te evitó perder 1 vida! ❤ ")

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
                break
