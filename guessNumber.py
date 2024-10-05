import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.secret_number = None
        self.attempts = 10
        self.time_left = 60  # Timer in seconds
        self.score = 0  # Player's score
        self.level = 1  # Starting level
        self.dark_mode = False  # Dark mode state

        # Define colors for light and dark mode
        self.light_bg = "#f0f0f0"
        self.light_fg = "#000000"
        self.dark_bg = "#2e2e2e"
        self.dark_fg = "#ffffff"

        self.master.configure(bg=self.light_bg)

        self.title_label = tk.Label(master, text="Welcome to Number Guessing Game!", bg=self.light_bg, fg=self.light_fg)
        self.title_label.pack(pady=10)

        self.range_label = tk.Label(master, text="Enter the maximum number you want to guess:", bg=self.light_bg, fg=self.light_fg)
        self.range_label.pack(pady=5)

        self.range_entry = tk.Entry(master)
        self.range_entry.pack(pady=5)

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.guess_label = tk.Label(master, text="Enter your guess:", bg=self.light_bg, fg=self.light_fg)
        self.guess_label.pack(pady=5)

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", bg=self.light_bg, fg=self.light_fg)
        self.result_label.pack(pady=10)

        self.time_label = tk.Label(master, text="Time left: 60 seconds", bg=self.light_bg, fg=self.light_fg)
        self.time_label.pack(pady=5)

        self.score_label = tk.Label(master, text=f"Score: {self.score}", bg=self.light_bg, fg=self.light_fg)
        self.score_label.pack(pady=5)

        self.level_label = tk.Label(master, text=f"Level: {self.level}", bg=self.light_bg, fg=self.light_fg)
        self.level_label.pack(pady=5)

        # Dark Mode button
        self.dark_mode_button = tk.Button(master, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.pack(pady=5)

        # Quit button
        self.quit_button = tk.Button(master, text="Quit", command=self.confirm_quit)
        self.quit_button.pack(pady=5)

    def start_game(self):
        try:
            self.number_range = int(self.range_entry.get())
            if self.number_range <= 0:
                raise ValueError
            self.secret_number = random.randint(1, self.number_range)
            self.attempts = 10
            self.time_left = 60  # Reset timer for each game
            self.result_label.config(text="You have 10 attempts to guess the number.")
            self.range_label.config(state='disabled')
            self.range_entry.config(state='disabled')
            self.start_button.config(state='disabled')
            self.submit_button.config(state='normal')  # Enable guess button
            self.update_timer()  # Start the timer when the game starts
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

    def submit_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess < self.secret_number:
                self.result_label.config(text="Your guess is too low.")
            elif guess > self.secret_number:
                self.result_label.config(text="Your guess is too high.")
            else:
                self.calculate_score()
                messagebox.showinfo("Congratulations!", f"You've guessed the secret number {self.secret_number} correctly!")
                self.level_up()  # Increase level after correct guess
                return

            self.attempts -= 1
            if self.attempts == 0:
                messagebox.showinfo("Game Over", f"Sorry, you've exhausted all your attempts. The secret number was {self.secret_number}.")
                self.reset_game()
            else:
                self.result_label.config(text=f"You have {self.attempts} attempts remaining.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

        self.guess_entry.delete(0, tk.END)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time left: {self.time_left} seconds")
            self.master.after(1000, self.update_timer)  # Call this function again after 1 second
        else:
            messagebox.showinfo("Time's up!", "Sorry, you've run out of time!")
            self.reset_game()

    def calculate_score(self):
        # Calculate score based on remaining time and attempts
        score_earned = (self.time_left * 10) + (self.attempts * 5)
        self.score += score_earned
        self.score_label.config(text=f"Score: {self.score}")

    def level_up(self):
        # Reset range entry and prompt user to input a new number range for the next level
        self.level += 1
        self.level_label.config(text=f"Level: {self.level}")
        self.range_label.config(state='normal', text=f"Level {self.level} - Enter the new maximum number:")
        self.range_entry.config(state='normal')
        self.start_button.config(state='normal', text="Set New Range and Continue")
        self.result_label.config(text="")

        # Setelah pemain men-set angka baru, mereka dapat melakukan penebakan lagi
        self.start_button.config(command=self.set_new_number)

    def set_new_number(self):
        try:
            self.number_range = int(self.range_entry.get())
            if self.number_range <= 0:
                raise ValueError
            self.secret_number = random.randint(1, self.number_range)
            self.attempts = 10
            self.time_left = 60  # Reset timer for new level
            self.result_label.config(text="You can now start guessing the new number!")
            self.range_label.config(state='disabled')
            self.range_entry.config(state='disabled')
            self.start_button.config(state='disabled')
            self.submit_button.config(state='normal')  # Enable guess button after new number is set
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

    def reset_game(self, next_level=False):
        # Reset everything back to the initial state if not progressing to next level
        if not next_level:
            self.level = 1
            self.score = 0
            self.level_label.config(text=f"Level: {self.level}")
            self.score_label.config(text=f"Score: {self.score}")

        self.range_label.config(state='normal', text="Enter the maximum number you want to guess:")
        self.range_entry.config(state='normal')
        self.start_button.config(state='normal', text="Start Game")
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.time_label.config(text="Time left: 60 seconds")
        self.submit_button.config(state='normal')

    def toggle_dark_mode(self):
        if self.dark_mode:
            # Switch to light mode
            self.master.configure(bg=self.light_bg)
            self.title_label.config(bg=self.light_bg, fg=self.light_fg)
            self.range_label.config(bg=self.light_bg, fg=self.light_fg)
            self.guess_label.config(bg=self.light_bg, fg=self.light_fg)
            self.result_label.config(bg=self.light_bg, fg=self.light_fg)
            self.time_label.config(bg=self.light_bg, fg=self.light_fg)
            self.score_label.config(bg=self.light_bg, fg=self.light_fg)
            self.level_label.config(bg=self.light_bg, fg=self.light_fg)
            self.dark_mode = False
        else:
            # Switch to dark mode
            self.master.configure(bg=self.dark_bg)
            self.title_label.config(bg=self.dark_bg, fg=self.dark_fg)
            self.range_label.config(bg=self.dark_bg, fg=self.dark_fg)
            self.guess_label.config(bg=self.dark_bg, fg=self.dark_fg)
            self.result_label.config(bg=self.dark_bg, fg=self.dark_fg)
            self.time_label.config(bg=self.dark_bg, fg=self.dark_fg)
            self.score_label.config(bg=self.dark_bg, fg=self.dark_fg)
            self.level_label.config(bg=self.dark_bg, fg=self.dark_fg)
            self.dark_mode = True

    def confirm_quit(self):
        # Confirm before quitting the game
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.master.quit()

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
