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
        self.reverse_words_list = []

    #set methods
    # get phrase method
    def get_phrase(self):
        self.original_phrase = input("Enter a phrase:  ")
    
    # split up phrase into a list with each word as a list element
    def split_up_phrase(self):
        self.words_list = self.original_phrase.split()

    # reverse the words in the array
    def reverse_words(self):
        for i in self.words_list:
            #store the word to be appended into new array
            self.reverse_words_list.append(i[::-1])

    # take new array and make a new phrase with reverse words but words in orginal order
    def new_user_phrase(self):
        for x in self.reverse_words_list:
            #use this to end the new string without an extra space at the end
            if self.reverse_words_list.index(x) == len(self.reverse_words_list):
                self.new_phrase += x
            #add the reverse word to the new phrase
            else:
                self.new_phrase += x + " "

#endregion - Class and Methods

#region - instantiat and print

#instantiate methods
user_phrase = Phrase()

#get user phrase
user_phrase.get_phrase()

#split up the phrase into an list of words
user_phrase.split_up_phrase()

#reverse each word in the new list
user_phrase.reverse_words()

#get the new reversed word phrase
user_phrase.new_user_phrase()

#print the result of each method call
print(user_phrase.original_phrase)
print(user_phrase.words_list)
print(user_phrase.reverse_words_list)
print(user_phrase.new_phrase)

#endregion 