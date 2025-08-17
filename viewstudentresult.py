from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk , messagebox
from tkinter  import Tk
import sqlite3
class vsrclass:
  def __init__(self,root):
    self.root=root
    self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
    self.root.geometry("1200x480+80+170")
    self.root.config(bg="white")
    self.root.focus_force()
    ##title
    title=Label(self.root,text=" Result",font=("JetBrains Mono",18,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)
  

    self.bg_img=Image.open("images/images/trs.jpeg")
    self.bg_img=self.bg_img.resize((1000,500))##Image.ANTIALIAS) ## we can remove  antialias as well 
    self.bg_img=ImageTk.PhotoImage(self.bg_img)
    self.lbl_bg=Label(self.root,image=self.bg_img).place(x=100,y=100)

    


if __name__=="__main__":
  root=Tk()
  obj=vsrclass(root)
  root.mainloop()