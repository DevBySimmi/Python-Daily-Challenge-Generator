import tkinter as tk
from tkinter import messagebox
import random
from datetime import date


# -----------------------------
# Challenge Data
# -----------------------------

challenges = {
    "🧠 Logic": {
        "Easy": [
            {
                "question": "What comes next? 2, 4, 6, 8, ?",
                "answer": "10",
                "hint": "The numbers increase by the same amount."
            },
            {
                "question": "If all cats are animals and Tom is a cat, is Tom an animal?",
                "answer": "yes",
                "hint": "Think about the relationship between cats and animals."
            },
        ],
        "Medium": [
            {
                "question": "What comes next? 3, 6, 12, 24, ?",
                "answer": "48",
                "hint": "Look at how each number changes."
            },
            {
                "question": "A clock shows 3:00. What is the angle between the hands?",
                "answer": "90",
                "hint": "Look at the position of the hour and minute hands."
            },
        ],
        "Hard": [
            {
                "question": "What comes next? 1, 4, 9, 16, 25, ?",
                "answer": "36",
                "hint": "Think about square numbers."
            },
            {
                "question": "If 5 machines make 5 items in 5 minutes, how many minutes will 100 machines take to make 100 items?",
                "answer": "5",
                "hint": "Each machine works at the same rate."
            },
        ]
    },

    "💻 Coding": {
        "Easy": [
            {
                "question": "Which Python function is used to display output?",
                "answer": "print",
                "hint": "It starts with the letter 'p'."
            },
            {
                "question": "Which symbol is used for a comment in Python?",
                "answer": "#",
                "hint": "It appears before a single-line comment."
            },
        ],
        "Medium": [
            {
                "question": "Which Python data type stores multiple items in an ordered collection?",
                "answer": "list",
                "hint": "Example: [1, 2, 3]"
            },
            {
                "question": "Which loop is commonly used to iterate through a sequence?",
                "answer": "for",
                "hint": "It can be used with range() or a list."
            },
        ],
        "Hard": [
            {
                "question": "What keyword is used to create a function in Python?",
                "answer": "def",
                "hint": "It is placed before the function name."
            },
            {
                "question": "Which Python keyword is used to handle exceptions?",
                "answer": "try",
                "hint": "It is usually paired with except."
            },
        ]
    },

    "🔢 Math": {
        "Easy": [
            {
                "question": "What is 15 + 27?",
                "answer": "42",
                "hint": "Add the tens first, then the ones."
            },
            {
                "question": "What is 8 × 7?",
                "answer": "56",
                "hint": "Think of the 7 times table."
            },
        ],
        "Medium": [
            {
                "question": "What is 15% of 200?",
                "answer": "30",
                "hint": "Convert 15% into a fraction."
            },
            {
                "question": "If x + 7 = 15, what is x?",
                "answer": "8",
                "hint": "Move 7 to the other side."
            },
        ],
        "Hard": [
            {
                "question": "What is the square root of 144?",
                "answer": "12",
                "hint": "12 × 12 = ?"
            },
            {
                "question": "If 2x + 6 = 20, what is x?",
                "answer": "7",
                "hint": "First subtract 6 from both sides."
            },
        ]
    },

    "🎯 General": {
        "Easy": [
            {
                "question": "How many days are there in a week?",
                "answer": "7",
                "hint": "Think Monday to Sunday."
            },
            {
                "question": "How many months are there in a year?",
                "answer": "12",
                "hint": "January to December."
            },
        ],
        "Medium": [
            {
                "question": "How many continents are there on Earth?",
                "answer": "7",
                "hint": "Count Asia, Africa, Europe and the others."
            },
            {
                "question": "How many sides does a hexagon have?",
                "answer": "6",
                "hint": "The prefix 'hex' can help."
            },
        ],
        "Hard": [
            {
                "question": "What is the largest planet in our Solar System?",
                "answer": "jupiter",
                "hint": "It is a gas giant."
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "answer": "mars",
                "hint": "Its surface appears reddish."
            },
        ]
    }
}


# -----------------------------
# Variables
# -----------------------------

current_challenge = None
score = 0
attempts = 0


# -----------------------------
# Functions
# -----------------------------

def generate_challenge():
    global current_challenge

    category = category_var.get()
    difficulty = difficulty_var.get()

    available = challenges[category][difficulty]
    current_challenge = random.choice(available)

    question_label.config(
        text=current_challenge["question"]
    )

    answer_entry.delete(0, tk.END)
    hint_label.config(text="💡 Hint: Click the Hint button")
    result_label.config(text="")

    difficulty_label.config(
        text=f"⭐ Difficulty: {difficulty}"
    )


def show_hint():
    if current_challenge is None:
        messagebox.showwarning(
            "No Challenge",
            "Generate a challenge first!"
        )
        return

    hint_label.config(
        text=f"💡 Hint: {current_challenge['hint']}"
    )


def check_answer():
    global score, attempts

    if current_challenge is None:
        messagebox.showwarning(
            "No Challenge",
            "Generate a challenge first!"
        )
        return

    user_answer = answer_entry.get().strip().lower()
    correct_answer = current_challenge["answer"].strip().lower()

    if not user_answer:
        messagebox.showwarning(
            "Empty Answer",
            "Please enter your answer."
        )
        return

    attempts += 1

    if user_answer == correct_answer:
        score += 10

        result_label.config(
            text="✅ Correct! +10 Points 🎉"
        )

    else:
        result_label.config(
            text=f"❌ Not quite! Correct answer: {current_challenge['answer']}"
        )

    update_score()


def update_score():
    score_label.config(
        text=f"🏆 Score: {score}    |    Attempts: {attempts}"
    )


