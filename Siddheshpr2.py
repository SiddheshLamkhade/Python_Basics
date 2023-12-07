# EXPERIMENT NO 02
#Write a python program to store  marks stored in subject "Fundamental of data structure" 


#function for average score of the class
def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            sum+=listofmarks[i]
            count=count+1
    avg=sum/count
    print("Total marks: ",sum)
    print("Average marks: {:.2f}".format(avg))
#--------------------------------------------------

#function for Highest score in the test for the class

def maximum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            max=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]>max:
            max=listofmarks[i]
        return (max)
#--------------------------------------------------------

#Function for lowest score in the class

def minimum(listofmarks):
    for i in range (len(listofmarks)):
        if listofmarks[i]!=-999:
           min = listofmarks[0]
           break 
    for i in range (1,len(listofmarks)):
        if listofmarks[i]<min:
            min=listofmarks[i]
    return (min)

#-----------------------------------------------

#function for counting absent no of students

def absentcount(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            count+=1
    return(count)

#--------------------------------------------------------

#function for displaying marks with highest frequency

def maxfrequency(listofmarks):
    i=0
    max=0
    print("Marks | Frequency ")
    for j in listofmarks:
        if listofmarks.index(j)==i:
            print(j," | ",listofmarks.count(j))
            if listofmarks.count(j)>max:
                max=listofmarks.count(j)
                mark=j
        i=i+1
    return(mark,max)
#--------------------------------------------------------


#Main function

marksinFDS =[]
numberofstudents=int(input("Enter total no of students :- "))
for i in range(numberofstudents):
    marks = int(input("marks of students :- "+ str (i+1)+":"))
    marksinFDS.append(marks)
flag=1
while flag==1:
    print("\n\n---------------MENU-----------------")
    print("1: Total and average marks of class")
    print("2: Highest and Lowest of Marks")
    print("3: No of students absent for test")
    print("4: Marks with Highest Frequency")
    print("5: Exit\n")
    ch=int(input("Enter your choice (from 1 to 5):"))

    if ch ==1:
        average(marksinFDS)
        a=input("Do you want to cotinue(yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program !!!")
    elif ch ==2:
        print("Highest Score in Class: ",maximum(marksinFDS))
        print("Lowest Score in Class: ",minimum(marksinFDS))
        a=input("Do you want to continue: (yes,no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program !!!")

   ''' elif ch ==
        print("Highest Score in Class: ",maximum(marksinFDS))
        print("Lowest Score in Class: ",minimum(marksinFDS))
        a=input("Do you want to continue: (yes,no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program !!!")'''


#-----------------------------------------------------------
