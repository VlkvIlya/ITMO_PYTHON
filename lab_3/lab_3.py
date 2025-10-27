#В терминал: pip install pygame

import tkinter as tk
import random
from pygame import mixer

# pygame.init()
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
        mixer.music.load("sound.mp3")  # Укажите путь к вашему MP3 файлу
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


word_label = tk.Label(window,
                      text="XXXXX-XXXXX-XXXXX",
                      font=("Consolas", 42),
                      bg="white",
                      fg='black')
word_label.place(x=0, y=25, relwidth=1)


btn_guess = tk.Button(window,
                      width=25,
                      height=3,
                      text="Generate",
                      command=generate)
btn_guess.place(relx=0.1, rely=0.4)


btn_exit = tk.Button(window,
                      width=25,
                      height=3,
                      text="Cancel",
                      command=cancel)
btn_exit.place(relx=0.1, rely=0.7)


window.mainloop()