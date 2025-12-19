import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
from PIL import Image, ImageTk
import random
import sys

class DarkDiceRoller:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark Dice Roller")
        self.dice_count = 1
        self.dice_images = self.load_dice_faces()
        self.total = 0

        self.root.configure(bg='black')
        self.style = ttk.Style()
        self.style.theme_use('alt')
        
        self.style.configure('.', bg='black', fg='white')
        self.style.configure('TButton', bg='#333', fg='white')
        self.style.map('TButton', bg=[('active', '#444'), ('disabled', '#222')],fg=[('active', '#fff'), ('disabled', '#777')])
        
        self.setup_ui()
        self.adapt_layout()

    def load_dice_faces(self):
        return {
            i: ImageTk.PhotoImage(Image.open(f"dice_{i}.png").resize((80,80)))
            for i in range(1,7)
        }

    def setup_ui(self):
        self.mode_switch = ttk.Checkbutton(
            self.root, 
            text="Two Dice Mode", 
            command=self.toggle_mode,
            style='TCheckbutton'
        )
        self.mode_switch.pack(pady=10)
        
        self.dice_frame = ttk.Frame(self.root, style='Dark.TFrame')
        self.dice_frame.pack(pady=20)
        
        self.dice1_label = ttk.Label(self.dice_frame, background='black')
        self.dice1_label.pack(side=tk.LEFT, padx=10)
        
        self.dice2_label = ttk.Label(self.dice_frame, background='black')
        self.dice2_label.pack(side=tk.LEFT, padx=10)
        self.dice2_label.pack_forget()
        
        self.total_label = ttk.Label(
            self.root, 
            text="Total: 0", 
            background='black', 
            foreground='white',
            font=('Arial', 14, 'bold')
        )
        self.total_label.pack(pady=10)
        
        self.roll_button = ttk.Button(
            self.root, 
            text="Roll Dice", 
            command=self.roll_dice,
            style='TButton'
        )
        self.roll_button.pack(pady=20)

    def toggle_mode(self):
        self.dice_count = 2 if self.dice_count == 1 else 1
        if self.dice_count == 2:
            self.dice2_label.pack(side=tk.LEFT, padx=10)
        else:
            self.dice2_label.pack_forget()
        self.adapt_layout()

    def roll_dice(self):
        result1 = random.randint(1,6)
        self.dice1_label.config(image=self.dice_images[result1])
        self.total = result1
        
        if self.dice_count == 2:
            result2 = random.randint(1,6)
            self.dice2_label.config(image=self.dice_images[result2])
            self.total = result1 + result2
        
        self.total_label.config(text=f"Total: {self.total}")

    def adapt_layout(self):
        if sys.platform in ['win32', 'darwin']:
            self.root.geometry("400x300" if self.dice_count ==1 else "600x300")
        else:
            self.root.geometry("320x480")
            self.style.configure('Mobile.TCheckbutton', background='black', foreground='white')
            self.style.configure('Mobile.TButton', background='#333', foreground='white')

if __name__ == "__main__":
    root = tk.Tk()
    app = DarkDiceRoller(root)
    root.mainloop()
