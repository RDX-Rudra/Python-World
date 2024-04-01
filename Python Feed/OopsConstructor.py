class person:
    def __init__(self, n, o) -> None:
        print("Hey i am a person")
        self.name = n 
        self.occ = o
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
        
a = person("rudra", "Devloper")
b = person("prithu", "Doctor")
a.info()
b.info()
c = person(1, 2)
c.info()
