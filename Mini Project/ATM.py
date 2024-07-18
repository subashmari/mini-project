import tkinter as tk
from tkinter import ttk

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ₹{self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount}. New balance is ₹{self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds. Withdrawal failed."
        else:
            self.balance -= amount
            return f"Withdrew ₹{amount}. New balance is ₹{self.balance}"

class ATMSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator - Indian Version")

        self.atm = ATM()

        # Label to display balance
        self.balance_label = ttk.Label(root, text="")
        self.balance_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry widget for deposit/withdraw amount
        self.amount_entry = ttk.Entry(root, font=('Arial', 12))
        self.amount_entry.grid(row=1, column=0, columnspan=2, pady=10)

        # Buttons for actions
        ttk.Button(root, text="Check Balance", command=self.check_balance).grid(row=2, column=0, pady=10)
        ttk.Button(root, text="Deposit", command=self.deposit).grid(row=2, column=1, pady=10)
        ttk.Button(root, text="Withdraw", command=self.withdraw).grid(row=3, column=0, columnspan=2, pady=10)

    def check_balance(self):
        result = self.atm.check_balance()
        self.update_balance_label(result)

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            result = self.atm.deposit(amount)
            self.update_balance_label(result)
        except ValueError:
            self.update_balance_label("Invalid input. Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            result = self.atm.withdraw(amount)
            self.update_balance_label(result)
        except ValueError:
            self.update_balance_label("Invalid input. Please enter a valid number.")

    def update_balance_label(self, text):
        self.balance_label.config(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMSimulatorApp(root)
    root.mainloop()
