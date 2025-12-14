#List
'''l1 = [2,4,1,3,5,7,4]
print(len(l1))'''
'''l1 = [2,34,2,1,5,6,23]
print(l1[4])'''
'''l1 = [2,34,2,1,5,6,23]
print(l1[-5])'''
#Sorting
'''l1 = [2,34,2,1,5,6,23]
l1.sort()
print(l1)'''
#insertion in list
'''l1 = []
n = int(input("enter how name no. to enter"))
for i in range(n):
    n = int(input("enter the no. you want to add"))
    l1.append(n)
print(l1)
'''
#inserting no. then printing the sorted array
'''def array(no,arr):
    for i in range(no):
        n = int(input("enter which no. to add"))
        arr.append(n)



no1 = int(input("enter how many no. you want to add"))
l1 = []
array(no1,l1)
l1.sort()
print(l1)'''
#list comprehension
'''l1 = [i for i in range(10)if i%2 == 0 ]
print(l1)'''
#Tuple
'''tup = (2,42,1,3,4)
l1 = list(tup)
l1.pop(4)
l1.insert(0,5)
tup = tuple(l1)
print(tup)'''
