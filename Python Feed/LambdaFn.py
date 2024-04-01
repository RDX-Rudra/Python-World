# def double(x):
#     return x*2
def appl(fx, value):
    return 6+fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
power = lambda x,n : x**n

print(double(5))
print(cube(5))
print(power(2,3))
print(appl(cube, 2))