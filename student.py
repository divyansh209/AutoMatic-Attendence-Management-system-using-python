from importlib.resources import contents
from msilib.schema import Error
from tkinter import*

from tkinter import ttk
from tkinter import font
from turtle import home, right, width

from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
from cv2 import FONT_HERSHEY_COMPLEX
from matplotlib.animation import MovieWriterRegistry   # for pop up masages
import mysql .connector
from scipy.misc import face          # for connection to our data base

# Class 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")

    
    #  ==================veriables====

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_Enrollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_adress=StringVar()
        self.var_teacher=StringVar()
         





   # for first image
        img=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\student11.jpg")
        img=img.resize((490,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

   # for second image
        img1=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\student22.jpg")
        img1=img1.resize((490,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=490,y=0,width=500,height=130)

   # for third image
        img2=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\student33.jpg")
        img2=img2.resize((490,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=980,y=0,width=500,height=130)

 # for bg Image 

        img3=Image.open(r"C:\Users\divya\OneDrive\Desktop\Face attendence system\project IMG\bg3.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)



     
     # title

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold "),bg="gray",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=50,width=1335,height=580)

     #    left label fram

        left_frame=LabelFrame(main_frame,bd=2,bg="silver",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold",))
        left_frame.place(x=10,y=10,width=650,height=580)


     # + + current course Frame

        current_course_frame=LabelFrame(left_frame,bd=3,bg="gray",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold",))
        current_course_frame.place(x=5,y=10,width=650,height=140)

     # depertment box


        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="silver")
        dep_label.grid(row=0,column=0)

     # depertment combo box
     #    
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")

        dep_combo["values"]=("Select Department","Computer","civil","machenical","EC")

        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)


        
      # Course box


        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="silver")
        course_label.grid(row=0,column=2)

      # Course combo box
         
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")

        course_combo["values"]=("Select Course","Btech","Mtech","MCA","ITI")

        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=20,pady=10,sticky=W)

      
       # Year box


        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="silver")
        year_label.grid(row=3,column=0)

      # Course combo box
         
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")

        year_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23")

        year_combo.current(0)
        year_combo.grid(row=3,column=1,padx=10,pady=15,sticky=W)


 # semester box


        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="silver")
        semester_label.grid(row=3,column=2)

      # semester combo box
         
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")

        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")

        semester_combo.current(0)
        semester_combo.grid(row=3,column=3,padx=20,pady=10,sticky=W)




     # + Class student  information 

        class_student_frame=LabelFrame(left_frame,bd=3,bg="gray",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold",))
        class_student_frame.place(x=5,y=140,width=650,height=335)


     #  Student id 

        student_ID_label=Label(class_student_frame,text="Student_ID",font=("times new roman",12,"bold"),bg="silver")
        student_ID_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

     # entry box
       
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=17,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)



     #  Student name 

        student_name_label=Label(class_student_frame,text="Student_Name",font=("times new roman",12,"bold"),bg="silver")
        student_name_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

     # entry box
       
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=17,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)


     #  Division id 

        student_division_label=Label(class_student_frame,text="Student_Division",font=("times new roman",12,"bold"),bg="silver")
        student_division_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

     # entry box
       
        studentdivision_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=17,font=("times new roman",12,"bold"))
        studentdivision_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)



   #  Enrollment no  

        student_enrollment_no_label=Label(class_student_frame,text="Enrollment_No",font=("times new roman",12,"bold"),bg="silver")
        student_enrollment_no_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

     # entry box
       
        studentenrollment_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_Enrollno,width=17,font=("times new roman",12,"bold"))
        studentenrollment_no_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)



    #  Student Gender 

        student_gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="silver")
        student_gender_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)

     # entry box
       
 #       studentgender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=17,font=("times new roman",12,"bold"))
 #       studentgender_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)
