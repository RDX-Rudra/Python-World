class Employee:
    companyName = "Apple"
    noofEmployee = 0
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        Employee.noofEmployee += 1
    def showDetails(self):
        print(f"the name of the employee is {self.name} and id is {self.id} in {self.noofEmployee} sized company {self.companyName}")
        
class programer(Employee):
    def showLanguage(self):
        print("the default language is python")

e1 = Employee("rudra das", 345)
e1.companyName = "Apple India"
e1.showDetails()
e2 = programer("asdw", 3443)
Employee.companyName = "amazon"
e2.showDetails()
e2.showLanguage()
