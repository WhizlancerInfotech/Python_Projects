import random

def hangman_game():
    word_list = ['python', 'hangman', 'challenge', 'code']
    chosen_word = random.choice(word_list)
    guessed_word = ['_'] * len(chosen_word)
    attempts = 6
    guessed_letters = []
    
    print("Welcome to Hangman!")
    
    while attempts > 0 and ''.join(guessed_word) != chosen_word:
        print(f"\nCurrent word: {' '.join(guessed_word)}")
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in chosen_word:
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    guessed_word[i] = letter
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")
    
    if ''.join(guessed_word) == chosen_word:
        print(f"\nCongratulations! You guessed the word: {chosen_word}")
    else:
        print(f"\nYou ran out of attempts! The word was: {chosen_word}")

hangman_game()
