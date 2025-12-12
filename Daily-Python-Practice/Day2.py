#Break and Continue
#Searching the no. in array using break(linear search)
'''arr = [2,3,6,7,89,4,7,56,448,2]
no = int(input("enter the no. you to search"))
for i in arr:
    if(no == i):
        print("found")
        break
else:
    print("not found")'''
#Printing odd no. till 100 using Continue
'''for i in range(100):
    if (i%2 == 0):
        continue
    print(i)'''
#Printing even no. till 100
'''for i in range(102):
    if (i%2 == 1):
        continue
    print(i)'''
#Printing no. to 100
'''i = 0
while True:
    i = i + 1
    print(i)
    if(i%100 == 0):
        break'''
#Function
#Simple Calculator using Function
'''def calculator():
    if (n == 1):
        print("Solution =", a + b)
    elif (n == 2):
        print("Solution =", a - b)
    elif (n == 3):
        print("Solution =", a * b)
    elif (n == 4):
        print("Solution =", a / b)
    else:
        print("wrong selection")


a = int(input("enter the valur of a :"))
b = int(input("enter the value of b :"))
n = int(input("Select option for performance\n1 ,2 ,3 ,4 :"))
calculator()
'''
#driving eligibility using function
'''def license(age):
    if (age>=18):
        print("you can drive")
    else:
        print("no you cannot drive")


age = int(input("enter the age: "))
license(age)

n = int(input("enter the age: "))
license(n)
'''
#searching using function
'''def arr(no,array2):
    for i in array2:
        if (i == no):
            print("found")
            break
    else:
        print("not found")


array1=[2,4,45,32,66,75,34,76,34,38]
no1 = int(input("enter the no."))
arr(no1,array1)
'''
#appending in array
'''arr = []
no = int(input("enter how many no. you want to add :"))
for i in range(no):
    n = int(input("enter which no. to add"))
    arr.append(n)
print(arr)
'''
#appending in array using function
'''def array(no):
    arr = []
    for i in range(no):
        n = int(input("enter which no. to add"))
        arr.append(n)
    print(arr)


no1 = int(input("enter how many no. you want to add"))
array(no1)'''

'''def array():
    arr = []
    no = int(input("enter how many no. you want to add :"))
    for i in range(no):
        n = int(input("enter which no. to add"))
        arr.append(n)
    print(arr)

array()'''





