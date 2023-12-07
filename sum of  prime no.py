print("                   Sum of prime numbers till 'n'")
n=int(input("Enter a no="))
sum=0
print("Following are prime no.s")
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break   #Because it is not a prime no
        else:
            sum=sum+i
            print(i)
            break
print("                   sum of prime numbers is",sum)