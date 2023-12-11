a = (input("enter a number: "))
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    #print(e)
    print("invalid input")
# except ValueError:
#     print("number entered is not an integer")
# except IndexError:
#     print("index error")   
print("end of program")