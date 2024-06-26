ep1 = {125: 45, 123: 80, 456: 47, 123: 87}
ep2 = {222: 67, 456: 32}
ep1.update(ep2)
print(ep1)

ep1.pop(123)
print(ep1)

ep1.popitem()
print(ep1)

#del ep1
del ep1[125]
print(ep1)