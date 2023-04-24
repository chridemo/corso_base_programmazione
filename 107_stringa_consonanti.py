i = 0
output = ""
stringa = input("inserisci una stringa: ")
lunghezza = len(stringa)
while i < lunghezza:
    if(stringa[i] != "a" and stringa[i] != "e" and stringa[i] != "i" and stringa[i] != "o" and stringa[i] != "u"):
        output = output + stringa[i]
    i = i + 1
print(output)
