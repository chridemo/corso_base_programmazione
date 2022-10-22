max = 1 
min = 1000000
while True:
    numero = int(input("inserisci un numero, premi 0 per terminare: "))
    if(numero == 0):
        break
    else:
        if(numero >= max):
         max = numero
        if(numero <= min):
         min = numero

print("il numero maggiore è: " + str(max))
print("il numero minore è: " + str(min))

input("press any key to exit")
