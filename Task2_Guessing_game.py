import random

def guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the guess to the target number
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number: {target_number}")
                print(f"It took you {attempts} attempts to guess the number.")
                break  # Exit the loop when the correct number is guessed

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the guessing game
guessing_game()
