import tkinter


def miles_to_kilometers(miles_value):
    return round(miles_value * 1.609344)

assert miles_to_kilometers(10) == 16

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
#Label
my_label = tkinter.Label(text="I am a label")
my_label.grid(column=0, row=1)

def button_clicked():
    result_label.config(text=miles_to_kilometers(float(input_field.get())))

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input_field = tkinter.Entry(width=7)
input_field.grid(column=1, row=0)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

window.mainloop()