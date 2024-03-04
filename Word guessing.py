import random
#dhjsfhj
# Define a dictionary to store words for each category
categories = {
    "Fruit": ["apple", "banana", "orange", "grape", "strawberry", "pineapple"],
    "Cities": ["London", "Paris", "New York", "Tokyo", "Sydney", "Rome"],
    "Books": ["Dune", "Sherlock", "Harry Potter", "Lord of the Rings", "The Great Gatsby", "To Kill a Mockingbird"]
}

def choose_word(category):
    # Select a random word from the chosen category
    return random.choice(categories[category])

def select_category():
    # Display available categories and prompt the player to choose one
    print("Available categories:")
    for category in categories:
        print("-", category)
    category = input("Choose a category: ").capitalize()
    # Ensure the chosen category is valid
    while category not in categories:
        print("Invalid category! Please choose from the available categories.")
        category = input("Choose a category: ").capitalize()
    return category

def play_game():
    # Allow the player to choose a category
    category = select_category()
    # Select a word from the chosen category
    word = choose_word(category)
    guessed_letters = []
    tries = 7

    print("Welcome to the Word Guessing Game!")
    print("Guess the word!")

    while tries > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        if display_word == word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Incorrect guess! You have", tries, "tries left.")

    if tries == 0:
        print("Sorry, you're out of tries! The word was:", word)

# Start the game
play_game()