#

   #  Gender combo box 

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=15,state="readonly")

        gender_combo["values"]=("Male","Female")

        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=10,pady=10,sticky=W)



     #  Student Dob 

        student_DOB_label=Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"),bg="silver")
        student_DOB_label.grid(row=3,column=2,padx=2,pady=10,sticky=W)

     # entry box
       
        studentDOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=17,font=("times new roman",12,"bold"))
        studentDOB_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)
        

    #  Student Email

        student_email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="silver")
        student_email_label.grid(row=4,column=0,padx=2,pady=10,sticky=W)

     # entry box
       
        studentemail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=17,font=("times new roman",12,"bold"))
        studentemail_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        
    
    #  Student phone 

        student_phone_label=Label(class_student_frame,text="Phone NO",font=("times new roman",12,"bold"),bg="silver")
        student_phone_label.grid(row=4,column=2,padx=2,pady=10,sticky=W)

     # entry box
       
        studentphone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=17,font=("times new roman",12,"bold"))
        studentphone_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)

     
    #  Student adress

        student_adress_label=Label(class_student_frame,text="Adress",font=("times new roman",12,"bold"),bg="silver")
        student_adress_label.grid(row=5,column=0,padx=2,pady=10,sticky=W)

     # entry box
       
        studentadress_entry=ttk.Entry(class_student_frame,textvariable=self.var_adress,width=17,font=("times new roman",12,"bold"))
        studentadress_entry.grid(row=5,column=1,padx=10,pady=10,sticky=W)
   

    #  Student Teacher Name

        student_Teacher_label=Label(class_student_frame,text="Teacher",font=("times new roman",12,"bold"),bg="silver")
        student_Teacher_label.grid(row=5,column=2,padx=2,pady=10,sticky=W)

     # entry box
       
        studentTeacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=17,font=("times new roman",12,"bold"))
        studentTeacher_entry.grid(row=5,column=3,padx=10,pady=10,sticky=W)




   #  +  redio buttons
        
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
         
        
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn1.grid(row=6,column=1)


   #  Button frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RAISED,bg="gray")
        btn_frame.place(x=0,y=250,width=650,height=35)

        # save butto
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="silver",fg="black")
        save_btn.grid(row=1,column=0)

        # update button

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="silver",fg="black")
        update_btn.grid(row=1,column=1)

        # delete button
  
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="silver",fg="black")
        delete_btn.grid(row=1,column=2)

        # reset button
  
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="silver",fg="black")
        reset_btn.grid(row=1,column=3)


      # button frame 02

        btn2_frame=Frame(class_student_frame,bd=2,relief=RAISED,bg="gray")
        btn2_frame.place(x=0,y=280,width=650,height=30)

      # Take photo semple  button
        
        Photo_semple_btn=Button(btn2_frame,text="Take Photo Semple",command=self.generate_dataset,width=35,font=("times new roman",12,"bold"),bg="silver",fg="black")
        Photo_semple_btn.grid(row=1,column=0)


        Update_semple_btn=Button(btn2_frame,text="Update Photo Semple",width=35,font=("times new roman",12,"bold"),bg="silver",fg="black")
        Update_semple_btn.grid(row=1,column=1)





     #  ++++  right label fram @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        Right_frame=LabelFrame(main_frame,bd=2,bg="silver",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold",))
        Right_frame.place(x=670,y=10,width=650,height=580)



#  ===================   Search System   ============================

        Search_frame=LabelFrame(Right_frame,bd=3,bg="gray",relief=RIDGE,text="Search Student Information",font=("times new roman",12,"bold",))
        Search_frame.place(x=5,y=10,width=650,height=80)

        
      # Search by label  
      
        student_Teacher_label=Label(Search_frame,text="Search By",font=("times new roman",12,"bold"),bg="silver")
        student_Teacher_label.grid(row=1,column=2,padx=2,pady=12,sticky=W)


      # Search by  combo box
         
        Searchby_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")

        Searchby_combo["values"]=("Select by","Student_ID","Student_Name","Enrollment_No","DOB")

        Searchby_combo.current(0)
        Searchby_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)

 #       Search entry box
       
        Search_entry=ttk.Entry(Search_frame,width=17,font=("times new roman",12,"bold"))
        Search_entry.grid(row=1,column=4,padx=1,pady=10,sticky=W)
   

