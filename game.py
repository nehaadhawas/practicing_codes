import random

# Computer randomly chooses -1 (water), 0 (gun), or 1 (snake)
computer = random.choice([-1, 0, 1])

# User input (s = snake, w = water, g = gun)
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

# Mapping user input to corresponding game values
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Ensure valid input from the user
if youstr not in youDict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    # Fetch user's choice
    you = youDict[youstr]

    # Print choices of both the user and the computer
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    # Determine the outcome
    if computer == you:
        print("It's a draw")
    else:
        # Winning conditions for the user:
        # snake (1) beats water (-1), water (-1) beats gun (0), gun (0) beats snake (1)
        if (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
            print("You win!")
        else:
            print("Computer wins!")
