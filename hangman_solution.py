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

# S1
p1_name = input("Player 1: Enter your name: ")
p2_name = input("Player 2: Enter your name: ")
word = input("Player 1: Enter the word/phrase for Player 2 to guess: ")

#S2
wrong_letters = ""
correct_letters = ""
found = False # this line is part of S8
lives = 5


while len(wrong_letters) < 6 and not found: # S7 AND S8
    found = True # S8
    for char in word: # S3
        if char in correct_letters or char == " ":
            print(char,end="")
        else:
            found = False
            print("_", end="")
    print()

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
    else:
        print(hangman5)

    # S5
    guessed_letter = input("Player 2: Guess a letter: ")

    #S6
    if guessed_letter in word:
        print("Correct!")
        correct_letters += guessed_letter
    else:
        if guessed_letter in wrong_letters: # BONUS
            print("You already guessed this letter!")
        else: 
            print("Incorrect! The letter '%s' does not appear in this word."%(letter))
            wrong_letters += guessed_letter

# S9
if found:
    print("Wow! You got it!") # S10
else:
    print(hangman6)
    print("You lose! Try to play again!") # S11
    








