#NOMI-COSE-STATI

#variabili
lettera_random = ""
nomi = ""
continuare = "s"
punteggio = 0
i = 0
x = 0
#______________________________________________________________________________________________________________

#import
import time
import random 
#______________________________________________________________________________________________________________

#liste
lettera = ["A","B","C","D","E","F","G"]
lunghezza_lettera = len(lettera)
#______________________________________________________________________________________________________________

lista_nomi_A = ["andrea","alfonso","ambrogio","anna","anastasia","angelica","armando"]
lista_cose_A = ["acqua","aria","ago","album","arco","armadio","astuccio","ancora"]
lista_stati_A = ["arabia saudita","afghanistan","alabama","america","albania","alaska","andorra"]
#______________________________________________________________________________________________________________

lista_nomi_B = ["baldo","brambilla","bartolomeo","beatrice","benito","berardo","busso"]
lista_cose_B = ["bacchetta","bagaglio","balestra","bandiera","banco","barattolo","bomba"]
lista_stati_B = ["bangladesh","belgio","bielorussia","bosnia","brasile","bolivia"]
#______________________________________________________________________________________________________________

lista_nomi_C = ["christian","chiara","cione","cristofaro","camilla","claudio","caterina"]
lista_cose_C = ["cacciavite","chiodo","calza","calamita","camicia","chitarra","campanella","cintura"]
lista_stati_C = ["california","ciad","cile","cina","canada","corea","croazia"]
#______________________________________________________________________________________________________________

lista_nomi_D = ["dario","daniele","donato","daria","deniso","demo","diaco"]
lista_cose_D = ["dado","dente","dito","dondolo","disco","diamante","dipinto","diedro"]
lista_stati_D = ["dominicana","danimarca","delaware","dani","dakota"]
#______________________________________________________________________________________________________________

lista_nomi_E = ["edoardo","edmundo","enrico","efesto","esseba","elena","eleonora"]
lista_cose_E = ["elastico","elicottero","estintore","elmo","elettrone","esagono","esofago"]
lista_stati_E = ["ecuador","egitto","estonia","eritrea","etiopia","emirati arabi"]
#______________________________________________________________________________________________________________

lista_nomi_F = ["farè","francesca","federico","franco","francesco","fabrizio","fernandez"]
lista_cose_F = ["forno","frigo","felpa","fazzoletto","finestra","fischietto","flauto","fisarmonica"]
lista_stati_F = ["figi","filippine","finlandia","florida","francia"]
#______________________________________________________________________________________________________________

lista_nomi_G = ["gaia","gabriele","gerardo","gertrude","giacomo","giovanni","gonzalez"]
lista_cose_G = ["galeone","gelato","gioco","gesso","gioiello","gomma","guanti","guscio"]
lista_stati_G = ["germania","georgia","guinea","giordania","grecia","ghana","giappone"]
#______________________________________________________________________________________________________________

#funzioni
def print_regole():
    print("-------------------------------------------------------------------------------------------------------")
    print("Le regole sono semplici:")
    time.sleep(1.0)
    print("1. Verrà generata una lettera casuale tra A e G")
    time.sleep(1.0)
    print("2. Dovrai inserire le parole richieste con la lettera iniziale uguale a quella generata")
    time.sleep(1.0)
    print("3. Ti verrà assegnato un punteggio di: ")
    time.sleep(1.0)
    print("0 punti se la parola inserita non è presente all'interno della lista e la lettera iniziale è diversa")
    time.sleep(1.0)
    print("5 punti se la parola inizia con la lettera corretta ma non è nell'elenco")
    time.sleep(1.0)
    print("10 punti se la parola è corretta ed è nella lista del programma")
    print("-------------------------------------------------------------------------------------------------------")
#______________________________________________________________________________________________________________

#inizio
print("")
print("--------NOMI-COSE-STATI--------")
print("")
print("Benvenuto nel gioco di nomi cose e stati!")
print("") 
time.sleep(1.0)
print("Durante il gioco inserisci 's' per approvare una domanda")
print("") 
time.sleep(1.0)
vuoi_iniziare = str(input("Desideri iniziare? "))
print("")
if (vuoi_iniziare == "s"):
    regole = str(input("Vuoi consoscere le regole del gioco? "))
    if(regole == "s"):
            print_regole()
    while continuare == "s":
        if (x == 6):
            break
        lettera_random:str = random.choice(lettera)
        print("")        
        print("La lettera generata è " + str(lettera_random))
        print("") 
