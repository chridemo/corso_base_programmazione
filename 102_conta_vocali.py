stringa = input("inserisci una stringa: ")
vocali = 0
i = 0
n = len(stringa)
while True:
        if(i == n):
            break
        singolo_carattere = stringa[i]
        i = i + 1
        if("a" == singolo_carattere) or ("e" == singolo_carattere) or ("i" == singolo_carattere) or ("o" == singolo_carattere) or ("u" == singolo_carattere) or ("A" == singolo_carattere) or ("E" == singolo_carattere) or ("I" == singolo_carattere) or ("O" == singolo_carattere) or ("U" == singolo_carattere):
            vocali = vocali + 1
print(vocali)



