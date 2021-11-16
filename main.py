from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
current_card = {}

try:
    data = pandas.read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/German_word.csv")

to_learn = data.to_dict(orient="records")
# ------------------ Next Card --------------------#
def is_right():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/word_to_learn.csv",index=False)
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="German",fill="black")
    canvas.itemconfig(word, text=current_card["German"],fill = "black")
    canvas.itemconfig(front_image,image=back_page)
    flip_timer = window.after(3000, flip_card)

# ------------------ Flip Card--------------------#


def flip_card():
    global current_card
    canvas.itemconfig(front_image, image=back_page)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


# ------------------ UI SETUP --------------------#
# WINDOW CONFIG
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


# CANVAS CONFIG
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
                bd=0, highlightthickness=0)
# FRONT IMAGE
front_page = PhotoImage(file="./images/card_front.png")
back_page = PhotoImage(file="./images/card_back.png")
front_image = canvas.create_image(400, 263, image=front_page)
canvas.grid(column=0, row=0, columnspan=2)
# Text
language = canvas.create_text(
    400, 150, text="Language", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))


# --------------------BUTTON--------------------#
# RIGHT BUTTON
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR,
                      bd=0, highlightthickness=0, command=is_right)
right_button.grid(column=1, row=1)

# WRONG BUTTON
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR,
                      bd=0, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()