#______________________________________________________________________________________________________________

#lettera "A"
        if(lettera_random == "A"):
            nome = input("-inserisci un nome che inizi con la lettera " + str(lettera_random) + ":")
            if(nome[0] == "a"):
                punteggio = punteggio + 5
                if(nome in lista_nomi_A):
                    punteggio = punteggio + 5
                else:
                    punteggio = punteggio
            print("")
            cosa = input("-inserisci una cosa che inizi con la lettera " + str(lettera_random) + ":")
            if(cosa[0] == "a"):
                punteggio = punteggio + 5
                if(cosa in lista_cose_A):
                    punteggio = punteggio + 5
            else:
                punteggio = punteggio        
            print("")    
            stato = input("-inserisci uno stato che inizi con la lettera " + str(lettera_random) + ":")
            if(stato[0] == "a"):
                punteggio = punteggio + 5
                if(cosa in lista_stati_A):
                    punteggio = punteggio + 5
            else:
                punteggio = punteggio
            lettera.remove(lettera_random)
            i = i + 3
            print("") 
            continuare = input("Desideri continuare? ")
            x = x + 1     
#______________________________________________________________________________________________________________

#lettera "B"
        if(lettera_random == "B"):
            nome = input("-inserisci un nome che inizi con la lettera " + str(lettera_random) + ":")
            if(nome[0] == "b"):
                punteggio = punteggio + 5
                if(nome in lista_nomi_B):
                    punteggio = punteggio + 5
            print("")    
            cosa = input("-inserisci una cosa che inizi con la lettera " + str(lettera_random) + ":")
            if(cosa[0] == "b"):
                punteggio = punteggio + 5
                if(cosa in lista_cose_B):
                    punteggio = punteggio + 5
            print("")    
            stato = input("-inserisci uno stato che inizi con la lettera " + str(lettera_random) + ":")
            if(stato[0] == "b"):
                punteggio = punteggio + 5
                if(stato in lista_stati_B):
                    punteggio = punteggio + 5
            else:
                punteggio = punteggio
            lettera.remove(lettera_random)
            i = i + 3
            print("") 
            continuare = input("Desideri continuare? ")
            x = x + 1               
#______________________________________________________________________________________________________________

#lettera "C"
        if(lettera_random == "C"):
            nome = input("-inserisci un nome che inizi con la lettera " + str(lettera_random) + ":")
            if(nome[0] == "c"):
                punteggio = punteggio + 5
                if(nome in lista_nomi_C):
                    punteggio = punteggio + 5
            print("")    
            cosa = input("-inserisci una cosa che inizi con la lettera " + str(lettera_random) + ":")
            if(cosa[0] == "c"):
                punteggio = punteggio + 5
                if(cosa in lista_cose_C):
                    punteggio = punteggio + 5
            print("")    
            stato = input("-inserisci uno stato che inizi con la lettera " + str(lettera_random) + ":")
            if(stato[0] == "c"):
                punteggio = punteggio + 5
                if(stato in lista_stati_C):
                    punteggio = punteggio + 5
            else:
                punteggio = punteggio
            lettera.remove(lettera_random)
            i = i + 3
            print("") 
            continuare = input("Desideri continuare? ")
            x = x + 1     
#______________________________________________________________________________________________________________

#lettera "D"
        if(lettera_random == "D"):
            nome = input("-inserisci un nome che inizi con la lettera " + str(lettera_random) + ":")
            if(nome[0] == "d"):
                punteggio = punteggio + 5
                if(nome in lista_nomi_D):
                    punteggio = punteggio + 5
            print("")    
            cosa = input("-inserisci una cosa che inizi con la lettera " + str(lettera_random) + ":")
            if(cosa[0] == "d"):
                punteggio = punteggio + 5
                if(cosa in lista_cose_D):
                    punteggio = punteggio + 5
            print("")    
            stato = input("-inserisci uno stato che inizi con la lettera " + str(lettera_random) + ":")
            if(stato[0] == "d"):
                punteggio = punteggio + 5
                if(stato in lista_stati_D):
                    punteggio = punteggio + 5
            else:
                punteggio = punteggio
            lettera.remove(lettera_random)
            i = i + 3
            print("") 
            continuare = input("Desideri continuare? ")
            x = x + 1 
