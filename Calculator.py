# A simple calculator application using Tkinter
# by Clayton Clostio

import tkinter as tk

class Calculator:
    # Initialize the Calculator class with the main application window (master)
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")  # Set the window title
        
        self.expression = ""  # This string will hold the current mathematical expression entered by the user
        self.result_var = tk.StringVar()  # This StringVar will hold the result to be displayed
        
        self.create_widgets()  # Call the method to create the calculator's widgets

    # Method to create the calculator's widgets (buttons, entry, etc.)
    def create_widgets(self):
        # Create and pack the label that will display the result or the current expression
        self.result_label = tk.Label(self.master, textvariable=self.result_var, font=("Arial", 14))
        self.result_label.pack()

        # Create and pack the entry widget where the user can type an expression
        self.expression_entry = tk.Entry(self.master, font=("Arial", 14), justify='right')
        self.expression_entry.pack()

        # Create a frame to hold the calculator buttons
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=5)

        # List of button labels in the order they will appear on the calculator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '=', '+'
        ]

        # Initialize grid position variables
        row_val = 0
        col_val = 0
        # Loop through the buttons list to create and place buttons in the button_frame
        for button in buttons:
            # Create a button for '=' that calls the calculate method when clicked
            if button == '=':
                btn = tk.Button(button_frame, text=button, command=self.calculate)
            # Create a button for 'C' that calls the clear method when clicked
            elif button == 'C':
                btn = tk.Button(button_frame, text=button, command=self.clear)
            # Create buttons for digits and operators that call append_expression when clicked
            else:
                btn = tk.Button(button_frame, text=button, command=lambda b=button: self.append_expression(b))
            # Place the button in the grid and update the position for the next button
            btn.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:  # Move to the next row after every 4th button
                col_val = 0
                row_val += 1

        # Create and pack a quit button that will close the application
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=5)

    # Method to append a value to the expression when a button is pressed
    def append_expression(self, value):
        self.expression += str(value)  # Add the value to the expression string
        self.result_var.set(self.expression)  # Update the result_var to display the current expression

    # Method to evaluate the expression and display the result
    def calculate(self):
        try:
            # Evaluate the expression using Python's eval function
            result = str(eval(self.expression))
            self.result_var.set(result)  # Display the result
            self.expression = result  # Update the expression to the result for further calculations
        except Exception as e:
            self.result_var.set("Error")  # Display an error message if evaluation fails
            self.expression = ""  # Reset the expression

    # Method to clear the current expression and result display
    def clear(self):
        self.expression = ""  # Reset the expression to an empty string
        self.result_var.set(self.expression)  # Update the result_var to clear the display

# The Calculator function inherently understands and correctly applies the order of operations according to standard mathematical rules.
# Therefore, the calculator as implemented will correctly handle the order of operations without needing any additional code for that specific purpose.

if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    calculator = Calculator(root)  # Instantiate the Calculator class with the main window
    root.mainloop()  # Start the application's main loop, waiting for user interaction
