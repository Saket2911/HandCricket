import tkinter as tk
from tkinter import messagebox
import random

runs = 0
runs_comp = 0
choices = [1, 2, 3, 4, 5]


def show_result():
    if runs > runs_comp:
        messagebox.showinfo(
            "Result",
            f"You WON the match!\n\nYour Score: {runs}\nComputer Score: {runs_comp}"
        )
    elif runs_comp > runs:
        messagebox.showinfo(
            "Result",
            f"You LOST the match!\n\nYour Score: {runs}\nComputer Score: {runs_comp}"
        )
    else:
        messagebox.showinfo(
            "Result",
            f"Match TIED!\n\nYour Score: {runs}\nComputer Score: {runs_comp}"
        )


def batting_round(parent, next_round):
    win = tk.Toplevel(parent)
    win.geometry("800x500")
    win.config(bg="black")
    win.title("Batting")

    label = tk.Label(
        win, text="You Are Batting",
        font=("Arial", 40, "bold"),
        fg="green", bg="black"
    )
    label.pack(pady=20)

    def play(run):
        global runs
        comp = random.choice(choices)
        if run == comp:
            messagebox.showinfo("Out", "You are OUT!")
            win.destroy()
            next_round()
        else:
            runs += run

    for i in range(1, 6):
        tk.Button(
            win, text=str(i),
            font=("Arial", 30, "bold"),
            command=lambda x=i: play(x)
        ).place(x=80 + (i - 1) * 140, y=250)


def bowling_round(parent, next_round):
    win = tk.Toplevel(parent)
    win.geometry("800x500")
    win.config(bg="black")
    win.title("Bowling")

    label = tk.Label(
        win, text="You Are Bowling",
        font=("Arial", 40, "bold"),
        fg="red", bg="black"
    )
    label.pack(pady=20)

    def play(ball):
        global runs_comp
        comp = random.choice(choices)
        if ball == comp:
            messagebox.showinfo("Out", "Computer is OUT!")
            win.destroy()
            next_round()
        else:
            runs_comp += comp

    for i in range(1, 6):
        tk.Button(
            win, text=str(i),
            font=("Arial", 30, "bold"),
            command=lambda x=i: play(x)
        ).place(x=80 + (i - 1) * 140, y=250)


def start_batting():
    batting_round(root, lambda: bowling_round(root, show_result))


def start_bowling():
    bowling_round(root, lambda: batting_round(root, show_result))


root = tk.Tk()
root.geometry("800x500")
root.title("Hand Cricket")
root.config(bg="black")

title = tk.Label(
    root, text="Hand Cricket With Computer",
    font=("Arial", 40, "bold"),
    fg="blue", bg="black"
)
title.pack(pady=30)

btn1 = tk.Button(
    root, text="Batting",
    font=("Arial", 35, "bold"),
    bg="green", command=start_batting
)
btn1.place(x=100, y=200)

btn2 = tk.Button(
    root, text="Bowling",
    font=("Arial", 35, "bold"),
    bg="red", command=start_bowling
)
btn2.place(x=450, y=200)

root.mainloop()
