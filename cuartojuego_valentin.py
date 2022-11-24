import random
import time

menu=4
while menu==4:
    def ver_dragon():  # definimos la forma del dragón
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


    def ver_caballero():  # definimos la forma del caballero
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
    player = input(str("Con quien me complace la aventura de hoy: "))  # preguntamos el nombre del jugador
    print("Bienvenido jugador ", player)
    dificultadjuego4 = int(
        input(
            "Ingrese en la dificultad que desea jugar\n(1)fácil\n(2)normal\n(3)difícil\ndificultad:"))  # preguntar qué dificultad desea jugar

    if dificultadjuego4 == 1:  # los niveles de dificultad
        hpdrake = 5000
        hpplayer = 1000
        print("Jugarás en dificultad Fácil")
    elif dificultadjuego4 == 2:  # los niveles de dificultad
        hpdrake = 50000
        hpplayer = 10000
        print("Jugarás en dificultad Normal")
    elif dificultadjuego4 == 3:  # los niveles de dificultad con condiciones especiales
        hpdrake = 500000
        hpplayer = 100000
        print("Jugarás en dificultad Difícil")

    print(ver_dragon())  # muestra la imagen del dragón
    print("has encontrado al dragón que acababa de despertar de su sueño ")
    print("cuidado soldado usted solo posee 3 pociones")

    pociones = 3
    time.sleep(5)
    while True:
        critico = random.randint(1, 10)
        golpedragon = random.randint(1, 3)

        if dificultadjuego4 == 1:  # mas condiciones que tiene cada dificultad
            curacion = 200
            dmg = random.randint(250, 500)
            dmgdrake = random.randint(100, 200)
            if critico == 2:
                dmg *= 2
                print("Has logrado hacer un golpe crítico!")
        elif dificultadjuego4 == 2:  # mas condiciones que tiene cada dificultad
            curacion = 1000
            dmg = random.randint(2500, 5000)
            dmgdrake = random.randint(1000, 2000)
            if critico == 5:
                dmg *= 2
                print("Has logrado hacer un golpe crítico!")
        elif dificultadjuego4 == 3:  # mas condiciones que tiene cada dificultad
            curacion = 5000
            dmg = random.randint(25000, 50000)
            dmgdrake = random.randint(10000, 20000)
            if critico == 8:
                dmg *= 2
                print("Has logrado hacer un golpe crítico!")

        if pociones > 0:
            accion = int(input("1) Atacar, (2)curar"))
            if accion == 1:  #el sistema de combate que tienes tu, con curación
                hpdrake -= dmg
                print("Atacas al dragón")
                print(ver_dragon())
            if accion == 2:
                pociones -= 1
                hpplayer += curacion
                print("usted se curó")
                print(ver_caballero())
        else:
            accion = int(input("1) Atacar"))  #el sistema de combate si te quedas sin la condición de curación
            if accion == 1:
                hpdrake -= dmg
                print("Atacas al dragón")
                print(ver_dragon())
        time.sleep(2)
        if golpedragon == 1 or golpedragon == 3:
            hpplayer -= dmgdrake
            print("El dragón te atacó")  # el sistema de combate que tienes el dragón
        print(ver_caballero())
        if hpdrake <= 0 and hpplayer <= 0:
            print("ha sido un empate")
            print(
                "Puedes reintentar ingresando 4, o volver al menú de juegos con 0: ")  # volver a jugar el programa o seleccionar otro juego
            menu = int(input())
            break

        if hpdrake <= 0:
            print("Felizidades ", player, " has logrado derrotar al dragón!")
            print(
                "Puedes reintentar ingresando 4, o volver al menú de juegos con 0: ")  # volver a jugar el programa o seleccionar otro juego
            menu = int(input())
            break

        if hpplayer <= 0:
            print("No has logrado vencer al dragón! Suerte a la próxima")
            print(
                "Puedes reintentar ingresando 4, o volver al menú de juegos con 0: ")  # volver a jugar el programa o seleccionar otro juego
            menu = int(input())
            break