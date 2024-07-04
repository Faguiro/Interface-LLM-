import os
from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk
Image.ANTIALIAS =  Image.LANCZOS
class GIFPlayer:
    def __init__(self, root, gif_path, frame_count, update_interval=100, width=None, height=None):
        self.root = root
        self.gif_path = gif_path
        self.frame_count = frame_count
        self.update_interval = update_interval
        self.width = width
        self.height = height
        self.frames = self.load_frames()
        self.label = Label(root)
        self.label.grid(row=3, column=0, columnspan=3, pady=10)  # Usando grid aqui
        self.current_frame = 0
        self.running = False

    def load_frames(self):
        if not os.path.exists(self.gif_path):
            raise FileNotFoundError(f"O arquivo {self.gif_path} não foi encontrado.")
        
        frames = []
        img = Image.open(self.gif_path)
        for i in range(self.frame_count):
            img.seek(i)
            frame = img.copy()
            if self.width and self.height:
                frame = frame.resize((self.width, self.height), Image.ANTIALIAS)
            frames.append(ImageTk.PhotoImage(frame.convert("RGBA")))  # Convertendo para RGBA para garantir compatibilidade
        return frames

    def start(self):
        self.running = True
        self.label.grid(row=3, column=0, columnspan=3, pady=10) 
        self.update_gif()

    def stop(self):
        self.running = False

    def update_gif(self):
        if self.running:
            frame = self.frames[self.current_frame]
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.label.configure(image=frame)
            self.root.after(self.update_interval, self.update_gif)

    def destroy(self):
        self.label.grid_forget()