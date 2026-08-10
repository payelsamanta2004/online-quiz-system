import tkinter as tk
from tkinter import messagebox

from database import connect_db
from quiz import Quiz



def login_window(parent):

    win = tk.Toplevel(parent)

    win.title("User Login")
    win.geometry("350x300")
    win.resizable(False, False)



    # Username

    tk.Label(
        win,
        text="Username",
        font=("Arial",12)
    ).pack(pady=5)


    username_entry = tk.Entry(win)

    username_entry.pack()



    # Password

    tk.Label(
        win,
        text="Password",
        font=("Arial",12)
    ).pack(pady=5)



    password_entry = tk.Entry(
        win,
        show="*"
    )

    password_entry.pack()



    # Login Function

    def login():


        username = username_entry.get().strip()

        password = password_entry.get().strip()



        if username == "" or password == "":

            messagebox.showwarning(
                "Warning",
                "Enter Username and Password"
            )

            return



        try:

            db = connect_db()

            cursor = db.cursor()



            cursor.execute(
                """
                SELECT * FROM users
                WHERE username=%s AND password=%s
                """,
                (
                    username,
                    password
                )
            )


            result = cursor.fetchone()


            db.close()



            if result:


                # IMPORTANT
                # destroy করার আগে username save

                login_user = username



                messagebox.showinfo(
                    "Success",
                    "Login Successful"
                )



                win.destroy()



                Quiz(
                    parent,
                    login_user
                )



            else:


                messagebox.showerror(
                    "Login Failed",
                    "Invalid Username or Password"
                )



        except Exception as e:


            messagebox.showerror(
                "Database Error",
                str(e)
            )



    # Login Button

    tk.Button(
        win,
        text="LOGIN",
        width=15,
        height=2,
        bg="#0078D7",
        fg="white",
        font=("Arial",12,"bold"),
        command=login
    ).pack(pady=30)


