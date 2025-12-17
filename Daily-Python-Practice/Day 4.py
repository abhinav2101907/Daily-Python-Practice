#string formatting
'''l1 = "Hey my name is {} and i am from {}"
name = "abhinav"
place = "Lucknow"
print(l1.format(name,place))'''
#f string meathod
'''name = "abhinav"
place = "Lucknow"
print(f"Hey my name is {name} and i am from {place}")
'''
'''price = 58.31458
print(f"you can get this under {price}")'''
#Doc String
'''def square(n):
    'hey give a no. and we will give the square of the no.'
    print(n*n)


no = int(input("enter the no."))
square(no)
print(square.__doc__)'''
#Recursion
#Calling function inside  function
'''def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n-1)

no = int(input())
print(fac(no))'''
#fibbonaci using recurssion
'''def fibbo(n):
    if n == 0:
         return 0
    if n == 1:
        return 1
    return fibbo(n-1) + fibbo(n-2)
n = int(input("enter no"))
print(fibbo(n))'''
