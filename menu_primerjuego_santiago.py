import math
import random
while True:
    menu = 0
    while menu == 0:
        print("Hola!, Bienvenido al algoritmo de Play.In, desarrollado para aprender jugando")
        print("Por favor, seleccione el número correspondiente al juego o actividad")
        print("1) Adivina el numero")
        print("2) Trivia Sports Mundial")  #menú principal navegable que nos deja seleccionar el juego
        print("3) Tabla Periodica Quizz")
        print("4) Medieval History")
        print("5) Salir")

        menu = int(input())   #lectura del juego a correr

    while menu == 1:   #mientras el usuario haya ingresado 1, se ejecuta el juego Adivina el número
        print("Bienvenido a Adivina el número")
        dificultadjuego1 = int(input("Por favor, ingrese la dificultad del juego, sea 1, 2 o 3: "))

        if dificultadjuego1 == 1:
            vidas = 6
        elif dificultadjuego1 == 2:  #según lo ingresado para dificultadjuego1, será la dificultad del juego
            vidas = 5                #siemdo la cantidad de vidas a tener durante el algoritmo
        elif dificultadjuego1 == 3:
            vidas = 4
        else:
            while dificultadjuego1 != 1 and dificultadjuego1 != 2 and dificultadjuego1 != 3:  #si lo ingresado no corresponde a 1,2 o 3, pregunta continuamente
                dificultadjuego1 = int(input("Por favor, ingrese la dificultad del juego, sea 1, 2 o 3: ")) #hasta que sea uno de los valores aceptados

        print("Tendrás que adivinar el numero generado aleatoriamente, o ingresado por el usuario ")

        inputnumero = int(input("Por favor, ingrese 1 si desea que el numero sea aleatorio, 0 si desea ingresarlo ")) #preguntamos al usuario si quiere que el numero
                                                                                                                      #sea generado aleatoriamente o ingresado por el/otro
        if inputnumero == 1:
            print("El número se generará aleatoriamente ")
            if dificultadjuego1 == 1:
                numero = random.randint(0, 100)  # Dificultad 1 = 7 vidas
            if dificultadjuego1 == 2:
                numero = random.randint(0, 500)  # Dificultad 2 = 6 vidas  #números generados aleatoriamente según la dificultad
            if dificultadjuego1 == 3:
                numero = random.randint(0, 1000)  # Dificultad 3 = 5 vidas

        else:
            numero = int(input("El numero será elegido por el otro jugador: "))  #ingresa el numero el usuario
            print("\n" * 15)
            while dificultadjuego1 == 1 and numero > 100:
                print("La dificultad fue seteada en nivel 1, el numero no puede superar el 100: ")
                numero = int(input("El numero será elegido por el otro jugador: "))  #si el numero ingresado y la dificultad no corresponden
                print("\n" * 10)                                                     #se genera un loop pidiendo que esté entre los parametros
            while dificultadjuego1 == 2 and 100 > numero < 500:
                print("La dificultad fue seteada en nivel 2, el numero no puede ser menor que 100 ni mayor que 500: ")
                numero = int(input("El numero será elegido por el otro jugador: "))
                print("\n" * 10)
            while dificultadjuego1 == 3 and 500 > numero < 1000:
                print("La dificultad fue seteada en nivel 3, el numero no puede ser menor que 100 ni mayor que 1000: ")
                numero = int(input("El numero será elegido por el otro jugador: "))
                print("\n" * 10)

        if numero > 0:
            digits = int(math.log10(numero)) + 1    #dato de proceso, la cantidad de digitos del número
            print("El numero tiene", digits, "digitos!")
        else:
            if numero == 0:
                digits = 1    ##dato de proceso, la cantidad de digitos del número
                print("El numero tiene", digits, "digitos!")

        primerdigito = int(str(numero)[0])  #obtenemos el primer digito

        numentrada = int(input("Intentemoslo!\n"))    # empezamos pidiendo el número con el cual vamos a jugar y comprar

        while vidas > 0 and numero != numentrada:   #mientras numero sea distinto al que ingresamos intentando
            numentrada = int(input("Oh, una vida menos :( , prueba de nuevo\n"))  #va a descontar vidas y pedir el número
            vidas -= 1                              #hasta que los numeros coincidan o las vidas lleguen a 0

            if vidas == 2 and digits > 1:
                print("Veo que ya solo te quedan 2 intentos D:")
                print("Voy a darte una pista mas...")   #si quedan 2 vidas y el número tiene mas de un digito, devuelve
                print("El numero empieza con", primerdigito) #este mensaje x pantalla

            if vidas == 2 and digits == 1:
                print("Lo siento, no puedo revelarte la cantidad de digitos")  #si tiene un solo digito y 2 vidas devuelve el print
                print("Pero puedo decirte que tu numero se encuentra entre el 0 y el 9")

            if vidas == 3:
                print("Voy a ofrecerte una ayuda extra")
                if numero % 2 == 0:
                    print("El número es par")    #si le quedan 3 vidas le devuelve al usuario si es par o impar el numero a adivinar
                else:
                    print("El número es impar")

        if numentrada == numero:
            vidas += 1
            print("Numero correcto!")    #si antes de llegar a 0 vidas el usuario acierta pide una entrada para reintar o volver al menu
            menu=int(input("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: "))

        if vidas == 0:
            print("Lo siento! perdiste :(")
            print("El numero era", numero)   #si las vidas llegan a 0, pierde y pide una entrada para reintar o volver al menu
            menu=int(input("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: "))