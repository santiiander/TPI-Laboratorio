menu=2 #borrar esto al ingresarlo al master
while menu==2:
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
            rtaC1 = 10
            print("Su puntaje:", rtaC1, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC1 = 0
        print("----------segunda pregunta----------")
        print("¿Cuantas selecciones participan en un mundial de futbol?")
        print("1) 32 equipos")
        print("2) 36 equipos")
        print("3) 40 equipos")
        print("4) 42 equipos")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 1:
            print("respuesta correcta")
            rtaC2 = 10
            print("Su puntaje:", rtaC2, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC2 = 0
        print("----------tercer pregunta----------")
        print("¿Que selección es la que mas ha ganado la copa del mundo?")
        print("1) Italia")
        print("2) Francia")
        print("3) Brasil")
        print("4) Alemania")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 3:
            print("respuesta correcta")
            rtaC3 = 10
            print("Su puntaje:", rtaC3, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC3 = 0
        print("----------cuarta pregunta----------")
        print("¿Donde se disputo la copa del mundo 2006?")
        print("1) España")
        print("2) Sudafrica")
        print("3) Alemania")
        print("4) Japon/Corea del sur")
        rta = int(input("ingrese el numero de la opcion correcta"))

        if rta == 3:
            print("respuesta correcta")
            rtaC4 = 10
            print("Su puntaje:", rtaC4, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC4 = 0
        print("----------quinta pregunta----------")
        print("¿Qué animal fue el escogido para ilustrar la mascota del Mundial de Rusia?")
        print("1) Lobo")
        print("2) Perro")
        print("3) Gato")
        print("4) Loro")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 1:
            print("respuesta correcta")
            rtaC5 = 10
            print("Su puntaje:", rtaC5, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC5 = 0
        print("----------sexta pregunta----------")
        print("¿Cada cuantos años se realiza esta competición?")
        print("1) Cada 4 años")
        print("2) Cada 6 años")
        print("3) Cada 5 años")
        print("4) Cada 3 años")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 1:
            print("respuesta correcta")
            rtaC6 = 10
            print("Su puntaje:", rtaC6, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC6 = 0
        print("----------septima y ultima pregunta----------")
        print("¿Recuerdas dónde se jugó la Copa del Mundial del año 2010?")
        print("1) Italia")
        print("2) Sudafrica")
        print("3) Alemania")
        print("4) España")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 2:
            print("respuesta correcta")
            rtaC7 = 10
            print("Su puntaje:", rtaC7, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC7 = 0
        break
        rtaT = (rtaC1 + rtaC2 + rtaC3 + rtaC4 + rtaC5 + rtaC6 + rtaC7)
        print("hemos finalizado la trivia y su puntaje es de:", rtaT, "puntos")
        if rtaT == 70:
            print("llegaste al puntaje maximo, felicitaciones")
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
            rtaC1 = 10
            print("Su puntaje:", rtaC1, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC1 = 0
        print("----------segunda pregunta----------")
        print("¿Qué selección llegó a tres finales de la Copa del Mundo pero nunca ganó el título?")
        print("1) suiza")
        print("2) croacia")
        print("3) hungria")
        print("4) holanda")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 4:
            print("respuesta correcta")
            rtaC2 = 10
            print("Su puntaje:", rtaC2, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC2 = 0
        print("----------tercer pregunta----------")
        print("¿Que jugador de futbol es el maximo goleador de este torneo?")
        print("1) Klose")
        print("2) Pelé")
        print("3) Muller")
        print("4) Ronaldo Nazario")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 1:
            print("respuesta correcta")
            rtaC3 = 10
            print("Su puntaje:", rtaC3, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC3 = 0
        print("----------cuarta pregunta----------")
        print("“Tenía miedo de que se me cayera el trofeo”. ¿Qué ganador del mundial confesó esto?")
        print("1) Iniesta")
        print("2) Puyol")
        print("3) Maradona")
        print("4) Matthaus")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 4:
            print("respuesta correcta")
            rtaC4 = 10
            print("Su puntaje:", rtaC4, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC4 = 0
        print("----------quinta pregunta----------")
        print("¿Cuánto pesa el trofeo de la Copa del Mundo?")
        print("1) 2 kilos")
        print("2) 5 kilos")
        print("3) 6 kilos")
        print("4) 8 kilos")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 3:
            print("respuesta correcta")
            rtaC5 = 10
            print("Su puntaje:", rtaC5, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC5 = 0
        print("----------sexta pregunta----------")
        print("En el Mundial de México en 1986, el argentino Diego Maradona anotó un gol con la mano, que se convirtió en una leyenda en el fútbol y es conocido como “la mano de Dios”. ¿Contra qué equipo marcó ese famoso tanto?")
        print("1) Francia")
        print("2) Brasil")
        print("3) Alemania")
        print("4) Inglaterra")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 4:
            print("respuesta correcta")
            rtaC6 = 10
            print("Su puntaje:", rtaC6, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC6 = 0
        print("----------septima y ultima pregunta----------")
        print("¿Dónde se disputó la Copa Mundial de 1998?")
        print("1) Italia")
        print("2) Francia")
        print("3) Alemania")
        print("4) Japon")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 2:
            print("respuesta correcta")
            rtaC7 = 10
            print("Su puntaje:", rtaC7, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC7 = 0
        rtaT = (rtaC1 + rtaC2 + rtaC3 + rtaC4 + rtaC5 + rtaC6 + rtaC7)
        print("hemos finalizado la trivia y su puntaje es de:", rtaT, "puntos")
        if rtaT == 70:
            print("llegaste al puntaje maximo, felicitaciones")
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
            rtaC1 = 10
            print("Su puntaje:", rtaC1, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC1 = 0
        print("----------segunda pregunta----------")
        print("¿En que año se jugo la primera copa del  mundo?")
        print("1) 1938")
        print("2) 1926")
        print("3) 1942")
        print("4) 1930")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 4:
            print("respuesta correcta")
            rtaC2 = 10
            print("Su puntaje:", rtaC2, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC2 = 0
        print("----------tercer pregunta----------")
        print("Que selección ha disputado mas finales de esta competencia?")
        print("1) Holanda")
        print("2) Inglaterra")
        print("3) Alemania")
        print("4) Brasil")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 3:
            print("respuesta correcta")
            rtaC3 = 10
            print("Su puntaje:", rtaC3, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC3 = 0
        print("----------cuarta pregunta----------")
        print("Quien es el único jugador en obtener tres veces la copa del mundo?")
        print("1) Pelé")
        print("2) Cafú")
        print("3) Meazza")
        print("4) Maradona")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 1:
            print("respuesta correcta")
            rtaC4 = 10
            print("Su puntaje:", rtaC4, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC4 = 0
        print("----------quinta pregunta----------")
        print("Quien fue el jugador mas joven en ganar la copa del mundo?")
        print("1) Mbappe")
        print("2) Pelé")
        print("3) Whiteside")
        print("4) Opabunmi")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 2:
            print("respuesta correcta")
            rtaC5 = 10
            print("Su puntaje:", rtaC5, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC5 = 0
        print("----------sexta pregunta----------")
        print("Quien fue el jugador mas veterano en disputar una copa del mundo?")
        print("1) Peter Cech")
        print("2) Dino Soff")
        print("3) Essam-El-Hadary")
        print("4) Macdonald Taylor")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 3:
            print("respuesta correcta")
            rtaC6 = 10
            print("Su puntaje:", rtaC6, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC6 = 0
        print("----------septima pregunta----------")
        print("Cual de estas selecciones nunca disputador un mundial?")
        print("1) Finlandia")
        print("2) Israel")
        print("3) El Salvador")
        print("4) Nueva Zelanda")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 1:
            print("respuesta correcta")
            rtaC7 = 10
            print("Su puntaje:", rtaC7, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC7 = 0
        print("----------octava y ultima pregunta----------")
        print("¿Quien anoto el primer gol en la historia de los mundiales?")
        print("1) Laurent")
        print("2) Delfour")
        print("3) Petrone")
        print("4) Chividini")

        rta = int(input("ingrese el numero de la opcion correcta"))
        if rta == 1:
            print("respuesta correcta")
            rtaC8 = 10
            print("Su puntaje:", rtaC8, "puntos")
        else:
            print("respuesta incorrecta")
            rtaC8 = 0
        break
        rtaT = (rtaC1 + rtaC2 + rtaC3 + rtaC4 + rtaC5 + rtaC6 + rtaC7)
        print("hemos finalizado la trivia y su puntaje es de:", rtaT, "puntos")
        if rtaT == 70:
            print("llegaste al puntaje maximo, felicitaciones")