from calendar import month
from tkinter import *

def valorGasto():
  gasto = input("Por favor ingrese el valor: $")
  return gasto

def nombreProducto():
  producto = input("Por favor ingrese nombre del gasto: ").upper()
  return producto

def save():
  month = month_entry.get()
  category = category_entry.get()
  description = description_entry.get()
  expenses = expenses_entry.get()

  with open(f"csv/{month}.csv", "a", encoding='utf-8-sig') as file:
    file.write(f"{category.upper()};{description};{expenses}\n")
    description_entry.delete(0, END)
    expenses_entry.delete(0, END)

# =================== UI SETUP =======================
window = Tk()
window.title("MONEY MANAGER")
window.config(padx=50, pady=50) # Relleno en los bordes del lienzo

canvas = Canvas(height=200, width=400)  #Creación del lienzo
#logo_img = PhotoImage(file="logo.png")
#canvas.create_image(100, 100, image=logo_img)
#canvas.grid(row=0, column=1)

#Labels

month_label = Label(text="Month (YYYYMM):")
month_label.grid(row=0, column=0)
category_label= Label(text="Category:")
category_label.grid(row=1, column=0)
description_label = Label(text="Description:")
description_label.grid(row=2, column=0)
expenses_label = Label(text="Expenses:")
expenses_label.grid(row=3, column=0)

#Entries

month_entry = Entry(width=20)
month_entry.grid(row=0, column=1)
category_entry = Entry(width=20)
category_entry.grid(row=1, column=1)
description_entry = Entry(width=20)
description_entry.grid(row=2, column=1)
expenses_entry = Entry(width=20)
expenses_entry.grid(row=3, column=1)

# Button

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=0, columnspan=2)


window.mainloop()