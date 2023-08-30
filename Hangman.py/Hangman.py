## اسامة محمد صالح الهرش

import random

def hangman():
    words = ['hangman', 'apple', 'banana', 'orange', 'computer']
    selected_word = random.choice(words).lower()
    guessed_letters = []
    tries = 6

    while True:
        print("\n")
        print_hangman(tries)
        print_word(selected_word, guessed_letters)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in selected_word:
            tries -= 1
            print("Wrong guess!")

            if tries == 0:
                print_hangman(tries)
                print("Game over! The word was:", selected_word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in selected_word):
            print_hangman(tries)
            print("Congratulations! You guessed the word:", selected_word)
            break

def print_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
        '''
    ]
    print(stages[tries])

def print_word(selected_word, guessed_letters):
    word = ''
    for letter in selected_word:
        if letter in guessed_letters:
            word += letter + ' '
        else:
            word += '_ '

    print(word)

hangman()