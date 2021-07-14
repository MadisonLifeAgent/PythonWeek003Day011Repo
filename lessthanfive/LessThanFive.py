#region

# get a list of numbers from user
def get_numbers():
    # number variable
    get_number = "0"

    # number list
    number_list = []

    # get 5 numbers from a user
    while(len(number_list) < 5):
        get_number = input("Enter any number:  ")
        
        #convert user input from string to number
        real_number = int(get_number)

        #store real number in list
        number_list.append(real_number)

        #debugging line
        print(number_list)

    #call function to check if number less than five only
    less_than_five_list = less_than_five(number_list)

    #print numbers less than five only
    print(less_than_five_list)

         

 #check and return numbers less than 5 from the array
def less_than_five(less_than_five_list):
    #temporarliy store numbers less than five, eventutally gets returned to where called
    less_than_five_numbers = []

    # check all the values in list to see if they are less than or greater than 5
    for n in less_than_five_list:
        if n < 5:
            less_than_five_numbers.append(n)

    if (len(less_than_five_numbers) == 0):
        return "No numbers less than 5"
    # sends numbers less than five to where called
    else:
        return less_than_five_numbers

# get numbers and return any number less than 5 in a list
get_numbers()
#endregion