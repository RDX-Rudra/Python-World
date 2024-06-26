# def average(a, b):
#     print("The average is ", (a+b)/2)
    
# average(4, 6)
# default , required arguement

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/ len(numbers)
    
c = average(3, 9, 6)
print(c)