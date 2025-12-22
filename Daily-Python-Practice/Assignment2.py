#Encryption and Decryption

def Encryption():
    user_input = input("Enter The line")
    length1 = len(user_input)
    index1 = 0
    if length1 < 4 :
        print(user_input[::-1])
    elif length1 > 4:
        res = user_input[:index1] + user_input[index1+1:] + user_input[index1]
        print(res[::-1])

Encryption()


def Decryption():
    user_input1 = input("Enter the string you want to decrypt: ")
    length2 = len(user_input1)
    index2 = 0
    if length2 < 4 :
        print(user_input1[::-1])
    elif length2 > 4:
        res1 = user_input1[:index2] + user_input1[index2 + 1:] + user_input1[index2]
        print(res1[::-1])
    
    
    
    
Decryption()