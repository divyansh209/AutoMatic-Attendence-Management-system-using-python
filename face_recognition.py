#from importlib.resources import path
#import re
from tkinter import*

from tkinter import ttk
#from tkinter import font
#from turtle import home, right, width

from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
#from cv2 import FONT_HERSHEY_COMPLEX
#from matplotlib.animation import MovieWriterRegistry   # for pop up masages
import mysql .connector
#from scipy.misc import face          # for connection to our data base

import os

import numpy as np
from time import strftime
from datetime import datetime
#from scipy.misc import face



# Class 
class Face_Recongnition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")



   # for bg Image 
        img3=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\bg3.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=710)

# title for train data

        title_lbl=Label(bg_img,text="FACE RECOGNITION ",font=("times new roman",35,"bold "),bg="gray",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


# train button for face recognition  our data set

        
        b1_1=Button(bg_img,text="FACE RECOGNITION",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold "),bg="gray",fg="black")
        b1_1.place(x=900,y=550,width=300,height=60)
        
################### Attendence =================
    def mark_attendance(self,i,e,n,d):
        with open("divyansh.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (e not in name_list) and (n not in name_list) and  (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{e},{n},{d},{dtString},{d1},Present")

 






#   ================FACE RECOGNITIONS ===========


    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Divy@123",database="face_recognition")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Student_name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Enrollment_no from student where Student_id="+str(id))
                e=my_cursor.fetchone()
                e="+".join(e)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                               

                if confidence>77:
                    cv2.putText(img,f"Student_id :{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Enrollment :{e}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Student_name :{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep :{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,e,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                coord=[x,y,w,h]
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recogniton",img)

            if cv2.waitKey(1):
               break
            video_cap.release()
            cv2.destroyAllWindows()



# main functions 
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recongnition(root)
    root.mainloop()
