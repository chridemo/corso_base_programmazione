import random
m = random.randrange(0,4)

list = ("ag", "al", "an")
print(list[m])

provincia = input("inserisci la provincia: ")
if(m==1):
    if(provincia== "agrigento"):
        print("giusto")
    else:
        print("sbagliato")

