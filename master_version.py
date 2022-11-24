# VERSIÓN FINAL TPI LAB
import math
import random
import time
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

    while menu == 2:                          #mientras el usuario haya ingresado 2, se ejecuta el juego Trivia Sports Mundial con un bucle
        rtac = 0                               #se definde la variable rtac con valor 0
        print("Bienvenidos a Trivia Sports Mundial")                                           #muestra por pantalla al usuario la bienvenida a este juego
        print("¿Capaz de lograr el maximo puntaje? Elije tu dificultad. Cada respuesta correcta son 10 puntos...Comenzemos")
        print("Para dificultad Amateur ingrese 1")                                              #muestra por pantalla al usuario las diferentes dificultades de este juego
        print("Para dificultad Profesional ingrese 2")
        print("Para dificultad Legendario ingrese 3")
        dificultadjuego2 = int(input("ingrese el numero de la dificultad de la trivia"))        #permitimos al usuario ingresar la dificultad que quiera jugar
        while dificultadjuego2 == 1:                                                            #si el usuario ingresa 1 la dificultad sera amateur
            print("----------primera pregunta----------")
            print("La Copa del Mundo de 2026 se jugará en tres países diferentes. ¿Puedes elegir la opcion correcta?")
            print("1) argentina,brasil y chile")
            print("2) eeuu, mexico y canada")                                                   #mostramos en pantalla la pregunta correspondiente con sus respuestas a elegir
            print("3) italia, francia y españa")
            print("4) australia, nueva zelanda y fiji")

            rta = int(input("ingrese el numero de la opcion correcta"))            #permitimos al usuario ingresar numero de respuesta seleccionada
            if rta == 2:                                                     #si la respuesta es el valor de la variable rta se muestra por pantalla que fue la eleccion correcta
                print("respuesta correcta")
                rtac += 10                                                  #muestra por pantalla al usuario los puntajes obtenidos acumulandose por respuesta
                print("Su puntaje:", rtac, "puntos")
            else:                                                           #sino ingresa el valor de la variable rta muestra por pantalla que la eleccion fue incorrecta obteniendo 0 puntos
                print("respuesta incorrecta")
                rtac += 0
            print("----------segunda pregunta----------")
            print("¿Cuantas selecciones participan en un mundial de futbol?")
            print("1) 32 equipos")
            print("2) 36 equipos")
            print("3) 40 equipos")
            print("4) 42 equipos")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 1:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------tercer pregunta----------")
            print("¿Que selección es la que mas ha ganado la copa del mundo?")
            print("1) Italia")
            print("2) Francia")
            print("3) Brasil")
            print("4) Alemania")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 3:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------cuarta pregunta----------")
            print("¿Donde se disputo la copa del mundo 2006?")
            print("1) España")
            print("2) Sudafrica")
            print("3) Alemania")
            print("4) Japon/Corea del sur")
            rta = int(input("ingrese el numero de la opcion correcta"))

            if rta == 3:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------quinta pregunta----------")
            print("¿Qué animal fue el escogido para ilustrar la mascota del Mundial de Rusia?")
            print("1) Lobo")
            print("2) Perro")
            print("3) Gato")
            print("4) Loro")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 1:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------sexta pregunta----------")
            print("¿Cada cuantos años se realiza esta competición?")
            print("1) Cada 4 años")
            print("2) Cada 6 años")
            print("3) Cada 5 años")
            print("4) Cada 3 años")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 1:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------septima y ultima pregunta----------")
            print("¿Recuerdas dónde se jugó la Copa del Mundial del año 2010?")
            print("1) Italia")
            print("2) Sudafrica")
            print("3) Alemania")
            print("4) España")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 2:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("hemos finalizado la trivia y su puntaje es de:", rtac, "puntos") #muestra por pantalla la finalizacion del juego en esta dificultad
            if rtac == 70:                                                          #si acumunla 70 puntos le indica al usuario el puntaje maximo obtenido
                print("llegaste al puntaje maximo, felicitaciones")
            menu = int(input("presione 2 para volver a jugar o 0 para regresar al menu")) #permite al usuario ingresar el 2 para volver a jugar o para regresar al menu presionando 0
            break                                                                        #corta el bucle while


        while dificultadjuego2 == 2:
            print("----------primera pregunta----------")
            print("¿Que seleccion de futbol gano el primer mundial?")
            print("1) argentina")
            print("2) alemania")
            print("3) uruguay")
            print("4) italia")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 3:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------segunda pregunta----------")
            print("¿Qué selección llegó a tres finales de la Copa del Mundo pero nunca ganó el título?")
            print("1) suiza")
            print("2) croacia")
            print("3) hungria")
            print("4) holanda")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 4:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------tercer pregunta----------")
            print("¿Que jugador de futbol es el maximo goleador de este torneo?")
            print("1) Klose")
            print("2) Pelé")
            print("3) Muller")
            print("4) Ronaldo Nazario")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 1:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------cuarta pregunta----------")
            print("“Tenía miedo de que se me cayera el trofeo”. ¿Qué ganador del mundial confesó esto?")
            print("1) Iniesta")
            print("2) Puyol")
            print("3) Maradona")
            print("4) Matthaus")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 4:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------quinta pregunta----------")
            print("¿Cuánto pesa el trofeo de la Copa del Mundo?")
            print("1) 2 kilos")
            print("2) 5 kilos")
            print("3) 6 kilos")
            print("4) 8 kilos")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 3:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------sexta pregunta----------")
            print(
                "En el Mundial de México en 1986, el argentino Diego Maradona anotó un gol con la mano, que se convirtió en una leyenda en el fútbol y es conocido como “la mano de Dios”. ¿Contra qué equipo marcó ese famoso tanto?")
            print("1) Francia")
            print("2) Brasil")
            print("3) Alemania")
            print("4) Inglaterra")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 4:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------septima y ultima pregunta----------")
            print("¿Dónde se disputó la Copa Mundial de 1998?")
            print("1) Italia")
            print("2) Francia")
            print("3) Alemania")
            print("4) Japon")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 2:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("hemos finalizado la trivia y su puntaje es de:", rtac, "puntos")
            if rtac == 70:
                print("llegaste al puntaje maximo, felicitaciones")
            menu = int(input("presione 2 para volver a jugar o 0 para regresar al menu"))
            break

        while dificultadjuego2 == 3:
            print("----------primera pregunta----------")
            print("Que país ha participado mas veces en la copa del mundo?")
            print("1) Argentina")
            print("2) Brasil")
            print("3) Alemania")
            print("4) Francia")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 2:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------segunda pregunta----------")
            print("¿En que año se jugo la primera copa del  mundo?")
            print("1) 1938")
            print("2) 1926")
            print("3) 1942")
            print("4) 1930")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 4:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------tercer pregunta----------")
            print("Que selección ha disputado mas finales de esta competencia?")
            print("1) Holanda")
            print("2) Inglaterra")
            print("3) Alemania")
            print("4) Brasil")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 3:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------cuarta pregunta----------")
            print("Quien es el único jugador en obtener tres veces la copa del mundo?")
            print("1) Pelé")
            print("2) Cafú")
            print("3) Meazza")
            print("4) Maradona")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 1:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------quinta pregunta----------")
            print("Quien fue el jugador mas joven en ganar la copa del mundo?")
            print("1) Mbappe")
            print("2) Pelé")
            print("3) Whiteside")
            print("4) Opabunmi")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 2:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------sexta pregunta----------")
            print("Quien fue el jugador mas veterano en disputar una copa del mundo?")
            print("1) Peter Cech")
            print("2) Dino Soff")
            print("3) Essam-El-Hadary")
            print("4) Macdonald Taylor")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 3:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------septima pregunta----------")
            print("Cual de estas selecciones nunca disputador un mundial?")
            print("1) Finlandia")
            print("2) Israel")
            print("3) El Salvador")
            print("4) Nueva Zelanda")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 1:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("----------octava y ultima pregunta----------")
            print("¿Quien anoto el primer gol en la historia de los mundiales?")
            print("1) Laurent")
            print("2) Delfour")
            print("3) Petrone")
            print("4) Chividini")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 1:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
                print("respuesta incorrecta")
                rtac += 0
            print("hemos finalizado la trivia y su puntaje es de:", rtac, "puntos")
            if rtac == 80:
                print("llegaste al puntaje maximo, felicitaciones")
            menu = int(input("presione 2 para volver a jugar o 0 para regresar al menu"))
            break

    while menu == 3:
        def nometal():                                       #funsion que es llamada dependiendo del elemento
            print("es un no metal")


        def metal():                                        #funsion que es llamada dependiendo del elemento
            print("es un metal")


        def semimetal():                                    #funsion que es llamada dependiendo del elemento
            print("es un semi metal")


        def desconocido():                                 #funsion que es llamada dependiendo del elemento
            print("su capacidad de conduccion electrica es aun desconocida")


        def intentos(atomo):
            vidas = 3                                              #al iniciar la funcion se definen las vidas
            guess = str.lower(input())
            if guess == atomo:
                print("¡CORRECTO!")                                #si el valor insertado corresponde con la variable se da por finalizado el intento
                return                                             #termina la funcion y se lo envia al proximo input
            elif guess != atomo:                                   #si no corresponde con el valor de la variable se inicia la segunda pista y se resta una vida
                vidas = vidas - 1
                if 0 < element < 5 or 10 < element < 13 or 18 < element < 21 or 36 < element < 39 or 54 < element < 57 or 86 < element < 89:
                    print("se encuentra en el bloque S")           #dependiendo del rango del numero en correspondiente al atomo en cuestion se le asigna una pista
                if 4 < element < 11 or 12 < element < 19 or 30 < element < 37 or 48 < element < 55 or 80 < element < 87 or 112 < element < 119:
                    print("se encuentra en el bloque P")
                if 20 < element < 31 or 38 < element < 49 or 70 < element < 81 or 103 < element < 113:
                    print("se encuentra en el bloque D")
                if 56 < element < 71 or 88 < element < 103:
                    print("se encuentra en el bloque F")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str.lower(input())
                if vidas > 0:
                    if guess != atomo:                   #al llegar a la ultima vida se da la ultima pista basada en el numero correspondiente al atomo en cuestion
                        print("su cantidad de electrones es de:", element)
                if guess == atomo:
                    print("¡CORRECTO!")      #si es correcto finaliza la funcion y salta al proximo input
                    break
                if vidas == 0:              #si se llega a 0 vidas la funcion finaliza y salta al proximo input
                    print("te quedaste sin intentos, a estudiar")
                    break


        print(
            "usted debera adivinar de que elemento se trata usando los datos que se iran otorgando por cada intento hasta un maximo de 3")
        vidas = 3
        element = random.randint(1, 118)          #se define el elemento mediante un numero al azar
        if element == 1:
            atomo = "hidrogeno"                   #cada elemento llama a su funcion correspondiente y se le asigna su nombre a la variable atomo
            nometal(), intentos(atomo)
        if element == 2:
            atomo = "helio"
            nometal(), intentos(atomo)
        if element == 3:
            atomo = "litio"
            metal(), intentos(atomo)
        if element == 4:
            atomo = "berilio"
            metal(), intentos(atomo)
        if element == 5:
            atomo = "boro"
            semimetal(), intentos(atomo)
        if element == 6:
            atomo = "carbono"
            nometal(), intentos(atomo)
        if element == 7:
            atomo = "nitrogeno"
            nometal(), intentos(atomo)
        if element == 8:
            atomo = "oxigeno"
            nometal(), intentos(atomo)
        if element == 9:
            atomo = "fluor"
            nometal(), intentos(atomo)
        if element == 10:
            atomo = "neon"
            nometal(), intentos(atomo)
        if element == 11:
            atomo = "sodio"
            metal(), intentos(atomo)
        if element == 12:
            atomo = "magnesio"
            metal(), intentos(atomo)
        if element == 13:
            atomo = "aluminio"
            metal(), intentos(atomo)
        if element == 14:
            atomo = ("silicio")
            semimetal(), intentos(atomo)
        if element == 15:
            atomo = ("fosforo")
            nometal(), intentos(atomo)
        if element == 16:
            atomo = ("azufre")
            nometal(), intentos(atomo)
        if element == 17:
            atomo = ("cloro")
            nometal(), intentos(atomo)
        if element == 18:
            atomo = ("argon")
            nometal(), intentos(atomo)
        if element == 19:
            atomo = ("potasio")
            metal(), intentos(atomo)
        if element == 20:
            atomo = ("calcio")
            metal(), intentos(atomo)
        if element == 21:
            atomo = ("escandio")
            metal(), intentos(atomo)
        if element == 22:
            atomo = ("titanio")
            metal(), intentos(atomo)
        if element == 23:
            atomo = ("vanadio")
            metal(), intentos(atomo)
        if element == 24:
            atomo = ("cromo")
            metal(), intentos(atomo)
        if element == 25:
            atomo = ("manganeso")
            metal(), intentos(atomo)
        if element == 26:
            atomo = ("hierro")
            metal(), intentos(atomo)
        if element == 27:
            atomo = ("cobalto")
            metal(), intentos(atomo)
        if element == 28:
            atomo = ("niquel")
            metal(), intentos(atomo)
        if element == 29:
            atomo = ("cobre")
            metal(), intentos(atomo)
        if element == 30:
            metal = ("zinc")
            nometal(), intentos(atomo)
        if element == 31:
            atomo = ("galio")
            metal(), intentos(atomo)
        if element == 32:
            atomo = ("germanio")
            semimetal(), intentos(atomo)
        if element == 33:
            atomo = ("arsenico")
            semimetal(), intentos(atomo)
        if element == 34:
            atomo = ("selenio")
            nometal(), intentos(atomo)
        if element == 35:
            atomo = ("bromo")
            nometal(), intentos(atomo)
        if element == 36:
            atomo = ("kripton")
            nometal(), intentos(atomo)
        if element == 37:
            atomo = ("rubidio")
            metal(), intentos(atomo)
        if element == 38:
            atomo = ("estroncio")
            metal(), intentos(atomo)
        if element == 39:
            atomo = ("itrio")
            metal(), intentos(atomo)
        if element == 40:
            atomo = ("circonio")
            metal(), intentos(atomo)
        if element == 41:
            atomo = ("niobio")
            metal(), intentos(atomo)
        if element == 42:
            atomo = ("molibdeno")
            metal(), intentos(atomo)
        if element == 43:
            atomo = ("tecnecio")
            metal(), intentos(atomo)
        if element == 44:
            atomo = ("rutenio")
            metal(), intentos(atomo)
        if element == 45:
            atomo = ("rodio")
            metal(), intentos(atomo)
        if element == 46:
            atomo = ("paladio")
            metal(), intentos(atomo)
        if element == 47:
            atomo = ("plata")
            metal(), intentos(atomo)
        if element == 48:
            atomo = ("cadmio")
            metal(), intentos(atomo)
        if element == 49:
            atomo = ("indio")
            metal(), intentos(atomo)
        if element == 50:
            atomo = ("estaño")
            metal(), intentos(atomo)
        if element == 51:
            atomo = ("antimonio")
            semimetal(), intentos(atomo)
        if element == 52:
            atomo = ("telurio")
            semimetal(), intentos(atomo)
        if element == 53:
            atomo = ("yodo")
            nometal(), intentos(atomo)
        if element == 54:
            atomo = ("xenon")
            nometal(), intentos(atomo)
        if element == 55:
            atomo = ("cesio")
            metal(), intentos(atomo)
        if element == 56:
            atomo = ("bario")
            metal(), intentos(atomo)
        if element == 57:
            atomo = ("lantano")
            metal(), intentos(atomo)
        if element == 58:
            atomo = ("cerio")
            metal(), intentos(atomo)
        if element == 59:
            atomo = ("praseodimio")
            metal(), intentos(atomo)
        if element == 60:
            atomo = ("neodimio")
            metal(), intentos(atomo)
        if element == 61:
            atomo = ("prometio")
            metal(), intentos(atomo)
        if element == 62:
            atomo = ("samario")
            metal(), intentos(atomo)
        if element == 63:
            atomo = ("europio")
            metal(), intentos(atomo)
        if element == 64:
            atomo = ("gadolinio")
            metal(), intentos(atomo)
        if element == 65:
            atomo = ("terbio")
            metal(), intentos(atomo)
        if element == 66:
            atomo = ("disprosio")
            metal(), intentos(atomo)
        if element == 67:
            atomo = ("holmio")
            metal(), intentos(atomo)
        if element == 68:
            atomo = ("erbio")
            metal(), intentos(atomo)
        if element == 69:
            atomo = ("tulio")
            metal(), intentos(atomo)
        if element == 70:
            atomo = ("iterbio")
            metal(), intentos(atomo)
        if element == 71:
            atomo = ("lutecio")
            metal(), intentos(atomo)
        if element == 72:
            atomo = ("hafnio")
            metal(), intentos(atomo)
        if element == 73:
            atomo = ("tantalo")
            metal(), intentos(atomo)
        if element == 74:
            atomo = ("wolframio")
            metal(), intentos(atomo)
        if element == 75:
            atomo = ("renio")
            metal(), intentos(atomo)
        if element == 76:
            atomo = ("osmio")
            metal(), intentos(atomo)
        if element == 77:
            atomo = ("iridio")
            metal(), intentos(atomo)
        if element == 78:
            atomo = ("platino")
            metal(), intentos(atomo)
        if element == 79:
            atomo = ("oro")
            metal(), intentos(atomo)
        if element == 80:
            atomo = ("mercurio")
            metal(), intentos(atomo)
        if element == 81:
            atomo = ("talio")
            metal(), intentos(atomo)
        if element == 82:
            atomo = ("plomo")
            metal(), intentos(atomo)
        if element == 83:
            atomo = ("bismuto")
            metal(), intentos(atomo)
        if element == 84:
            atomo = ("polonio")
            metal(), intentos(atomo)
        if element == 85:
            atomo = ("astato")
            semimetal(), intentos(atomo)
        if element == 86:
            atomo = ("radon")
            nometal(), intentos(atomo)
        if element == 87:
            atomo = ("francio")
            metal(), intentos(atomo)
        if element == 88:
            atomo = ("radio")
            metal(), intentos(atomo)
        if element == 89:
            atomo = ("actinio")
            metal(), intentos(atomo)
        if element == 90:
            atomo = ("torio")
            metal(), intentos(atomo)
        if element == 91:
            atomo = ("protactinio")
            metal(), intentos(atomo)
        if element == 92:
            atomo = ("uranio")
            metal(), intentos(atomo)
        if element == 93:
            atomo = ("neptunio")
            metal(), intentos(atomo)
        if element == 94:
            atomo = ("plutonio")
            metal(), intentos(atomo)
        if element == 95:
            atomo = ("americio")
            metal(), intentos(atomo)
        if element == 96:
            atomo = ("curio")
            metal(), intentos(atomo)
        if element == 97:
            atomo = ("berkelio")
            metal(), intentos(atomo)
        if element == 98:
            atomo = ("californio")
            metal(), intentos(atomo)
        if element == 99:
            atomo = ("einstenio")
            metal(), intentos(atomo)
        if element == 100:
            atomo = ("fermio")
            metal(), intentos(atomo)
        if element == 101:
            atomo = ("mendelevio")
            metal(), intentos(atomo)
        if element == 102:
            atomo = ("nobelio")
            metal(), intentos(atomo)
        if element == 103:
            atomo = ("lawrencio")
            metal(), intentos(atomo)
        if element == 104:
            atomo = ("rutherfordio")
            metal(), intentos(atomo)
        if element == 105:
            atomo = ("dubnio")
            metal(), intentos(atomo)
        if element == 106:
            atomo = ("seaborgio")
            metal(), intentos(atomo)
        if element == 107:
            atomo = ("bohrio")
            metal(), intentos(atomo)
        if element == 108:
            atomo = ("hasio")
            metal(), intentos(atomo)
        if element == 109:
            atomo = ("meitnerio")
            desconocido(), intentos(atomo)
        if element == 110:
            atomo = ("darmstatio")
            desconocido(), intentos(atomo)
        if element == 111:
            atomo = ("roentgenio")
            desconocido(), intentos(atomo)
        if element == 112:
            atomo = ("copernicio")
            desconocido(), intentos(atomo)
        if element == 113:
            atomo = ("nihonio")
            desconocido(), intentos(atomo)
        if element == 114:
            atomo = ("flerevio")
            desconocido(), intentos(atomo)
        if element == 115:
            atomo = ("moscovio")
            desconocido(), intentos(atomo)
        if element == 116:
            atomo = ("livermorio")
            desconocido(), intentos(atomo)
        if element == 117:
            atomo = ("teneso")
            desconocido(), intentos(atomo)
        if element == 118:
            atomo = ("organeson")
            desconocido(), intentos(atomo)
        menu = int(input("si desea jugar de nuevo presione 3, si quiere volver al menu presione 0"))   #pregunta si el usario desea reintentar o volver al menu


    while menu == 4:
        def ver_dragon(): #definimos la forma del dragón
            print("                                   HP:", hpdrake, "                          ")
            print("                         ⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⡞⡀⣤⣬⣴⠀⠀⢳⣶⣶⣤⣄⡀                        ")
            print("                            ⣠⣾⣿⣿⣿⣿⡇⠀⢸⣿⠿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣷⣦.                      ")
            print("                         ⢠⡾⣫⣿⣻⣿⣽⣿⡇⠀⠈⢿⣧⡝⠟⠀⠀⢸⣿⣿⣿⣿⣿⣟⢷⣄                     ")
            print("                       ⠀⢠⣯⡾⢿⣿⣿⡿⣿⣿⣿⣆⣠⣶⣿⣿⣷⣄⣰⣿⣿⣿⣿⣿⣿⣿⢷⣽⣄⠀                  ")
            print("                       ⢠⣿⢋⠴⠋⣽⠋⡸⢱⣯⡿⣿⠏⣡⣿⣽⡏⠹⣿⣿⣿⡎⢣⠙⢿⡙⠳⡙⢿⠄                  ")
            print("                        ⣰⢣⣃⠀⠊⠀⠀⠁⠘⠏⠁⠁⠸⣶⣿⡿⢿⡄⠈⠀⠁⠃⠈⠂⠀⠑⠠⣈⡈⣧                  ")
            print("                        ⡏⡘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡥⢄⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⢸                      ")
            print("                         ⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⣸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢨                      ")
            print("                                  ⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠈                       ")
            print("                                ⠀⠀⠀⠀⠀ ⡳⣶⣄. ")


        def ver_caballero(): #definimos la forma del caballero
            print("                               Tu HP: ", hpplayer, "                       ")
            print("                              _   _   _   _+       |                     ")
            print("                             /_`-'_`-'_`-'_|  \+/  |                     ")
            print("                             \_`M'_`D'_`C'_| _<=>_ |                     ")
            print("                               `-' `-' `-' 0/ \ / o=o                    ")
            print("                                           \/\ ^ /`0                     ")
            print("                                           | /_^_\                       ")
            print("                                           | || ||                       ")
            print("                                         __|_d|_|b__                     ")


        print("Hoy vamos a entra en los zapatos de un caballero de la historia media,")
        print("El caballero debe derrotar a un dragón para la protección de su reino ")
        player = input(str("Con quien me complace la aventura de hoy: ")) #preguntamos el nombre del jugador
        print("Bienvenido jugador ", player)
        dificultadjuego4 = int(
            input("Ingrese en la dificultad que desea jugar\n(1)fácil\n(2)normal\n(3)difícil\ndificultad:")) #preguntar qué dificultad desea jugar

        if dificultadjuego4 == 1: #los niveles de dificultad
            hpdrake = 5000
            hpplayer = 1000
            print("Jugarás en dificultad Fácil")
        elif dificultadjuego4 == 2: #los niveles de dificultad
            hpdrake = 50000
            hpplayer = 10000
            print("Jugarás en dificultad Normal")
        elif dificultadjuego4 == 3: #los niveles de dificultad con condiciones especiales
            hpdrake = 500000
            hpplayer = 100000
            print("Jugarás en dificultad Difícil")

        print(ver_dragon()) # muestra la imagen del dragón
        print("has encontrado al dragón que acababa de despertar de su sueño ")
        print("cuidado soldado usted solo posee 3 pociones")

        pociones = 3
        time.sleep(5)
        while True:
            critico = random.randint(1, 10)
            golpedragon = random.randint(1, 3)

            if dificultadjuego4 == 1: #mas condiciones que tiene cada dificultad
                curacion = 200
                dmg = random.randint(250, 500)
                dmgdrake = random.randint(100, 200)
                if critico == 2:
                    dmg *= 2
                    print("Has logrado hacer un golpe crítico!")
            elif dificultadjuego4 == 2: #mas condiciones que tiene cada dificultad
                curacion = 1000
                dmg = random.randint(2500, 5000)
                dmgdrake = random.randint(1000, 2000)
                if critico == 5:
                    dmg *= 2
                    print("Has logrado hacer un golpe crítico!")
            elif dificultadjuego4 == 3: #mas condiciones que tiene cada dificultad
                curacion = 5000
                dmg = random.randint(25000, 50000)
                dmgdrake = random.randint(10000, 20000)
                if critico == 8:
                    dmg *= 2
                    print("Has logrado hacer un golpe crítico!")

            if pociones > 0:
                accion = int(input("1) Atacar, (2)curar"))
                if accion == 1: # el sistema de combate que tienes tu, con curación
                    hpdrake -= dmg
                    print("Atacas al dragón")
                    print(ver_dragon())
                if accion == 2:
                    pociones -= 1
                    hpplayer += curacion
                    print("usted se curó")
                    print(ver_caballero())
            else:
                accion = int(input("1) Atacar")) #el sistema de combate si te quedas sin la condición de curación
                if accion == 1:
                    hpdrake -= dmg
                    print("Atacas al dragón")
                    print(ver_dragon())
            time.sleep(2)
            if golpedragon == 1 or golpedragon == 3:
                hpplayer -= dmgdrake
                print("El dragón te atacó")  #el sistema de combate que tienes el dragón
            print(ver_caballero())
            if hpdrake <= 0 and hpplayer <= 0:
                print("ha sido un empate")
                print("Puedes reintentar ingresando 4, o volver al menú de juegos con 0: ") #volver a jugar el programa o seleccionar otro juego
                menu = int(input())
                break

            if hpdrake <= 0:
                print("Felizidades ", player, " has logrado derrotar al dragón!")
                print(
                    "Puedes reintentar ingresando 4, o volver al menú de juegos con 0: ")  # volver a jugar el programa o seleccionar otro juego
                print(
                    "Caballero....En un mundo donde un dragón antiguo está sembrando el caos por donde pase, existe un soldado/a bien formado")
                print(
                    "con un pelo negro como la oscuridad y unos ojos de color cabe claros que demuestras la fuerza que contiene su alma nacido")
                print(
                    "en una familia comun con una aspiración de ser el primer caballero de su reino en derrotar a un monstruo que atente con ")
                print(
                    "el reino en el que reside, con un ímpetu inquebrantable , una determinación infinita y los más importante mucho valor ")
                print("para enfrentar el caos que causa el dragón")
                menu = int(input())
                break

            if hpplayer <= 0:
                print("No has logrado vencer al dragón! Suerte a la próxima")
                print(
                    "Puedes reintentar ingresando 4, o volver al menú de juegos con 0: ")  # volver a jugar el programa o seleccionar otro juego
                print(
                    "Dragon... Uno de los monstruos más temidos en el mundo nacido del odio a los seres vivos con hambre de destrucción y muerte ")
                print(
                    "un dragon negro con escamas que parecen hojas afiladas y unas apariencia que parece muerto, con unas alas destruidas y un ")
                print(
                    "cuerpo completamente lasitmado una bestia con mas de 5000 años que a despertado de sus 1000 años de sueño, para volver a causar ")
                print(
                    "desesperacion y terror en el mundo como lo conoce acabando con todo lo que pueda ver a su paso sin una gota de compasión por todo en el mundo")
                menu = int(input())
                break

    if menu == 5:
        print("Gracias por jugar!") #fin del juego
        break