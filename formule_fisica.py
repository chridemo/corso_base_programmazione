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
vuoi_iniziare = input("inserire 'inizia' per iniziare: ")
if(vuoi_iniziare == "inizia"):
  print("- m.r.u.")
  print("- m.r.u.a.")
  print("- m.c.u.")
  print("- m.p.")
  inserisci_moto = input("inserisre il moto interessato: ")
# m.r.u.
if(inserisci_moto == "mru"):
  print("- legge oraria inserire 'lo'")    
  print("- legge oraria, t0 = 0 inserire 'lo,t0'")
  print("- legge oraria, t0 = 0, x0 = 0 inserire 'lo,t0,x0'")
  inserisci_legge = input("inserire la legge interessata: ")
  if(inserisci_legge == "lo,t0,x0"):
    v = int(input("inserire la velocità: "))
    t = int(input("inserire il tempo: "))
    legge_oraria_x_t = v * t 
    print("")
    print( "x = " + str(legge_oraria_x_t) + " m")
    print("")
    input = ("exit")
  if(inserisci_legge == "lo,t0"):
    v = int(input("inserire la velocità: "))
    t = int(input("inserire il tempo: "))
    x0 = int(input("inserire la posizione iniziale: "))
    legge_oraria_t = v * t + x0
    print("")
    print("x = " + str(legge_oraria_t) + " m")
    print("")
    input = ("exit")
  if(inserisci_legge == "lo"):
    x0 = int(input("inserire la posizione iniziale: "))
    t = int(input("inserire il tempo finale: "))
    t0 = int(input("inserire il tempo iniziale: "))
    v = int(input("inserire la velocità: "))
    legge_oraria = v * (t - t0) + x0
    print("")
    print("x = " + str(legge_oraria) + " m")
    print("")
    input = ("exit")
# m.r.u.a.
if(inserisci_moto == "mrua"):
  print("- accellerazione media inserire 'am'")
  print("- legge della velocità inserire 'lv'")
  print("- legge della velocità, t0 = 0 inserire 'lv,t0'")
  print("- legge della velocità, t0 = 0, v0 = 0 inserire 'lv,t0,v0'")
  print("- legge oraria inserire 'lo'")                
  print("- legge oraria, v0 = 0 inserire 'lo,v0'")
  print("- legge oraria, v0 = 0, x0 = 0 inserire 'lo,v0,x0'")
  inserisci_legge = input("inserire la legge interessata: ")
  if(inserisci_legge == "am"):
    delta_v = int(input("inserire la variazione di velocità: "))
    delta_t = int(input("inserire l'intervallo di tempo: "))
    accellerazione_media = delta_v / delta_t
    print("")
    print("am = " + str(accellerazione_media) + " m/s^2")
    print("")
    input = ("exit")
  if(inserisci_legge == "lo"):
    x0 = int(input("inserire la posizione iniziale: "))
    v0 = int(input("inserire la velocità iniziale: "))
    t = int(input("inserire l'intervallo tempo: "))
    a = int(input("inserire l'accellerazione: "))
    legge_oraria = x0 + v0 * t + a / 2 * (t * t)
    print("")
    print("x = " + str(legge_oraria) + " m")
    print("")
    input = ("exit")
  if(inserisci_legge == "lo,v0"):
    x0 = int(input("inserire la posizione iniziale: "))
    t = int(input("inserire l'intervallo tempo: "))
    a = int(input("inserire l'accellerazione: "))
    legge_oraria = x0 + a / 2 * (t * t)
    print("")
    print("x = " + str(legge_oraria) + " m")
    print("")
    input = ("exit")
  if(inserisci_legge == "lo,v0,x0"):
    t = int(input("inserire l'intervallo tempo: "))
    a = int(input("inserire l'accellerazione: "))
    legge_oraria = (a / 2) * t * t
    print("")
    print("x = " + str(legge_oraria) + " m")
    print("")
  if(inserisci_legge == "lv"):
    v0 = int(input("inserire la velocità iniziale: "))
    a = int(input("inserire l'accellerazione: "))
    t = int(input("inserire l'intervallo tempo: "))
    t0 = int(input("inserire il tempo iniziale"))
    legge_velocità = v0 + a * (t - t0)
    print("")
    print("x = " + str(legge_velocità) + " m/s")
    print("")
  if(inserisci_legge == "lv,t0"):  
    v0 = int(input("inserire il tempo iniziale"))
    a = int(input("inserire l'accellerazione: "))
    t = int(input("inserire l'intervallo tempo: "))
    legge_velocità = v0 + a * t
  if(inserisci_legge == "lv,t0,v0"):
    a = int(input("inserire l'accellerazione: "))
    t = int(input(("inserire l'intervallo di tempo: ")))
    legge_velocità = a * t
    print("")
    print("x = " + str(legge_velocità) + " m/s")
    print("")
