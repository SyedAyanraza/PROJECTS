from tkinter import*
from PIL import Image,ImageTk
from course import courseclass
from student import studentclass
from result import resultclass
from logout import logoutclass
from resukt import resultclass
from viewstudentresult import vsrclass
from exit import exitclass
class RMS:
  def __init__(self,root):
    self.root=root
    self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
    self.root.geometry("1350x700+0+0")
    self.root.config(bg="white")

    ##icons
    self.logo_dash=ImageTk.PhotoImage(file="images/images/logo_p.png")

    ##----title of the project--##
    title=Label(self.root,text=" STUDENT RESULT MANAGEMENT SYSTEM",padx=10,compound=LEFT,image=self.logo_dash,font=("JetBrains Mono",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
    ##menus
    M_frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
    M_frame.place(x=10,y=70,width=1340,height=80)

    #buttons
    btn_course=Button(M_frame,text="course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
    btn_student=Button(M_frame,text="students",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
    btn_result=Button(M_frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_resultt).place(x=460,y=5,width=200,height=40)
    btn_view=Button(M_frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.viewstudentresult).place(x=680,y=5,width=200,height=40)
    btn_logout=Button(M_frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
    btn_exit=Button(M_frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit).place(x=1120,y=5,width=200,height=40)
    
    #windowcontent
    self.bg_img=Image.open("images/images/bg.png")
    self.bg_img=self.bg_img.resize((920,350))##Image.ANTIALIAS) ## we can remove  antialias as well 
    self.bg_img=ImageTk.PhotoImage(self.bg_img)
    self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

    ##updatedetails
    self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white").place(x=400,y=530,width=200,height=80)
    
    self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
    self.lbl_course.place(x=400,y=530,width=200,height=80)

    self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE)
    self.lbl_student.place(x=720,y=530,width=200,height=80)


    self.lbl_result=Label(self.root,text="Total Result\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE)
    self.lbl_result.place(x=1020,y=530,width=200,height=80)



    ##footer

    footer=Label(self.root,text="SRMS-STUDENT RESULT MANAGEMENT SYSTEM\n Contact us for any issue at @ayanraza2004oct@gmail.com or Mareeb@gmail.com" ,font=("JetBrains Mono",8),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
  
  def add_course(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=courseclass(self.new_win)
  def add_student(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=studentclass(self.new_win)

  def add_resultt(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=resultclass(self.new_win)

  


  def add_result(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=resultclass(self.new_win)


  def viewstudentresult(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=vsrclass(self.new_win)
  
    
    
  def logout(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=logoutclass(self.new_win)


  def exit(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=exitclass(self.new_win)


if __name__=="__main__":
  root=Tk()
  obj=RMS(root)
  root.mainloop()