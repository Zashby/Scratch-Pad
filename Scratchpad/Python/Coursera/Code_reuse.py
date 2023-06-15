class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


class Turtle(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)
        Animal.set_category(self, 'reptile')


turtle = Turtle("biggie")
print(turtle.category)


class Snake(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)
        Animal.set_category(self, 'reptile')


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result


zoo = Zoo()

turtle = Turtle("Turtle")  # create an instance of the Turtle class
snake = Snake("Snake")  # create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

# how many zoo animal types in the reptile category
print(zoo.total_of_category("reptile"))
