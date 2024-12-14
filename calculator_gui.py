import tkinter as tk
from tkinter import ttk
import math

# Tugma bosilganda amalga oshiriladigan funksiya
def button_click(value):
    if value == "C":
        entry_var.set("")  # Tozalash
    elif value == "x":
        entry_var.set(entry_var.get()[:-1])  # Bitta belgini o'chirish
    elif value == "=":
        try:
            expression = entry_var.get()
            # Trigonometric functions
            expression = expression.replace("sin(", "math.sin(math.radians(")
            expression = expression.replace("cos(", "math.cos(math.radians(")
            expression = expression.replace("tan(", "math.tan(math.radians(")
            expression = expression.replace("pi", "math.pi")
            expression = expression.replace("e", "math.e")
            result = eval(expression)  # Ifodani baholash
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + value)

# Oynani sozlash
root = tk.Tk()
root.title("Kalkulyator")
root.geometry("360x500")
root.resizable(False, False)
root.configure(bg="#2C3E50")

# Kirish maydoni
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right")
entry.place(x=10, y=20, width=340, height=50)

# Tugmalarni joylashtirish uchun ro'yxat
buttons = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", "sin(",
    "1", "2", "3", "-", "cos(",
    "0", ".", "=", "+", "tan(",
    "pi", "e", "x", "", ""
]

# Tugmalar yaratish va joylashtirish
row, col = 0, 0
for btn in buttons:
    if btn:
        button = tk.Button(
            root, text=btn, font=("Arial", 16), bg="#34495E", fg="white",
            activebackground="#1ABC9C", activeforeground="white",
            command=lambda b=btn: button_click(b)
        )
        button.place(x=10 + col * 70, y=80 + row * 70, width=60, height=60)
    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()
