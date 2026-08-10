import tkinter as tk
from tkinter import messagebox
from database import connect_db



def admin_window(parent):

    window = tk.Toplevel(parent)

    window.title("Admin Panel")
    window.geometry("450x550")
    window.configure(bg="#d9f2ff")
    window.resizable(False, False)



    # ================= ADD QUESTION =================

    def add_question():

        add_window = tk.Toplevel(window)
        add_window.title("Add Question")
        add_window.geometry("500x500")


        entries=[]


        fields=[
            "Question",
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4",
            "Correct Answer"
        ]


        for field in fields:

            tk.Label(
                add_window,
                text=field
            ).pack()

            entry=tk.Entry(
                add_window,
                width=50
            )

            entry.pack(pady=5)

            entries.append(entry)



        def save_question():

            data=[e.get().strip() for e in entries]


            if "" in data:

                messagebox.showwarning(
                    "Warning",
                    "Fill all fields"
                )

                return



            db=connect_db()

            cursor=db.cursor()


            cursor.execute(
                """
                INSERT INTO questions
                (question,option1,option2,option3,option4,answer)
                VALUES(%s,%s,%s,%s,%s,%s)
                """,
                data
            )


            db.commit()
            db.close()


            messagebox.showinfo(
                "Success",
                "Question Added"
            )


            add_window.destroy()



        tk.Button(
            add_window,
            text="Save Question",
            bg="green",
            fg="white",
            command=save_question
        ).pack(pady=20)



    # ================= VIEW QUESTION =================


    def view_questions():

        win=tk.Toplevel(window)

        win.title("Questions")

        win.geometry("700x400")


        text=tk.Text(win)

        text.pack(
            fill="both",
            expand=True
        )


        db=connect_db()

        cursor=db.cursor()


        cursor.execute(
            "SELECT id,question,answer FROM questions"
        )


        rows=cursor.fetchall()


        db.close()



        for row in rows:

            text.insert(
                tk.END,
                f"{row[0]}  {row[1]}\nAnswer: {row[2]}\n\n"
            )



    # ================= UPDATE QUESTION =================


    def update_question():

        win=tk.Toplevel(window)

        win.title("Update Question")

        win.geometry("400x250")


        tk.Label(
            win,
            text="Question ID"
        ).pack()


        id_entry=tk.Entry(win)

        id_entry.pack()



        tk.Label(
            win,
            text="New Question"
        ).pack()


        q_entry=tk.Entry(
            win,
            width=40
        )

        q_entry.pack()



        def update():

            qid=id_entry.get()

            question=q_entry.get()



            db=connect_db()

            cursor=db.cursor()


            cursor.execute(
                """
                UPDATE questions
                SET question=%s
                WHERE id=%s
                """,
                (question,qid)
            )


            db.commit()

            db.close()



            messagebox.showinfo(
                "Success",
                "Question Updated"
            )


            win.destroy()



        tk.Button(
            win,
            text="Update",
            bg="orange",
            command=update
        ).pack(pady=20)




    # ================= DELETE QUESTION =================


    def delete_question():

        win=tk.Toplevel(window)

        win.title("Delete Question")

        win.geometry("350x200")


        tk.Label(
            win,
            text="Question ID"
        ).pack(pady=10)


        id_entry=tk.Entry(win)

        id_entry.pack()



        def delete():

            qid=id_entry.get()


            db=connect_db()

            cursor=db.cursor()


            cursor.execute(
                "DELETE FROM questions WHERE id=%s",
                (qid,)
            )


            db.commit()

            db.close()



            messagebox.showinfo(
                "Success",
                "Question Deleted"
            )


            win.destroy()



        tk.Button(
            win,
            text="Delete",
            bg="red",
            fg="white",
            command=delete
        ).pack(pady=20)




    # ================= VIEW RESULT =================


    def view_results():

        win=tk.Toplevel(window)

        win.title("Quiz Results")

        win.geometry("500x400")


        text=tk.Text(win)

        text.pack(
            fill="both",
            expand=True
        )


        db=connect_db()

        cursor=db.cursor()


        cursor.execute(
            """
            SELECT username,score
            FROM results
            ORDER BY score DESC
            """
        )


        rows=cursor.fetchall()


        db.close()



        text.insert(
            tk.END,
            "Username\tScore\n\n"
        )


        for row in rows:

            text.insert(
                tk.END,
                f"{row[0]}\t{row[1]}\n"
            )


        text.config(
            state="disabled"
        )




    # ================= LEADERBOARD =================


    def leaderboard():

        win=tk.Toplevel(window)

        win.title("Leaderboard")

        win.geometry("500x400")


        text=tk.Text(win)

        text.pack(
            fill="both",
            expand=True
        )


        db=connect_db()

        cursor=db.cursor()


        cursor.execute(
            """
            SELECT username,MAX(score)
            FROM results
            GROUP BY username
            ORDER BY MAX(score) DESC
            LIMIT 10
            """
        )


        rows=cursor.fetchall()


        db.close()


        text.insert(
            tk.END,
            "🏆 TOP 10 LEADERBOARD\n\n"
        )


        rank=1


        for row in rows:

            text.insert(
                tk.END,
                f"{rank}. {row[0]}  {row[1]}\n"
            )

            rank+=1



    # ================= ADMIN UI =================


    tk.Label(
        window,
        text="ONLINE QUIZ SYSTEM\nADMIN PANEL",
        font=("Arial",18,"bold"),
        bg="#d9f2ff",
        fg="darkblue"
    ).pack(pady=30)



    buttons=[

        ("Add Question",add_question,"green"),

        ("View Questions",view_questions,"blue"),

        ("Update Question",update_question,"orange"),

        ("Delete Question",delete_question,"red"),

        ("View Results",view_results,"purple"),

        ("Leaderboard",leaderboard,"brown")

    ]



    for text,cmd,color in buttons:

        tk.Button(
            window,
            text=text,
            width=25,
            height=2,
            bg=color,
            fg="white",
            command=cmd
        ).pack(pady=5)



    tk.Button(
        window,
        text="Exit",
        width=25,
        height=2,
        bg="black",
        fg="white",
        command=window.destroy
    ).pack(pady=10)