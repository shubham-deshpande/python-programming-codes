#PROGRAM : ARMSTRONG NUMBER
#NAME : SHUBHAM DESHPANDE
#ROLL.NO. : 57
#GR.NO. : 11810105
#DIVISION : 11810105
def armstrong(n):
    sum=0
    t=n
    while t>0:
        d=t%10
        sum=t**3
        t=t/10
    return sum
n=int(input("ENTER A NUMBER="))
y=armstrong(n)
if y==n:
    print(str(n)+" IS AN ARMSTRONG NUMBER")
else:
    print(str(n)+" IS NOT AN ARMSTRONG NUMBER")
