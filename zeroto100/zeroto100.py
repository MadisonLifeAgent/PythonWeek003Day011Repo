# number variables
number_one = 1
number_one_hundred = 100

# loop through range of numbers in reverse order
for i in reversed(range(number_one, number_one_hundred)):
    #print the appropriate result
    if(i % 4 == 0):
        print("Banana")
    elif(i % 7 == 0):
        print("Flamingo")
    elif(i % 4 == 0 and i % 7 == 0):
        print("Flamingo - Banana")
    else:
        print(i)