import random
from tkinter import *
import csv
from math import *
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
DEFAULT_FONT = (FONT_NAME, 20, "bold")
word_list = "./data/french_words.csv"
curr_word_english = ""
curr_word_french = ""
curr_word_int = 0

# ----------------------------Rand.

# ----------------------------Functions
def initialize():
    correct_button.after_cancel(gen_rand_word)
    canvas.itemconfig(card_image, image=c_front_image)
    print(f"inside initialize")
    gen_rand_word()
    time.sleep(1)


def gen_rand_word():
    global curr_word_english
    global curr_word_french
    global curr_word_int
    canvas.itemconfig(card_image, image=c_front_image)

    data = pandas.read_csv(word_list)
    data_dict = data.to_dict() # couldv'e done data.to_dict(orient='record') if i wanted the french and englsih in one dict together in small sectinos
    print(data_dict)
    curr_word_int = random.randint(0, len(data_dict["French"])-1)
    curr_word_french = data_dict["French"][curr_word_int]
    curr_word_english = data_dict["English"][curr_word_int]
    canvas.itemconfig(title_word, text="French")
    canvas.itemconfig(word_word, text=curr_word_french)

    print(f"French: {curr_word_french} \nEnglish: {curr_word_english}")
    canvas.itemconfig(word_word, text=curr_word_french)
    print('after edit')
    flip_card()


def flip_card():
    time.sleep(1)
    canvas.itemconfig(card_image, image=c_back_image)
    canvas.itemconfig(title_word, text="English")
    canvas.itemconfig(word_word, text=curr_word_english)








# ----------------------------Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# ----------------------------Images
check_image = PhotoImage(file='./images/right.png')
x_image = PhotoImage(file='./images/wrong.png')
c_front_image = PhotoImage(file='./images/card_front.png')
c_back_image = PhotoImage(file='./images/card_back.png')

canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 262, image=c_front_image)
canvas.grid(column=1, row=1, columnspan=2)


# ----------------------------Titles
title_text = "French"
word_text = "word"
title_word = canvas.create_text(400, 150, text=title_text, font=(FONT_NAME, 25, "bold"))
word_word = canvas.create_text(400, 263, text=word_text, font=(FONT_NAME, 40, "bold"))
# ----------------------------Buttons
correct_button = Button(window, image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=initialize)
correct_button.grid(column=2, row=2)

wrong_button = Button(window, image=x_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=initialize)
wrong_button.grid(column=1, row=2)

initialize()






















































window.mainloop()





























