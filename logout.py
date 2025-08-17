from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk , messagebox
from tkinter  import Tk
import sqlite3
class logoutclass:
  def __init__(self,root):
    self.root=root
    self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
    self.root.geometry("1200x480+80+170")
    self.root.config(bg="white")
    self.root.focus_force()
    ##title
    title=Label(self.root,text="Thank You for using the portal !",font=("JetBrains Mono",18,"bold"),bg="orange",fg="white").place(x=10,y=15,width=1180,height=50)

def logout(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=logoutclass(self.new_win)
    











    

if __name__=="__main__":
  root=Tk()
  obj=logoutclass(root)
  root.mainloop()