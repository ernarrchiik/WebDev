class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def eating(self):
        return f"{self.name} is eating"
    def sleep(self):
        return f"{self.name} is sleeping"
    def speak(self):
        return "Animal makes a sound"
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}"
    
class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age,color)
    def speak(self):
        return "Meow!"
    def climb(self):
        return f"{self.name} is climbing"
    
class Dog(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age,color)
    def speak(self):
        return "Woof!"
    def fetch(self):
        return f"{self.name} is fetching a ball"
    