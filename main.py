from tkinter import * 


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"



# ------------------ UI SETUP --------------------#

# WINDOW CONFIG
window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


# CANVAS CONFIG
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,bd=0,highlightthickness=0)
front_page = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 270, image=front_page)
canvas.grid(column=0,row=0,columnspan=2)
canvas.create_text(400,263,text="English", font=(FONT_NAME,60,"bold"))
canvas.create_text(400,150,text="German",font=(FONT_NAME,40,"italic"))


# --------------------BUTTON--------------------#
# RIGHT BUTTON
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image,bg=BACKGROUND_COLOR,bd=0,highlightthickness=0)
right_button.grid(column=1,row=1)

# WRONG BUTTON
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,bg=BACKGROUND_COLOR,bd=0,highlightthickness=0,borderwidth=0)
wrong_button.grid(column=0,row=1)



window.mainloop()