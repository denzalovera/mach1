class Customers:
    greeting = "Welcome to Coffee Palace!"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total


c1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
c2 = Customers("Elaine", "Strawberry Frappucino", "Tuna Wrap", 270)
c3 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
c4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c5 = Customers("Paz", "Iced tea", "Blueberry pancake", 315)

print(Customers.greeting)
print(c1.name + c1.food + c1.beverage + str(c1.total))

print(Customers.greeting)
print(c2.name + c2.food + c2.beverage + str(c2.total))

