# Gets word from user and displays the rew
def reversed_word():
    # get word from user
    original_word = input("Enter a word:  ")

    print("User Word:  " + original_word)

    reversed_word = ""

    #find the length of the word
    index_length = len(original_word)

    # spell the word backward by getting the last letter of the word and work backwards
    current_index = index_length -1

    # loop through the word and create the reversed word
    for x in original_word:
        if current_index == len(original_word) - 1:
            get_letter = original_word[current_index]
            reversed_word = reversed_word + get_letter
            current_index = current_index -1
        else:
            get_letter = original_word[current_index]
            reversed_word = reversed_word + get_letter
            current_index = current_index - 1

    # output reversed word
    return reversed_word

#output user word revered
print("Reversed Word: " + reversed_word())