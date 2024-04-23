import random  # Import the random module for generating random choices
import tkinter as tk  # Import the tkinter module for creating GUI
from pydoc import text

# from PIL import ImageTk
# from PIL import Image

# Import styles module which presumably contains custom styles
from styles import *
from tkinter import messagebox  # Import the messagebox class from tkinter for displaying messages
# from PIL import Image, ImageTk
# Assuming you have a file named word_bank.py with categories defined in it
from word_bank import categories

# Define difficulty levels
Difficulty_Levels = ["Easy", "Medium", "Hard"]

# Class for the word guessing game, inheriting from tk.Tk
class WordGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass
        self.title("Pineapple")  # Set the title of the window
        self.geometry("1280x720")  # Set an initial size (optional)
        self.fullscreen()  # Call the method to make the window fullscreen
        self.configure(background=YELLOW)  # Set the background color of the window
        #self.iconbitmap("Pineapple.ico")  # Set the icon for the window
        self.current_frame = None  # Initialize a variable to hold the current frame
        self.word = ""  # Initialize a variable to hold the word to be guessed
        self.guessed_letters = []  #start game Initialize a list to hold guessed letters
        self.tries = 7  # Initialize the number of tries allowed
        self.show_start_menu()  # Call a method to display the start menu


    def fullscreen(self):
        self.attributes('-fullscreen', True)  # Set the window to fullscreen
        self.bind("<Escape>", self.exit_fullscreen)  # Escape key to exit fullscreen mode

    def exit_fullscreen(self, event=None):
        """Exit fullscreen mode."""
        self.attributes('-fullscreen', False)  # Set fullscreen attribute to False

    # Method to display the start menu
    def show_start_menu(self):
        """Display the start menu where the player can start the game."""
        self.reset_game_state()  # Call a method to reset game state
        self.destroy_current_frame()  # Call a method to destroy the current frame
        self.current_frame = tk.Frame(self, background=YELLOW)  # Create a new frame
        self.current_frame.pack()  # Pack the frame into the window

        try:
            # Open the image using Tkinter's PhotoImage
            tk_image = tk.PhotoImage(file="menubackground.jpg")

            # Create a label widget to display the image
            img_label = tk.Label(self.current_frame, image=tk_image, background='yellow')
            img_label.image = tk_image  # Keep a reference to prevent garbage collection

            # Place the image label at the desired position
            img_label.pack()
        except Exception as e:
            print("An error occurred:", e)

        label = tk.Label(self.current_frame,
                         # text="Welcome to PINEAPPLE - A hangman alternative",
                         font=HEADER_FONT, background=YELLOW)  # Create a label widget
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
        self.current_frame = tk.Frame(self, background=YELLOW)  # Create a new frame
        self.current_frame.pack()  # Pack the frame into the window
        # Start the game by displaying the difficulty level selection screen.
        self.show_difficulty_level()  # Call a method to display the difficulty level selection screen

        try:
            # Open the image using Tkinter's PhotoImage
            tk_image = tk.PhotoImage(file="menubackground.jpg")

            # Create a label widget to display the image
            img_label = tk.Label(self.current_frame, image=tk_image, background='yellow')
            img_label.image = tk_image  # Keep a reference to prevent garbage collection

            # Place the image label at the desired position
            img_label.pack()
        except Exception as e:
            print("An error occurred:", e)

        label = tk.Label(self.current_frame,
                         # text="Choose a category:",
                         font=LABEL_FONT, background=YELLOW)  # Create a label widget
        label.pack()  # Pack the label into the frame
        category_columns = 5

        for category in categories:  # Iterate through categories
            button = tk.Button(self.current_frame, text=category, font=BUTTON_FONT, command=lambda c=category: self.choose_word(c))  # Create a button widget for each category
            button.pack(side="left")  # Pack the button into the frame with some padding

        back_button = tk.Button(self.current_frame, text="Back", font=BUTTON_FONT, command=self.show_start_menu)  # Create a button widget
        back_button.pack(side="bottom")  # Pack the button into the frame with specified positioning
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")
        tries_count = 0

    # Method to display the difficulty level selection screen
    def show_difficulty_level(self):
        """Display the difficulty level selection screen."""
        self.destroy_current_frame()  # Call a method to destroy the current frame
        self.current_frame = tk.Frame(self, background=YELLOW)  # Create a new frame
        self.current_frame.pack()  # Pack the frame into the window
        label = tk.Label(self.current_frame, text="Choose a difficulty level:", font=LABEL_FONT, background=YELLOW)  # Create a label widget
        label.grid(row=0, column=0, columnspan=2, pady=10)  # Place the label in the grid
        row_offset = 1  # Offset for placing buttons

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
        back_button.grid(row=row_offset, column=0, columnspan=2, pady=10, sticky="sw")
        center_widget(self.current_frame)

    def set_difficulty_level(self, level):
        """Set the difficulty level chosen by the user."""
        self.difficulty_level = level
        self.show_category_selection()  # Proceed to category selection

    # Method to display the category selection screen
    def show_category_selection(self):
        """Display the category selection screen."""
        self.destroy_current_frame()  # Call a method to destroy the current frame
        self.current_frame = tk.Frame(self, background=YELLOW)  # Create a new frame
        self.current_frame.pack()  # Pack the frame into the window
        label = tk.Label(self.current_frame, text="Choose a category:", font=LABEL_FONT,
                         background=YELLOW)  # Create a label widget
        label.pack()  # Pack the label into the frame
        for category in categories:  # Iterate through categories
            button = tk.Button(self.current_frame, text=category, font=BUTTON_FONT,
                               command=lambda c=category: self.choose_word(
                                   c))  # Create a button widget for each category
            button.pack(pady=5)  # Pack the button into the frame with some padding
        back_button = tk.Button(self.current_frame, text="Back", font=BUTTON_FONT,
                                command=self.show_difficulty_level)  # Create a button widget
        back_button.pack(side="top", anchor="nw", pady=10)  # Pack the button into the frame with specified positioning
        center_widget(self.current_frame)  # Call a method to center the frame in the window


    # Method to choose a word from a category
    def choose_word(self, category):
        """Choose a word from the selected category and start the guessing game."""

        self.destroy_current_frame()  # Call a method to destroy the current frame
        self.current_frame = tk.Frame(self, background=YELLOW)  # Create a new frame
        # self.current_frame.pack()
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")


        # canvas = tk.Canvas(width=1920, height=1080, bg='blue')
        # canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        # image = tk.PhotoImage(file="background.png")
        # canvas.create_image(0, 0, image=image, anchor=NW)

        # try:
        #     # Load background image
        #     bg_img = tk.PhotoImage(file="background.png")
        #     print("Background Image Loaded:", bg_img)
        #
        #     # Create a Canvas widget to display the background image
        #     canvas = tk.Canvas(self.current_frame, width=1920, height=1080)
        #     canvas.pack(fill="both", expand=True)
        #     print("Canvas created and placed")
        #
        #     # Place the background image on the canvas
        #     canvas.create_image(0, 0, image=bg_img, anchor="nw")
        #     print("Background Image placed on Canvas")
        #
        # except tk.TclError as e:
        #     print("Error loading background image:", e)

        # try:
        #     # Open the image using Tkinter's PhotoImage
        #     tk_image = tk.PhotoImage(file="background.png")
        #
        #     # Create a label widget to display the image
        #     img_label = tk.Label(self.current_frame, image=tk_image, background=YELLOW)
        #     img_label.image = tk_image  # Keep a reference to prevent garbage collection
        #
        #     # Place the image label at the desired position
        #     img_label.grid(row=1, column=0, columnspan=2, pady=5)
        #
        # except Exception as e:
        #     print("Error loading image:", e)

        # Choose a random word from the selected category
        self.word = random.choice(categories[category][self.difficulty_level])
        self.word = self.word.upper() # Uppercase Letters

        # self.word = random.choice(categories[category])  # Choose a random word from the selected category
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
                              background=YELLOW)  # Create a label widget to display the word
        # word_label.pack()  # Pack the label into the frame
        word_label.grid(row=0, column=0)

        tries_label = tk.Label(self.current_frame, text=f"Tries Left: {self.tries}", font=LABEL_FONT,
                               background=YELLOW)  # Create a label widget to display the number of tries
        # tries_label.pack()  # Pack the label into the frame
        tries_label.grid(row=1, column=0)

        incorrect_guess_label = tk.Label(self.current_frame, text="Incorrect guesses:", font=LABEL_FONT,
                                         background=YELLOW)  # Create a label widget to display incorrect guesses
        # incorrect_guess_label.pack()  # Pack the label into the frame
        # incorrect_guess_label.grid(row=2, column=0, columnspan=2, pady=5)


        back_button = tk.Button(self.current_frame, text="Back", font=BUTTON_FONT, command=self.show_start_menu)
        # back_button.pack(side="top", anchor="ne", pady=1)  # Place the "Back" button at the top right
        back_button.grid(row=4, column=0, sticky="nw", pady=5)

        congrats_label = tk.Label(self.current_frame, text="Congratulations! You guessed the word!", font=LABEL_FONT, background=YELLOW)
        congrats_label.grid(row=1, column=0)
        congrats_label.grid_remove()  # Initially hide the congratulations label

        quit_button = tk.Button(self.current_frame, text="Quit", font=BUTTON_FONT, command=self.quit)
        # quit_button.pack(side="top", anchor="ne", pady=1)  # Place the "Quit" button to the left of the "Back" button
        quit_button.grid(row=4, column=0, sticky="ne", pady=5)

        alphabet_frame = tk.Frame(self.current_frame, background=YELLOW)  # Create a new frame for alphabet buttons
        # alphabet_frame.pack(pady=10)  # Pack the frame into the window with some padding
        alphabet_frame.grid(row=3, column=0)

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

        # center_widget(self.current_frame)  # Center the frame in the window



        try:
            # Open the image file directly using Tkinter's PhotoImage
            img = tk.PhotoImage(file='pineapple.png')

            # Create a label widget to display the image
            img_label = tk.Label(self.current_frame, image=img, background='cyan')
            img_label.image = img  # Keep a reference to prevent garbage collection
            img_label.grid(row=2, column=0, pady=5)  # Place the image at desired position
        except Exception as e:
            print("An error occurred:", e)

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
            self.next_image()
            if self.tries == 0:  # Check if no tries left
                word_label.config(text=f"Sorry, you're out of tries! The word was: {self.word}")  # Update the word label
                self.after(2000, self.show_start_menu)  # Wait for 2 seconds before showing the start menu
                return  # Return from the method
        else:  # If the guessed letter is in the word
            new_display = "".join([letter if letter in self.guessed_letters or letter == " " else "_" for letter in self.word])  # Update the display
            word_label.config(text=f"Guess the Word: {new_display}")  # Update the word label
            if new_display == self.word:  # Check if the word has been completely guessed
                congrats_label.grid()  # Show congrats message
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

    def next_image(self):
        if self.tries >= 0:
            from PIL import Image, ImageTk
            # Load image file
            stage = str(self.tries)
            img = Image.open('pineapple'+stage+'.png')
            img = img.convert("RGBA")
            # canvas = tk.Canvas(self.current_frame, bg="blue")
            # canvas.grid(row=1, column=0, columnspan=2, pady=5)
            # canvas.create_image(0, 0, image=img, anchor=tk.NW)

            img = ImageTk.PhotoImage(img)
            # Create a label widget to display the image
            img_label = tk.Label(self.current_frame, image=img, background=CYAN)
            img_label.image = img
            img_label.grid(row=2, column=0, columnspan=2, pady=5)  # Place the image at desired position
        else:
            print("end")

# Check if the script is being run directly
if __name__ == "__main__":
    app = WordGuessingGame()  # Create an instance of the this game class
    app.mainloop()  # Run the main event loop of the tkinter application
