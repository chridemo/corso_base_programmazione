i = 0
somma = 0
stringa:str = input("inserire una stringa: ")
carattere:str = input("inserire un carattere: ")
n = len(stringa)
while i < n:
    c =  stringa[i]
    if(c == carattere):
        somma = somma + 1
    i = i + 1
print(somma)
