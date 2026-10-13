def task1():
    # Ask user for number of apples
    print("How many apples should I remove?")
    apples_to_remove = int(input())
    # Declare a control variable
    apples_removed = 0
    # Remove apples
    print()
    while apples_removed < apples_to_remove:
        print("Removed apple.")
        apples_removed = apples_removed + 1
def task2():
    # Ask user for number of obstacles
    print("How many obstacles should I avoid?")
    obstacles_to_avoid = int(input())
    # Declare a control variable
    obstacles_avoided = 0
    # Avoid obstacles
    print()
    while obstacles_avoided < obstacles_to_avoid:
        print("Avoiding...", end="")
        obstacles_avoided = obstacles_avoided + 1
        print(f"Done! {obstacles_avoided} obstacles avoided.")
def task3():
    # Ask user for number of bars
    print("How many bars should be charged?")
    bars_to_charge = int(input())
    # Declare a control variable
    bars_charged = 0
    # Display bars
    print()
    while bars_charged < bars_to_charge:
        bars_charged = bars_charged + 1
        print(f"Charging: {'█' * bars_charged}")

    print("The battery is fully charged.")