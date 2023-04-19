import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")
BOLD_FONT = ("Ariel", 60, "bold")
current_word = {}

# -------------- flash card database -------------------


flash_cards = pandas.read_csv("./data/french_words.csv")
cards_dict = flash_cards.to_dict(orient="records")
r_card = random.choice(cards_dict)


# -------------- App commands --------------------------


def random_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(cards_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word['French'], fill="black")
    canvas.itemconfig(card_img, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")


def is_known():
    cards_dict.remove(current_word)
    data = pandas.DataFrame(cards_dict)
    data.to_csv("./data/words_to_learn.csv")
    random_word()


# --------------   UI setup   __________________________


window = Tk()
window.title("Flash card study")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
# canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, font=FONT)
card_word = canvas.create_text(400, 263, font=BOLD_FONT)
# front_text = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)


# buttons
right = PhotoImage(file="./images/right.png")
right_btn = Button(image=right, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)
wrong = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong, highlightthickness=0, command=random_word)
wrong_btn.grid(row=1, column=0)


random_word()

window.mainloop()
