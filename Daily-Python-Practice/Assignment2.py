#Encryption and Decryption
import random
import string

def Encryption():
    user_input = input("Enter The line")
    length1 = len(user_input)
    index1 = 0
    if length1 <= 4 :
        random_letters1 = "".join(random.choice(string.ascii_lowercase) for _ in range(4))
        result1 = (random_letters1) + user_input + random_letters1
        print(result1[::-1])
    elif length1 > 4:
        new = user_input[:index1] + user_input[index1+1:] + user_input[index1]
        random_letters = "".join(random.choice(string.ascii_lowercase) for _ in range(4))
        res = (random_letters)+ new + random_letters
        print(res[::-1])

Encryption()


def Decryption():
    user_input1 = input("Enter the string you want to decrypt: ")
    length2 = len(user_input1)
    if length2<=4:
        temp = user_input1[::-1]
        res1 = temp[4: -4:]
        print(res1)
    else:
        temp = user_input1[::-1]
        res1 = temp[4: -4:]
        res2 = res1[-1: ]+res1[: -1 ]
        print(res2)
    
Decryption()