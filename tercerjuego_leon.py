import random
menu=3
while menu == 3:
    def nometal(): print("es un no metal")
    def metal(): print("es un metal")
    def semimetal(): print("es un semi metal")
    def desconocido(): print("su capacidad de conduccion electrica es aun desconocida")
    def intentos(atomo):
        vidas=3
        guess = str.lower(input())
        if guess == atomo:
            print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
            menu = int(input())
        elif guess != atomo:
            vidas = vidas - 1
            if 0<element<5 or 10<element<13 or 18<element<21 or 36<element<39 or 54<element<57 or 86<element<89:
                print("se encuentra en el bloque S")
            if 4<element<11 or 12<element<19 or 30<element<37 or 48<element<55 or 80<element<87 or 112<element<119:
                print("se encuentra en el bloque P")
            if 20<element<31 or 38<element<49 or 70<element<81 or 103<element<113:
                print("se encuentra en el bloque D")
            if 56<element<71 or 88<element<103:
                print("se encuentra en el bloque F")
        while 0 < vidas < 3:
            vidas = vidas - 1
            guess = str.lower(input())
            if vidas > 0:
                if guess != atomo:
                    print("su cantidad de electrones es de:",element)
            if guess == atomo:
                print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
                menu = int(input())
                break
            if vidas == 0:
                print("te quedaste sin intentos, a estudiar")
                menu = int(input())
    print("usted debera adivinar de que elemento se trata usando los datos que se iran otorgando por cada intento hasta un maximo de 3")
    vidas=3
    element = random.randint(1, 118)
    if element == 1:
        atomo="hidrogeno"
        nometal(),intentos(atomo)
    if element == 2:
        atomo="helio"
        nometal(),intentos(atomo)
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