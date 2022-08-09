class Employee():
    def __init__(self,name,title):
        self.name = name
        self.title = title
    def print(self):
        print(self.name,self.title)
        

    
class welcome(Employee):
    def __init__(self, name, title, year):
        super().__init__(name, title)
        self.joinyear = year
        print(self.name, "welome to the company as", self.title, "in", self.joinyear)


# obj1 = welcome("sailesh","VP",2022)

obj2 = Employee("viha","associate")
obj2.print()
