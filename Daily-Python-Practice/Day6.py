#More with Loops
'''for i in range(6):
    print(i)
    if i == 3:
        break
else:
    print("not in i")'''
'''i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("not in i")'''
#error handling

'''try:
    a = int(input("enter"))
    for i in range(a):
        print("7 *",i+1,"=",7*(i+1))
except:
    print("invalid input")'''
'''try:
    a = int(input("enter the no."))
    lst = [2,4,1,6]
    print(lst[a])
except ValueError:
    print("print not a valid input")
except IndexError:
    print("print not a valid index")'''
'''def func1():
    try:
        a = int(input("enter a no."))
        for i in range(10):
            print(a,"*",i+1,"=",(i+1)*a)
    except :
        print("wrong value")
    finally:
        print("letss go again")

func1()'''












