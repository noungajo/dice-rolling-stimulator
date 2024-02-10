import random



repeat_again = 'y'
#looping
while repeat_again == 'y':
    #developping a random number
    random_number = random.randint(1,6)
    print(random_number)
    #check the number
    if random_number == 1:
        #print the face
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")

    if random_number == 2:
        print("---------")
        print("|       |")
        print("|0     0|")
        print("|       |")
        print("---------")

    if random_number == 3:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("|   0   |")
        print("---------")

    if random_number == 4:
        print("---------")
        print("|0     0|")
        print("|       |")
        print("|0     0|")
        print("---------")

    if random_number == 5:
        print("---------")
        print("|0     0|")
        print("|   0   |")
        print("|0     0|")
        print("---------")

    if random_number == 6:
        print("---------")
        print("|0     0|")
        print("|0     0|")
        print("|0     0|")
        print("---------")
        repeat_again = input("Do you want to continue ? y/n ")