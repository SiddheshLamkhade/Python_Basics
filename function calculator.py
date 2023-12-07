add=lambda n,m:n+m
sub=lambda n,m:n-m
def mul(n,m):
    print(n*m)
def div(n,m):
    return n/m

print(" Operations          1. add               2. sub          3. mul              4. div")
ch=int(input("ENTER YOUR CHOICE="))  #Due to I forgot to type int here, program was not working that time.

n=int(input("Enter no: "))
m=int(input("Enter no: "))
if ch==1:                           #lambda fun hence variable name instead of lambda name with print
    print(add(n,m))                 
elif ch==2:                         #lambda fun hence variable name instead of lambda name with print
    print(sub(n,m))
elif ch==3:                         #standard fun functionname()   standard function calling
    mul(n,m)
else:                               #function with return statement hence functionname with print
    print(div(n,m))
print("↑↑↑ is your answer")