#sets
'''a = {2,5,3,4,5}
print(a)'''
#add no. to a set
'''a = set()
n = int(input())
for i in range(n):
    n1 = int(input())
    a.add(n1)
print(a)'''
#union of a set
'''s1 = {2,4,3,5,9}
s2 = {2,8,7,9,4}
print(s1.union(s2))'''
#intersecction of set
'''s1 = {2,4,3,5,9}
s2 = {2,8,7,9,4}
print(s1.intersection(s2))'''
#find commom value in list
'''l1 =[2,4,2,5,8,7]
l2 =[3,5,2,7,9,5]
s1 = set(l1)
s2 = set(l2)
l3 = s1.intersection(s2)
print(list(l3))'''
#intersection_update
'''l1 ={2,4,2,5,8,7}
l2 ={3,5,2,7,9,5}
l1.intersection_update(l2)
print(l1)
'''
#symmetric_difference_update
'''l1 ={2,4,2,5,8,7}
l2 ={3,5,2,7,9,5}
l1.symmetric_difference_update(l2)
print(l1)'''
#difference_update
'''l1 ={2,4,2,5,8,7}
l2 ={3,5,2,7,9,5}
l2.difference_update(l1)
print(l2)
'''
'''l1 ={4,5,8,7,8,2,9}
l2 ={2,7,9}
print(l1.issuperset(l2))
'''
#Dictionary
'''dic = [{
    "name": "abhinav",
    "age" : 21,
    "roll" : 24
    },
    {
    "name": "rahul",
    "age" : 20,
    "roll" : 25
    }
]

n = int(input())
for i in dic:
    if n == i["roll"]:
        print(i["name"],i["age"])
        break
else:
    print("wrong roll no.")
'''
'''p1 ={12: 45,13:56,14:78,15:34}
p2 = {16:54 , 17: 90}
p1.update(p2)
print(p1)
p1.pop(15)
print(p1)
p1.popitem()
print(p1)'''
















