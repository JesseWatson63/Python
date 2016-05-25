# Word Jumble
#
# The computer picks a random word and then "jumbles" it 
# The player has to guess the original

import random

# creat a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use later to see if the uess is correct
correct = word

# create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word  = word[:position] + word[(position + 1):]
    
# start the game
print(
    """
            Welcome to Word Jumble!
            
        Unscramble the letters to make a word.
    (Press enter key at the prompt to quit.)
    """
)
print("The jubmle is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
    
if guess == correct:
    print("That's it! You guessed it!\n")
    
print("thanks for playing.")
print("\n\nPress the enter key to exit.")