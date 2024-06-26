a = int(input("Enter your age: "))
print("your age is: ",a)
b=18
if(a>18):
    print("you can vote")
elif(a==18):
    print("you are new voter")
else:
    print("you cann't vote")
print("Thankyou")

print("mature") if a>b else print("=") if a==b else print("adult")

c = 9 if a>b else 0
print(c)