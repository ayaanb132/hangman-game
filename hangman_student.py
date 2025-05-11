#STUDENT VERSION

# Here are all your hangman drawings
hangman0 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''

hangman1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
hangman2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
hangman3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
hangman4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
hangman5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
hangman6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

# S1 - ask for user's name and word to guess
player1_name = str(input("Enter Player 1 Name: "))
player2_name = str(input("Enter Player 2 Name: "))

full_answer = str(input(f"{player1_name}, please type a word or phrase "))

# S2 - initialize important variables
wrong_letters = ""
correct_letters = ""
lives = 5
game_won = False

while lives > 0 and not game_won: # S7
    # S3
    all_letters_guessed = True
    for letter in full_answer:
        if letter in correct_letters or letter == " ":
            print(letter, end=" ")
        else:
            print("_", end=" ")
            all_letters_guessed = False
    print()
    
    # Check if player has won
    if all_letters_guessed:
        game_won = True
        break

    # S4
    if len(wrong_letters) == 0:
        print(hangman0)
    elif len(wrong_letters) == 1:
        print(hangman1)
    elif len(wrong_letters) == 2:
        print(hangman2)
    elif len(wrong_letters) == 3:
        print(hangman3)
    elif len(wrong_letters) == 4:
        print(hangman4)
    elif len(wrong_letters) == 5:
        print(hangman5)
    elif len(wrong_letters) == 6:
        print(hangman6)
    # S5

    guessed_letter = str(input(f"{player2_name}, please guess a letter."))

    #S6
    if guessed_letter in full_answer:
        correct_letters+=guessed_letter
    else:
        wrong_letters+=guessed_letter
        lives-=1

# S9, S10 and S11
if game_won:
    print(f"Congratulations {player2_name}! You guessed the word: {full_answer}")
else:
    print(f"Sorry {player2_name}, you ran out of lives. The word was: {full_answer}")
    print(hangman6)

