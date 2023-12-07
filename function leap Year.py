def yearfun(y):
    """
    Normally leap year is exactly divisible by 4
    leap year=366 days
    normal year=365 days
    e.g 1900 is divisible by 4 but it is NOT leap year
    
    """
    if(y%4==0 and y%100!=0 or y%400==0):
        print(y,"is leap year")
    else:
        print(y,"is NOT leap year")
yearfun(y=int(input("Enter Year=")))
print(yearfun.__doc__)