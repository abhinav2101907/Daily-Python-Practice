#Create a simple calculator
a = int(input("enter the valur of a"))
b = int(input("enter the value of b"))
c = int(input("Select option for performance\n1 ,2 ,3 ,4"))
if (c == 1):
    print("Solution =", a +b)
elif(c == 2):
    print("Solution =", a - b)
elif(c == 3):
    print("Solution =", a *b)
elif(c == 4):
    print("Solution =", a /b)
else:
    print("wrong selection")