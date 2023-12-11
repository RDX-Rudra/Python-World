import strring
import random

def code_word(user1):
    b = user1.split()
    lst = []
    for i in b:
        if (len(i)<3):
            a=i[::-1]
            lst.append(a)
        else:
            code = i[1:] + i[0]
            code1 = "".join(random.choices(strring.strings, k= 4)) + code +"".join(random.choices(strring.strings, k= 4))
            lst.append(code1)
    a=' '.join(lst)
    return a
            
def decode_word(user):
    b = user.split()
    lst =[]
    for i in b:
        if(len(i)<3):
            code = i[::-1]
            lst.append(code)
        else:
            code2 = i[4:-4]
            try:
                code1 = code2[-1] + code2[0:-1]
            except IndexError:
                print('your encription key is greater than your massage')
            lst.append(code1)
    a=' '.join(lst)
    return a        

while True:
    print("0. Quit\n 1. Code_word\n 2. Decode_word\n")
    u=int(input("Enter your choice: "))
    if(u == 1):
        user = input("Enter your massage: ")
        print(code_word(user))  
    elif(u==2):
        user = input("Enter your massage: ")
        print(decode_word(user))  
    elif(u==0):
        exit()
    else:
        print("enter a valid input\n")          
    
                  