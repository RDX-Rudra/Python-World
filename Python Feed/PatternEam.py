def pattern(n):
    a = 1
    for i in range(0, n):
        for _ in range(0, i+1):
            print(a, end=" ")
            a+=1
        print()
            
pattern(5)