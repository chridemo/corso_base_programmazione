stringa = input("inserisci il tuo nome: ")
i:int = len(stringa) - 1
risultato:str = ""
while i >= 0:
    risultato = risultato + [i]
    i = i - 1
print(risultato)
