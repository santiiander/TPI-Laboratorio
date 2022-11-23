# VERSIÓN FINAL TPI LAB
import math
import random
while True:
    menu = 0
    while menu == 0:
        print("Hola!, Bienvenido al algoritmo de Play.In, desarrollado para aprender jugando")
        print("Por favor, seleccione el número correspondiente al juego o actividad")
        print("1) Adivina el numero")
        print("2) Trivia Sports Mundial")
        print("3) Tabla Periodica Quizz")
        print("4) Medieval History")
        print("5) Salir")
        menu = int(input())

    while menu == 1:
        print("Bienvenido a Adivina el número")
        dificultadjuego1 = int(input("Por favor, ingrese la dificultad del juego, sea 1, 2 o 3: "))

        if dificultadjuego1 == 1:
            vidas = 6
        elif dificultadjuego1 == 2:
            vidas = 5
        elif dificultadjuego1 == 3:
            vidas = 4
        else:
            while dificultadjuego1 != 1 and dificultadjuego1 != 2 and dificultadjuego1 != 3:
                dificultadjuego1 = int(input("Por favor, ingrese la dificultad del juego, sea 1, 2 o 3: "))

        print("Tendrás que adivinar el numero generado aleatoriamente, o ingresado por el usuario ")

        inputnumero = int(input("Por favor, ingrese 1 si desea que el numero sea aleatorio, 0 si desea ingresarlo "))

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
            print("\n" * 15)
            while dificultadjuego1 == 1 and numero > 100:
                print("La dificultad fue seteada en nivel 1, el numero no puede superar el 100: ")
                numero = int(input("El numero será elegido por el otro jugador: "))
                print("\n" * 10)
            while dificultadjuego1 == 2 and 100 > numero < 500:
                print("La dificultad fue seteada en nivel 2, el numero no puede ser menor que 100 ni mayor que 500: ")
                numero = int(input("El numero será elegido por el otro jugador: "))
                print("\n" * 10)
            while dificultadjuego1 == 3 and 500 > numero < 1000:
                print("La dificultad fue seteada en nivel 3, el numero no puede ser menor que 100 ni mayor que 1000: ")
                numero = int(input("El numero será elegido por el otro jugador: "))
                print("\n" * 10)

        if numero > 0:
            digits = int(math.log10(numero)) + 1
            print("El numero tiene", digits, "digitos!")
        else:
            if numero == 0:
                digits = 1
                print("El numero tiene", digits, "digitos!")

        primerdigito = int(str(numero)[0])

        numentrada = int(input("Intentemoslo!\n"))

        while vidas > 0 and numero != numentrada:
            numentrada = int(input("Oh, una vida menos :( , prueba de nuevo\n"))
            vidas -= 1

            if vidas == 2 and digits > 1:
                print("Veo que ya solo te quedan 2 intentos D:")
                print("Voy a darte una pista mas...")
                print("El numero empieza con", primerdigito)

            if vidas == 2 and digits == 1:
                print("Lo siento, no puedo revelarte la cantidad de digitos")
                print("Pero puedo decirte que tu numero se encuentra entre el 0 y el 9")

            if vidas == 3:
                print("Voy a ofrecerte una ayuda extra")
                if numero % 2 == 0:
                    print("El número es par")
                else:
                    print("El número es impar")

        if numentrada == numero:
            vidas += 1
            print("Numero correcto!")
            menu=int(input("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: "))

        if vidas == 0:
            print("Lo siento! perdiste :(")
            print("El numero era", numero)
            menu=int(input("Puedes reintentar ingresando 1, o volver al menú de juegos con 0: "))

    while menu == 2:
        rtac = 0
        print("Bienvenidos a Trivia Sports Mundial")
        print("¿Capaz de lograr el maximo puntaje? Elije tu dificultad. Cada respuesta correcta son 10 puntos...Comenzemos")
        print("Para dificultad Amateur ingrese 1")
        print("Para dificultad Profesional ingrese 2")
        print("Para dificultad Legendario ingrese 3")
        dificultadjuego2 = int(input("ingrese el numero de la dificultad de la trivia"))
        while dificultadjuego2 == 1:
            print("----------primera pregunta----------")
            print("La Copa del Mundo de 2026 se jugará en tres países diferentes. ¿Puedes elegir la opcion correcta?")
            print("1) argentina,brasil y chile")
            print("2) eeuu, mexico y canada")
            print("3) italia, francia y españa")
            print("4) australia, nueva zelanda y fiji")

            rta = int(input("ingrese el numero de la opcion correcta"))
            if rta == 2:
                print("respuesta correcta")
                rtac += 10
                print("Su puntaje:", rtac, "puntos")
            else:
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
            print("hemos finalizado la trivia y su puntaje es de:", rtac, "puntos")
            if rtac == 70:
                print("llegaste al puntaje maximo, felicitaciones")
            menu = int(input("presione 2 para volver a jugar o 0 para regresar al menu"))

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

    while menu == 3:
        def nometal():
            print("es un no metal")


        def metal():
            print("es un metal")


        def semimetal():
            print("es un semi metal")


        def desconocido():
            print("su capacidad de conduccion electrica es aun desconocida")


        def intentos(atomo):
            vidas = 3
            guess = str.lower(input())
            if guess == atomo:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != atomo:
                vidas = vidas - 1
                if 0 < element < 5 or 10 < element < 13 or 18 < element < 21 or 36 < element < 39 or 54 < element < 57 or 86 < element < 89:
                    print("se encuentra en el bloque S")
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
                    if guess != atomo:
                        print("su cantidad de electrones es de:", element)
                if guess == atomo:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    menu = int(input())


        print(
            "usted debera adivinar de que elemento se trata usando los datos que se iran otorgando por cada intento hasta un maximo de 3")
        vidas = 3
        element = random.randint(1, 118)
        if element == 1:
            atomo = "hidrogeno"
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

    while menu == 5:
        print("Gracias por jugar!")
        break