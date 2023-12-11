class Employee:
    def __init__(self, name, id) -> None:
        self.__name = name
        self.id = id
        
a =Employee("rudra", 23454)
# print(a.__name)
print(a._Employee__name) # private access modifier
print(a.id) # public
print(a.__dir__())

