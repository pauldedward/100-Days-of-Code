from tkinter import *

def mile_to_km():
    mile = float(mile_input.get())
    km = round(mile * 1.60934, 2)
    km_rs_label.configure(text=f"{km}")
    
window = Tk()
window.minsize(width=100, height=80)
window.title("Mile to km converter")
window.configure(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

miles_label = Label(text="Miles:")
miles_label.grid(column=2, row=0)

is_eq_label = Label(text="is equal to:")
is_eq_label.grid(column=0, row=1)

km_rs_label = Label(text="0")
km_rs_label.grid(column=1, row=1) 

km_label = Label(text="Kms")
km_label.grid(column=2, row=1) 

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()

