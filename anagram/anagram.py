#region - User Story & Algorithm

#Write a function that takes in two words and determines if the two words are an anagram of each other.
    #An anagram is a word or phrase that is formed by rearranging the letters of another word or phrase.
    #b. Assume any word that is passed in is a word that exists in the English language
    #c. If the two words are an anagram, return true. Otherwise, return false.

# Algorithm
    #get user words and store as attributes
    #compare each word
        #take second word and check each letter to see if they are in first word
        #must check every letter agains every letter
        #once a letter is used it can't be used again??


#endregion - User Story

#region - Class
class User_words:
    def __init__(self):
        self.first_word = ""
        self.second_word = ""
        self.reamining_letters = ""

    # get user words
    def get_user_words(self):
        self.first_word = input("Please enter a word:  ")
        self.second_word = input("Please enter another word:  ")
        
        #make sure words are the same length
        if len(self.first_word) != len(self.second_word):
            print("Please enter words of the same length")
            self.get_user_words()
        else:
            print("Your words are:  " + self.first_word + " and " + self.second_word)

    #check to see if words are anagrams of each other
    def check_for_anagram(self):
        #go through each character and check against characters of first word
        for s in self.second_word:
            for f in self.first_word:
                #if a match is found 
                if s == f:
                    self.first_word = self.first_word.replace(f, '')
                    self.second_word = self.second_word.replace(s, '')

    #check to make sure all letters were checked, otherwise words are not an anagram
    def final_check(self):
        if len(self.first_word) == 0 and len(self.second_word) == 0:
            print("Your words ARE Anagrams!!")
        else:
            print("Your words are NOT Anagrams!!")


#instantiate class and methods
user_words = User_words()

#get user words
user_words.get_user_words()

#check the words to see if they are anagrams
user_words.check_for_anagram()

#check to make sure all the letters in the first word were used up
user_words.final_check()