# m.c.u.
if(inserisci_moto == "mcu"):
  print("- accellerazione centripeta inserire 'ac'")
  print("- frequenza inserire 'f'")
  print("- periodo inserire 'p'")
  print("- velocità con periodo inserire 'v,p'")
  print("- velocità con frequenzainserire 'v,f'")
  inserisci_legge = input("inserire la legge interessata: ")
  if(inserisci_legge == "ac"):
    v = int(input("inserire la velocità: "))
    r = int(input("inserire il raggio: "))
    accellerazione_centripeta = (v * v) / r
    print("")
    print("ac = " + str(accellerazione_centripeta) + " m/s^2")
    print("")
  if(inserisci_legge == "f"):
    p = int(input("inserire il periodo: "))
    frequenza = 1 / p
    print("")
    print("f = " + str(frequenza) + " Hz")
    print("")
  if(inserisci_legge == "p"):
    f = int(input("inserici la frequenza: "))
    periodo = 1 / f
    print("")
    print("p = " + str(periodo) + " s")
    print("")
  if(inserisci_legge == "v,p"):
    r = int(input("inserici il raggio: "))
    p = int(input("inserici il periodo: "))
    velocità_periodo = (6.28 * r) / p
    print("")
    print("v = " + str(velocità_periodo) + " m/s")
    print("")
  if(inserisci_legge == "v,f"):
    r = int(input("inserici il raggio: "))
    f = int(input("inserici la frequenza: "))
    velocità_frequenza = (6.28 * r) * f
    print("")
    print("v = " + str(velocità_frequenza) + " m/s")
    print("")
# m.p. 
if(inserisci_moto == "mp"):
  print("- legge oraria x inserire 'lo,x'")
  print("- legge oraria x, x0 = 0 inserire 'lo,x,x0'")
  print("- legge oraria y inserire 'lo,y'")
  print("- legge oraria y, v0 = 0 inserire 'lo,y,v0'")
  print("- legge oraria y, v0 = 0, y0 = 0 inserire 'lo,y,v0,y0'")
  print("- legge della velocità x inserire 'lv,x'")                
  print("- legge della velocità y inserire 'lv,y'")
  print("- legge della velocità y, v0 = 0 inserire 'lv,y,v0'")
  inserisci_legge = input("inserire la legge interessata: ")
  if(inserisci_legge == "lo,x"):
    x0 = int(input("inserire la posizione iniziale: "))
    v0 = int(input("inserire la velocità iniziale: "))
    t = int(input("inserire l'intervallo di tempo: "))
    legge_oraria_x = x0 + v0 * t
    print("")
    print("x = " + str(legge_oraria_x) + " m")
    print("")
    input = ("exit")
  if(inserisci_legge == "lo,x,x0"):
    v0 = int(input("inserire la velocità iniziale: "))
    t = int(input("inserire l'intervallo di tempo: "))
    legge_oraria_x = v0 * t
    print("")
    print("x = " + str(legge_oraria_x) + " m")
    print("")
    input = ("exit")
  if(inserisci_legge == "lo,y"):
    y0 = int(input("inserire la posizione iniziale: "))
    v0 = int(input("inserire la velocità iniziale: "))
    t = int(input("inserire l'intervallo di tempo: "))
    a = int(input("inserire l'accellerazione: "))
    legge_oraria_y = y0 + v0 * t + (a / 2)* (t * t)
    print("")
    print("x = " + str(legge_oraria_y) + " m")
    print("")
    input = ("exit")
  if(inserisci_legge == "lo,y,v0"):
    y0 = int(input("inserire la posizione iniziale: "))
    t = int(input("inserire l'intervallo di tempo: "))
    a = int(input("inserire l'accellerazione: "))
    legge_oraria_y = y0 + (a / 2)* (t * t)
    print("")
    print("x = " + str(legge_oraria_y) + " m")
    print("")
    input = ("exit")
  if(inserisci_legge == "lo,y,v0,y0"):
    t = int(input("inserire l'intervallo di tempo: "))
    a = int(input("inserire l'accellerazione: "))
    legge_oraria_y =  (a / 2)* (t * t)
    print("")
    print("x = " + str(legge_oraria_y) + " m")
    print("")
    input = ("exit")
  if(inserisci_legge == "lv,x"):
    v0 = int(input("inserire la velocità iniziale: "))
    legge_velocità_x = v0
    print("")
    print("x = " + str(legge_velocità_x) + " m/s")
    print("")
    input = ("exit")
  if(inserisci_legge == "lv,y"):
    v0 = int(input("inserire la velocitlà iniziale: "))
    t = int(input("inserire l'intervallo di tempo: "))
    a = int(input("inserire l'accellerazione: "))
    legge_velocità_y = v0 + a * t
    print("")
    print("x = " + str(legge_velocità_y) + " m/s")
    print("")
    input = ("exit")
  if(inserisci_legge == "lv,y"):
    t = int(input("inserire l'intervallo di tempo: "))
    a = int(input("inserire l'accellerazione: "))
    legge_velocità_y = a * t
    print("")
    print("x = " + str(legge_velocità_y) + " m/s")
    print("")
    input = ("exit")