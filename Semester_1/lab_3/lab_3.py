#В терминал: pip install pygame (для звука) и pip install Pillow (для гифки)

import tkinter as tk
import random
from pygame import mixer
from PIL import Image, ImageTk, ImageSequence

mixer.init()

alph = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789']


def cancel():
    window.destroy()


def generate():
    string = ''
    for i in range(3):
        block = ''
        alph_block = [[], []]
        for i in range(3):
            alph_block[0].append(alph[0][random.randint(0, len(alph[0]) - 1)])
        for i in range(2):
            alph_block[1].append(alph[1][random.randint(0, len(alph[1])-1)])

        for i in range(5):
            if alph_block[0] != [] and alph_block[1] != []:
                numb = random.randint(0, 1)
                index = random.randint(0, len(alph_block[numb])-1)
                block += alph_block[numb][index]
                alph_block[numb].pop(index)
            else:
                if alph_block[0] == []:
                    index = random.randint(0, len(alph_block[1]) - 1)
                    block += alph_block[1][index]
                    alph_block[1].pop(index)

                else:
                    index = random.randint(0, len(alph_block[0]) - 1)
                    block += alph_block[0][index]
                    alph_block[0].pop(index)

        string += block + "-"
    string = string[:-1]

    word_label.configure(text=string)


def sound():
    try:
        mixer.music.load("sound.mp3")
        mixer.music.play(-1)
    except:
        print("Нет файла sound.mp3")


window = tk.Tk()
window.title("KeyGeneration")
window.geometry("600x400")
sound()

bg = tk.PhotoImage(file='bg.png')
label_bg = tk.Label(window, image=bg)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)



gif_image = Image.open("golden_key.gif")
gif_frames = []

for frame in ImageSequence.Iterator(gif_image):
    gif_frame = ImageTk.PhotoImage(frame.convert('RGB'))
    gif_frames.append(gif_frame)

current_frame = 0

def gif():
    global current_frame
    if current_frame == len(gif_frames)-1:
        current_frame = -1
    current_frame = current_frame + 1
    gif_label.configure(image=gif_frames[current_frame])
    window.after(130, gif)

gif_label = tk.Label(window)
gif_label.place(x=350, y=155)
gif()


word_label = tk.Label(window,
                      text="XXXXX-XXXXX-XXXXX",
                      font=("Consolas", 42),
                      bg="white",
                      fg='black')
word_label.place(x=0, y=25, relwidth=1)


btn_gen = tk.Button(window,
                      width=27,
                      height=4,
                      text="Generate",
                      command=generate)
btn_gen.place(relx=0.1, y=160)


btn_exit = tk.Button(window,
                      width=27,
                      height=4,
                      text="Cancel",
                      command=cancel)
btn_exit.place(relx=0.1, y=270)


window.mainloop()