import tkinter as tk
from PIL import Image, ImageTk

# Creating the window
window = tk.Tk()
window.title("Rock_Paper_Scissors")
window.geometry("600x600")
window.config(bg="lightblue")

# Making canvas in window
canvas = tk.Canvas(window, width=600, height=600, bg="lightblue")
canvas.pack()

# Canvas and circle parameters
canvas_width = 600
canvas_height = 600
circle_radius = 50
spacing = 200  # Distance between circles
# Places the circles on the bottom quarterish
y_position = int(canvas_height * 0.700)

default_color = "#ffb347"  # Pastel orange (default color)
clicked_color = "#ff6666"  # Color when clicked

def change_color_on_press(event, circle_id):
    canvas.itemconfig(circle_id, fill=clicked_color)
   
def revert_color_on_release(event, circle_id):
    canvas.itemconfig(circle_id, fill=default_color)

# Position circles
first_circle_x_position = (canvas_width // 2) - spacing

# Make 3 circles on x-axis with middle centered
for i in range(3):
    # Keeps them on x-axis spaced by value
    x_position = first_circle_x_position + i * spacing
    circle_id = canvas.create_oval(
        x_position - circle_radius, y_position - circle_radius, 
        x_position + circle_radius, y_position + circle_radius,
        fill=default_color
    )


# Mouse events
    canvas.tag_bind(circle_id, "<ButtonPress-1>", lambda event, cid=circle_id: change_color_on_press(event, cid))
    canvas.tag_bind(circle_id, "<ButtonRelease-1>", lambda event, cid=circle_id: revert_color_on_release(event, cid))






# Start the event loop
window.mainloop()