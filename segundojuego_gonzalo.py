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
        seleccion1 = str("Klose")
        seleccion2 = str("Pelé")
        seleccion3 = str("Muller")
        seleccion4 = str("Ronaldo Nazario")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Iniesta")
        seleccion2 = str("Puyol")
        seleccion3 = str("Maradona")
        seleccion4 = str("Matthaus")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("2 kilos")
        seleccion2 = str("5 kilos")
        seleccion3 = str("6 kilos")
        seleccion4 = str("8 kilos")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Francia")
        seleccion2 = str("Brasil")
        seleccion3 = str("Alemania")
        seleccion4 = str("Inglaterra")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Italia")
        seleccion2 = str("Francia")
        seleccion3 = str("Alemania")
        seleccion4 = str("Japon")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Argentina")
        seleccion2 = str("Brasil")
        seleccion3 = str("Alemania")
        seleccion4 = str("Francia")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("1938")
        seleccion2 = str("1926")
        seleccion3 = str("1942")
        seleccion4 = str("1930")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Holanda")
        seleccion2 = str("Inglaterra")
        seleccion3 = str("Alemania")
        seleccion4 = str("Brasil")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Pelé")
        seleccion2 = str("Cafú")
        seleccion3 = str("Meazza")
        seleccion4 = str("Maradona")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Mbappe")
        seleccion2 = str("Pelé")
        seleccion3 = str("Whiteside")
        seleccion4 = str("Opabunmi")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Peter Cech")
        seleccion2 = str("Dino Soff")
        seleccion3 = str("Essam-El-Hadary")
        seleccion4 = str("Macdonald Taylor")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Finlandia")
        seleccion2 = str("Israel")
        seleccion3 = str("El Salvador")
        seleccion4 = str("Nueva Zelanda")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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
        seleccion1 = str("Laurent")
        seleccion2 = str("Delfour")
        seleccion3 = str("Petrone")
        seleccion4 = str("Chividini")
        print("1", seleccion1)
        print("2", seleccion2)
        print("3", seleccion3)
        print("4", seleccion4)
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






