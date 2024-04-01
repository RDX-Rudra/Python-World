def filter_fun(x):
    return x>4

l = [1,2,3,4,5,6,7,8,9]
newl = list(filter(filter_fun, l))
print(newl)

