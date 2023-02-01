#(105_conta_n_vocali) Conta il numero di vocali e stampane il risultato per ogni vocale. Giorgio. a=0, e=0, i=2, o=2, u=0
a:int = 0
e:int = 0
i:int = 0
o:int = 0
u:int = 0
stringa:str = input("inserisci una stringa: ")
n = len(stringa)
c:int = 0
while c < n:
    is_a_present:bool = "a" or "A" in stringa 
    if(is_a_present == "True"):
        a = a + 1
    is_e_present = "e" or "E" in stringa
    if(is_a_present == "True"):
        e = e + 1
    is_i_present = "i" or "I" in stringa 
    if(is_a_present == "True"):
        i = i + 1
    is_o_present = "o" or "O" in stringa 
    if(is_a_present == "True"):
        o = o + 1
    is_u_present = "u" or "U" in stringa 
    if(is_a_present == "True"):
        u = u + 1
    c = c + 1
print(a)
print(e)
print(i)
print(o)
print(u)