import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

number_guessing_game()