#        Search button

        Search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="silver",fg="black")
        Search_btn.grid(row=1,column=5,padx=5)


#        Show button
        Show_btn=Button(Search_frame,text="Show",width=12,font=("times new roman",12,"bold"),bg="silver",fg="black")
        Show_btn.grid(row=1,column=6,padx=5)



        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=90,width=650,height=370)


#        Scroll bar
         
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","Enrollno","gender","dob","email","phone","adress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

#         hidder
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_ID")
        self.student_table.heading("name",text="Student_Name")
        self.student_table.heading("div",text="Student_Division")
        self.student_table.heading("Enrollno",text="Enrollment_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("adress",text="Adress")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo_semple")
        
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("Enrollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("adress",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
         



        self.student_table.pack(fill=BOTH,expand=1)
        
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
   #=================function


    def add_data(self):
       if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
        
       else:
         try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Divy@123",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                              self.var_dep.get(),
                              self.var_course.get(),
                              self.var_year.get(),
                              self.var_semester.get(),
                              self.var_std_id.get(),
                              self.var_std_name.get(),
                              self.var_div.get(),
                              self.var_Enrollno.get(),
                              self.var_gender.get(),
                              self.var_dob.get(),
                              self.var_email.get(),
                              self.var_phone.get(),
                              self.var_adress.get(),
                              self.var_teacher.get(),
                              self.var_radio1.get()                       
   
                  ))
       
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root) 

         except Exception as e:  
            messagebox.showerror("error",f"Due to :{str(e)}",parent=self.root)   
       

   # =========fetch data ==========

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Divy@123",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
           self.student_table.delete(*self.student_table.get_children())
           
           for i in data:
              self.student_table.insert("",END,values=i)


           conn.commit()
        conn.close()


#  =============get coursor functions for update button===

    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dep.set(data[0]),
       self.var_course.set(data[1]),
       self.var_year.set(data[2]),
       self.var_semester.set(data[3]),
       self.var_std_id.set(data[4]),
       self.var_std_name.set(data[5]),
       self.var_div.set(data[6]),
       self.var_email.set(data[7]),
       self.var_gender.set(data[8]),
       self.var_dob.set(data[9]),
       self.var_email.set(data[10]),
       self.var_phone.set(data[11]),
       self.var_adress.set(data[12]),
       self.var_teacher.set(data[13]),
       self.var_radio1.set(data[14]),


  # ======Update function

    def update_data(self):
       if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)

         
       else:
          try:
             Upadate=messagebox.askyesno("update","Do you want ot update this tudent details",parent=self.root)
             if Upadate>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="Divy@123",database="face_recognition")
               my_cursor=conn.cursor()
               my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_name=%s,Student_division=%s,Enrollment_no=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSemple=%s where Student_id=%s",(
               
               
                                                                                                                                                                                           self.var_dep.get(),
                                                                                                                                                                                           self.var_course.get(),
                                                                                                                                                                                           self.var_year.get(),
                                                                                                                                                                                           self.var_semester.get(),
                                                                                                         
                                                                                                                                                                                           self.var_std_id.get(),
                                                                                                                                                                                           self.var_div.get(),
                                                                                                                                                                                           self.var_Enrollno.get(),
                                                                                                                                                                                           self.var_gender.get(),
                                                                                                                                                                                           self.var_dob.get(),
                                                                                                                                                                                           self.var_email.get(),
                                                                                                                                                                                           self.var_phone.get(),
                                                                                                                                                                                           self.var_adress.get(),
                                                                                                                                                                                           self.var_teacher.get(),
                                                                                                                                                                                           self.var_radio1.get(),
                                                                                                                                                                                           self.var_std_id.get(),
                                                                                                                                                                                                                                                                                                                                       
               ) )

             else:
                if not Upadate:
                   return
             messagebox.showinfo("Success","student details successfulyly updated")   
             conn.commit()
             self.fetch_data()
             conn.close()
          except Exception as ea:
             messagebox.showerror("Error",f"Due to :{str(ea)}",parent=self.root)

    # ===============@ for delete and reset button============@

    def delete_data(self):
       if self.var_std_id.get()=="":
          messagebox.showerror("Error","Student id must be required",parent=self.root)

       else:
          try:
             delete=messagebox.askyesno("Student Delte Page","Do you want delete this studernt details",parent=self.root)
             if delete>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="Divy@123",database="face_recognition")
               my_cursor=conn.cursor()
               sql="delete from student where Student_id=%s"
               val=(self.var_std_id.get(),)
               my_cursor.execute(sql,val)
             
             else:
                if not delete:
                   return
               
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Delete"," Successfully deleted Student detail ",parent=self.root)

          except Exception as ea:
             messagebox.showerror("Error",f"Due to :{str(ea)}",parent=self.root)




