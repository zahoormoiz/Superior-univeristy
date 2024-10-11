#task1
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def additional_info(self):
        print(f"Number of Doors: {self.num_doors}")


class LuxuryCar(Car):
    def __init__(self, make, model, num_doors, features=None):
        super().__init__(make, model, num_doors)
        self.features = features if features else []

    def additional_info(self):
        super().additional_info()  
        if self.features:
            print(f"Luxury Features: {', '.join(self.features)}")
        else:
            print("No additional luxury features.")

if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 4)
    car.display_info()
    car.additional_info()


    luxury_car = LuxuryCar("Mercedes-Benz", "S-Class", 4, ["Leather Seats", "Sunroof", "Premium Sound System"])
    luxury_car.display_info()
    luxury_car.additional_info()

    basic_luxury_car = LuxuryCar("BMW", "7 Series", 4)
    basic_luxury_car.display_info()
    basic_luxury_car.additional_info()

# task 2


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}")


class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def additional_info(self):
        print(f"Department: {self.department}")


class Worker(Employee):
    def __init__(self, name, position, hours_worked):
        super().__init__(name, position)
        self.hours_worked = hours_worked

    def additional_info(self):
        print(f"Hours Worked: {self.hours_worked}")


if __name__ == "__main__":

    manager = Manager("Alice", "Manager", "HR")
    manager.display_info()
    manager.additional_info()

    worker = Worker("Bob", "Worker", 40)
    worker.display_info()
    worker.additional_info()
