def task1():
    print("Welcome to COM 411")
def task2():
    print("Welcome to COM411!")
    print("In week 1 we will learn...")
def task3():
    print("Welcome to COM411!")
    print("In week 1 we will learn...")
    print()
    print("...How to use Git and GitHub")
    print("...How to output to the screen")
    print("...How to get user input")
    print()
    print("I hope you are enjoying the lesson thus far!")
    # An alternative approach using a long string.
    print("""
    Welcome to COM411!
    In week 1 we will learn...
    ...How to use Git and GitHub
    ...How to output to the screen
    ...How to get user input
    I hope you are enjoying the lesson thus far!
    """)
def task4():
    print("\n Displays a new line")
    print("\t Displays a tab space")
    print("\\ Displays a back slash")
    print("\" Displays a double quote")
    print("\' Displays a single quote")
    # Display a message
    print(" \n\t\t\"I am programming!\" ")
def task5():
    print("##########")
    print("# o o #")
    print("# ---- #")
    print("##########")
    print("""
    ##########
    # o o #
    # ---- #
    ##########
    """)
def task6():
    print("What is your name?")
    name = input()
    print(f"Nice to meet you {name}")
def task7():
    print("Please enter eye character")
    eye = input()
    print("##########")
    print(f"# {eye} {eye} #")
    print("# ---- #")
    print("##########")
def task8():
    print("What is your name?")
    name = input()
    print("What is your age?")
    age = int(input())
    print("What is your weight?")
    weight = float(input())
    print("What is your height?")
    height = float(input())
    bmi = weight / (height ** 2)
    print(f"{name} your bmi is {bmi}")
def task9():
    print("Please enter number of lives")
    lives = int(input())
    print("Please enter energy level")
    energy = int(input())
    print("Please enter shield level")
    shield = int(input())
    print(f"Lives: {'♥' * lives}")
    print(f"Energy: {'♦' * energy}")
    print(f"Shield: {'♦' * shield}")

