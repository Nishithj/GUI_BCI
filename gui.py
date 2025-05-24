import tkinter as tk
from model_prediction import get_model_output
import numpy as np

class CursorGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Cursor Movement Game")
        self.canvas = tk.Canvas(master, width=500, height=500, bg="white")
        self.canvas.pack()

        self.cursor = self.canvas.create_oval(245, 245, 255, 255, fill="blue")
        self.target = None
        self.spawn_target()

        self.score = 0
        self.score_text = self.canvas.create_text(450, 20, text=f"Score: {self.score}", font=("Arial", 12))

        self.update_game()

    def spawn_target(self):
        from random import randint
        x, y = randint(0, 480), randint(0, 480)
        if self.target:
            self.canvas.delete(self.target)
        self.target = self.canvas.create_oval(x, y, x+10, y+10, fill="red")

    def move_cursor(self, direction):
        dx, dy = 0, 0
        if direction == "up":
            dy = -10
        elif direction == "down":
            dy = 10
        elif direction == "left":
            dx = -10
        elif direction == "right":
            dx = 10
        self.canvas.move(self.cursor, dx, dy)

    def check_collision(self):
        cursor_coords = self.canvas.coords(self.cursor)
        target_coords = self.canvas.coords(self.target)

        if (abs(cursor_coords[0] - target_coords[0]) < 10 and
            abs(cursor_coords[1] - target_coords[1]) < 10):
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.spawn_target()

    def update_game(self):
        # Replace this with actual input data generation
        input_data = self.create_fake_input()

        print("Input shape:", input_data.shape)  # Debugging line

        direction = get_model_output(input_data)
        self.move_cursor(direction)
        self.check_collision()
        self.master.after(500, self.update_game)

    def create_fake_input(self):
    # Simulate correct-shaped input: (1, 22, 30, 11, 1)
        fake_trial = np.random.rand(1, 22, 30, 11, 1)
        return fake_trial.reshape(1, -1)  # Now shape is (1, 7260)


root = tk.Tk()
game = CursorGame(root)
root.mainloop()
'''

import tkinter as tk  # original code
import random

class CursorGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Cursor Movement Game")
        self.canvas = tk.Canvas(master, width=500, height=500, bg="white")
        self.canvas.pack()

        self.cursor = self.canvas.create_oval(245, 245, 255, 255, fill="blue")
        self.target = None
        self.spawn_target()

        self.score = 0
        self.score_text = self.canvas.create_text(450, 20, text=f"Score: {self.score}", font=("Arial", 12))

        self.update_game()

    def spawn_target(self):
        x, y = random.randint(0, 480), random.randint(0, 480)
        if self.target:
            self.canvas.delete(self.target)
        self.target = self.canvas.create_oval(x, y, x+10, y+10, fill="red")

    def move_cursor(self, direction):
        dx, dy = 0, 0
        if direction == "up":
            dy = -10
        elif direction == "down":
            dy = 10
        elif direction == "left":
            dx = -10
        elif direction == "right":
            dx = 10
        self.canvas.move(self.cursor, dx, dy)

    def check_collision(self):
        cursor_coords = self.canvas.coords(self.cursor)
        target_coords = self.canvas.coords(self.target)

        if (abs(cursor_coords[0] - target_coords[0]) < 10 and
            abs(cursor_coords[1] - target_coords[1]) < 10):
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.spawn_target()

    def get_model_output(self):
        # Replace this with your model's actual output
        # Example: output = model.predict(input_data)
        # Output should be one of: "up", "down", "left", "right"
        directions = ["up", "down", "left", "right"]
        return random.choice(directions)  # simulate model prediction

    def update_game(self):
        direction = self.get_model_output()
        self.move_cursor(direction)
        self.check_collision()
        self.master.after(500, self.update_game)

root = tk.Tk()
game = CursorGame(root)
root.mainloop()
'''