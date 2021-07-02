from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card ={}
to_learnDict = {}
#reading data from pandas
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learnDict = data.to_dict(orient="records")
else:
    #converting csv-Data to a dict
    to_learnDict = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card= random.choice(to_learnDict)
    canvas.itemconfig(french_label,text="French")
    current_word = current_card['French']
    canvas.itemconfig(frenchMeaning_label, text=current_word)
    canvas.itemconfig(card_bg, image= card_front)
    flip_timer = screen.after(3000,func=flip_card)





def flip_card():
    canvas.itemconfig(french_label,text="English",fill = 'white')
    card_front.config(file = "images/card_back.png")
    current_word = current_card['English']
    canvas.itemconfig(frenchMeaning_label, text=current_word,fill = 'white')
    canvas.itemconfig(card_bg, image=card_back)

def is_know():
    to_learnDict.remove(current_card)
    data = pandas.DataFrame(to_learnDict)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()



screen = Tk()
screen.title("Flash Card")
screen.config(bg= BACKGROUND_COLOR,padx = 50,pady = 50)
flip_timer= screen.after(3000,func=flip_card)


canvas = Canvas(width = 800, height = 525, highlightthickness = 0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file= "images/card_front.png")
card_back = PhotoImage(file= "images/card_back.png")
card_bg = canvas.create_image(400,263, image= card_front)
canvas.grid(row = 0, column = 0,columnspan = 2)


french_label = canvas.create_text(400,150,text="",font= ("Arial", 40,"italic"))
frenchMeaning_label = canvas.create_text(400,263,text="",font= ("Arial", 60,"bold"))



right_img = PhotoImage(file= "images/right.png")
known_btn = Button(image = right_img,command = is_know)
known_btn.grid(row = 1 ,column = 1)

wrong_img = PhotoImage(file= "images/wrong.png")
unknown_btn = Button(image = wrong_img,command = next_card)
unknown_btn.grid(row = 1 ,column = 0)

next_card()


screen.mainloop()