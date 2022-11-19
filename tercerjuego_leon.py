import random
menu=3
while menu == 3:
    def nometal(): print("es un no metal")
    def metal(): print("es un metal")
    def semimetal(): print("es un semi metal")
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
    print(element)
    if element == 1:
        atomo="hidrogeno"
        nometal(),intentos(atomo)
    if element == 2:
        atomo="helio"
        nometal(),intentos(atomo)
    if element == 3:
        atomo = "litio"
        nometal(), intentos(atomo)
    if element == 4:
        atomo = "berilio"
        nometal(), intentos(atomo)
    if element == 5:
        atomo = "boro"
        nometal(), intentos(atomo)
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
        nometal(), intentos(atomo)
    if element == 12:
        atomo = "magnesio"
        nometal(), intentos(atomo)
    if element == 13:
        atomo = "aluminio"
        nometal(), intentos(atomo)
    if element == 14:
        atomo = ("silicio")
        nometal(), intentos(atomo)
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
        nometal(), intentos(atomo)
    if element == 20:
        atomo = ("calcio")
        nometal(), intentos(atomo)
    if element == 21:
        atomo = ("escandio")
        nometal(), intentos(atomo)
    if element == 22:
        atomo = ("titanio")
        nometal(), intentos(atomo)
    if element == 23:
        atomo = ("vanadio")
        nometal(), intentos(atomo)
    if element == 24:
        atomo = ("cromo")
        nometal(), intentos(atomo)
    if element == 25:
        atomo = ("manganeso")
        nometal(), intentos(atomo)
    if element == 26:
        atomo = ("hierro")
        nometal(), intentos(atomo)
    if element == 27:
        atomo = ("cobalto")
        nometal(), intentos(atomo)
    if element == 28:
        atomo = ("niquel")
        nometal(), intentos(atomo)
    if element == 29:
        atomo = ("cobre")
        nometal(), intentos(atomo)
    if element == 30:
        atomo = ("zinc")
        nometal(), intentos(atomo)
    if element == 31:
        atomo = ("galio")
        nometal(), intentos(atomo)
    if element == 32:
        atomo = ("germanio")
        nometal(), intentos(atomo)
    if element == 33:
        atomo = ("arsenico")
        nometal(), intentos(atomo)
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
        nometal(), intentos(atomo)
    if element == 38:
        atomo = ("estroncio")
        nometal(), intentos(atomo)
    if element == 39:
        atomo = ("itrio")
        nometal(), intentos(atomo)
    if element == 40:
        atomo = ("circonio")
        nometal(), intentos(atomo)
    if element == 41:
        atomo = ("niobio")
        nometal(), intentos(atomo)
    if element == 42:
        atomo = ("molibdeno")
        nometal(), intentos(atomo)
    if element == 43:
        atomo = ("tecnecio")
        nometal(), intentos(atomo)
    if element == 44:
        atomo = ("rutenio")
        nometal(), intentos(atomo)
    if element == 45:
        atomo = ("rodio")
        nometal(), intentos(atomo)
    if element == 46:
        atomo = ("paladio")
        nometal(), intentos(atomo)
    if element == 47:
        atomo = ("plata")
        nometal(), intentos(atomo)
    if element == 48:
        atomo = ("cadmio")
        nometal(), intentos(atomo)
    if element == 49:
        atomo = ("indio")
        nometal(), intentos(atomo)
    if element == 50:
        atomo = ("estaño")
        nometal(), intentos(atomo)
    if element == 51:
        atomo = ("antimonio")
        nometal(), intentos(atomo)
    if element == 52:
        atomo = ("telurio")
        nometal(), intentos(atomo)
    if element == 53:
        atomo = ("yodo")
        nometal(), intentos(atomo)
    if element == 54:
        atomo = ("xenon")
        nometal(), intentos(atomo)
    if element == 55:
        atomo = ("cesio")
        nometal(), intentos(atomo)
    if element == 56:
        atomo = ("bario")
        nometal(), intentos(atomo)
    if element == 57:
        atomo = ("lantano")
        nometal(), intentos(atomo)
    if element == 58:
        atomo = ("cerio")
        nometal(), intentos(atomo)
    if element == 59:
        atomo = ("praseodimio")
        nometal(), intentos(atomo)
    if element == 60:
        atomo = ("neodimio")
        nometal(), intentos(atomo)
    if element == 61:
        atomo = ("prometio")
        nometal(), intentos(atomo)
    if element == 62:
        atomo = ("samario")
        nometal(), intentos(atomo)
    if element == 63:
        atomo = ("europio")
        nometal(), intentos(atomo)
    if element == 64:
        atomo = ("gadolinio")
        nometal(), intentos(atomo)
    if element == 65:
        atomo = ("terbio")
        nometal(), intentos(atomo)
    if element == 66:
        atomo = ("disprosio")
        nometal(), intentos(atomo)
    if element == 67:
        atomo = ("holmio")
        nometal(), intentos(atomo)
    if element == 68:
        atomo = ("erbio")
        nometal(), intentos(atomo)
    if element == 69:
        atomo = ("tulio")
        nometal(), intentos(atomo)
    if element == 70:
        atomo = ("iterbio")
        nometal(), intentos(atomo)
    if element == 71:
        atomo = ("lutecio")
        nometal(), intentos(atomo)
    if element == 72:
        atomo = ("hafnio")
        nometal(), intentos(atomo)
    if element == 73:
        atomo = ("tantalo")
        nometal(), intentos(atomo)
    if element == 74:
        atomo = ("wolframio")
        nometal(), intentos(atomo)
    if element == 75:
        atomo = ("renio")
        nometal(), intentos(atomo)
    if element == 76:
        atomo = ("osmio")
        nometal(), intentos(atomo)
    if element == 77:
        atomo = ("iridio")
        nometal(), intentos(atomo)
    if element == 78:
        atomo = ("platino")
        nometal(), intentos(atomo)
    if element == 79:
        atomo = ("oro")
        nometal(), intentos(atomo)
    if element == 80:
        atomo = ("mercurio")
        nometal(), intentos(atomo)
    if element == 81:
        atomo = ("talio")
        nometal(), intentos(atomo)
    if element == 82:
        atomo = ("plomo")
        nometal(), intentos(atomo)
    if element == 83:
        atomo = ("bismuto")
        nometal(), intentos(atomo)
    if element == 84:
        atomo = ("polonio")
        nometal(), intentos(atomo)
    if element == 85:
        atomo = ("astato")
        nometal(), intentos(atomo)
    if element == 86:
        atomo = ("radon")
        nometal(), intentos(atomo)
    if element == 87:
        atomo = ("francio")
        nometal(), intentos(atomo)
    if element == 88:
        atomo = ("radio")
        nometal(), intentos(atomo)
    if element == 89:
        atomo = ("actinio")
        nometal(), intentos(atomo)
    if element == 90:
        atomo = ("torio")
        nometal(), intentos(atomo)
    if element == 91:
        atomo = ("protactinio")
        nometal(), intentos(atomo)
    if element == 92:
        atomo = ("uranio")
        nometal(), intentos(atomo)
    if element == 93:
        atomo = ("neptunio")
        nometal(), intentos(atomo)
    if element == 94:
        atomo = ("plutonio")
        nometal(), intentos(atomo)
    if element == 95:
        atomo = ("americio")
        nometal(), intentos(atomo)
    if element == 96:
        atomo = ("curio")
        nometal(), intentos(atomo)
    if element == 97:
        atomo = ("berkelio")
        nometal(), intentos(atomo)
    if element == 98:
        atomo = ("californio")
        nometal(), intentos(atomo)
    if element == 99:
        atomo = ("einstenio")
        nometal(), intentos(atomo)
    if element == 100:
        atomo = ("fermio")
        nometal(), intentos(atomo)
    if element == 101:
        atomo = ("mendelevio")
        nometal(), intentos(atomo)
    if element == 102:
        atomo = ("nobelio")
        nometal(), intentos(atomo)
    if element == 103:
        atomo = ("lawrencio")
        nometal(), intentos(atomo)
    if element == 104:
        atomo = ("rutherfordio")
        nometal(), intentos(atomo)
    if element == 105:
        atomo = ("dubnio")
        nometal(), intentos(atomo)
    if element == 106:
        atomo = ("seaborgio")
        nometal(), intentos(atomo)
    if element == 107:
        atomo = ("bohrio")
        nometal(), intentos(atomo)
    if element == 108:
        atomo = ("hasio")
        nometal(), intentos(atomo)
    if element == 109:
        atomo = ("meitnerio")
        nometal(), intentos(atomo)
    if element == 110:
        atomo = ("darmstatio")
        nometal(), intentos(atomo)
    if element == 111:
        atomo = ("roentgenio")
        nometal(), intentos(atomo)
    if element == 112:
        atomo = ("copernicio")
        nometal(), intentos(atomo)
    if element == 113:
        atomo = ("nihonio")
        nometal(), intentos(atomo)
    if element == 114:
        atomo = ("flerevio")
        nometal(), intentos(atomo)
    if element == 115:
        atomo = ("moscovio")
        nometal(), intentos(atomo)
    if element == 116:
        atomo = ("livermorio")
        nometal(), intentos(atomo)
    if element == 117:
        atomo = ("teneso")
        nometal(), intentos(atomo)
    if element == 118:
        atomo = ("organeson")
        nometal(), intentos(atomo)