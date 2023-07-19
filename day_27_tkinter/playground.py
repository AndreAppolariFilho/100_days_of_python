import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
#Label



my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

def button_clicked():

    my_label.config(text=input_field.get())

button = tkinter.Button(text="Click Me", command=button_clicked)

button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command=button_clicked)

new_button.grid(column=2, row=0)

input_field = tkinter.Entry(width=10)

input_field = tkinter.Entry(width=10)

input_field.grid(column=3, row=2)

window.mainloop()
