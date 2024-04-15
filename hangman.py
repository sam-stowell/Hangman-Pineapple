
# Hang man

import random


list_of_words = ['Ball', 'Catapillar', 'Micoscope', 'Television','Watch', 'Plane', 'Computer', 'Mouse','Dog', 'Family', 'Monitor', 'Baby', 'Sofa', 'Kettle', 
'Battery','Abruptly', 'Thifty', 'Crusade', 'Religon', 'Axiom', 'Badger','Finger', 'Append', 'Pillow', 'Labyrinth', 'Alpanumeric', 'Deflector', 'Sheild', 'Razor',
'Awkward', 'Watch', 'Microwave', 'Helicopter', 'Stadium', 'Rotund', 'Retronymic']



# function to choose a random wrod from the list and cast it in to upper case

def choose_random_word (list_of_words):
    random_word = random.choice(list_of_words)
    return random_word.upper()

def play (word):
    print (word)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    # whilst loop asking for user input and to check against word and previous guesses
    while not guessed and tries > 0:
# ask for user input and cast into upper case
        guess = input("Please guess a letter or word: ").upper()
# do this when the user only enters 1 letter and its in the alpha bet
        if len(guess) == 1 and guess.isalpha():
# IF THE WORD GUESS AS ALRWADY BEEN GUESS DO THIS
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
#IF NOT ADD THE LETTER TO GUESS LETTERS LISTS FOR CHECKING AGAINST NEXT GUESS
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
# IF THE LETTER IS IN THE WORD 
            else:
# ADD THE LETTER TO THE LIST AND CAST WORD AS Q LIST THEN CHECK THE LETTER AGAINST ITS POSITION AND ADD APPEND THE LIST WITH THE LETTER THEN MAKE 
#IT A STRING AGAIN
                print("Good gjob,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
# SAME AS ABOVE BUT FOR WORDS CHECK THE USER GUESS IS EQUAL TO NUMBER LETTER IIN THE WORD AND IS ALPHABTIC
        elif len(guess) == len(word) and guess.isalpha():
#IF USER GUESS AS BEEN ENTERED
            if guess in guessed_words:
                print("You already guessed the word", guess)
#IF USER WORD AS NOT BEEN USED PRINT GUESS IS NOT THE WORD
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
#OTHERWISE THE WORD IS TRUE
            else:
                guessed = True
                word_completion = word
# uSER INPUT IS NOT VALID 
        else: 
            print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  ]
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main(): 
    word = choose_random_word (list_of_words)
    play(word)
    
    while input ("Do you want to play again? Y/N:  ").upper() =="Y":
        word = choose_random_word (list_of_words)
        play(word)
        
if __name__ == "__main__":
    main()