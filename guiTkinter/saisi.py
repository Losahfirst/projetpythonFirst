import tkinter as tk

def button_click():
    """This function is called when the button is clicked."""
    label.config(text="Button Clicked!")  # Change the label's text

# Create the main window
root = tk.Tk()
root.title("Hello, World!")

# Add a label
label = tk.Label(root, text="Hello, World!")
label.pack()  # Pack the label into the window

# Add a button
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()