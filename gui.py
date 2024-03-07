from tkinter import Tk, Canvas, Button, PhotoImage
from pathlib import Path
import os
import sys
from air_canvas_with_presentation import presentation
from main import canvass  # Import the functions from the other Python file

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Air-Canvas-Interactive-Gesture-Brush-with_UI\Air-Canvas-Interactive-Gesture-Brush-main\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_button_1_click():
    presentation()  # Call the function from the other Python file for button 1

def on_button_2_click():
    canvass()  # Call the function from the other Python file for button 2

def restart_script():
    python = sys.executable
    os.execl(python, python, "gui.py")  # Restart the "gui.py" file

window = Tk()
window.geometry("811x497")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=497,
    width=811,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(650.0, 239.0, image=image_image_1)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_1_click,  # Assign the function to run on button 1 click
    relief="flat"
)
button_1.place(x=29.0, y=270.0, width=195.0, height=115.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_2_click,  # Assign the function to run on button 2 click
    relief="flat"
)
button_2.place(x=285.0, y=270.0, width=183.0, height=115.0)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(271.0, 125.0, image=image_image_2)

window.resizable(False, False)

# Function to restart the script
def on_close():
    restart_script()

# Bind the restart function to window closing event
window.protocol("WM_DELETE_WINDOW", on_close)

window.mainloop()