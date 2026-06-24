
choice = "y"

# Repeat the program while the user chooses y
while choice == "y":

    # Get Quiz 1 mark from the user
    quiz_1 = float(input("Enter Quiz 1 mark: "))

    # Get Quiz 2 mark from the user
    quiz_2 = float(input("Enter Quiz 2 mark: "))

    # Get Quiz 3 mark from the user
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Calculate the average mark
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    # Check if the student passes or fails
    if average >= 50:
        print("Pass")
    else:
        print("Fail")

    # Ask the user if they want to continue
    choice = input("Continue? Select Y/N: ")

print("Program Ended")
