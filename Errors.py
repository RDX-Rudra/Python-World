try:
    num= int(input("enter an integer: "))
    a = [6,4]
    print(a[num])
    
except ValueError:
    print("number entered is not an integer")
    
except IndexError:
    print("index Error")