#______________________________________________________________________________________________________________

#lettera "E"
        if(lettera_random == "E"):
            nome = input("-inserisci un nome che inizi con la lettera " + str(lettera_random) + ":")
            if(nome[0] == "e"):
                punteggio = punteggio + 5
                if(nome in lista_nomi_E):
                    punteggio = punteggio + 5
            print("")    
            cosa = input("-inserisci una cosa che inizi con la lettera " + str(lettera_random) + ":")
            if(cosa[0] == "e"):
                punteggio = punteggio + 5
                if(cosa in lista_cose_E):
                    punteggio = punteggio + 5
            print("")    
            stato = input("-inserisci uno stato che inizi con la lettera " + str(lettera_random) + ":")
            if(stato[0] == "e"):
                punteggio = punteggio + 5
                if(stato in lista_stati_E):
                    punteggio = punteggio + 5
            else:
                punteggio = punteggio
            lettera.remove(lettera_random)
            i = i + 3
            print("") 
            continuare = input("Desideri continuare? ")
            x = x + 1 
#______________________________________________________________________________________________________________

#lettera "F"
        if(lettera_random == "F"):
            nome = input("-inserisci un nome che inizi con la lettera " + str(lettera_random) + ":")
            if(nome[0] == "f"):
                punteggio = punteggio + 5
                if(nome in lista_nomi_F):
                    punteggio = punteggio + 5
            print("")    
            cosa = input("-inserisci una cosa che inizi con la lettera " + str(lettera_random) + ":")
            if(cosa[0] == "f"):
                punteggio = punteggio + 5
                if(cosa in lista_cose_F):
                    punteggio = punteggio + 5
            print("")    
            stato = input("-inserisci uno stato che inizi con la lettera " + str(lettera_random) + ":")
            if(stato[0] == "f"):
                punteggio = punteggio + 5
                if(stato in lista_stati_F):
                    punteggio = punteggio + 5
            else:
                punteggio = punteggio
            lettera.remove(lettera_random)
            i = i + 3
            print("") 
            continuare = input("Desideri continuare? ")
            x = x + 1
#______________________________________________________________________________________________________________

#lettera "G"
        if(lettera_random == "G"):
            nome = input("-inserisci un nome che inizi con la lettera " + str(lettera_random) + ":")
            if(nome[0] == "g"):
                punteggio = punteggio + 5
                if(nome in lista_nomi_G):
                    punteggio = punteggio + 5
            print("")
            cosa = input("-inserisci una cosa che inizi con la lettera " + str(lettera_random) + ":")
            if(cosa[0] == "g"):
                punteggio = punteggio + 5
                if(cosa in lista_cose_G):
                    punteggio = punteggio + 5
            print("")    
            stato = input("-inserisci uno stato che inizi con la lettera " + str(lettera_random) + ":")
            if(stato[0] == "g"):
                punteggio = punteggio + 5
                if(stato in lista_stati_G):
                    punteggio = punteggio + 5
            else:
                punteggio = punteggio
            lettera.remove(lettera_random)
            i = i + 3
            print("") 
            continuare = input("Desideri continuare? ")
            x = x + 1
#______________________________________________________________________________________________________________ 

#stampa finale
    print("-------------------------------------------------------------------------------------------------------")
    print("IL TUO PUNTEGGIO: " + str(punteggio))
    percentuale_punteggio = punteggio / (i * 10) * 100
    if(percentuale_punteggio == 100):
        print("Hai ottenuto un punteggio perfetto, complimenti!")
    if(percentuale_punteggio < 100 and percentuale_punteggio >= 75):
        print("Bravo, non è il massimo ma c'eri vicino!")
    if(percentuale_punteggio < 75 and percentuale_punteggio >= 50):
        print("Non male ma puoi fare di meglio!")
    if(percentuale_punteggio < 50 and percentuale_punteggio >= 25 ):
        print("Non è andata malissimo ma cerca di superare il 50% dei punti totali!")
    if(percentuale_punteggio < 25 ):
        print("Che delusione! Vedi di riprovare!")
    print("")