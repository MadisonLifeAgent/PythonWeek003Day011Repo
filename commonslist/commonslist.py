#make two lists []
#function that takes both lists and compares each lists
    # compare one string at a time and only once
    # if a string has been checked already skip it 
    # store common strings in a new list []

#create class
class Lists():
    def __init__(self):
        #class attributes
        self.first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.third_list = []

    def check_these_lists(self):
        #loop through first list
        for f in self.first_list:
                #loop through second list
                for s in self.second_list:
                #check to see if number in first list is in second list
                    if f == s:
                        #if number is not in third list already then add it, if not go to next number
                        if f not in self.third_list:
                            self.third_list.append(f)
        

#instantiate method to check for similar numbers
same_numbers = Lists()
same_numbers.check_these_lists()

print(same_numbers.third_list)

