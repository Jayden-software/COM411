def task1():
    print("What type of book is this?")
    book_type = input()
    if book_type == "adventure":
        print("I like adventure books!")
        print("Finished reading book.")
def task2():
    print("Please enter the activity to be performed.")
    activity = input()
    if activity == "calculate":
        print("Performing calculations...")
    else:
        print("Performing activity...")
        print("Activity completed.")
def task3():
    print("Towards which direction should I go (up, down, left or right)?")
    direction = input()
    if direction == "up":
        print("I am moving in the upward direction!")
    elif direction == "down":
        print("I am moving in the downward direction!")
    elif direction == "left":
        print("I am moving in the leftward direction!")
    elif direction == "right":
        print("I am moving in the rightward direction!")
    else:
        print("Not sure which direction to move!")
def task4():
    print("Please enter a whole number.")
    number = int(input())
    if number % 2 == 0:
        print(f"The number {number} is an even number.")
    else:
        print(f"The number {number} is an odd number.")
def task5():
    print("Please enter the first number.")
    first_number = int(input())
    print("Please enter the second number.")
    second_number = int(input())
    if first_number < second_number:
        print("The first number is the smallest.")
    elif first_number > second_number:
        print("The second number is the smallest.")
    else:
        print("The two numbers are equal.")
def task6():
    print("Please enter the first whole number?")
    first_number = int(input())
    print("Please enter the second whole number?")
    second_number = int(input())
    print("Please enter the third whole number?")
    third_number = int(input())
    even_numbers = 0
    if first_number % 2 == 0:
        even_numbers = even_numbers + 1
    else:
        odd_numbers = odd_numbers + 1
    if second_number % 2 == 0:
        even_numbers = even_numbers + 1
    else:
        odd_numbers = odd_numbers + 1
    if third_number % 2 == 0:
        even_numbers = even_numbers + 1
    else:
        odd_numbers = odd_numbers + 1
    # Display result
    print(f"There were {even_numbers} even and {odd_numbers} odd numbers.")
def task7():
    print("What type of cover does this book have?")
    cover_type = input()
    if cover_type == "soft":
        print("Is the book perfect-bound?")
        perfect_bound = input()
        if perfect_bound == "yes":
            print("Soft cover, perfect bound books are very popular!")
        else:
            print("Soft covers with coils or stitches are great for short books")
    else:
        print("Books with hard covers can be more expensive!")
def task8():
    print("Where should I look?")
    place = input()
    if place == "in the bedroom":
        print("Where in the bedroom should I look?")
        bedroom_place = input()
        if bedroom_place == "under the bed":
            print("Found some shoes but no phone")
        else:
            print("Found some mess but no phone."
            elif place == "in the bathroom":
            print("Where in the bathroom should I look?")
            bathroom_place = input()
            if bathroom_place == "in the bathtub":
                print("Found a rubber duck but no phone")
def task9():
    print("What type of adventure should I have?")
    adventure_type = input()
    if (adventure_type == "scary") or (adventure_type == "short"):
        print("Entering the dark forest!")
    elif (adventure_type == "safe") or (adventure_type == "long"):
        print("Taking the safe route!")
    else:
        print("Not sure which route to take.")
def task10():
    print("What did I hear?")
    hear = input()
    print("What did I see?")
    see = input()
    if (hear == "grr") and (see == "two red eyes"):
        print("There is a scary creature. I should get out of here!")
    else:
        print("I am a little scared but I will continue.")



=









