import random
menu=3
while menu == 3:
    def nometal(): print("es un no metal")
    def metal(): print("es un metal")
    def bloqueP(): print("se encuentra en el bloque P")
    def bloqueS(): print("se encuentra en el bloque S")
    def bloqueD(): print("se encuentra en el bloque D")
    def bloqueF(): print("se encuentra en el bloque F")
    def intentos(atomo):
        vidas=3
        guess = str.lower(input())
        if guess == atomo:
            print("¡CORRECTO!, si desea jugar de nuevo presione 3, si quiere volver al menu presione 0")
            menu = int(input())
        elif guess != atomo:
            vidas = vidas - 1
            if 0<element<5 or 10<element<13 or 18<element<21 or 36<element<39 or 54<element<57 or 86<element<89:
                bloqueS()
            if 4<element<11 or 12<element<19 or 30<element<37 or 48<element<55 or 80<element<87 or 112<element<119:
                bloqueP()
            if 20<element<31 or 38<element<49 or 70<element<81 or 103<element<113:
                bloqueD()
            if 56<element<71 or 88<element<103:
                bloqueF()
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
    while element == 1:
        atomo="hidrogeno"
        nometal(),intentos(atomo)
    while element == 2:
        atomo="helio"
        nometal(),intentos(atomo)
    while element == 3:
        atomo = "litio"
        nometal(), intentos(atomo)
    while element == 4:
        atomo = "berilio"
        nometal(), intentos(atomo)
    while element == 5:
        atomo = "boro"
        nometal(), intentos(atomo)
    while element == 6:
        atomo = "carbono"
        nometal(), intentos(atomo)
    while element == 7:
        atomo = "nitrogeno"
        nometal(), intentos(atomo)
    while element == 8:
        atomo = "oxigeno"
        nometal(), intentos(atomo)
    while element == 9:
        atomo = "fluor"
        nometal(), intentos(atomo)
    while element == 10:
        atomo = "neon"
        nometal(), intentos(atomo)
    while element == 11:
        atomo = "sodio"
        nometal(), intentos(atomo)
    while element == 12:
        atomo = "magnesio"
        nometal(), intentos(atomo)
    while element == 13:
        atomo = "aluminio"
        nometal(), intentos(atomo)
    while element == 14:
        atomo = ("silicio")
        nometal(), intentos(atomo)
    while element == 15:
        atomo = ("fosforo")
        nometal(), intentos(atomo)
    while element == 16:
        atomo = ("azufre")
        nometal(), intentos(atomo)
    while element == 17:
        atomo = ("cloro")
        nometal(), intentos(atomo)
    while element == 18:
        atomo = ("argon")
        nometal(), intentos(atomo)
    while element == 19:
        atomo = ("potasio")
        nometal(), intentos(atomo)
    while element == 20:
        atomo = ("calcio")
        nometal(), intentos(atomo)
    while element == 21:
        atomo = ("escandio")
        nometal(), intentos(atomo)
    while element == 22:
        atomo = ("titanio")
        nometal(), intentos(atomo)
    while element == 23:
        atomo = ("vanadio")
        nometal(), intentos(atomo)
    while element == 24:
        atomo = ("cromo")
        nometal(), intentos(atomo)
    while element == 25:
        atomo = ("manganeso")
        nometal(), intentos(atomo)
    while element == 26:
        atomo = ("hierro")
        nometal(), intentos(atomo)
    while element == 27:
        atomo = ("cobalto")
        nometal(), intentos(atomo)
    while element == 28:
        atomo = ("niquel")
        nometal(), intentos(atomo)
    while element == 29:
        atomo = ("cobre")
        nometal(), intentos(atomo)
    while element == 30:
        atomo = ("zinc")
        nometal(), intentos(atomo)
    while element == 31:
        atomo = ("galio")
        nometal(), intentos(atomo)
    while element == 32:
        atomo = ("germanio")
        nometal(), intentos(atomo)
    while element == 33:
        atomo = ("arsenico")
        nometal(), intentos(atomo)
    while element == 34:
        atomo = ("selenio")
        nometal(), intentos(atomo)
    while element == 35:
        atomo = ("bromo")
        nometal(), intentos(atomo)
    while element == 36:
        atomo = ("kripton")
        nometal(), intentos(atomo)
    while element == 37:
        atomo = ("rubidio")
        nometal(), intentos(atomo)
    while element == 38:
        atomo = ("estroncio")
        nometal(), intentos(atomo)
    while element == 39:
        atomo = ("itrio")
        nometal(), intentos(atomo)
    while element == 40:
        atomo = ("circonio")
        nometal(), intentos(atomo)
    while element == 41:
        atomo = ("niobio")
        nometal(), intentos(atomo)
    while element == 42:
        atomo = ("molibdeno")
        nometal(), intentos(atomo)
    while element == 43:
        atomo = ("tecnecio")
        nometal(), intentos(atomo)
    while element == 44:
        atomo = ("rutenio")
        nometal(), intentos(atomo)
    while element == 45:
        atomo = ("rodio")
        nometal(), intentos(atomo)
    while element == 46:
        atomo = ("paladio")
        nometal(), intentos(atomo)
    while element == 47:
        atomo = ("plata")
        nometal(), intentos(atomo)
    while element == 48:
        atomo = ("cadmio")
        nometal(), intentos(atomo)
    while element == 49:
        atomo = ("indio")
        nometal(), intentos(atomo)
    while element == 50:
        atomo = ("estaño")
        nometal(), intentos(atomo)
    while element == 51:
        atomo = ("antimonio")
        nometal(), intentos(atomo)
    while element == 52:
        atomo = ("telurio")
        nometal(), intentos(atomo)
    while element == 53:
        atomo = ("yodo")
        nometal(), intentos(atomo)
    while element == 54:
        atomo = ("xenon")
        nometal(), intentos(atomo)
    while element == 55:
        atomo = ("cesio")
        nometal(), intentos(atomo)
    while element == 56:
        atomo = ("bario")
        nometal(), intentos(atomo)
    while element == 57:
        atomo = ("lantano")
        nometal(), intentos(atomo)
    while element == 58:
        atomo = ("cerio")
        nometal(), intentos(atomo)
    while element == 59:
        atomo = ("praseodimio")
        nometal(), intentos(atomo)
    while element == 60:
        atomo = ("neodimio")
        nometal(), intentos(atomo)
    while element == 61:
        atomo = ("prometio")
        nometal(), intentos(atomo)
    while element == 62:
        atomo = ("samario")
        nometal(), intentos(atomo)
    while element == 63:
        atomo = ("europio")
        nometal(), intentos(atomo)
    while element == 64:
        atomo = ("gadolinio")
        nometal(), intentos(atomo)
    while element == 65:
        atomo = ("terbio")
        nometal(), intentos(atomo)
    while element == 66:
        atomo = ("disprosio")
        nometal(), intentos(atomo)
    while element == 67:
        atomo = ("holmio")
        nometal(), intentos(atomo)
    while element == 68:
        atomo = ("erbio")
        nometal(), intentos(atomo)
    while element == 69:
        atomo = ("tulio")
        nometal(), intentos(atomo)
    while element == 70:
        atomo = ("iterbio")
        nometal(), intentos(atomo)
    while element == 71:
        atomo = ("lutecio")
        nometal(), intentos(atomo)
    while element == 72:
        atomo = ("hafnio")
        nometal(), intentos(atomo)
    while element == 73:
        atomo = ("tantalo")
        nometal(), intentos(atomo)
    while element == 74:
        atomo = ("wolframio")
        nometal(), intentos(atomo)
    while element == 75:
        atomo = ("renio")
        nometal(), intentos(atomo)
    while element == 76:
        atomo = ("osmio")
        nometal(), intentos(atomo)
    while element == 77:
        atomo = ("iridio")
        nometal(), intentos(atomo)
    while element == 78:
        atomo = ("platino")
        nometal(), intentos(atomo)
    while element == 79:
        atomo = ("oro")
        nometal(), intentos(atomo)
    while element == 80:
        atomo = ("mercurio")
        nometal(), intentos(atomo)
    while element == 81:
        atomo = ("talio")
        nometal(), intentos(atomo)
    while element == 82:
        atomo = ("plomo")
        nometal(), intentos(atomo)
    while element == 83:
        atomo = ("bismuto")
        nometal(), intentos(atomo)
    while element == 84:
        atomo = ("polonio")
        nometal(), intentos(atomo)
    while element == 85:
        atomo = ("astato")
        nometal(), intentos(atomo)
    while element == 86:
        atomo = ("radon")
        nometal(), intentos(atomo)
    while element == 87:
        atomo = ("francio")
        nometal(), intentos(atomo)
    while element == 88:
        atomo = ("radio")
        nometal(), intentos(atomo)
    while element == 89:
        atomo = ("actinio")
        nometal(), intentos(atomo)
    while element == 90:
        atomo = ("torio")
        nometal(), intentos(atomo)
    while element == 91:
        atomo = ("protactinio")
        nometal(), intentos(atomo)
    while element == 92:
        atomo = ("uranio")
        nometal(), intentos(atomo)
    while element == 93:
        atomo = ("neptunio")
        nometal(), intentos(atomo)
    while element == 94:
        atomo = ("plutonio")
        nometal(), intentos(atomo)
    while element == 95:
        atomo = ("americio")
        nometal(), intentos(atomo)
    while element == 96:
        atomo = ("curio")
        nometal(), intentos(atomo)
    while element == 97:
        atomo = ("berkelio")
        nometal(), intentos(atomo)
    while element == 98:
        atomo = ("californio")
        nometal(), intentos(atomo)
    while element == 99:
        atomo = ("einstenio")
        nometal(), intentos(atomo)
    while element == 100:
        atomo = ("fermio")
        nometal(), intentos(atomo)
    while element == 101:
        atomo = ("mendelevio")
        nometal(), intentos(atomo)
    while element == 102:
        atomo = ("nobelio")
        nometal(), intentos(atomo)
    while element == 103:
        atomo = ("lawrencio")
        nometal(), intentos(atomo)
    while element == 104:
        atomo = ("rutherfordio")
        nometal(), intentos(atomo)
    while element == 105:
        atomo = ("dubnio")
        nometal(), intentos(atomo)
    while element == 106:
        atomo = ("seaborgio")
        nometal(), intentos(atomo)
    while element == 107:
        atomo = ("bohrio")
        nometal(), intentos(atomo)
    while element == 108:
        atomo = ("hasio")
        nometal(), intentos(atomo)
    while element == 109:
        atomo = ("meitnerio")
        nometal(), intentos(atomo)
    while element == 110:
        atomo = ("darmstatio")
        nometal(), intentos(atomo)
    while element == 111:
        atomo = ("roentgenio")
        nometal(), intentos(atomo)
    while element == 112:
        atomo = ("copernicio")
        nometal(), intentos(atomo)
    while element == 113:
        atomo = ("nihonio")
        nometal(), intentos(atomo)
    while element == 114:
        atomo = ("flerevio")
        nometal(), intentos(atomo)
    while element == 115:
        atomo = ("moscovio")
        nometal(), intentos(atomo)
    while element == 116:
        atomo = ("livermorio")
        nometal(), intentos(atomo)
    while element == 117:
        atomo = ("teneso")
        nometal(), intentos(atomo)
    while element == 118:
        atomo = ("organeson")
        nometal(), intentos(atomo)