import tkinter

window = tkinter.Tk()
window.title('login')
window.geometry('400x400')
#window.configure(bg='#333333')

# CRIANDO ITENS
login_label = tkinter.Label(window, text='Login')
user_label = tkinter.Label(window, text='Username')
user_entry = tkinter.Entry(window)
password_label = tkinter.Label(window, text='Password')
password_entry = tkinter.Entry(window, show='*')
login_button = tkinter.Button(window, text='Enter')

# MOSTRANDO ITENS NA TELA
login_label.grid(row=1, column=1, columnspan=2)
user_label.grid(row=2, column=1)
user_entry.grid(row=2, column=2)
password_label.grid(row=3, column=1)
password_entry.grid(row=3, column=2)


window.mainloop()
