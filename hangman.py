import random
import tkinter as tk
from tkinter import messagebox

words = ["python", "laptop", "science", "gaming", "rocket"]
word = random.choice(words)

guessed_letters = []
tries = 6

root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")

word_label = tk.Label(root, text="_ " * len(word), font=("Arial", 24))
word_label.pack(pady=20)

tries_label = tk.Label(root, text=f"Remaining Tries: {tries}", font=("Arial", 14))
tries_label.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

def update_word():
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    word_label.config(text=display)

    if "_" not in display:
        messagebox.showinfo("Hangman", "You Won!")
        root.destroy()

def guess_letter():
    global tries

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if guess in word:
        guessed_letters.append(guess)
    else:
        tries -= 1
        tries_label.config(text=f"Remaining Tries: {tries}")

    update_word()

    if tries == 0:
        messagebox.showerror("Hangman", f"You Lost! Word was {word}")
        root.destroy()

button = tk.Button(root, text="Guess", command=guess_letter)
button.pack()

update_word()

root.mainloop()
