from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
from tkinter import messagebox
from tkinter import filedialog
win = Tk()
win.title("Епишев Егор Константинович")
win.geometry('600x600')
win.resizable(False, False)
tab_control = Notebook(win)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбокс')
tab_control.add(tab3, text='Текст')

def calculator():
    one = txt1.get()
    sign = combo.get()
    two = txt2.get()
    if sign == '+':
        label3.configure(text=int(one) + int(two))
    if sign == '*':
        label3.configure(text=int(one) * int(two))
    if sign == '/':
        label3.configure(text=int(one) / int(two))
    if sign == '-':
        label3.configure(text=int(one) - int(two))


label1 = Label(tab1, text='Первое число:')
label1.grid(column=0, row=0)
txt1 = Entry(tab1, width=10)
txt1.grid(column=1, row=0)
combo = Combobox(tab1)
combo['values'] = ('+', '-', '*', '/')
combo.current(0)
combo.grid(column=2, row=0)
label2 = Label(tab1, text='Второе число:')
label2.grid(column=3, row=0)
txt2 = Entry(tab1, width=10)
txt2.grid(column=4, row=0)
label3 = Label(tab1)
label3.grid(column=6, row=0)
button = Button(tab1, command=calculator, text='=')
button.grid(column=5, row=0)


def btn():
    selection = []
    if option1.get():
        selection.append('первый')
    if option2.get():
        selection.append('второй')
    if option3.get():
        selection.append('третий')
    stroka = ""
    for i in selection:
        stroka += i+"  "

    message = f"Вы выбрали {stroka} вариант"
    messagebox.showinfo('Ваш выбор', message)


option1 = BooleanVar()
option2 = BooleanVar()
option3 = BooleanVar()
chk1 = Checkbutton(tab2, text='Первый', variable=option1)
chk2 = Checkbutton(tab2, text='Второй', variable=option2)
chk3 = Checkbutton(tab2, text='Третий', variable=option3)
chk1.grid(column=0, row=0)
chk2.grid(column=1, row=0)
chk3.grid(column=2, row=0)
button2 = Button(tab2, command=btn, text='Ответить')
button2.grid(column=0, row=1)


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_entry.insert(END, file.read())


menu = Menu(tab3)
new_item = Menu(menu)
new_item.add_command(label='Загрузить файл', command=open_file)
menu.add_cascade(label='Файл', menu=new_item)
win.config(menu=menu)
text_entry = Text(tab3)
text_entry.grid()
tab_control.pack(expand=1, fill='both')
win.mainloop()