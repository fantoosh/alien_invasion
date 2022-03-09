
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")


class Restaurant:
    """A simple attempt to model a retaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints out a brief description of a restaurant"""
        print(f"Restaurant name: {self.name}")
        print(f"cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is now open")

    def increment_number_served(self, increment):
        """Implement an increment to the number_served attribute"""
        if increment > 0:
            self.number_served += increment

        else:
            print("You can only add positive integers")

my_restaurant = Restaurant('madam quantity', 'cheap')
my_restaurant.number_served = 100
print(my_restaurant.number_served)

my_restaurant.increment_number_served(-50)
print(my_restaurant.number_served)
