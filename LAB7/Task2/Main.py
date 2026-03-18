from LAB7.Task2.models import Animal,Dog,Cat

animal1 = Animal("Volf",5,"seriy")
dog1 = Dog("Bobik",3,"Yellow")
cat1 = Cat("Mysyk",4,"Black")

animals = [animal1,dog1,cat1]

for animal in animals:
    print(animal)
    print(animal.eating())
    print(animal.speak())
    print(animal.speak())
