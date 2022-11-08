print("Bienvenidos a Trivia Sports")
print("¿Capaz de lograr el maximo puntaje? Cada respuesta correcta son 10 puntos...Comenzemos")
print("----------primera pregunta----------")
print("¿Que seleccion de futbol gano el primer mundial en 1930?")
seleccion1 = str("argentina")
seleccion2 = str("alemania")
seleccion3 = str("uruguay")
seleccion4 = str("italia")
print("1", seleccion1)
print("2", seleccion2)
print("3", seleccion3)
print("4", seleccion4)
rta = int(input("ingrese el numero de la opcion correcta"))
if rta == 3:
    print("respuesta correcta")
    rtaC1 = 10
    print("Su puntaje:",rtaC1,"puntos")
else:
    print("respuesta incorrecta")
    rtaC1 = 0
print("----------segunda pregunta----------")
print("La Copa del Mundo de 2026 se jugará en tres países diferentes. ¿Puedes elegir la opcion correcta?")
seleccion1 = str("argentina,brasil y chile")
seleccion2 = str("eeuu, mexico y canada")
seleccion3 = str("italia, francia y españa")
seleccion4 = str("australia, nueva zelanda y fiji")
print("1", seleccion1)
print("2", seleccion2)
print("3", seleccion3)
print("4", seleccion4)
rta = int(input("ingrese el numero de la opcion correcta"))
if rta == 2:
    print("respuesta correcta")
    rtaC2 = 10
    print("Su puntaje:",rtaC2,"puntos")
else:
    print("respuesta incorrecta")
    rtaC2 = 0
print("----------tercera pregunta----------")
print("¿Qué selección llegó a tres finales de la Copa del Mundo pero nunca ganó el título?")
seleccion1 = str("suiza")
seleccion2 = str("croacia")
seleccion3 = str("hungria")
seleccion4 = str("holanda")
print("1", seleccion1)
print("2", seleccion2)
print("3", seleccion3)
print("4", seleccion4)
rta = int(input("ingrese el numero de la opcion correcta"))
if rta == 4:
    print("respuesta correcta")
    rtaC3 = 10
    print("Su puntaje:",rtaC3,"puntos")
else:
    print("respuesta incorrecta")
    rtaC3 = 0
rtaT = (rtaC1+rtaC2+rtaC3)
print("hemos finalizado la trivia y su puntaje es de:" ,rtaT, "puntos")
if rtaT == 30:
    print("llegaste al puntaje maximo, felicitaciones")
