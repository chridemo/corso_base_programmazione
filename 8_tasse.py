guadagno = int(input("inserisci il guadagno annuale: "))
tot1 = guadagno * 22/100
eccesso1 = guadagno - 30000
eccesso2 = eccesso1 * 33/100
if(guadagno <= 30000):
    print(tot1)
    if(guadagno < 10000 ):
        print("0")
else:
    if(guadagno > 30000):
        tot2 = tot1 + eccesso2
        print(str(tot2) + "$")

input("press any key to exit")