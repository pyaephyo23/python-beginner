class Pet :
    def __init__(self,name,types,color,age) :
        self.name=name
        self.types= types
        self.color=color
        self.age=age
    
    def callpet(self):
        print(f'{self.name} is a {self.types} and {self.age} years old and it is {self.color}.');



cat= Pet("Shwe","cat","yellow",4)

cat.callpet();
        