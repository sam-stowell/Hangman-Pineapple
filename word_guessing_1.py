import random  # Import the random module for generating random choices
import tkinter as tk  # Import the tkinter module for creating GUI
from pydoc import text

# Import styles module which presumably contains custom styles
from styles import *
from tkinter import messagebox  # Import the messagebox class from tkinter for displaying messages

# Assuming you have a file named word_bank.py with categories defined in it
from word_bank_old import categories

# Class for the word guessing game, inheriting from tk.Tk
BACKGROUND_COLOR_PRIMARY = YELLOW
BACKGROUND_COLOR_SECONDARY = YELLOW
class WordGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass
        self.title("Pineappleeeeeeeeeee")  # Set the title of the window
        self.geometry("800x600")  # Set an initial size (optional)
        self.fullscreen()  # Call the method to make the window fullscreen
        self.configure(background=BACKGROUND_COLOR_PRIMARY)  # Set the background color of the window
        # self.iconbitmap("Pineapple.ico")  # Set the icon for the window
        self.current_frame = None  # Initialize a variable to hold the current frame
        self.word = ""  # Initialize a variable to hold the word to be guessed
        self.guessed_letters = []  # Initialize a list to hold guessed letters
        self.tries = 7  # Initialize the number of tries allowed
        self.show_start_menu()  # Call a method to display the start menu

    def fullscreen(self):
        self.attributes('-fullscreen', True)  # Set the window to fullscreen
    # Method to display the start menu

    def show_start_menu(self):
        """Display the start menu where the player can start the game."""
        self.reset_game_state()  # Call a method to reset game state
        self.destroy_current_frame()  # Call a method to destroy the current frame
        self.current_frame = tk.Frame(self, background=BACKGROUND_COLOR_PRIMARY)  # Create a new frame
        self.current_frame.pack()  # Pack the frame into the window
        label = tk.Label(self.current_frame, text="Welcome to ...Still Figuring out the name...", font=HEADER_FONT,
                         background=BACKGROUND_COLOR_PRIMARY)  # Create a label widget
        label.pack()  # Pack the label into the frame
        start_button = tk.Button(self.current_frame, text="Start Game", font=BUTTON_FONT, command=self.start_game)  # Create a button widget
        start_button.pack()  # Pack the button into the frame
        quit_button = tk.Button(self.current_frame, text="Quit Game", font=BUTTON_FONT, command=self.quit_game)  # Create a button widget
        quit_button.pack()  # Pack the button into the frame
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Method to reset game state
    def reset_game_state(self):
        """Reset game state variables."""
        self.word = ""  # Reset the word
        self.guessed_letters = []  # Reset the guessed letters
        self.tries = 7  # Reset the number of tries

    # Method to start the game
    def start_game(self):
        """Start the game by displaying categories to choose from."""
        self.destroy_current_frame()  # Call a method to destroy the current frame
        self.current_frame = tk.Frame(self, background=BACKGROUND_COLOR_SECONDARY)  # Create a new frame
        self.current_frame.pack()  # Pack the frame into the window
        label = tk.Label(self.current_frame, text="Choose a category:", font=LABEL_FONT,
                         background=BACKGROUND_COLOR_SECONDARY)  # Create a label widget
        label.pack()  # Pack the label into the frame
        for category in categories:  # Iterate through categories
            button = tk.Button(self.current_frame, text=category, font=BUTTON_FONT,
                               command=lambda c=category: self.choose_word(c))  # Create a button widget for each category
            button.pack(pady=5)  # Pack the button into the frame with some padding
        back_button = tk.Button(self.current_frame, text="Back", font=BUTTON_FONT, command=self.show_start_menu)  # Create a button widget
        back_button.pack(side="top", anchor="nw", pady=10)  # Pack the button into the frame with specified positioning
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Method to choose a word from a category
    def choose_word(self, category):
        """Choose a word from the selected category and start the guessing game."""
        self.destroy_current_frame()  # Call a method to destroy the current frame
        self.current_frame = tk.Frame(self, background=BACKGROUND_COLOR_SECONDARY)  # Create a new frame
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.word = random.choice(categories[category])  # Choose a random word from the selected category
        self.word = self.word.upper() # Uppercase letters
        print(self.word) # Testing
        display_word_origional = self.word # Word before underscores
        display_word = "" # Set blank variable
        for x in display_word_origional: # Cycle through letters
            if x == " ":
                display_word = display_word + " " # Display space as a gap
            else:
                display_word = display_word + "_" # Display letters as an underscore
        print(display_word) # Testing
        word_label = tk.Label(self.current_frame, text=f"Guess the Word: {display_word}", font=LABEL_FONT,
                              background=BACKGROUND_COLOR_SECONDARY)  # Create a label widget to display the word
        # word_label.pack()  # Pack the label into the frame
        word_label.grid(row=0, column=0, columnspan=2, pady=5)

        tries_label = tk.Label(self.current_frame, text=f"Tries Left: {self.tries}", font=LABEL_FONT,
                               background=BACKGROUND_COLOR_SECONDARY)  # Create a label widget to display the number of tries
        # tries_label.pack()  # Pack the label into the frame
        tries_label.grid(row=1, column=0, columnspan=2, pady=5)

        incorrect_guess_label = tk.Label(self.current_frame, text="Incorrect guesses:", font=LABEL_FONT,
                                         background=BACKGROUND_COLOR_SECONDARY)  # Create a label widget to display incorrect guesses
        # incorrect_guess_label.pack()  # Pack the label into the frame
        # incorrect_guess_label.grid(row=2, column=0, columnspan=2, pady=5)

        congrats_label = tk.Label(self.current_frame, text="Congratulations! You guessed the word!", font=LABEL_FONT,
                                  background=BACKGROUND_COLOR_SECONDARY)  # Create a label widget for congratulatory message
        # congrats_label.grid(row=3, column=0, columnspan=2, pady=5)


        back_button = tk.Button(self.current_frame, text="Back", font=BUTTON_FONT, command=self.show_start_menu)
        # back_button.pack(side="top", anchor="ne", pady=1)  # Place the "Back" button at the top right
        back_button.grid(row=4, column=0, sticky="ne", pady=5)


        quit_button = tk.Button(self.current_frame, text="Quit", font=BUTTON_FONT, command=self.quit)
        # quit_button.pack(side="top", anchor="ne", pady=1)  # Place the "Quit" button to the left of the "Back" button
        quit_button.grid(row=4, column=1, sticky="ne", pady=5)

        alphabet_frame = tk.Frame(self.current_frame, background=BACKGROUND_COLOR_SECONDARY)  # Create a new frame for alphabet buttons
        # alphabet_frame.pack(pady=10)  # Pack the frame into the window with some padding
        alphabet_frame.grid(row=0, column=0)

        alphabet_rows = 2  # Number of rows for alphabet buttons
        alphabet_columns = 13  # Number of columns for alphabet buttons
        row_offset = 5
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  # Iterate through the alphabet
            button = tk.Button(alphabet_frame, text=char, font=BUTTON_FONT,
                               command=lambda c=char: self.handle_alphabet_button(c, word_label,
                                                                                  tries_label,
                                                                                  incorrect_guess_label,
                                                                                  congrats_label),
                               bg=BUTTON_BACKGROUND_COLOR,
                               activebackground="green",  # Change color when the button is clicked
                               activeforeground="white")  # Change text color when the button is clicked
            row_index = (ord(char) - ord('A')) // alphabet_columns + row_offset # Calculate row index
            col_index = (ord(char) - ord('A')) % alphabet_columns  # Calculate column index
            button.grid(row=row_index, column=col_index, padx=5, pady=5)  # Grid the button with specified padding

    # Method to handle alphabet button clicks
    def handle_alphabet_button(self, char, word_label, tries_label, incorrect_guess_label, congrats_label):
        """Handle button clicks for guessing letters."""
        if char in self.guessed_letters:  # Check if the letter has already been guessed
            messagebox.showinfo("Repeated Guess", "You've already guessed that letter!")  # Show a message
            return  # Return from the method
        self.guessed_letters.append(char)  # Add the guessed letter to the list
        if char not in self.word:  # Check if the guessed letter is not in the word
            self.tries -= 1  # Decrement the number of tries
            tries_label.config(text=f"Tries Left: {self.tries}")  # Update the tries label
            incorrect_guess_label.config(text=f"Incorrect guesses: {' '.join(self.guessed_letters)}")  # Update incorrect guesses label
            if self.tries == 0:  # Check if no tries left
                word_label.config(text=f"Sorry, you're out of tries! The word was: {self.word}")  # Update the word label
                self.after(2000, self.show_start_menu)  # Wait for 2 seconds before showing the start menu
                return  # Return from the method
        else:  # If the guessed letter is in the word
            new_display = "".join([letter if letter in self.guessed_letters or letter == " " else "_" for letter in self.word])  # Update the display
            word_label.config(text=f"Guess the Word: {new_display}")  # Update the word label
            if new_display == self.word:  # Check if the word has been completely guessed
                congrats_label.pack()  # Show congrats message
                self.after(2000, self.show_start_menu)  # Wait for 2 seconds before showing the start menu
                return  # Return from the method
        button = self.current_frame.nametowidget(f".!frame.!frame.{char}")  # Get the button widget by name
        button.config(bg=ACTIVE_BUTTON_BACKGROUND_COLOR, fg=ACTIVE_BUTTON_FOREGROUND_COLOR)  # Update button appearance

    # Method to destroy the current frame
    def destroy_current_frame(self):
        """Destroy the current frame to clear the screen."""
        if self.current_frame:  # Check if current frame exists
            self.current_frame.destroy()  # Destroy the current frame

    # Method to quit the game
    def quit_game(self):
        """Quit the game."""
        self.destroy()  # Call destroy method to close the window

# Check if the script is being run directly
if __name__ == "__main__":
    app = WordGuessingGame()  # Create an instance of the this game class
    app.mainloop()  # Run the main event loop of the tkinter application
