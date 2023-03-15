v = 0
t = 0
x0 = 0
t0 = 0
delta_v = 0
delta_t = 0
v0 = 0
a = 0
r = 0
p = 0
f = 0
y0 = 0
while True:
    print("Benvenuto nel formulario di fisica!")
    print("")
    print("- mru inserire (1)")
    print("- mrua inserire (2)")
    print("- mcu inserire (3)")
    print("- mcp inserire (4)")
    print("- per uscire inserire (0)")
    moto = int(input("inserisci il moto: "))
    
    if(moto == 0):
        break
    
    if (moto == 1):
        print("----------------------------------------------------")
        print("- legge oraria inserire (1,1)")    
        print("- legge oraria, t0 = 0 inserire (2,1)")
        print("- legge oraria, t0 = 0, x0 = 0 inserire (3,1)")
        inserisci_legge = input("inserire la legge interessata: ")
        if(inserisci_legge == "3,1"):
            v = int(input("inserire la velocità: "))
            t = int(input("inserire il tempo: "))
            legge_oraria_t_x = v * t
             
            print("")
            print( "x = " + str(legge_oraria_t_x) + " m")
            print("")
            

        if(inserisci_legge == "2,1"):
            v = int(input("inserire la velocità: "))
            t = int(input("inserire il tempo: "))
            x0 = int(input("inserire la posizione iniziale: "))
            legge_oraria_t = v * t + x0
            print("")
            print("x = " + str(legge_oraria_t) + " m")
            print("")
        
        if(inserisci_legge == "1,1"):
            x0 = int(input("inserire la posizione iniziale: "))
            t = int(input("inserire il tempo finale: "))
            t0 = int(input("inserire il tempo iniziale: "))
            v = int(input("inserire la velocità: "))
            legge_oraria = v * (t - t0) + x0
            print("")
            print("x = " + str(legge_oraria) + " m")
            print("")
        
    if (moto == 2):
        print("----------------------------------------------------")
        print("- accellerazione media inserire (1,2)")
        print("- legge della velocità inserire (2,2)")
        print("- legge della velocità, t0 = 0 inserire (3,2)")
        print("- legge della velocità, t0 = 0, v0 = 0 inserire (4,2))")
        print("- legge oraria inserire (5,2)")                
        print("- legge oraria, v0 = 0 inserire (6,2)")
        print("- legge oraria, v0 = 0, x0 = 0 inserire (7,2)")
        inserisci_legge = input("inserire la legge interessata: ")   
        if(inserisci_legge == "1,2"):
            delta_v = int(input("inserire la variazione di velocità: "))
            delta_t = int(input("inserire l'intervallo di tempo: "))
            accellerazione_media = delta_v / delta_t
            print("")
            print("am = " + str(accellerazione_media) + " m/s^2")
            print("")
        
        if(inserisci_legge == "5,2"):
            x0 = int(input("inserire la posizione iniziale: "))
            v0 = int(input("inserire la velocità iniziale: "))
            t = int(input("inserire l'intervallo tempo: "))
            a = int(input("inserire l'accellerazione: "))
            legge_oraria = x0 + v0 * t + a / 2 * (t * t)
            print("")
            print("x = " + str(legge_oraria) + " m")
            print("")
        
        if(inserisci_legge == "6,2"):
            x0 = int(input("inserire la posizione iniziale: "))
            t = int(input("inserire l'intervallo tempo: "))
            a = int(input("inserire l'accellerazione: "))
            legge_oraria = x0 + a / 2 * (t * t)
            print("")
            print("x = " + str(legge_oraria) + " m")
            print("")
        
        if(inserisci_legge == "7,2"):
            t = int(input("inserire l'intervallo tempo: "))
            a = int(input("inserire l'accellerazione: "))
            legge_oraria = (a / 2) * t * t
            print("")
            print("x = " + str(legge_oraria) + " m")
            print("")
        
        if(inserisci_legge == "2,2"):
            v0 = int(input("inserire la velocità iniziale: "))
            a = int(input("inserire l'accellerazione: "))
            t = int(input("inserire l'intervallo tempo: "))
            t0 = int(input("inserire il tempo iniziale: "))
            legge_velocità = v0 + a * (t - t0)
            print("")
            print("x = " + str(legge_velocità) + " m/s")
            print("")
        
        if(inserisci_legge == "3,2"):  
            v0 = int(input("inserire il tempo iniziale: "))
            a = int(input("inserire l'accellerazione: "))
            t = int(input("inserire l'intervallo tempo: "))
            legge_velocità = v0 + a * t
            print("")
            print("x = " + str(legge_velocità) + " m/s")
            print("")
          
        if(inserisci_legge == "4,2"):
            a = int(input("inserire l'accellerazione: "))
            t = int(input(("inserire l'intervallo di tempo: ")))
            legge_velocità = a * t
            print("")
            print("x = " + str(legge_velocità) + " m/s")
            print("")
        
    if (moto == 3):
        print("----------------------------------------------------")
        print("- accellerazione centripeta inserire (1,3)")
        print("- frequenza inserire (2,3)")
        print("- periodo inserire (3,3)")
        print("- velocità con periodo inserire (4,3)")
        print("- velocità con frequenzainserire (5,3)")
        inserisci_legge = input("inserire la legge interessata: ")
        if(inserisci_legge == "1,3"):
            v = int(input("inserire la velocità: "))
            r = int(input("inserire il raggio: "))
            accellerazione_centripeta = (v * v) / r
            print("")
            print("ac = " + str(accellerazione_centripeta) + " m/s^2")
            print("")
        
        if(inserisci_legge == "2,3"):
            p = int(input("inserire il periodo: "))
            frequenza = 1 / p
            print("")
            print("f = " + str(frequenza) + " Hz")
            print("")
        
        if(inserisci_legge == "3,3"):
            f = input("inserire la frequenza: ")
            periodo = 1 / f
            print("")
            print("p = " + str(periodo) + " s")
            print("")
        
        if(inserisci_legge == "4,3"):
            r = int(input("inserire il raggio: "))
            p = int(input("inserire il periodo: "))
            velocità_periodo = (6.28 * r) / p
            print("")
            print("v = " + str(velocità_periodo) + " m/s")
            print("")
        
        if(inserisci_legge == "5,3"):
            r = int(input("inserire il raggio: "))
            f = int(input("inserire la frequenza: "))
            velocità_frequenza = (6.28 * r) * f
            print("")
            print("v = " + str(velocità_frequenza) + " m/s")
            print("")
        
    if (moto == 4):
        print("----------------------------------------------------")
        print("- legge oraria x inserire (1,4)")
        print("- legge oraria x, x0 = 0 inserire (2,4)")
        print("- legge oraria y inserire (3,4)")
        print("- legge oraria y, v0 = 0 inserire (4,4)")
        print("- legge oraria y, v0 = 0, y0 = 0 inserire (5,4)")
        print("- legge della velocità x inserire (6,4)")                
        print("- legge della velocità y inserire (7,4)")
        print("- legge della velocità y, v0 = 0 inserire (8,4)")
        inserisci_legge = input("inserire la legge interessata: ")
        if(inserisci_legge == "1,4"):
            x0 = int(input("inserire la posizione iniziale: "))
            v0 = int(input("inserire la velocità iniziale: "))
            t = int(input("inserire l'intervallo di tempo: "))
            legge_oraria_x = x0 + v0 * t
            print("")
            print("x = " + str(legge_oraria_x) + " m")
            print("")
        
        if(inserisci_legge == "2,4"):
            v0 = int(input("inserire la velocità iniziale: "))
            t = int(input("inserire l'intervallo di tempo: "))
            legge_oraria_x = v0 * t
            print("")
            print("x = " + str(legge_oraria_x) + " m")
            print("")
        
        if(inserisci_legge == "3,4"):
            y0 = int(input("inserire la posizione iniziale: "))
            v0 = int(input("inserire la velocità iniziale: "))
            t = int(input("inserire l'intervallo di tempo: "))
            a = int(input("inserire l'accellerazione: "))
            legge_oraria_y = y0 + v0 * t + (a / 2)* (t * t)
            print("")
            print("x = " + str(legge_oraria_y) + " m")
            print("")
        
        if(inserisci_legge == "4,4"):
            y0 = int(input("inserire la posizione iniziale: "))
            t = int(input("inserire l'intervallo di tempo: "))
            a = int(input("inserire l'accellerazione: "))
            legge_oraria_y = y0 + (a / 2)* (t * t)
            print("")
            print("x = " + str(legge_oraria_y) + " m")
            print("")
        
        if(inserisci_legge == "5,4"):
            t = int(input("inserire l'intervallo di tempo: "))
            a = int(input("inserire l'accellerazione: "))
            legge_oraria_y =  (a / 2)* (t * t)
            print("")
            print("x = " + str(legge_oraria_y) + " m")
            print("")
        
        if(inserisci_legge == "6,4"):
            v0 = int(input("inserire la velocità iniziale: "))
            legge_velocità_x = v0
            print("")
            print("x = " + str(legge_velocità_x) + " m/s")
            print("")
              
        if(inserisci_legge == "7,4"):
            v0 = int(input("inserire la velocitlà iniziale: "))
            t = int(input("inserire l'intervallo di tempo: "))
            a = int(input("inserire l'accellerazione: "))
            legge_velocità_y = v0 + a * t
            print("")
            print("x = " + str(legge_velocità_y) + " m/s")
            print("")
        
        if(inserisci_legge == "8,4"):
            t = int(input("inserire l'intervallo di tempo: "))
            a = int(input("inserire l'accellerazione: "))
            legge_velocità_y = a * t
            print("")
            print("x = " + str(legge_velocità_y) + " m/s")
            print("")
            
input = ("exit")
