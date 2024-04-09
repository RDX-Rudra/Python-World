data= [x for x in range(5)] 
temp = [x for x in range(7) if x in data and x%2==0]
print(temp)

D = dict()
for i in range(3):
    for j in range(2):
        D[i] = j
print(D)

tuple= (1, 2, 3) 
print(2*tuple)

list= [1, 2, 3, None, (1, 2, 3, 4, 5), ['G', 'for', 'A']] 
print(len(list))

list= ['python', 'learning', '@', 'A', 'for', 'abc'] 
print(list[ ::-2]) 
