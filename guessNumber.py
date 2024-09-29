import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.number_range = None
        self.secret_number = None
        self.attempts = 10

        self.title_label = tk.Label(master, text="Welcome to Number Guessing Game!")
        self.title_label.pack(pady=10)

        self.range_label = tk.Label(master, text="Enter the maximum number you want to guess:")
        self.range_label.pack(pady=5)

        self.range_entry = tk.Entry(master)
        self.range_entry.pack(pady=5)

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.guess_label = tk.Label(master, text="Enter your guess:")
        self.guess_label.pack(pady=5)

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def start_game(self):
        try:
            self.number_range = int(self.range_entry.get())
            if self.number_range <= 0:
                raise ValueError
            self.secret_number = random.randint(1, self.number_range)
            self.attempts = 10
            self.result_label.config(text="You have 10 attempts to guess the number.")
            self.range_label.config(state='disabled')
            self.range_entry.config(state='disabled')
            self.start_button.config(state='disabled')
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
                messagebox.showinfo("Congratulations!", f"You've guessed the secret number {self.secret_number} correctly!")
                self.reset_game()
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

    def reset_game(self):
        self.range_label.config(state='normal')
        self.range_entry.config(state='normal')
        self.start_button.config(state='normal')
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")
        
def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
