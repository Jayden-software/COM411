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