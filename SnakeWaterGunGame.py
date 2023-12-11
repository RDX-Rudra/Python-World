import random

result = [["d","l","w"],["w","d","l"],["l","w","d"]]
choices = [0,1,2]
while(True):
    x = random.choice(choices)
    print("choices:\n 0.snake\n 1.water\n 2.gun\n 3.quit")
    y= int(input("enter your choice: "))
    if(y == 3):
        exit()
    elif(y ==0 or y==1 or y==2):   
        if(result[x][y]=="d"):
            print("Match Draw")
        if(result[x][y]=="l"):
            print("Computer Win")
        if(result[x][y]=="w"):
            print("you Win")
    else:
        print("enter a valid choice")
