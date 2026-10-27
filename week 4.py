def task1():
    print("Program Started!")
    print("Please enter a standard character:")
    character = input()
    if len(character) == 1:
        print(f"The ASCII code for {character} is {ord(character)}")
    else:
        print("A single character was expected.")
    print("Program Ended!")
def task2():
    print("Program Started!")
    print("Please enter an ASCII code:")
    code = int(input())
    if code >= 32 and code <= 126:
        print(f"The ASCII code for {code} is {chr(code)}")
def task3():
    def listen():
        print("What sound did you hear?")
        sound = input()
        print(sound)
def task 4():


def identify():
    # Ask user for what lies ahead
    print("What lies before us?")
    response = input()
    # Display message
    if response == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")
identify()

def task5():
    def escape_by(plan):
        # Determine which message to display
        if plan == "jumping over":
            print("We cannot escape that way! The boulder is too big!")
        elif plan == "running around":
            print("We cannot escape that way! The boulder is moving too fast!")
        elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
        else:
        print("Not sure about that plan!")

    # Calls to the function
    escape_by("jumping over")
    escape_by("running around")
    escape_by("cross bridge ahead")




