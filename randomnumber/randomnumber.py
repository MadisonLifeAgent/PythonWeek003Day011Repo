# takes in a number string and converts it to an integer
def get_number():
    just_a_number = input("Enter a number:  ")
    just_a_number = int(just_a_number)

    return just_a_number

# get two numbers from user
first_number = get_number()
print("Minimum Number is: ")
print(first_number)

second_number = get_number()


# if second number is lower than first reprompt user
while second_number <= first_number + 1:
    print("Second Number must be significantly higher than the first number")
    second_number = get_number()

print("Maximum Number is:")
print(second_number)


#generate random number from user input numbers
import random

print("Random number is:")
print(random.randrange(first_number, second_number))
