i = 0 
output = 0 
while True:
    a = int(input("inserisci un numero: "))
    if(a == 0):
     break
    else:   
        output = a + output
    i = i + 1
print(output)

input("press any key to exit")