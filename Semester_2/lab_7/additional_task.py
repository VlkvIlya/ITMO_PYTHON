import requests
import tkinter as tk
from PIL import Image, ImageTk

def next_cat():
    response = requests.get("https://cataas.com/cat?type=square")
    with open('temp_cat.jpg', 'wb') as f:
        f.write(response.content)
    img = Image.open('temp_cat.jpg')
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

def cancel():
    window.destroy()

window = tk.Tk()
window.title("Cats")
window.geometry("550x300")

label = tk.Label(window)
label.pack(expand=True)

btn_next = tk.Button(window, text="Next", command=next_cat)
btn_next.pack(side="left", padx=20, pady=10)

btn_exit = tk.Button(window, text="Cancel", command=cancel)
btn_exit.pack(side="right", padx=20, pady=10)


next_cat()

window.mainloop()