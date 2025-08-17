from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from tkinter import Tk
import sqlite3

class resultclass:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        ## Title
        title = Label(self.root, text=" Add student results Details", font=("JetBrains Mono", 18, "bold"), bg="orange", fg="white")
        title.place(x=10, y=15, width=1180, height=50)

        ##### Variables
        self.var_roll = StringVar(self.root)
        self.var_name = StringVar(self.root)
        self.var_course = StringVar(self.root)
        self.var_marks_ob = StringVar(self.root)
        self.var_full_marks = StringVar(self.root)
        self.roll_list = []
        self.fetch_roll()

        ####### Widgets
        lbl_select = Label(self.root, text="Select student", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=(self.roll_list), font=("goudy old style", 15), state='readonly', justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=500, y=100, width=100, height=28)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20), bg='lightyellow', state='readonly')
        txt_name.place(x=280, y=160, width=320)

        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20), bg='lightyellow', state='readonly')
        txt_course.place(x=280, y=220, width=320)

        txt_marks_ob = Entry(self.root, textvariable=self.var_marks_ob, font=("goudy old style", 20), bg='lightyellow')
        txt_marks_ob.place(x=280, y=280, width=320)

        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20), bg='lightyellow')
        txt_full_marks.place(x=280, y=340, width=320)

        ### Buttons
        btn_add = Button(self.root, text="Submit", font=("times new roman", 15), bg="lightgreen", activebackground="lightgreen", cursor="hand2", command=self.add)
        btn_add.place(x=300, y=420, width=120, height=35)

        btn_clear = Button(self.root, text="Clear", font=("times new roman", 15), bg="white", activebackground="lightgray", cursor="hand2")
        btn_clear.place(x=430, y=420, width=120, height=35)

        ### Image
        self.bg_img = Image.open("images/images/result.jpg")
        self.bg_img = self.bg_img.resize((500, 300))  # Image.ANTIALIAS can be omitted
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=630, y=100)

    ### Fetch roll numbers
    def fetch_roll(self):
        con = sqlite3.connect(database="ams.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    ### Search student by roll
    def search(self):
        con = sqlite3.connect(database="ams.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, course FROM student WHERE roll = ?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is not None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    ### Add result
    def add(self):
        con = sqlite3.connect(database="ams.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first search student record", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=? AND course=?", (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Result already available", parent=self.root)
                else:
                    per = (int(self.var_marks_ob.get()) * 100) / int(self.var_full_marks.get())
                    cur.execute("INSERT INTO result (roll, name, course, marks_ob, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks_ob.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)
                    
                    # ✅ Show result window after submit
                    self.show_result_window(
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks_ob.get(),
                        self.var_full_marks.get()
                    )
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    ### ✅ Show Result Window (NEW FUNCTION)
    def show_result_window(self, name, course, marks_ob, full_marks):
        try:
            percentage = round((int(marks_ob) / int(full_marks)) * 100, 2)

            view_win = Toplevel(self.root)
            view_win.title("View Submitted Result")
            view_win.geometry("400x300+200+200")
            view_win.config(bg="white")

            Label(view_win, text="Result Submitted", font=("Arial", 16, "bold"), bg="white", fg="green").pack(pady=10)
            Label(view_win, text=f"Name: {name}", font=("Arial", 12), bg="white").pack(anchor="w", padx=20)
            Label(view_win, text=f"Course: {course}", font=("Arial", 12), bg="white").pack(anchor="w", padx=20)
            Label(view_win, text=f"Marks Obtained: {marks_ob}", font=("Arial", 12), bg="white").pack(anchor="w", padx=20)
            Label(view_win, text=f"Full Marks: {full_marks}", font=("Arial", 12), bg="white").pack(anchor="w", padx=20)
            Label(view_win, text=f"Percentage: {percentage}%", font=("Arial", 12), bg="white").pack(anchor="w", padx=20)

        except Exception as ex:
            messagebox.showerror("Error", f"Error in result view: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = resultclass(root)
    root.mainloop()
