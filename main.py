import tkinter as tk
from PIL import Image, ImageTk
import imageio

evernight = "evernight.gif"
evernight_width = 200
evernight_height = 200 

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-transparentcolor", "white")
root.configure(bg='white')
reader = imageio.get_reader(evernight)

frames = []
for frame in reader:
    img = Image.fromarray(frame)
    img.thumbnail((evernight_width, evernight_height), Image.Resampling.LANCZOS)
    frames.append(ImageTk.PhotoImage(img))

frame_width, frame_height = frames[0].width(), frames[0].height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - frame_width - 20
y = screen_height - frame_height - 40
root.geometry(f"{frame_width}x{frame_height}+{x}+{y}")

label = tk.Label(root, bg='white')
label.pack()

frame_index = 0
def update_evernight():
    global frame_index
    label.config(image=frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)
    root.after(50, update_evernight)  # adjust speed

update_evernight()
root.mainloop()
