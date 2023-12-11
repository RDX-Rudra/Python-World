def fun1():
    try:
        l=[1,2,3]
        i= int(input("enter input: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("i am always executed")
        
x = fun1()
print(x)