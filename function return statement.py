n=int(input("Enter any no: "))
def squ(n):
    print("Square of",n,"is ") 
    return n*n
print(squ(n))  
"""if we use return statement them we can't call function directly as
                   in standard form as      functionname(var) 
                for that we have to use different syntax as      print(functionname(var))  """
#squ(8)    it not gives output