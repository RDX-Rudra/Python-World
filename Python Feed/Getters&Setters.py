class Myclass:
    def __init__(self, v) -> None:
        self.value = v
        
    def show(self):
        print(f"value is {self.value}")
        
    @property
    def ten_value(self):
        return 10 * self.value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value/10
    
obj = Myclass(10)
obj.ten_value = 56
print(obj.value)
obj.show()