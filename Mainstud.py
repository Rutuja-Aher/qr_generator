from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Mainstud:
 def __init__(self,root):
  self.root=root
  self.root.geometry("900x500+200+50")
  self.root.title("QR Generator | Developed by rutuja")
  self.root.resizable(False,False)

  title=Label(self.root,text="             QR Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

 #====Students DETAILS window=======
   #=====variable====
  self.var_stud_code=StringVar()
  self.var_name=StringVar()
  self.var_department=StringVar()
  self.var_percentage=StringVar()
  
  stud_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
  stud_Frame.place(x=50,y=100,width=500,height=380)

  stud_title=Label(stud_Frame,text="Students Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

  lbl_stud_code=Label(stud_Frame,text="Student ID",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
  lbl_name=Label(stud_Frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
  lbl_department=Label(stud_Frame,text="Department",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
  lbl_percentage=Label(stud_Frame,text="percentage",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)

  txt_stud_code=Entry(stud_Frame,font=("times new roman",15),textvariable=self.var_stud_code,bg='lightyellow').place(x=200,y=60)
  txt_name=Entry(stud_Frame,font=("times new roman",15),textvariable=self.var_name,bg='lightyellow').place(x=200,y=100)
  txt_department=Entry(stud_Frame,font=("times new roman",15),textvariable=self.var_department,bg='lightyellow').place(x=200,y=140)
  txt_percentage=Entry(stud_Frame,font=("times new roman",15),textvariable=self.var_percentage,bg='lightyellow').place(x=200,y=180)

  btn_generate=Button(stud_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
  btn_clear=Button(stud_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=282,y=250,width=120,height=30)
 
  self.msg=''

  self.lbl_msg=Label(stud_Frame,text=self.msg,font=("times new roman",20),bg='white',fg='purple')
  self.lbl_msg.place(x=0,y=320,relwidth=1)
  
#====Employee QR code window=======

  qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
  qr_Frame.place(x=600,y=100,width=250,height=380)

  stud_title=Label(qr_Frame,text="Student QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

  
  self.qr_code=Label(qr_Frame,text='No QR\nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
  self.qr_code.place(x=35,y=100,width=180,height=180)

 def clear(self):
     self.var_stud_code.set('')
     self.var_name.set('')
     self.var_department.set('')
     self.var_percentage.set('')
     self.msg=''
     self.lbl_msg.config(text=self.msg)
     self.qr_code.config(image='')
 def generate(self):
    if self.var_percentage.get()==''or self.var_stud_code.get()=='' or self.var_name.get()=='' or self.var_department.get()=='':
        self.msg='All Fields Are Required!'
        self.lbl_msg.config(text=self.msg,fg='red')
    else:
        qr_data=(f"Student ID:{self.var_stud_code.get()}\nStudent Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\npercentage:{self.var_percentage.get()}")
        qr_code=qrcode.make(qr_data)
        qr_code=resizeimage.resize_cover(qr_code,[180,180])
        #print(qr_code)
        #qr_code.save(file="Employee_QR/Emp_"+str(self.var_emp_code.get())'.png')
        #=====QR code image update=====
        self.im=ImageTk.PhotoImage(qr_code)
        self.qr_code.config(image=self.im)
        #=====updating notification=====
        self.msg='QR Generated Succesfully!! '
        self.lbl_msg.config(text=self.msg,fg='green')
            

root=Tk()
obj =Mainstud(root)
root.mainloop()

