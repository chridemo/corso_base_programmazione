b = ""
i = 1
numeri = 10
while i <= 10:
    numero = (input(str(numeri) + " numeri da inserire ancora "))
    b = (numero + b)
    numeri = numeri - 1
    i = i + 1   
if(i == 10):
    print (b)

input("press any key to exit")
