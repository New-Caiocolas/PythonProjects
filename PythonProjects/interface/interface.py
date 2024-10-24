import tkinter

window = tkinter.Tk()
window.title('login')
window.geometry('400x400')
window.configure(bg='#333333')

def login():
    if user_entry.get() == 'caio' and password_entry.get() == '123':
        print('Acesso autorizado!')
    else:
        print('Acesso Negado!')

frame = tkinter.Frame(bg='#333333')

# CRIANDO ITENS
login_label = tkinter.Label(frame, text='Login', bg='#333333', font='arial, 20', fg='#0094DA')
user_label = tkinter.Label(frame, text='Username', bg='#333333', font='arial, 16', fg='#fff')
user_entry = tkinter.Entry(frame, font='arial, 16')
password_label = tkinter.Label(frame, text='Password', bg='#333333', font='arial, 16', fg='#fff')
password_entry = tkinter.Entry(frame, font='arial, 16' , show='*')
login_button = tkinter.Button(frame, text='ENTER', bg='#0094DA', font='arial, 16', fg='#fff', command=login)
login_button = tkinter.Button(frame, text='ENTER', bg='#0094DA', font='arial, 16', fg='#fff', command=login)

# MOSTRANDO ITENS NA TELA
login_label.grid(row=0, column=1, columnspan=2, sticky='news', pady=20)
user_label.grid(row=2, column=1, pady=20)
user_entry.grid(row=2, column=2)
password_label.grid(row=3, column=1, pady=20)
password_entry.grid(row=3, column=2 )
login_button.grid(row=4, column=1, columnspan=2, pady=20)
login_button.grid(row=4, column=1, columnspan=2, pady=20)

frame.pack()
window.mainloop()
