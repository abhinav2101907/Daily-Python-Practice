#Basic Question
#1.) Write a program to print all elements of a list using a for loop.
#2.) Find the sum of all numbers in a list using a loop (no sum()).
#3.) Count how many even and odd numbers are in a list.
#4.) Find the largest and smallest element in a list without using max() or min().
#5.) Reverse a list using a loop (do not use slicing or reverse()).
#6.) Print all numbers divisible by 3 from a list.
'''lst = [12, 7, 5, 18, 3, 10]
for i in lst:
    print(i)'''
'''lst = [12, 7, 5, 18, 3, 10]
sum1 = 0
for i in lst:
    sum1 += i
print(sum1)
'''
'''lst = [12, 7, 5, 18, 3, 10]
count1 = 0
count2 = 0
for i in lst:
    if i%2 == 0:
        count1 +=1
    else:
        count2 +=1


print("total even are =",count1)
print("total odd are =",count2)'''
'''lst = [12, 7, 5, 18, 3, 10]
largest = lst[0]
smallest = lst[0]
for i in lst:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i
print(smallest)
print(largest)
'''
'''lst = [12, 7, 5, 18, 3, 10]
arr = []
for i in lst[::-1]:
    arr.append(i)
print(arr)
'''
'''lst = [12, 7, 5, 18, 3, 10]
arr=[]
for i in lst:
    if i%3==0:
        arr.append(i)
print(arr)'''
#Q7.)Remove all duplicate elements from a list using loops.
#Q8.)Find the second largest number in a list.
#Q9.)Check whether a list is sorted or not.
#Q10.)Rotate a list to the left by k positions.
#Q11.)Find all elements that appear more than once and print them.
#Q12.)Merge two lists and sort the result without using sort().



'''lst = [12, 7, 5, 18, 3, 10, 4, 5, 7]
arr=[]
for i in lst:
    if i not in arr:
        arr.append(i)
print(arr)'''
#q7
'''lst = [12, 7, 5, 18, 3, 10, 4, 5, 7]
i = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        if lst[i] == lst[j]:
            lst.pop(j)
        else:
            j+=1
    i+= 1
print(lst)'''
#q8
'''lst = [12, 7, 5, 18, 3, 10, 4, 12]
l1 = lst[0]
l2 = None
for i in lst:
    if i > l1:
        l2= l1
        l1 = i
    elif i<l1 and(l2 is None or l2<i):
        l2 = i
print(l2)
'''
#q9

'''lst = [12, 7, 5, 18, 3, 10, 4]
flag = 0
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        flag = 1
        break
    else:
        flag = 0

if (flag == 1):
    print("not sorted")
else:
    print("sorted")'''






