def reset_score():
    global score, attempts

    score = 0
    attempts = 0

    update_score()

    result_label.config(
        text="🔄 Score reset!"
    )


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()

root.title("🎯 Daily Challenge Generator")
root.geometry("720x680")
root.resizable(False, False)
root.configure(bg="#121212")


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    root,
    text="🎯 Daily Challenge",
    font=("Arial", 26, "bold"),
    bg="#121212",
    fg="white"
)

title_label.pack(pady=(22, 3))


subtitle_label = tk.Label(
    root,
    text="Challenge yourself. Learn something new every day!",
    font=("Arial", 11),
    bg="#121212",
    fg="#aaaaaa"
)

subtitle_label.pack()


# -----------------------------
# Date
# -----------------------------

date_label = tk.Label(
    root,
    text=f"📅 {date.today().strftime('%d %B %Y')}",
    font=("Arial", 11),
    bg="#121212",
    fg="#1db954"
)

date_label.pack(pady=10)


# -----------------------------
# Selection Frame
# -----------------------------

selection_frame = tk.Frame(
    root,
    bg="#121212"
)

selection_frame.pack(pady=5)


category_var = tk.StringVar(
    value="🧠 Logic"
)

difficulty_var = tk.StringVar(
    value="Easy"
)


tk.Label(
    selection_frame,
    text="Category:",
    font=("Arial", 11, "bold"),
    bg="#121212",
    fg="white"
).grid(row=0, column=0, padx=5)


category_menu = tk.OptionMenu(
    selection_frame,
    category_var,
    *challenges.keys()
)

category_menu.config(
    width=15,
    bg="#292929",
    fg="white",
    activebackground="#333333",
    activeforeground="white",
    relief="flat"
)

category_menu.grid(row=0, column=1, padx=10)


tk.Label(
    selection_frame,
    text="Difficulty:",
    font=("Arial", 11, "bold"),
    bg="#121212",
    fg="white"
).grid(row=0, column=2, padx=5)


difficulty_menu = tk.OptionMenu(
    selection_frame,
    difficulty_var,
    "Easy",
    "Medium",
    "Hard"
)

difficulty_menu.config(
    width=10,
    bg="#292929",
    fg="white",
    activebackground="#333333",
    activeforeground="white",
    relief="flat"
)

difficulty_menu.grid(row=0, column=3, padx=10)


# -----------------------------
# Difficulty Label
# -----------------------------

difficulty_label = tk.Label(
    root,
    text="⭐ Difficulty: Easy",
    font=("Arial", 10, "bold"),
    bg="#121212",
    fg="#bbbbbb"
)

difficulty_label.pack(pady=8)


# -----------------------------
# Question Box
# -----------------------------

question_frame = tk.Frame(
    root,
    bg="#1e1e1e",
    width=620,
    height=150
)

question_frame.pack(pady=10)

question_frame.pack_propagate(False)


question_label = tk.Label(
    question_frame,
    text="Click 'New Challenge' to begin!",
    font=("Arial", 17, "bold"),
    bg="#1e1e1e",
    fg="white",
    wraplength=560,
    justify="center"
)

question_label.pack(
    expand=True,
    padx=20
)


# -----------------------------
# Answer Section
# -----------------------------

answer_entry = tk.Entry(
    root,
    width=45,
    font=("Arial", 13),
    bg="#242424",
    fg="white",
    insertbackground="white",
    relief="flat"
)

answer_entry.pack(
    pady=8,
    ipady=9
)


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(
    root,
    bg="#121212"
)

button_frame.pack(pady=8)


new_button = tk.Button(
    button_frame,
    text="🎲 New Challenge",
    command=generate_challenge,
    font=("Arial", 10, "bold"),
    bg="#1db954",
    fg="white",
    activebackground="#1ed760",
    relief="flat",
    padx=15,
    pady=8
)

new_button.grid(
    row=0,
    column=0,
    padx=5
)


check_button = tk.Button(
    button_frame,
    text="✅ Check Answer",
    command=check_answer,
    font=("Arial", 10, "bold"),
    bg="#333333",
    fg="white",
    activebackground="#444444",
    relief="flat",
    padx=15,
    pady=8
)

check_button.grid(
    row=0,
    column=1,
    padx=5
)


hint_button = tk.Button(
    button_frame,
    text="💡 Hint",
    command=show_hint,
    font=("Arial", 10, "bold"),
    bg="#333333",
    fg="white",
    activebackground="#444444",
    relief="flat",
    padx=15,
    pady=8
)

hint_button.grid(
    row=0,
    column=2,
    padx=5
)


# -----------------------------
# Result
# -----------------------------

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="#1db954"
)

result_label.pack(pady=5)


# -----------------------------
# Hint
# -----------------------------

hint_label = tk.Label(
    root,
    text="💡 Hint: Click the Hint button",
    font=("Arial", 10),
    bg="#121212",
    fg="#aaaaaa",
    wraplength=600
)

hint_label.pack(pady=5)


# -----------------------------
# Score
# -----------------------------

score_label = tk.Label(
    root,
    text="🏆 Score: 0    |    Attempts: 0",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="white"
)

score_label.pack(pady=8)


# -----------------------------
# Reset Button
# -----------------------------

reset_button = tk.Button(
    root,
    text="🔄 Reset Score",
    command=reset_score,
    font=("Arial", 9, "bold"),
    bg="#8b2e2e",
    fg="white",
    activebackground="#a33a3a",
    relief="flat",
    padx=12,
    pady=6
)

reset_button.pack()


# -----------------------------
# Keyboard Shortcut
# -----------------------------

root.bind(
    "<Return>",
    lambda event: check_answer()
)


# -----------------------------
# Start App
# -----------------------------

root.mainloop()