class Dog:
    def __init__(self, name, age, colour, danger):  # the self parameter
        # (e.g. dog1 or dog2) is automatically passed to the dog class
        # - so that we know which dog we're talking about

        self.name = name  # Creates a 'name' attribute for Dog
        self.age = age  # Creates a 'age' attribute for Dog
        self.colour = colour  # Creates a 'colour' attribute for Dog
        self.danger = danger

    def print_details(self):  # Creates a method of displaying information
        return f"{self.name} is a {self.danger} {self.colour} dog aged {self.age}"

    def age_days(self):
        return f"{self.name} is {self.age * 5.75} dog years old"


# These are two different Dog objects
dog1 = Dog("Spot", 7, "black", "savage")
dog2 = Dog("Jazz", 5, "white", "playful")
dog3 = Dog("Boss", 9, "ginger", "biting")

# Calling the printDetails method for each dog object
print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
print(Dog.print_details(dog3))

print(Dog.age_days(dog1))
print(Dog.age_days(dog2))
print(Dog.age_days(dog3))
