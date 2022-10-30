i = 0
counter = ""
counter2 = 0
n_operazioni = int(input("inserisci il numero di operazioni da eseguire: "))
numero = int(input("inserisci un numero: "))

while i < n_operazioni:
    operazione = int(input("inserisci l'operazione da eseguire: 1 '+' ; 2 '-' ; 3 '/' ; 4 '*': "))
    numero2 = int(input("inserisci un altro numero: "))
    
    if(operazione == 1):
        counter = counter2 + (numero + numero2)
    if(operazione == 2):
        counter = counter2 + (numero - numero2)
    if(operazione == 3):
        if(numero2 == 0):
            print("Non puoi dividere per 0!")
        if(numero2 > 0):
            counter = counter2 + (numero / numero2)
    if(operazione == 4):
        counter = counter2 + (numero * numero2)
    i = i + 1
print(counter)

input("press any key to exit")
