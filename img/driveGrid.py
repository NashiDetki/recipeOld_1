from tkinter import *

def clickBtnForword():
    btnForword['text'] = 'нажата'

def clickBtnBack():
    btnBack['text'] = 'нажата'   

root = Tk()
root.title('Управление')
root.geometry('250x200')

root.columnconfigure(index=1, weight=2)
root.columnconfigure(index=2, weight=1)
root.columnconfigure(index=3, weight=1)
root.rowconfigure(index=1,weight=1)
root.rowconfigure(index=2,weight=1)
root.rowconfigure(index=3,weight=1)
root.rowconfigure(index=4,weight=1)
root.rowconfigure(index=5,weight=1)

btnForword = Button(text='Вперед')
btnForword.grid(row=1, column=2)
btnForword['command'] = clickBtnForword

btnBack = Button(text='Назад')
btnBack.grid(row=3, column=2)
btnBack['command'] = clickBtnBack

btnRight = Button(text='Направо')
btnRight.grid(row=2, column=3)

btnLeft = Button(text='Налево')
btnLeft.grid(row=2, column=1)

btnConnect = Button(text='Подключиться')
btnConnect.grid(row=5, column=1)

btnDisconnect = Button(text='Отключиться')
btnDisconnect.grid(row=5, column=3)

lbText = Label(text='Text')
lbText.grid(row=4, column=2)

root.mainloop()
