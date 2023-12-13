x = 4
x=7
x = "hello"
x = [1, 2, 3]
y = x
print(y)
x.append(4)
print(y)
y.append(5)
print(x)
x='something else'
print(y)
print(x)

a=10
b=a
a += 5
print("a =", a)
print("b =", b)

x = 4
print(type(x))
x = 'hello'
print(type(x))
x = 3.14
print(type(x))

x=4.5
print(x.real, "+", x.imag, 'i')
print(x.is_integer())
x=4.0
print(x.is_integer())
print(type(x.is_integer()))
type(x.is_integer())
