#imports
from person import Person

#istantiate get persons info
age = Person()
age.get_name_and_age()

#calculate year they turn 100
year_one_hundred = Person()
year_one_hundred.one_hundred_years(age.birth_year)

#display name and year they turn 100
print = Person()
print.print_info(age.name, year_one_hundred.year_one_hundred)