
somma = 0
while True:
    stringa = int(input("inserisci una stringa con sole cifre: "))
    is_1_2_3_present = "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in stringa
    print(is_1_2_3_present)
    #if(is_1_2_3_present == "true"):
     #   somma = somma + is_1_2_3_present