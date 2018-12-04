#PROGRAM : PRIME NUMBER
#NAME : SHUBHAM DESHPANDE
#ROLL.NO. : 57
# GR.NO. : 11810105
#DIVISION : M
def prime(x):
    i=2
    while i<x:
        if x%i==0:
            t=1
            break
        else:
            t=0
        i+=1
    if t==1:
        print("IT'S NOT A PRIME NUMBER")
    else:
        print("IT'S A PRIME NUMBER")
y=int(input("ENTER THE NUMBER : "))
prime(y)
