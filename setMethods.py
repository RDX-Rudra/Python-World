s1 = {1, 2, 4, 6, 7, 5}
s2 = {3, 6, 8, 5, 2, 0}
s3 = {10, 12, 11}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s1.intersection_update(s2))
print(s1)
s1.update(s2)
print(s1, s2)
# dono me cimmon nehi hai kya
print(s1.isdisjoint(s3)) 
print(s1.issuperset(s3)) 
print(s2.issubset(s3)) 
print(s2.issubset(s3)) 
s1.add("ram")
print(s1)
s1.discard(0)
print(s1)
s4 = s2.pop()
print(s2)
print(s4)
if "ram" in s1:
    print("present")
else:
    print("not present")