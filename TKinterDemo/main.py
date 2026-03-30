# bing tkinter tutorial

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple Tkinter App")

# Create a label widget
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

click_count = 0

# Create a button widget
def on_button_click():
    global click_count
    click_count += 1
    label.config(text=f"Button Clicked {click_count} times")

def on_button_click2():
    global click_count
    click_count += 1
    label.config(text=f"Button 2 Clicked {click_count} times")

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

button2 = tk.Button(window, text="Click Me too!", command=on_button_click2)
button2.pack()

# Run the application
window.mainloop()