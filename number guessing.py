import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Your task is to guess the number.")
    
    attempts = 0  # To track the number of attempts
    
    while True:
        # Ask the user for their guess
        user_guess = input("Enter your guess: ")
        
        # Check if the input is a number
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        # Convert input to integer
        user_guess = int(user_guess)
        
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
            break

# Run the game
number_guessing_game()
