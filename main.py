
# import packages 
#import imp
from tkinter import*

from tkinter import ttk

from PIL import Image,ImageTk

from student import Student

import os  # 

from train import Train  # importing train classs

from face_recognition import Face_Recongnition # Importing face class  

from student import*

from train import*






# Class 
class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")


   # for first image
        img=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\student1")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

   # for second image
        img1=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\collage1.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

   # for third image
        img2=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\face1.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


   # for bg Image 
        img3=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\bg3.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)



     
     # title

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold "),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

     # student button

        img4=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\s.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
     
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold "),bg="white",fg="blue")
        b1_1.place(x=100,y=260,width=200,height=40)
        
        
     # Detect Face

        img5=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\face_re1.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
     
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold "),bg="white",fg="blue")
        b1_1.place(x=400,y=260,width=200,height=40)
     
     # Attendanc5

        img6=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\att_1.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
     
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=700,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold "),bg="white",fg="blue")
        b1_1.place(x=700,y=260,width=200,height=40)      

     # Help Desk

        img7=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\help_1.png")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
     
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1000,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold "),bg="white",fg="blue")
        b1_1.place(x=1000,y=260,width=200,height=40)      


     # Train data

        img8=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\train_1.png")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
     
        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=100,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold "),bg="white",fg="blue")
        b1_1.place(x=100,y=510,width=200,height=40)      


    # 2 Photos data 

        img9=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\photo_1.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
     
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Photo Data",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold "),bg="white",fg="blue")
        b1_1.place(x=400,y=510,width=200,height=40)      

    # 3 Devloper

        img10=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\devloper_1.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
   
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=700,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Devloper",cursor="hand2",font=("times new roman",15,"bold "),bg="white",fg="blue")
        b1_1.place(x=700,y=510,width=200,height=40)      

    # 9 Exit 

        img11=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\exit_1.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
     
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1000,y=310,width=200,height=200)

        b1_1=Button(bg_img,text=" Exit ",cursor="hand2",font=("times new roman",15,"bold "),bg="white",fg="blue")
        b1_1.place(x=1000,y=510,width=200,height=40)      


    def open_img(self):
       os.startfile("data")

# ===========================FUNCTION BUTTON======================================================================

    def student_details(self):
       self.new_windows=Toplevel(self.root)
       self.app=Student(self.new_windows)

# ==========================FUNCTION BUTTON FOR ==================================================================

    def train_data(self):
       self.new_windows=Toplevel(self.root)
       self.app=Train(self.new_windows)

# =========================FUNCTION BUTTON FOR FACE RECONGNIZATON========================================
   
    def face_data(self):
       self.new_windows=Toplevel(self.root)
       self.app=Face_Recongnition(self.new_windows)

# main functions 
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()
