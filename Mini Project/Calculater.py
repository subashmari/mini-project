import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        if y != 0:
            self.result = x / y
            return self.result
        else:
            return "Cannot divide by zero."

    def exponentiate(self, x, y):
        self.result = x ** y
        return self.result

    def square_root(self, x):
        if x >= 0:
            self.result = x ** 0.5
            return self.result
        else:
            return "Invalid input for square root. Please enter a non-negative number."

    def get_result(self):
        return self.result

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.calculator = Calculator()

        # Entry widget to display and input numbers
        self.entry = ttk.Entry(root, justify="right", font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Buttons for numbers and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(root, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure row and column weights so that they expand proportionally
        for i in range(1, 5):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        current_entry = self.entry.get()

        if button == "=":
            try:
                result = eval(current_entry)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.calculator.result = result
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_entry + button)

if __name__ == "__main__":
    root = tk.Tk()
    calculator_gui = CalculatorGUI(root)
    root.mainloop()
