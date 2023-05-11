class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name, 'Кушає')
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(self.name, 'Гавкає')
hotdog = Dog("Bobik", 3, 'Labrodor')
print(hotdog.name, hotdog.breed, hotdog.age)
hotdog.eat()

