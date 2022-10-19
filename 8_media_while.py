i = 1
totale = 0
numeri = 10
while i <= 10:
    numero = int(input(str(numeri) + ", da inserire ancora "))
    numeri = numeri - 1
    i = i + 1
    totale = (str(totale) + str(numero))
    
    break  
    
    
    print(totale)


input("press any key to exit")
