i = 0
while i <= 10:
    a = int(input("indovina il numero magico:"))
    if ( a== 7):
        print("Complimenti hai indovinato!")
        break
    else:
        i = i + 1
    if (i == 10):
        print ("Ritenta, hai perso!")

input("press any key to exit")
