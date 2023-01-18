c = int(0)
i = int(0)
somma = int(0)
while True:
        stringa = input("inserisci una stringa di sole cifre: ")
        c = stringa[i]
        if(c == "0") or (c == "1") or (c == "2") or (c == "3") or (c == "4") or (c == "5") or (c == "6") or (c == "7") or (c == "8") or (c == "9"):
                i = i + 1
                somma = somma + c
        else: 
                break
print(somma)
