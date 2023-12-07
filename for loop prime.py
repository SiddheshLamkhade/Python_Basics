n=int(input("Enter a no="))
if n>2:
    for i in range(2,n):
        if (n%i==0):
            print("no. is not prime")
        else:
            print("no. is prime")
        break
else:
    print("Given no is not prime")

