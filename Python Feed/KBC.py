# kaun banega cororpati
questions = [["which language was used to create fb?", "python", "c++", "javaScript", "none", 4],["which language was used to create fb?", "python", "c++", "javaScript", "none", 4],["which language was used to create fb?", "python", "c++", "javaScript", "none", 4],["which language was used to create fb?", "python", "c++", "javaScript", "none", 4],["which language was used to create fb?", "python", "c++", "javaScript", "none", 4],["which language was used to create fb?", "python", "c++", "javaScript", "none", 4],["which language was used to create fb?", "python", "c++", "javaScript", "none", 4],["which language was used to create fb?", "python", "c++", "javaScript", "none", 4],]
levels = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000, 55000, 90000, 150000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"question for Rs. {levels[i]}")
    print(f"a.{question[1]}    b.{question[2]}")
    print(f"a.{question[3]}    b.{question[4]}")
    reply = int(input("enter your ans(1-4) or 0 to quit: "))
    if(reply == 0):
        break
    if(reply == question[-1]):
        print(f"correct answer, you have won Rs. {levels[i]}")
        if(i==4):
            money = 8000
        elif(i== 8):
            money= 55000
        elif(i== 10):
            money= 150000
    else:
        print("wrong answer!")
        break
print(f"your take home money is {money}")