import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Number 1 entry
        self.num1_label = tk.Label(root, text="Enter first number:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(root)
        self.num1_entry.pack(padx = 80)

        # Number 2 entry
        self.num2_label = tk.Label(root, text="Enter second number:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(root)
        self.num2_entry.pack(padx = 80,pady=10)

        # Operation choice
        self.operation_label = tk.Label(root, text="Choose an operation:")
        self.operation_label.pack()

        self.operations = ["Add", "Subtract", "Multiply", "Divide"]
        self.operation_var = tk.StringVar(value=self.operations[0])
        self.operation_menu = tk.OptionMenu(root, self.operation_var, *self.operations)
        self.operation_menu.pack(padx = 80)

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack(padx = 80,pady=10)

        # Result label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(padx = 80,pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 == 0:  # Edge case: Division by zero
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
