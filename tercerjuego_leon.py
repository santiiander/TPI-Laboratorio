import random
menu=3
while menu == 3:
        print("usted debera adivinar de que elemento se trata usando los datos que se iran otorgando por cada intento hasta un maximo de 3")
        element = random.randint(1, 1)
        vidas=3
        while element == 1:
            element = "hidrogeno"
            print("es un no metal")
            guess=str.lower(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas-1
                print("se encuentra en el bloque S")
            while 0<vidas<3:
                vidas=vidas-1
                guess=str.lower(input())
                if vidas > 0:
                    if guess != element:
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
            guess=str.lower(input())
            if guess == element:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
            elif guess != element:
                vidas = vidas - 1
                print("")
            while 0 < vidas < 3:
                vidas = vidas - 1
                guess=str.lower(input())
                if vidas > 0:
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
        while element == 4:
            element = "berilio"
        while element == 5:
            element = "boro"
        while element == 6:
            element = "carbono"
        while element == 7:
            element = "nitrogeno"
        while element == 8:
            element = "oxigeno"
        while element == 9:
            element = "fluor"
        while element == 10:
            element = "neon"
        while element == 11:
            print("sodio")
        while element == 12:
            print("magnesio")
        while element == 13:
            print("aluminio")
        while element == 14:
            print("silicio")
        while element == 15:
            print("fosforo")
        while element == 16:
            print("azufre")
        while element == 17:
            print("cloro")
        while element == 18:
            print("argon")
        while element == 19:
            print("potasio")
        while element == 20:
            print("calcio")
        while element == 21:
            print("escandio")
        while element == 22:
            print("titanio")
        while element == 23:
            print("vanadio")
        while element == 24:
            print("cromo")
        while element == 25:
            print("manganeso")
        while element == 26:
            print("hierro")
        while element == 27:
            print("cobalto")
        while element == 28:
            print("niquel")
        while element == 29:
            print("cobre")
        while element == 30:
            print("zinc")
        while element == 31:
            print("galio")
        while element == 32:
            print("germanio")
        while element == 33:
            print("arsenico")
        while element == 34:
            print("selenio")
        while element == 35:
            print("bromo")
        while element == 36:
            print("kripton")
        while element == 37:
            print("rubidio")
        while element == 38:
            print("estroncio")
        while element == 39:
            print("itrio")
        while element == 40:
            print("circonio")
        while element == 41:
            print("niobio")
        while element == 42:
            print("molibdeno")
        while element == 43:
            print("tecnecio")
        while element == 44:
            print("rutenio")
        while element == 45:
            print("rodio")
        while element == 46:
            print("paladio")
        while element == 47:
            print("plata")
        while element == 48:
            print("cadmio")
        while element == 49:
            print("indio")
        while element == 50:
            print("estaño")
        while element == 51:
            print("antimonio")
        while element == 52:
            print("telurio")
        while element == 53:
            print("yodo")
        while element == 54:
            print("xenon")
        while element == 55:
            print("cesio")
        while element == 56:
            print("bario")
        while element == 57:
            print("lantano")
        while element == 58:
            print("cerio")
        while element == 59:
            print("praseodimio")
        while element == 60:
            print("neodimio")
        while element == 61:
            print("prometio")
        while element == 62:
            print("samario")
        while element == 63:
            print("europio")
        while element == 64:
            print("gadolinio")
        while element == 65:
            print("terbio")
        while element == 66:
            print("disprosio")
        while element == 67:
            print("holmio")
        while element == 68:
            print("erbio")
        while element == 69:
            print("tulio")
        while element == 70:
            print("iterbio")
        while element == 71:
            print("lutecio")
        while element == 72:
            print("hafnio")
        while element == 73:
            print("tantalo")
        while element == 74:
            print("wolframio")
        while element == 75:
            print("renio")
        while element == 76:
            print("osmio")
        while element == 77:
            print("iridio")
        while element == 78:
            print("platino")
        while element == 79:
            print("oro")
        while element == 80:
            print("mercurio")
        while element == 81:
            print("talio")
        while element == 82:
            print("plomo")
        while element == 83:
            print("bismuto")
        while element == 84:
            print("polonio")
        while element == 85:
            print("astato")
        while element == 86:
            print("radon")
        while element == 87:
            print("francio")
        while element == 88:
            print("radio")
        while element == 89:
            print("actinio")
        while element == 90:
            print("torio")
        while element == 91:
            print("protactinio")
        while element == 92:
            print("uranio")
        while element == 93:
            print("neptunio")
        while element == 94:
            print("plutonio")
        while element == 95:
            print("americio")
        while element == 96:
            print("curio")
        while element == 97:
            print("berkelio")
        while element == 98:
            print("californio")
        while element == 99:
            print("einstenio")
        while element == 100:
            print("fermio")
        while element == 101:
            print("mendelevio")
        while element == 102:
            print("nobelio")
        while element == 103:
            print("lawrencio")
        while element == 104:
            print("rutherfordio")
        while element == 105:
            print("dubnio")
        while element == 106:
            print("seaborgio")
        while element == 107:
            print("bohrio")
        while element == 108:
            print("hasio")
        while element == 109:
            print("meitnerio")
        while element == 110:
            print("darmstatio")
        while element == 111:
            print("roentgenio")
        while element == 112:
            print("copernicio")
        while element == 113:
            print("nihonio")
        while element == 114:
            print("flerevio")
        while element == 115:
            print("moscovio")
        while element == 116:
            print("livermorio")
        while element == 117:
            print("teneso")
        while element == 118:
            print("organeson")