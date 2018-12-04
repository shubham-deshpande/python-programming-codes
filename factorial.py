#PROGRAM : FACTORIAL
#NAME : SHUBHAM DESHPANDE
#ROLL.NO. : 57
#GR.NO. : 11810105
#DIVISION: M
x=int(input("ENTER THE NUMBER TO FIND IT'S FACTORIAL="))
y=x
total=1
if x<0:
     print("FACTORIAL DOES NO EXISTS")
elif x==0 or x==1:
     print("FACTORIAL OF "+str(x)+" IS 1")
else:
     while x>0:
          total=x*total
          x-=1
     print("FACTORIAL OF "+str(y)+" IS "+str(total))
    
