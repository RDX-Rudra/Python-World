x=10 #global variable

print(x)

def my_fun():
    global x
    x=4
    y = 5 #local variable
    print(y)
    
    
my_fun()
print(x)
# print(y)