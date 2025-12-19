#Inharitance - Allow a class to inharit attributes and mrthod from another class
#               helps with code reusability and extensibility
#               class Child 

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_allive =True

    def eat(self):
        print(f"{self.name} is eating ")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Red Cherry")
mouse = Mouse("ratatatoi")

print(dog.name)
print(dog.is_allive)
dog.eat()
dog.sleep()

dog.speak()