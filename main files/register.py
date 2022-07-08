from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        ########## variables#########

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        ######## bg image #####


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\hall1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        ############ left image #####################

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\1.jpg")
        lbl_bg1=Label(self.root,image=self.bg1)
        lbl_bg1.place(x=70,y=100,width=470,height=460)
        

        ########### main frame #############

        frame=Frame(self.root,bg="gray80")
        frame.place(x=540,y=100,width=650,height=460)
       
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="hotpink4",bg="grey80")
        register_lbl.place(x=20,y=20)

        #### label and entry #####

        #### row 1 ####

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="hotpink4",bg="grey80")
        fname.place(x=50,y=80)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname.place(x=50,y=110,width=230)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="hotpink4",bg="grey80")
        lname.place(x=370,y=80)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=110,width=230)

        ##### row 2 #####

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="grey80",fg="hotpink4")
        contact.place(x=50,y=150)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=180,width=230)

        email=Label(frame,text="Email ID",font=("times new roman",15,"bold"),bg="grey80",fg="hotpink4")
        email.place(x=370,y=150)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=180,width=230)

        ##### row 3 #####

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="grey80",fg="hotpink4")
        security_Q.place(x=50,y=220)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your birth place","Your Best Fiend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=250,width=230)
        self.combo_security_Q.current(0)

        security=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="grey80",fg="hotpink4")
        security.place(x=370,y=220)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=250,width=230)



              #####   row 4 ######

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="grey80",fg="hotpink4")
        pswd.place(x=50,y=290)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=320,width=230)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="grey80",fg="hotpink4")
        confirm_pswd.place(x=370,y=290)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=320,width=230)


         ### check button###
        
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the terms & conditions",font=("times new roman",12,"bold"),bg="grey80",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=350)


        ######## buttons #######

        img=Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\btn2.png")
        img=img.resize((130,40))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="grey80",fg="hotpink4")
        b1.place(x=80,y=385,width=200)


        img1=Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\login.jpg")
        img1=img1.resize((130,40))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="grey80",fg="hotpink4")
        b1.place(x=350,y=385,width=200)

       

 ######## function declaration ###############

    def clear(self):
        self.txt_lname.delete(0,END)
        self.txt_fname.delete(0,END)
        self.txt_email.delete(0, END)
        self.txt_security.delete(0, END)
        # self.txt_securityA.delete(0, END)
        self.txt_pswd.delete(0, END)
        self.txt_confirm_pswd.delete(0, END)
        self.txt_contact.delete(0, END)
        self.combo_security_Q.current(0)

    def register_data(self):
        if self.var_fname.get=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password doesnt match",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                  
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)
            self.clear()




if __name__== "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()