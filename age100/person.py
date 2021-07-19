#declare person class
class Person:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.birth_year = ""
        self.year_one_hundred = 0

    #set get person info method
    def get_name_and_age(self):
        self.name = input("Enter your name:  ")

        self.age = input("Enter your age:  ")
        #convert user age from string to number
        self.age = int(self.age)

        #get current year
        self.birth_year = input("What year were you born?  ")
        self.birth_year = int(self.birth_year)

    #calculate 
    def one_hundred_years(self, year):
            self.year_one_hundred = year + 100

    def print_info(self, name, year):
        print(f'{name + " will turn 100 years old in "}{year}')