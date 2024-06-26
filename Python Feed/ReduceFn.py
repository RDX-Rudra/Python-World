from functools import reduce

l = [1,3,2,4,5,6,7,8,9]

sum = reduce(lambda x,y: x+y, l)
print(sum)