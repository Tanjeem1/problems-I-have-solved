import tkinter as tk
import numpy as np


# Function to perform the first division
def first():
    z = []
    y = list(map(int, entry1.get().split()))  # Get the numbers from entry1
    for i in range(0, len(y)):
        a = y[i] / 2
        z.append(a)
        b = y[i] / 2
        z.append(b)
    second(z)


# Function to perform the second division
def second(z):
    n = []
    for w in z:
        c = w / 2
        n.append(c)
        d = w / 2
        n.append(d)
    third(n)


# Function to perform the third division and sum the results
def third(n):
    p = []
    for q in n:
        e = q / 2
        p.append(e)
        f = q / 2
        p.append(f)

    final_result = np.sum(p)
    result_label.config(text=f"Final result is: {final_result}")


# Function to handle the "Add" button click
def add_numbers():
    try:
        # Call the first function with the entered values
        first()
    except ValueError:
        result_label.config(text="Please enter valid numbers.")


# Set up the main window
root = tk.Tk()
root.title("Add AS MANY Numbers YOU WANT")

# Create and place the input fields and button
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.grid(row=1, column=1, padx=10, pady=10)

# Labels to describe inputs and show the result
tk.Label(root, text="After input one number (press-space Button):").grid(row=0, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=1, padx=10, pady=10)

# Run the application
root.mainloop()