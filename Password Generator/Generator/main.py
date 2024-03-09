# Import necessary modules for GUI creation
import tkinter as tk
from tkinter import ttk
# Import the generator module that contains the password generation logic
import generator

# Function to generate a password and update the GUI with the result
def generate_password():
    # Retrieve user inputs from the GUI
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    # Generate the password using the user's preferences
    password = generator.generate_password(length, include_uppercase, include_lowercase,
                                           include_digits, include_special_chars)
    # Clear the password entry field and insert the new password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # Assess the strength of the generated password
    strength = generator.assess_password_strength(password)
    # Update the strength label with the assessment result
    strength_label.config(text="Password Strength: " + strength)

    # Provide recommendations based on the password strength
    if strength == 'Weak':
        recommendation_label.config(text="Recommendation: Consider increasing the password length and including a mix of character types.", foreground="red")
    elif strength == 'Moderate':
        recommendation_label.config(text="Recommendation: Consider including additional character types to enhance password strength.", foreground="orange")
    elif strength == 'Strong':
        recommendation_label.config(text="Your password is strong. Good job!", foreground="green")
    else:  # Very Strong
        recommendation_label.config(text="Your password is very strong. Excellent!", foreground="darkgreen")

# Initialize the main window for the GUI
window = tk.Tk()
window.title("Password Generator")

# Create and arrange the GUI elements for user input and display
length_label = ttk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
length_entry = ttk.Entry(window)
length_entry.grid(row=0, column=1, padx=5, pady=5)

uppercase_var = tk.BooleanVar()
uppercase_checkbutton = ttk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_checkbutton.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

lowercase_var = tk.BooleanVar()
lowercase_checkbutton = ttk.Checkbutton(window, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_checkbutton.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

digits_var = tk.BooleanVar()
digits_checkbutton = ttk.Checkbutton(window, text="Include Digits", variable=digits_var)
digits_checkbutton.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

special_chars_var = tk.BooleanVar()
special_chars_checkbutton = ttk.Checkbutton(window, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbutton.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

generate_button = ttk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

password_label = ttk.Label(window, text="Generated Password:")
password_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
password_entry = ttk.Entry(window, width=30)
password_entry.grid(row=6, column=1, padx=5, pady=5)

strength_label = ttk.Label(window, text="Password Strength:")
strength_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

recommendation_label = ttk.Label(window, text="")
recommendation_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

# Start the GUI event loop to listen for user interactions
window.mainloop()