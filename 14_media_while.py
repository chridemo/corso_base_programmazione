counter = 0
i = 1
while True:
    numero = int(input("inserisci un numero: "))
    if(numero == 0):
        break
    counter = counter + numero
    i = i + 1
print(counter / i)

input("press any key to exit")
