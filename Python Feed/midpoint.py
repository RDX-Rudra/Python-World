# set the midpoint
midpoint = 5
 # make two empty lists
lower = []; upper = []
 # split the numbers into lower and upper
for i in range(10):
    if(i < midpoint):
            lower.append(i)
    else:
            upper.append(i)
            print("lower:", lower)
            print("upper:", upper)