#################### Reset Button functions++++

    def reset_data(self):
       self.var_dep.set("Select Department")
       self.var_course.set("Select Course")
       self.var_year.set("Select Year")
       self.var_semester.set("Select Semester")
       self.var_std_id.set("")
       self.var_std_name.set("")
       self.var_div.set("Select Division")
       self.var_Enrollno.set("Select Enrollment")
       self.var_gender.set("")
       self.var_dob.set("")
       self.var_email.set("")
       self.var_phone.set("")
       self.var_adress.set("")
       self.var_teacher.set("")
       self.var_radio1.set("")



# =======GENERATE DATA SET OR TAKE PHOO SAMPLEES =====


    def generate_dataset(self): 
       if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)

       else:
          try:
             conn=mysql.connector.connect(host="localhost",username="root",password="Divy@123",database="face_recognition")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from student")
             myresult=my_cursor.fetchall()
             id=0
             for x in myresult:
                id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_name=%s,Student_division=%s,Enrollment_no=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSemple=%s where Student_id=%s",(
                  
                  
                                                                                                                                                                                             self.var_dep.get(),
                                                                                                                                                                                             self.var_course.get(),
                                                                                                                                                                                             self.var_year.get(),
                                                                                                                                                                                             self.var_semester.get(),
                                                                                                            
                                                                                                                                                                                             self.var_std_id.get(),
                                                                                                                                                                                             self.var_div.get(),
                                                                                                                                                                                             self.var_Enrollno.get(),
                                                                                                                                                                                             self.var_gender.get(),
                                                                                                                                                                                             self.var_dob.get(),
                                                                                                                                                                                             self.var_email.get(),
                                                                                                                                                                                             self.var_phone.get(),
                                                                                                                                                                                             self.var_adress.get(),
                                                                                                                                                                                             self.var_teacher.get(),
                                                                                                                                                                                             self.var_radio1.get(),
                                                                                                                                                                                             self.var_std_id.get()==id+1
                                                                                                                                                                                                                                                                                                                                          
                  ) )
               
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
   

      # ============= Load predifiend data on face frontals form opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
               
                def face_croped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                   faces=face_classifier.detectMultiScale(gray,1.3,5)

                  # sciling factor 1.3
                  # minimum neighbor =5

                   for (x,y,w,h) in faces:
                      face_croped=img[y:y+h,x:x+w]
                      return face_croped

                cap=cv2.VideoCapture(0)
                img_id=0

                while True:
                   ret,my_frame=cap.read()
                   if face_croped(my_frame) is not None:
                      img_id+=1
                      face=cv2.resize(face_croped(my_frame),(450,450))
                      face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)  
                      file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"  
                      cv2.imwrite(file_name_path,face)
                      cv2.putText(face,str(img_id),(50,50),FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                      cv2.imshow("Cropped Face",face)

                   if cv2.waitKey(1)==13 or int(img_id)==100:
                      break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating daa sets completed ")

          except Exception as e:  
             messagebox.showerror("error",f"Due to :{str(e)}",parent=self.root)   
   # main functions 
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()