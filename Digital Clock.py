# Digital Clock using Tkinter
# Author: Albin Anu

from tkinter import *
import time

# Create main window
root = Tk()
root.title("Digital Clock - Albin Anu")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="black")

# Label to show the time
label = Label(root, font=("Arial", 50, "bold"), bg="black", fg="lime")
label.pack(anchor="center", pady=40)

# Function to update time every 1 second
def update_time():
    current_time = time.strftime("%H:%M:%S %p")  # e.g. 14:30:45 PM
    label.config(text=current_time)
    label.after(1000, update_time)  # call again after 1000 ms

# Start the clock
update_time()

# Run the GUI window
root.mainloop()
