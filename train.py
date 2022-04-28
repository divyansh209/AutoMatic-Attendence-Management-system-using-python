#from importlib.resources import contents
#from msilib.schema import Error
from importlib.resources import path
from tkinter import*

from tkinter import ttk
from tkinter import font
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

# Class 
class Train:
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

        title_lbl=Label(bg_img,text="TRAIN DATA SET ",font=("times new roman",35,"bold "),bg="gray",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


# train button for train our data set

        
        b1_1=Button(bg_img,text="Train Data set",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold "),bg="gray",fg="black")
        b1_1.place(x=900,y=550,width=300,height=60)
        

# for train modul using of LBPH algorithim using cv2



    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join (data_dir,file) for file in os.listdir(data_dir) ]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L") # Gray Scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        # ++++++++++++++++++ Train the Classifier And save

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows() 

        messagebox.showinfo("Result","tran data is completed")
            































if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()