#region - User story and algorithm

#10. Print downward Pyramid Pattern with Star (asterisk).
#a. ***** **** *** ** *

#endregion - User story and algorithm
#create original stars
# loop through the stars and take one 


#region - class
class Pyramid:
    def __init__(self):
        self.five_stars = "* * * * *"
        self.stars_list = []
        self.updated_stars = ""

    #set methods

    #method to reduce number of stars
    def reduce_stars(self):
        self.


    #method to print pyramid
    def show_pyramid(self):
        counter = 0

        while counter < len(self.five_stars):
            print(self.five_stars)
            counter += 1
            self.reduce_stars()


#reduce the number of stars
star_pyramid = Pyramid()
star_pyramid.show_pyramid()


print(star_pyramid.five_stars)

