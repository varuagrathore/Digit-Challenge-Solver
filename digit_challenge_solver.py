import itertools
import tkinter as tk
from tkinter import messagebox

def solve_digit_challenge(equation):
    lhs, rhs = equation.split('=')
    rhs = int(rhs.strip())
    placeholders = lhs.count('_')
    digit_combinations = itertools.permutations(range(1, 10), placeholders)
    
    solutions = []
    for combination in digit_combinations:
        test_equation = lhs
        for digit in combination:
            test_equation = test_equation.replace('_', str(digit), 1)
        try:
            if eval(test_equation) == rhs:
                solutions.append(test_equation)
        except:
            continue
    
    return solutions

def on_solve():
    equation = equation_var.get()
    if not equation:
        messagebox.showwarning("Input Error", "Please enter an equation.")
        return
    
    solutions = solve_digit_challenge(equation)
    if solutions:
        result_text = "Possible solutions:\n" + "\n".join(solutions)
    else:
        result_text = "No solutions found."
    
    result_label.config(text=result_text)

def on_button_click(char):
    current_text = equation_var.get()
    equation_var.set(current_text + char)

def on_clear():
    equation_var.set("")

# Set up the GUI
root = tk.Tk()
root.title("Digit Challenge Solver")

equation_var = tk.StringVar()

frame = tk.Frame(root, bg="lightblue")
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, textvariable=equation_var, width=50, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    '_', '0', '=', '/',
    '(', ')', 'C', '%'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        tk.Button(frame, text=button, width=5, height=2, command=on_clear, bg="red", fg="white").grid(row=row_val, column=col_val, pady=5, padx=5)
    else:
        tk.Button(frame, text=button, width=5, height=2, command=lambda char=button: on_button_click(char), bg="lightgrey").grid(row=row_val, column=col_val, pady=5, padx=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

result_label = tk.Label(frame, text="", justify=tk.LEFT, bg="lightblue", font=("Helvetica", 14))
result_label.grid(row=row_val + 1, column=0, columnspan=4, pady=10)

solve_button = tk.Button(frame, text="Solve", command=on_solve, width=20, height=2, bg="green", fg="white", font=("Helvetica", 14))
solve_button.grid(row=row_val + 2, column=0, columnspan=4, pady=10)

# Run the GUI event loop
root.mainloop()
