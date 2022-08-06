class ClubMembers:

    def __init__(self, name, birthday, age, favorite_food, goals):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goals = goals

    def display(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite Food:", self.favorite_food)
        print("Goals:", self.goals)


class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goals, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favorite_food, goals)

    def display2(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite Food:", self.favorite_food)
        print("Goals:", self.goals)
        print("Position:", self.position)


n_1 = ClubMembers("Tom", "Jan 26", 14, "Ice Cream", "To be happy")
n_2 = ClubOfficers("Vera", "Jun 22", 16, "Beef Stroganoff", "To be the world's greatest chef", "Treasurer")

n_1.display()
n_2.display()
