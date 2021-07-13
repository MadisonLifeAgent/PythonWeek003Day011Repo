# takes in a number string and converts it to an integer
def get_number():
    number_one = input("Enter a number:  ")
    print("Minimum Number is: " + number_one)
    number_one = int(number_one)

    number_two = input("Enter a number higher than the first number:  ")
    number_two = int(number_two)

    # if second number is lower than first reprompt user
    while number_two <= number_one + 1:
        print("Second Number must be significantly higher than the first number")
        number_two = input("Enter a number higher than the first number:  ")
        number_two = int(number_two)

    print("Maximum Number is:")
    print(number_two)

    # generate random number between two numbers
    import random

    random_number = random.randrange(number_one, number_two)

    while (random_number == number_one or random_number == number_two):
        random_number = random.randrange(number_one, number_two)

    print("Random number is:")
    print(random_number)


get_number()