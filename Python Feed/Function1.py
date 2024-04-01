def calculateGmean(a, b):
    mean = (a+b)/(a-b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("First no is greater")
    else:
        print("Second no is greater")
    
a=9
b=8
isGreater(a, b)
calculateGmean(a, b)
