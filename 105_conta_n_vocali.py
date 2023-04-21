i = 0
stringa = input("Inserisci una stringa: ")
A = 0
E = 0
I = 0
O = 0
U = 0
lunghezza = len(stringa)
while i < lunghezza:
    if (stringa[i]=="A" or stringa[i]=="a"):
        A = A + 1
    if (stringa[i]=="E" or stringa[i]=="e"):
        E = E + 1
    if (stringa[i]=="I" or stringa[i]=="i"):
        I = I + 1
    if (stringa[i]=="O" or stringa[i]=="o"):
        O = O + 1
    if (stringa[i]=="U" or stringa[i]=="u"):
        U = U + 1
    i = i + 1

print("A: " + str(A))
print("E: " + str(E))
print("I: " + str(I))
print("O: " + str(O))
print("U: " + str(U))
