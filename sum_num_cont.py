# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/11/10
# Get the input for the amount of numbers the
# User would like to add. Then, get the inputs for
# Numbers the user would like to add together using a while
# Loop. Then displays this back to the user.


def main():
    # Title
    print("\n")
    print("Sum of many numbers")

    # Sum of the numbers
    sum = 0

    # User input
    amount_inputs = input(
        "Enter the amount of numbers you would like to add together: "
    )

    # To make sure the input is an integer
    try:
        amount_inputs_int = int(amount_inputs)

    # Exception which tells the user to enter an integer
    except Exception:
        print("Your number must be an integer!")

    else:
        if amount_inputs_int >= 0:
            while amount_inputs_int > 0:
                # Number user input
                numbers = input("Enter a number: ")
                # Try catch for the number user input
                try:
                    numbers_int = int(numbers)
                except Exception:
                    print("Please enter an integer")
                else:
                    # Calculations
                    if numbers_int > 0:
                        sum = sum + numbers_int
                        amount_inputs_int = amount_inputs_int - 1
                    else:
                        continue
                    print("{} added to the sum".format(numbers_int))
        else:
            print("Please enter a positive number!")
        # Displaying the sum
        print("The sum of both numbers is {}".format(sum))


if __name__ == "__main__":
    main()
