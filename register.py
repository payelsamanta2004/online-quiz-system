import tkinter as tk
from tkinter import messagebox

from database import connect_db



def register_window(parent):

    win=tk.Toplevel(parent)

    win.title("Register")
    win.geometry("350x250")



    tk.Label(
        win,
        text="Username"
    ).pack()


    username=tk.Entry(win)
    username.pack()



    tk.Label(
        win,
        text="Password"
    ).pack()


    password=tk.Entry(
        win,
        show="*"
    )

    password.pack()



    def register():

        db=connect_db()

        cursor=db.cursor()


        cursor.execute(
            """
            INSERT INTO users(username,password)
            VALUES(%s,%s)
            """,
            (
                username.get(),
                password.get()
            )
        )


        db.commit()

        db.close()



        messagebox.showinfo(
            "Success",
            "Registration Done"
        )

        win.destroy()



    tk.Button(
        win,
        text="Register",
        command=register
    ).pack(pady=20)