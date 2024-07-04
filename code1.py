import tkinter as tk

calc = ""

def add_to_calc(n):
    global calc
    calc += str(n)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calc)

def evaluate():
    global calc
    try:
        result = str(eval(calc))
        calc = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        pass

def clear_field():
    global calc
    calc = ""
    text_result.delete(1.0, "end")

#The GUI of the Calculator
root = tk.Tk()
root.geometry("300x275")
root.configure(background="light gray")
root.title("Basic Arithmatic Calculator")

#The text field of the Calculator
text_result = tk.Text(root, height=2, width=16, font=("Ariel", 24))
text_result.grid(columnspan=5)

#The numerical buttons in the Calculator
btn_1 = tk.Button(root, text="1", bg="light blue", command=lambda: add_to_calc(1), width=5, font=("Ariel", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", bg="light blue", command=lambda: add_to_calc(2), width=5, font=("Ariel", 14))
btn_2.grid(row=2, column=2)

btn_3= tk.Button(root, text="3", bg="light blue", command=lambda: add_to_calc(3), width=5, font=("Ariel", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", bg="light blue", command=lambda: add_to_calc(4), width=5, font=("Ariel", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", bg="light blue", command=lambda: add_to_calc(5), width=5, font=("Ariel", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", bg="light blue", command=lambda: add_to_calc(6), width=5, font=("Ariel", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", bg="light blue", command=lambda: add_to_calc(7), width=5, font=("Ariel", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", bg="light blue", command=lambda: add_to_calc(8), width=5, font=("Ariel", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", bg="light blue", command=lambda: add_to_calc(9), width=5, font=("Ariel", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", bg="light blue", command=lambda: add_to_calc(0), width=5, font=("Ariel", 14))
btn_0.grid(row=5, column=2)

#The operation buttons in the Calculator
btn_plus = tk.Button(root, text="+", bg="light blue", command=lambda: add_to_calc("+"), width=5, font=("Ariel", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", bg="light blue", command=lambda: add_to_calc("-"), width=5, font=("Ariel", 14))
btn_minus.grid(row=3, column=4)

btn_multiplication = tk.Button(root, text="*", bg="light blue", command=lambda: add_to_calc("*"), width=5, font=("Ariel", 14))
btn_multiplication.grid(row=4, column=4)

btn_division = tk.Button(root, text="/", bg="light blue", command=lambda: add_to_calc("/"), width=5, font=("Ariel", 14))
btn_division.grid(row=5, column=4)

#Other buttons
btn_paran_open = tk.Button(root, text="(", bg="light blue", command=lambda: add_to_calc("("), width=5, font=("Ariel", 14))
btn_paran_open.grid(row=5, column=1)

btn_paran_close = tk.Button(root, text=")", bg="light blue", command=lambda: add_to_calc(")"), width=5, font=("Ariel", 14))
btn_paran_close.grid(row=5, column=3)

btn_equals = tk.Button(root, text="=", bg="light blue", command=evaluate, width=5, font=("Ariel", 14))
btn_equals.grid(row=6, column=4)

btn_point = tk.Button(root, text=".", bg="light blue", command=lambda: add_to_calc("."), width=5, font=("Ariel", 14))
btn_point.grid(row=6, column=3)

btn_clear = tk.Button(root, text="Clear", bg="light blue", command=clear_field, width=11, font=("Ariel", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
