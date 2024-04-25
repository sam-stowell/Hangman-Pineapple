import random  # Import the random module for generating random choices
import tkinter as tk  # Import the tkinter module for creating GUI

# Import styles module which presumably contains custom styles
from styles import *
from tkinter import messagebox  # Import the messagebox class from tkinter for displaying messages
from word_bank import categories

# Define difficulty levels
Difficulty_Levels = ["Easy", "Medium", "Hard"]

# Class for the word guessing game, inheriting from tk.Tk
class WordGuessingGame(tk.Tk):
    def __init__(self):
        # Call the constructor of the superclass
        super().__init__()
        # Set the title of the window
        self.title("Pineapple")
        # Set an initial size (optional)
        self.geometry("1280x720")
        # Call the method to make the window fullscreen
        self.fullscreen()
        # Set the background color of the window
        self.configure(background=YELLOW)
        # Set the icon for the window
        self.iconbitmap("icon.ico")
        # Initialize a variable to hold the current frame
        self.current_frame = None
        # Initialize a variable to hold the word to be guessed
        self.word = ""
        # Initialize a list to hold guessed letters
        self.guessed_letters = []
        # Initialize the number of tries allowed
        self.tries = 7
        # Call a method to display the start menu
        self.show_start_menu()


    def fullscreen(self):
        # Set the window to fullscreen
        self.attributes('-fullscreen', True)
        # Escape key to exit fullscreen mode
        self.bind("<Escape>", self.exit_fullscreen)

    def exit_fullscreen(self, event=None):
        # Exit fullscreen mode.
        self.attributes('-fullscreen', False)

    # Display the start menu where the player can start the game.
    def show_start_menu(self):
        # Call a method to reset game state
        self.reset_game_state()
        # Call a method to destroy the current frame
        self.destroy_current_frame()
        # Create a new frame
        self.current_frame = tk.Frame(self, background=YELLOW)
        # Pack the frame into the window
        self.current_frame.pack()

        # Try to open the image
        try:
            # Open the image using Tkinter's PhotoImage
            tk_image = tk.PhotoImage(file="menubackground2.png")
            # Create a label widget to display the image
            img_label = tk.Label(self.current_frame, image=tk_image, background='yellow')
            img_label.image = tk_image  # Keep a reference to prevent garbage collection
            # Place the image label at the desired position
            img_label.pack()

        # Provide error message if doesnt work
        except Exception as e:
            print("An error occurred:", e)

        # Create a label widget
        label = tk.Label(self.current_frame,
                         # text="Welcome to PINEAPPLE - A hangman alternative",
                         font=HEADER_FONT, background=YELLOW)

        # Pack the label into the frame
        label.pack()
        # Create a button widget
        start_button = tk.Button(self.current_frame, text="Start Game", font=BUTTON_FONT, command=self.start_game)
        # Pack the button into the frame
        start_button.pack()
        # Create a button widget
        quit_button = tk.Button(self.current_frame, text="Quit Game", font=BUTTON_FONT, command=self.quit_game)
        # Pack the button into the frame
        quit_button.pack()
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")


    # Method to reset game state
    def reset_game_state(self):
        # Reset the word
        self.word = ""
        # Reset the guessed letters
        self.guessed_letters = []
        # Reset the number of tries
        self.tries = 7

    # Method to start the game
    def start_game(self):
        # Call a method to destroy the current frame
        self.destroy_current_frame()
        # Create a new frame
        self.current_frame = tk.Frame(self, background=YELLOW)
        # Pack the frame into the window
        self.current_frame.pack()
        # Start the game by displaying the difficulty level selection screen.
        self.show_difficulty_level()

        # Create a label widget
        label = tk.Label(self.current_frame,
                         # text="Choose a category:",
                         font=LABEL_FONT, background=YELLOW)

        # Pack the label into the frame
        label.pack()
        category_columns = 5

        # Iterate through categories
        for category in categories:
            # Create a button widget for each category
            button = tk.Button(self.current_frame, text=category, font=BUTTON_FONT, command=lambda c=category: self.choose_word(c))
            # Pack the button into the frame with some padding
            button.pack(side="left")

        # Create a button widget
        back_button = tk.Button(self.current_frame, text="Back", font=BUTTON_FONT, command=self.show_start_menu)
        # Pack the button into the frame with specified positioning
        back_button.pack(side="bottom")
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")
        tries_count = 0

    # Method to display the difficulty level selection screen
    def show_difficulty_level(self):
        # Call a method to destroy the current frame
        self.destroy_current_frame()
        # Create a new frame
        self.current_frame = tk.Frame(self, background=YELLOW)
        # Pack the frame into the window
        self.current_frame.pack()
        # Create a label widget
        label = tk.Label(self.current_frame, text="Choose a difficulty level:", font=LABEL_FONT, background=YELLOW)
        # Place the label in the grid
        label.grid(row=0, column=0, columnspan=2, pady=10)
        # Offset for placing buttons
        row_offset = 1

        for level in Difficulty_Levels:
            button = tk.Button(self.current_frame, text=level, font=BUTTON_FONT,
                               command=lambda l=level: self.set_difficulty_level(l))
            if level == "Easy":
                button.config(bg="green")
            elif level == "Medium":
                button.config(bg="yellow")
            elif level == "Hard":
                button.config(bg="red")
            button.grid(row=row_offset, column=0, columnspan=2, pady=5)
            row_offset += 1

        # Create a back button
        back_button = tk.Button(self.current_frame, text="Back", font=BUTTON_FONT, command=self.show_start_menu)
        # Place button into grid
        back_button.grid(row=row_offset, column=0, columnspan=2, pady=10, sticky="sw")
        center_widget(self.current_frame)

    def set_difficulty_level(self, level):
        # Set the difficulty level chosen by the user
        self.difficulty_level = level
        self.show_category_selection()  # Proceed to category selection

    # Method to display the category selection screen
    def show_category_selection(self):
        # Call a method to destroy the current frame
        self.destroy_current_frame()
        # Create a new frame
        self.current_frame = tk.Frame(self, background=YELLOW)
        # Pack the frame into the window
        self.current_frame.pack()

        # Create a label widget
        label = tk.Label(self.current_frame, text="Choose a category:", font=LABEL_FONT,
                         background=YELLOW)

        # Pack the label into the frame
        label.pack()

        # Iterate through categories
        for category in categories:
            # Create a button widget for each category
            button = tk.Button(self.current_frame, text=category, font=BUTTON_FONT,command=lambda c=category: self.choose_word(c))
            # Pack the button into the frame with some padding
            button.pack(pady=5)

        # Create a button widget
        back_button = tk.Button(self.current_frame, text="Back", font=BUTTON_FONT, command=self.show_difficulty_level)
        # Pack the button into the frame with specified positioning
        back_button.pack(side="top", anchor="nw", pady=10)
        # Call a method to center the frame in the window
        center_widget(self.current_frame)


    # Method to choose a word from a category
    def choose_word(self, category):
        # Call a method to destroy the current frame
        self.destroy_current_frame()
        # Create a new frame
        self.current_frame = tk.Frame(self, background=YELLOW)
        # self.current_frame.pack()
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Sets word to random one based on category and difficulty
        self.word = random.choice(categories[category][self.difficulty_level])#
        # Uppercase Letters
        self.word = self.word.upper()

        # Choose a random word from the selected category
        # self.word = random.choice(categories[category])

        # Testing
        print(self.word)
        # Word before underscores
        display_word_origional = self.word
        # Set blank variable
        display_word = ""
        # Cycle through letters
        for x in display_word_origional:
            if x == " ":
                # Display space as a gap
                display_word = display_word + " / "
            else:
                # Display letters as an underscore
                display_word = display_word + "_ "

        # Testing
        print(display_word)

        # Create a label widget to display the word
        word_label = tk.Label(self.current_frame, text=f"Guess the Word: {display_word}", font=LABEL_FONT, background=YELLOW)
        # Pack the label into the frame
        word_label.grid(row=0, column=0)

        # Create a label widget to display the number of tries
        tries_label = tk.Label(self.current_frame, text=f"Tries Left: {self.tries}", font=LABEL_FONT, background=YELLOW)
        # Pack the label into the frame
        tries_label.grid(row=1, column=0)

        # Create a label widget to display incorrect guesses
        incorrect_guess_label = tk.Label(self.current_frame, text="Incorrect guesses:", font=LABEL_FONT, background=YELLOW)
        # incorrect_guess_label.grid(row=2, column=0, columnspan=2, pady=5)

        # Create a back button
        back_button = tk.Button(self.current_frame, text="Back", font=BUTTON_FONT, command=self.show_start_menu)
        # Place the back button at the top right
        # back_button.pack(side="top", anchor="ne", pady=1)
        back_button.grid(row=4, column=0, sticky="nw", pady=5)

        # Create end game label
        congrats_label = tk.Label(self.current_frame, text="Congratulations! You guessed the word!", font=LABEL_FONT, background=YELLOW)
        # Place end game label
        congrats_label.grid(row=1, column=0)
        # Initially hide the end game label
        congrats_label.grid_remove()

        # Create a quit button
        quit_button = tk.Button(self.current_frame, text="Quit", font=BUTTON_FONT, command=self.quit)
        # Place the quit button to the left
        # quit_button.pack(side="top", anchor="ne", pady=1)
        quit_button.grid(row=4, column=0, sticky="ne", pady=5)

        # Create a new frame for alphabet buttons
        alphabet_frame = tk.Frame(self.current_frame, background=YELLOW)
        # Pack the frame into the window with some padding
        # alphabet_frame.pack(pady=10)
        alphabet_frame.grid(row=3, column=0)

        # Number of rows for alphabet buttons
        alphabet_rows = 2
        # Number of columns for alphabet button
        alphabet_columns = 13
        # Row offset
        row_offset = 5

        # Iterate through the alphabet
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            button = tk.Button(alphabet_frame, text=char, font=BUTTON_FONT,
                               command=lambda c=char: self.handle_alphabet_button(c, word_label,
                                                                                  tries_label,
                                                                                  incorrect_guess_label,
                                                                                  congrats_label),
                               bg=BUTTON_BACKGROUND_COLOR,
                               # Change color when the button is clicked
                               activebackground="green",
                               # Change text color when the button is clicked
                               activeforeground="white")
            # Calculate row index
            row_index = (ord(char) - ord('A')) // alphabet_columns + row_offset
            # Calculate column index
            col_index = (ord(char) - ord('A')) % alphabet_columns
            # Grid the button with specified padding
            button.grid(row=row_index, column=col_index, padx=5, pady=5)

        # center_widget(self.current_frame)  # Center the frame in the window

        # Try to open the image
        try:
            # Open the image using Tkinter's PhotoImage
            tk_image = tk.PhotoImage(file="STARTbackground1.png")

            # Create a label widget to display the image
            img_label = tk.Label(self.current_frame, image=tk_image, background=YELLOW)
            # Keep a reference
            img_label.image = tk_image

            # Place the image label at the desired position
            img_label.grid(row=2, column=0, pady=5)
        # Provide error message if it doesnt work
        except Exception as e:
            print("Error loading image:", e)

        # Try to open the image
        try:
            # Open the image file directly using Tkinter's PhotoImage
            img = tk.PhotoImage(file='pineapple.png')

            # Create a label widget to display the image
            img_label = tk.Label(self.current_frame, image=img, background=CYAN)
            # Keep a reference
            img_label.image = img
            # Place the image at desired position
            img_label.grid(row=2, column=0, pady=5)
        # Provide error message if it doesnt work
        except Exception as e:
            print("An error occurred:", e)



        # Method to handle alphabet button clicks
    def handle_alphabet_button(self, char, word_label, tries_label, incorrect_guess_label, congrats_label):
        # Check if the letter has already been guessed
        if char in self.guessed_letters:
            # Show a messagebox
            messagebox.showinfo("Repeated Guess", "You've already guessed that letter!")
            return
        # Add the guessed letter to the list
        self.guessed_letters.append(char)

        # Check if the guessed letter is not in the word
        if char not in self.word:
            # Decrement the number of tries
            self.tries -= 1
            # Update the tries label
            tries_label.config(text=f"Tries Left: {self.tries}")
            # Update incorrect guesses label
            incorrect_guess_label.config(text=f"Incorrect guesses: {' '.join(self.guessed_letters)}")
            # Next stage of pineapple
            self.next_image()

            # Check if no tries left
            if self.tries == 0:
                # Update the word label
                word_label.config(text=f"Sorry, you're out of tries! The word was: {self.word}")
                # Wait for 2 seconds before showing the start menu
                self.after(2000, self.show_start_menu)
                return

        # If the guessed letter is in the word
        else:
            # Update the display
            new_display = "".join([letter if letter in self.guessed_letters or letter == " " else "_ " for letter in self.word])
            # Update the word label
            word_label.config(text=f"Guess the Word: {new_display}")
            # Check if the word has been completely guessed
            if new_display == self.word:
                # Show congrats message
                congrats_label.grid()
                # Wait for 2 seconds before showing the start menu
                self.after(2000, self.show_start_menu)
                return

        # Get the button widget by name
        button = self.current_frame.nametowidget(f".!frame.!frame.{char}")
        # Update button appearance
        button.config(bg=ACTIVE_BUTTON_BACKGROUND_COLOR, fg=ACTIVE_BUTTON_FOREGROUND_COLOR)

    # Method to destroy the current frame
    def destroy_current_frame(self):
        # Check if current frame exists
        if self.current_frame:
            # Destroy the current frame
            self.current_frame.destroy()

    # Method to quit the game
    def quit_game(self):
        # Call destroy method to close the window
        self.destroy()

    def next_image(self):
        if self.tries >= 0:
            # Find the stage of pineapple to display
            stage = str(self.tries)
            img = tk.PhotoImage(file='pineapple'+stage+'.png')
            # Create a label widget to display the image
            img_label = tk.Label(self.current_frame, image=img, background=CYAN)
            img_label.image = img
            # Place the image at desired position
            img_label.grid(row=2, column=0, columnspan=2, pady=5)
        else:
            print("end")

# Check if the script is being run directly
if __name__ == "__main__":
    # Create an instance of the game class
    app = WordGuessingGame()
    # Run the main event loop of the tkinter application
    app.mainloop()
