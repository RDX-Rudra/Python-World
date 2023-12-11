def fibSeq(a, b, n):
    if(n==0):
        return
    c = a+ b
    print(c,end=", ")
    fibSeq(b, c, n-1)
a=0
b=1
n = int(input("enter the no of terms: "))
print("fibonacci Sequence is: ", a,",", b,end=", ")
fibSeq(a, b, n-2)
