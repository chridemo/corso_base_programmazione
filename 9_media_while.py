output = ""
numero = input("inserisci un numero")
i = 1
while True:
    if(numero != 0):
        output = numero + output
        i = i + 1
    else:
        break    
    a = numero / i
    print(i)

    input("press any key to exit")
