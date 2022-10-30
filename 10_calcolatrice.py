numero1 = int(input("inserisci un numero: "))
numero2 = int(input("inserisci un altro numero: "))
operazione = int(input("scegli l'operazione: 1 per +, 2 per -, 3 per /, 4 per * "))
if(operazione == 1):
    print(numero1 + numero2)
if(operazione == 2):
    print(numero1 - numero2)
if(operazione == 3):
	if(numero2 == 0):
       		print("Non puoi dividere per 0! ") 
	else:
   		print(numero1/nnumero2) 
if(operazione == 4):
    print(numero1 * numero2)

if(operazione >= 5):
    operzaione = 1

input("pess any key to exit")
