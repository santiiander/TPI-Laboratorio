import random
menu=3
while menu == 3:
        print("usted debera adivinar de que elemento se trata usando los datos que se iran otorgando por cada intento hasta un maximo de 3")
        element = random.randint(1, 1)
        vidas=3
        while element == 1:
            element = "hidrogeno"
            print("es un no metal")
            guess=str(input()) #validar en minusculas
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas-1
                print("se encuentra en el bloque S")
            while 0<vidas<3:
                vidas=vidas-1
                guess=str(input())
                if guess != element: #arreglar que no salga cuando se pierde
                    print("posee un solo nivel de energia")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el hidrogeno")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))

        while element == 2:
            element = "helio"
            print("")
            guess = str(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str(input())
                if guess != element:
                    print("")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el helio")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))

        while element == 3:
            element = "litio"
            print("")
            guess = str(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str(input())
                if guess != element:
                    print("")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el litio")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))

        while element == 4:
            element = "berilio"
            print("")
            guess = str(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str(input())
                if guess != element:
                    print("")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el berilio")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))

        while element == 5:
            element = "boro"
            print("")
            guess = str(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str(input())
                if guess != element:
                    print("")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el boro")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))

        while element == 6:
            element = "carbono"
            print("")
            guess = str(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str(input())
                if guess != element:
                    print("")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el carbono")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))
        while element == 7:
            element = "nitrogeno"
            print("")
            guess = str(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str(input())
                if guess != element:
                    print("")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el nitrogeno")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))

        while element == 8:
            element = "oxigeno"
            print("")
            guess = str(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str(input())
                if guess != element:
                    print("")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el oxigeno")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))

        while element == 9:
            element = "fluor"
            print("")
            guess = str(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str(input())
                if guess != element:
                    print("")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el fluor")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))

        while element == 10:
            element = "neon"
            print("")
            guess = str(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess = str(input())
                if guess != element:
                    print("")
                if guess == element:
                    print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                    menu = int(input())
                    break
                if vidas == 0:
                    print("te quedaste sin intentos, a estudiar")
                    print("el elemento era el neon")
                    menu = int(input("presione 0 para regresar al menu o 3 para reintentar"))

        while element == 11:
            print("sodio")
            print("")
            print("")
            print("")
            print("")

        while element == 12:
            print("magnesio")
            print("")
            print("")
            print("")
            print("")

        while element == 13:
            print("aluminio")
            print("")
            print("")
            print("")
            print("")

        while element == 14:
            print("silicio")
            print("")
            print("")
            print("")
            print("")

        while element == 15:
            print("fosforo")
            print("")
            print("")
            print("")
            print("")

        while element == 16:
            print("azufre")
            print("")
            print("")
            print("")
            print("")

        while element == 17:
            print("cloro")
            print("")
            print("")
            print("")
            print("")

        while element == 18:
            print("argon")
            print("")
            print("")
            print("")
            print("")

        while element == 19:
            print("potasio")
            print("")
            print("")
            print("")
            print("")

        while element == 20:
            print("calcio")
            print("")
            print("")
            print("")
            print("")

        while element == 21:
            print("escandio")
            print("")
            print("")
            print("")
            print("")

        while element == 22:
            print("titanio")
            print("")
            print("")
            print("")
            print("")

        while element == 23:
            print("vanadio")
            print("")
            print("")
            print("")
            print("")

        while element == 24:
            print("cromo")
            print("")
            print("")
            print("")
            print("")

        while element == 25:
            print("manganeso")
            print("")
            print("")
            print("")
            print("")

        while element == 26:
            print("hierro")
            print("")
            print("")
            print("")
            print("")

        while element == 27:
            print("cobalto")
            print("")
            print("")
            print("")
            print("")

        while element == 28:
            print("niquel")
            print("")
            print("")
            print("")
            print("")

        while element == 29:
            print("cobre")
            print("")
            print("")
            print("")
            print("")

        while element == 30:
            print("zinc")
            print("")
            print("")
            print("")
            print("")

        while element == 31:
            print("galio")
            print("")
            print("")
            print("")
            print("")

        while element == 32:
            print("germanio")
            print("")
            print("")
            print("")
            print("")

        while element == 33:
            print("arsenico")
            print("")
            print("")
            print("")
            print("")

        while element == 34:
            print("selenio")
            print("")
            print("")
            print("")
            print("")

        while element == 35:
            print("bromo")
            print("")
            print("")
            print("")
            print("")

        while element == 36:
            print("kripton")
            print("")
            print("")
            print("")
            print("")

        while element == 37:
            print("rubidio")
            print("")
            print("")
            print("")
            print("")

        while element == 38:
            print("estroncio")
            print("")
            print("")
            print("")
            print("")

        while element == 39:
            print("itrio")
            print("")
            print("")
            print("")
            print("")

        while element == 40:
            print("circonio")
            print("")
            print("")
            print("")
            print("")

        while element == 41:
            print("niobio")
            print("")
            print("")
            print("")
            print("")

        while element == 42:
            print("molibdeno")
            print("")
            print("")
            print("")
            print("")

        while element == 43:
            print("tecnecio")
            print("")
            print("")
            print("")
            print("")

        while element == 44:
            print("rutenio")
            print("")
            print("")
            print("")
            print("")

        while element == 45:
            print("rodio")
            print("")
            print("")
            print("")
            print("")

        while element == 46:
            print("paladio")
            print("")
            print("")
            print("")
            print("")

        while element == 47:
            print("plata")
            print("")
            print("")
            print("")
            print("")

        while element == 48:
            print("cadmio")
            print("")
            print("")
            print("")
            print("")

        while element == 49:
            print("indio")
            print("")
            print("")
            print("")
            print("")

        while element == 50:
            print("estaño")
            print("")
            print("")
            print("")
            print("")

        while element == 51:
            print("antimonio")
            print("")
            print("")
            print("")
            print("")

        while element == 52:
            print("telurio")
            print("")
            print("")
            print("")
            print("")
        while element == 53:
            print("yodo")
            print("")
            print("")
            print("")
            print("")

        while element == 54:
            print("xenon")
            print("")
            print("")
            print("")
            print("")

        while element == 55:
            print("cesio")
            print("")
            print("")
            print("")
            print("")

        while element == 56:
            print("bario")
            print("")
            print("")
            print("")
            print("")

        while element == 57:
            print("lantano")
            print("")
            print("")
            print("")
            print("")

        while element == 58:
            print("cerio")
            print("")
            print("")
            print("")
            print("")

        while element == 59:
            print("praseodimio")
            print("")
            print("")
            print("")
            print("")

        while element == 60:
            print("neodimio")
            print("")
            print("")
            print("")
            print("")

        while element == 61:
            print("prometio")
            print("")
            print("")
            print("")
            print("")

        while element == 62:
            print("samario")
            print("")
            print("")
            print("")
            print("")

        while element == 63:
            print("europio")
            print("")
            print("")
            print("")
            print("")

        while element == 64:
            print("gadolinio")
            print("")
            print("")
            print("")
            print("")

        while element == 65:
            print("terbio")
            print("")
            print("")
            print("")
            print("")

        while element == 66:
            print("disprosio")
            print("")
            print("")
            print("")
            print("")

        while element == 67:
            print("holmio")
            print("")
            print("")
            print("")
            print("")

        while element == 68:
            print("erbio")
            print("")
            print("")
            print("")
            print("")

        while element == 69:
            print("tulio")
            print("")
            print("")
            print("")
            print("")

        while element == 70:
            print("iterbio")
            print("")
            print("")
            print("")
            print("")

        while element == 71:
            print("lutecio")
            print("")
            print("")
            print("")
            print("")

        while element == 72:
            print("hafnio")
            print("")
            print("")
            print("")
            print("")

        while element == 73:
            print("tantalo")
            print("")
            print("")
            print("")
            print("")

        while element == 74:
            print("wolframio")
            print("")
            print("")
            print("")
            print("")

        while element == 75:
            print("renio")
            print("")
            print("")
            print("")
            print("")

        while element == 76:
            print("osmio")
            print("")
            print("")
            print("")
            print("")

        while element == 77:
            print("iridio")
            print("")
            print("")
            print("")
            print("")

        while element == 78:
            print("platino")
            print("")
            print("")
            print("")
            print("")

        while element == 79:
            print("oro")
            print("")
            print("")
            print("")
            print("")

        while element == 80:
            print("mercurio")
            print("")
            print("")
            print("")
            print("")

        while element == 81:
            print("talio")
            print("")
            print("")
            print("")
            print("")

        while element == 82:
            print("plomo")
            print("")
            print("")
            print("")
            print("")

        while element == 83:
            print("bismuto")
            print("")
            print("")
            print("")
            print("")

        while element == 84:
            print("polonio")
            print("")
            print("")
            print("")
            print("")

        while element == 85:
            print("astato")
            print("")
            print("")
            print("")
            print("")

        while element == 86:
            print("radon")
            print("")
            print("")
            print("")
            print("")

        while element == 87:
            print("francio")
            print("")
            print("")
            print("")
            print("")

        while element == 88:
            print("radio")
            print("")
            print("")
            print("")
            print("")

        while element == 89:
            print("actinio")
            print("")
            print("")
            print("")
            print("")

        while element == 90:
            print("torio")
            print("")
            print("")
            print("")
            print("")

        while element == 91:
            print("protactinio")
            print("")
            print("")
            print("")
            print("")

        while element == 92:
            print("uranio")
            print("")
            print("")
            print("")
            print("")

        while element == 93:
            print("neptunio")
            print("")
            print("")
            print("")
            print("")

        while element == 94:
            print("plutonio")
            print("")
            print("")
            print("")
            print("")

        while element == 95:
            print("americio")
            print("")
            print("")
            print("")
            print("")

        while element == 96:
            print("curio")
            print("")
            print("")
            print("")
            print("")

        while element == 97:
            print("berkelio")
            print("")
            print("")
            print("")
            print("")

        while element == 98:
            print("californio")
            print("")
            print("")
            print("")
            print("")

        while element == 99:
            print("einstenio")
            print("")
            print("")
            print("")
            print("")

        while element == 100:
            print("fermio")
            print("")
            print("")
            print("")
            print("")

        while element == 101:
            print("mendelevio")
            print("")
            print("")
            print("")
            print("")

        while element == 102:
            print("nobelio")
            print("")
            print("")
            print("")
            print("")

        while element == 103:
            print("lawrencio")
            print("")
            print("")
            print("")
            print("")

        while element == 104:
            print("rutherfordio")
            print("")
            print("")
            print("")
            print("")

        while element == 105:
            print("dubnio")
            print("")
            print("")
            print("")
            print("")

        while element == 106:
            print("seaborgio")
            print("")
            print("")
            print("")
            print("")

        while element == 107:
            print("bohrio")
            print("")
            print("")
            print("")
            print("")

        while element == 108:
            print("hasio")
            print("")
            print("")
            print("")
            print("")

        while element == 109:
            print("meitnerio")
            print("")
            print("")
            print("")
            print("")

        while element == 110:
            print("darmstatio")
            print("")
            print("")
            print("")
            print("")

        while element == 111:
            print("roentgenio")
            print("")
            print("")
            print("")
            print("")

        while element == 112:
            print("copernicio")
            print("")
            print("")
            print("")
            print("")

        while element == 113:
            print("nihonio")
            print("")
            print("")
            print("")
            print("")

        while element == 114:
            print("flerevio")
            print("")
            print("")
            print("")
            print("")

        while element == 115:
            print("moscovio")
            print("")
            print("")
            print("")
            print("")

        while element == 116:
            print("livermorio")
            print("")
            print("")
            print("")
            print("")

        while element == 117:
            print("teneso")
            print("")
            print("")
            print("")
            print("")

        while element == 118:
            print("organeson")
            print("")
            print("")
            print("")
            print("")
