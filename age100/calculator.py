from person import Person

#calculate person's age
class Calculator:
    def __init__(self):
        self.birth_year = 0
        self.year_one_hundred = 0

    def one_hundred_years(self):
        self.year_one_hundred = Person(birth_year) + 100
        print(self.year_one_hundred)