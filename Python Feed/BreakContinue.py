for i in range(10):
    print("5 x", i+1, "=", 5* (i+1))
    if(i==8):
        break
print("the end")    

for i in range(10):
    if(i==8):
        print("skiped")
        continue
    print("5 x", i+1, "=", 5* (i+1))