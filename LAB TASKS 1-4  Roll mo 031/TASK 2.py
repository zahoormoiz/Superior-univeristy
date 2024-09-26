#Class vs Object
class Car:
    def __init__(self, model, color):
        self.model = model  
        self.color = color   
    
    def start(self):   
        print(f"The {self.color} {self.model} is starting.")
        
my_car = Car("Toyota", "Red")

print(f"My car is a {my_car.color} {my_car.model}.")  
my_car.start()  

# examples of Constructor methods
class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize the name 
        self.age = age  # Imitialize the age 

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}" \

person1 = Person("Alice", 30)

print(person1)