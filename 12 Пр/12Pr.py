import requests
import json


from tkinter import *

win = Tk()
win.title("Епишев Егор Константинович")
win.geometry('200x200')
win.resizable(False, False)

def btn():
    username = txt.get()
    url = f'https://api.github.com/users/{username}'
    user_data = requests.get(url).json()
    info = ('company', 'created_at', 'email', 'id', 'name', 'url')

    for i in list(user_data.keys()):
        if i not in info:
            del user_data[i]

    with open("git.json", "w") as write_file:
        json.dump(user_data, write_file, indent=2)

txt = Entry(win, width=30)
txt.grid(column=0, row=0, padx=3, pady=3)
button = Button(win, command=btn, text='Потвердить')
button.grid(column=0, row=1)


win.mainloop()