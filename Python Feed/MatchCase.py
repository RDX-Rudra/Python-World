x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("zero")
    case 1:
        print("one")
    case 2:
        print("two")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)