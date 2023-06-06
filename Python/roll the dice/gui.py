import tkinter as tk
from PIL import ImageTk, Image
import random


def roll_dice():
    return random.randint(1, 6)


def update_dice_image(dice_value):
    dice_image_path = f'Dices/dice{dice_value}.png'
    image = Image.open(dice_image_path)
    image = image.resize((250, 250), Image.ANTIALIAS)
    dice_image = ImageTk.PhotoImage(image)
    dice_label.configure(image=dice_image)
    dice_label.image = dice_image


def roll_button_clicked():
    dice_result = roll_dice()
    update_dice_image(dice_result)
    result_label.configure(text=f"You rolled a {dice_result}")


# Create the main window
window = tk.Tk()
window.title("Dice Rolling Simulator")
window.geometry("400x400")
window.resizable(False, False)

# Load dice images
dice_images = [
    ImageTk.PhotoImage(Image.open("Dices/dice1.png").resize((250, 250), Image.ANTIALIAS)),
    ImageTk.PhotoImage(Image.open("Dices/dice2.png").resize((250, 250), Image.ANTIALIAS)),
    ImageTk.PhotoImage(Image.open("Dices/dice3.png").resize((250, 250), Image.ANTIALIAS)),
    ImageTk.PhotoImage(Image.open("Dices/dice4.png").resize((250, 250), Image.ANTIALIAS)),
    ImageTk.PhotoImage(Image.open("Dices/dice5.png").resize((250, 250), Image.ANTIALIAS)),
    ImageTk.PhotoImage(Image.open("Dices/dice6.png").resize((250, 250), Image.ANTIALIAS))
]

# Create GUI elements
dice_label = tk.Label(window, image=dice_images[0])
dice_label.pack(pady=20)

result_label = tk.Label(window, text="Press Roll Dice to start")
result_label.pack()

roll_button = tk.Button(window, text="Roll Dice", command=roll_button_clicked)
roll_button.pack(pady=10)

# Start the GUI main loop
window.mainloop()
