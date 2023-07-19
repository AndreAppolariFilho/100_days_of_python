from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
timer = None

def get_random_word(list_of_words):
    return random.choice(list_of_words)

# ---------------------------- Load Data ------------------------------- #
try:
    csv_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    csv_data = pd.read_csv("data/french_words.csv")
data_dict = csv_data.to_dict(orient="records")
chosen_word = get_random_word(data_dict)


# ----------------------------Leaned/Not Learned actions --------------- #
def reset_canvas():
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=chosen_word["French"], fill="black")
    if timer:
        window.after_cancel(timer)


def generate_card():
    global timer
    global chosen_word
    reset_canvas()
    chosen_word = get_random_word(data_dict)
    canvas.itemconfig(word_text, text=chosen_word["French"])
    timer = window.after(3000, func=flip_card)


def not_learned_trigger():
    generate_card()


def learned_trigger():
    global chosen_word
    data_dict.remove(chosen_word)
    pd.DataFrame(data_dict).to_csv("data/words_to_learn.csv", index=False)
    generate_card()


# ---------------------------- Flip the card -------------------------- #

def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=chosen_word["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(
    400,
    263,
    image=card_front_image
)
language_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

not_learned_image = PhotoImage(file="images/wrong.png")
not_learned_button = Button(image=not_learned_image, highlightthickness=0, command=not_learned_trigger)
not_learned_button.grid(column=0, row=1)

learned_image = PhotoImage(file="images/right.png")
learned_button = Button(image=learned_image, highlightthickness=0, command=learned_trigger)
learned_button.grid(column=1, row=1)

generate_card()

window.mainloop()