from data.helper import login, add_user, get_usernames
from tkinter import *
from functools import partial
from user.User import User


def run():
    frame = f2
    Label(frame, text="User Name").grid(row=0, column=0)
    username = StringVar()
    Entry(frame, textvariable=username).grid(row=0, column=1)

    Label(frame, text="Password").grid(row=1, column=0)
    password = StringVar()
    Entry(frame, textvariable=password, show='*').grid(row=1, column=1)

    validate_login = partial(user_login, username, password)

    Button(frame, text="Login", command=validate_login).grid(row=4, column=0)


def user_login(username, password):
    user = login(username.get(), password.get())
    if user is None:
        create_account_ui()
    else:
        success(user[0], user[1], user[2])


def create_account_ui():
    f2.pack_forget()
    frame = f3
    frame.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)

    Label(frame, text="Full Name").grid(row=0, column=0)
    name = StringVar()
    Entry(frame, textvariable=name).grid(row=0, column=1)

    Label(frame, text="User Name").grid(row=1, column=0)
    username = StringVar()
    Entry(frame, textvariable=username).grid(row=1, column=1)

    # password label and password entry box
    Label(frame, text="Password").grid(row=2, column=0)
    password = StringVar()
    Entry(frame, textvariable=password, show='*').grid(row=2, column=1)

    add_account = partial(create_account, name, username, password)

    Button(frame, text="Create Account", command=add_account).grid(row=4, column=0)


def create_account(name, username, password):
    add_user(name.get(), username.get(), password.get())
    f3.pack_forget()
    f2.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)
    run()


def success(name, username, password):
    User(name, username, password)
    f2.pack_forget()
    frame = f4
    frame.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)
    user_logout = partial(logout)

    Button(frame, text="Logout", command=user_logout).grid(row=0, column=0)


def logout():
    f4.pack_forget()
    f2.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)
    run()


if __name__ == "__main__":
    # globals
    global f2
    global f3
    global f4

    # window
    tkWindow = Tk()
    tkWindow.geometry('300x720')
    tkWindow.title('Listener')

    f1 = Frame(width=200, height=200, background="#ffffff")
    f2 = Frame(tkWindow, width=400, height=200)
    f3 = Frame(tkWindow, width=400, height=200)
    f4 = Frame(tkWindow, width=400, height=200)
    f2.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)


    run()

    tkWindow.mainloop()
