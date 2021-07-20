#region - User Story & Algorithm

#Write a function that takes in a phrase and reverse each word inside the string, but keeps the same order of the phrase.
    #a. “Hello world I am a programmer”
    #b. “olleh dlrow I ma a remmargorp”

# get phrase from user
# split up each word and put into a list
# take each word and reverse the words
    # store the reversed words into a list (new or same)
# put words back into a string and in original order

#endregion - User Story & Algorithm

#region - Class and Methods
class Phrase:
    def __init__(self):
        self.original_phrase = ""
        self.words_list = []
        self.new_phrase = ""
        self.reversed_words_list = []

    #set methods
    # get phrase method
    def get_phrase(self):
        self.original_phrase = input("Enter a phrase:  ")
    
    # split up phrase into a list with each word as a list element
    def split_up_phrase(self):
        self.words_list = self.original_phrase.split()

#instantiate methods
user_phrase = Phrase()

#get user phrase
user_phrase.get_phrase()

#debugging
print(user_phrase.original_phrase)