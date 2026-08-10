import tkinter as tk

from login import login_window
from register import register_window
from admin import admin_window

print("MAIN START")
import tkinter as tk
print("TK IMPORT OK")

window = tk.Tk()

window.title("Online Quiz System")
window.geometry("500x550")
window.configure(bg="#EAF4FF")
window.resizable(False,False)



def open_login():

    login_window(window)



def open_register():

    register_window(window)



def open_admin():

    admin_window(window)



# Title

tk.Label(
    window,
    text="📝 ONLINE QUIZ SYSTEM",
    font=("Arial",22,"bold"),
    bg="#EAF4FF",
    fg="#003366"
).pack(pady=40)



# Login Button

tk.Button(
    window,
    text="👤 User Login",
    width=25,
    height=2,
    bg="#0078D7",
    fg="white",
    font=("Arial",12,"bold"),
    command=open_login
).pack(pady=15)



# Register Button

tk.Button(
    window,
    text="📝 Register",
    width=25,
    height=2,
    bg="#28A745",
    fg="white",
    font=("Arial",12,"bold"),
    command=open_register
).pack(pady=15)



# Admin Button

tk.Button(
    window,
    text="🔐 Admin Panel",
    width=25,
    height=2,
    bg="#FF9800",
    fg="white",
    font=("Arial",12,"bold"),
    command=open_admin
).pack(pady=15)



# Exit

tk.Button(
    window,
    text="🚪 Exit",
    width=25,
    height=2,
    bg="red",
    fg="white",
    command=window.destroy
).pack(pady=15)



window.mainloop()