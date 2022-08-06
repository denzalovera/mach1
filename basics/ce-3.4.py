class Customers:
    greeting = "Welcome to the Coffee Palace!"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total


c1 = Customers("Samirah", "Latte", "Blue Berry", 250.0)
c2 = Customers("Jerry", "Capuccino", "Chocolate Cake", 180.0)

print(Customers.greeting)
print(c1.beverage)
print(c2.food)
