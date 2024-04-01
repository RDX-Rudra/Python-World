class person:
    name = ""
    occupation = "software devloper"
    network = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = person()
a.name = "Rudra"
print(a.name)
a.info()

b = person()
b.name = "prithu"
b.occupation = "Doctor"
b.info()