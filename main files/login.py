from email import message
from cProfile import label
from email.mime import image
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from turtle import textinput
from PIL import Image, ImageTk    # pip install pillow
from villa import TheMoonVilla
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

def main():
    win = Tk()
    app = Login_Window(win)
    win .mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\z14.jpg")
        lbl_bg=Label(self.root , image=self.bg)
        lbl_bg.place(x=0,y=0, relwidth=1, relheight=1)

        frame=Frame(self.root,bg="darkslategray")
        frame.place(x=500,y=150,width=360,height=420)

        img1=Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\l1.jpg")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="darkslategray",borderwidth=0)
        lblimg1.place(x=630,y=150,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",25,"bold","italic"),fg="darkslategray3",bg="darkslategray")
        get_str.place(x=100,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="darkslategray")
        username.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="darkslategray")
        password.place(x=40,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
       
       #login button

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=SUNKEN,fg="gray44",bg="gray19",activeforeground="gray44",activebackground="honeydew4")
        loginbtn.place(x=110,y=300,width=120,height=35)


      # register button

        registerbtn=Button(frame,text=" New User Register",command=self.register_window,font=("times new roman",13,"bold","underline"),borderwidth=0,fg="white",bg="darkslategray",
        activeforeground="white",activebackground="darkslategray")
        registerbtn.place(x=5,y=350,width=180)

    #forgotpassword button

        registerbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",13,"bold","underline"),borderwidth=0,fg="white",bg="darkslategray",
                           activeforeground="white",activebackground="darkslategray")
        registerbtn.place(x=170,y=350,width=180)
       

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields  are required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
             messagebox.showinfo("Success","Welcome to our Villa")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and  password=%s",(
                                                                                         self.txtuser.get(),
                                                                                         self.txtpass.get()
                                                                                       ))
            
            row=my_cursor.fetchone()
            if row==None:
                 messagebox.showerror("Error","Invalid Username & Password")
            else:
                 open_main=messagebox.askyesno("YesNo","Access only admin")
                 if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=TheMoonVilla(self.new_window)
                 else:
                     if not open_main:
                        return
            conn.commit()
            conn.close()


     ##################### reset password #####################



    def reset_pass(self):
       if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
       elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
       elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
       else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset please login with new password",parent=self.root2)
                self.root2.destroy()




     ######### forgot password window ################
                        
    def forgot_password_window(self):
       if self.txtuser.get()=="":
           messagebox.showerror("Error","Please enter the email address to reset password")
       else:   
           conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.txtuser.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           # print(row)
         
           if row==None:
               messagebox.showerror("My Error","Please Enter the Valid Username")
           else:
               conn.close()
               self.root2=Toplevel()
               self.root2.title("Forgot Password")
               self.root2.geometry("400x430+500+150")

               fimg = Image.open(
                   r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\n.jpg")
               fimg = fimg.resize((600, 700))
               self.photoimmage1 = ImageTk.PhotoImage(fimg)
               lblimg = Label(self.root2,image=self.photoimmage1)
               lblimg.place(x=0, y=0, width=600, height=700)



               l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="yellow",bg="black")
               l.place(x=0,y=10,relwidth=1)

               security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="black",fg="gold")
               security_Q.place(x=70,y=80)

               self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
               self.combo_security_Q["values"]=("Select","Your birth place","Your best Friend Name","Your Pet Name")
               self.combo_security_Q.place(x=70,y=115,width=250)
               self.combo_security_Q.current(0)


               security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="black",fg="gold")
               security_A.place(x=70,y=170)

               self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
               self.txt_security.place(x=70,y=205,width=250)

               new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="black",fg="gold")
               new_password.place(x=70,y=250)

               self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
               self.txt_newpass.place(x=70,y=280,width=250)
               
               btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="black")
               btn.place(x=130,y=340)







class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        ########## variables#########

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        ######## bg image #####

        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\hall1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        ############ left image #####################

        self.bg1 = ImageTk.PhotoImage(
            file=r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\1.jpg")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=70, y=100, width=470, height=460)

        ########### main frame #############

        frame = Frame(self.root, bg="gray80")
        frame.place(x=540, y=100, width=650, height=460)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="hotpink4",
                             bg="grey80")
        register_lbl.place(x=20, y=20)

        #### label and entry #####

        #### row 1 ####

        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="hotpink4", bg="grey80")
        fname.place(x=50, y=80)

        self.txt_fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.txt_fname.place(x=50, y=110, width=230)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="hotpink4", bg="grey80")
        lname.place(x=370, y=80)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=110, width=230)

        ##### row 2 #####

        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="grey80", fg="hotpink4")
        contact.place(x=50, y=150)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=180, width=230)

        email = Label(frame, text="Email ID", font=("times new roman", 15, "bold"), bg="grey80", fg="hotpink4")
        email.place(x=370, y=150)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=180, width=230)

        ##### row 3 #####

        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="grey80",
                           fg="hotpink4")
        security_Q.place(x=50, y=220)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                             font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your birth place", "Your Best Fiend Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=250, width=230)
        self.combo_security_Q.current(0)

        security = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="grey80",
                         fg="hotpink4")
        security.place(x=370, y=220)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=250, width=230)

        #####   row 4 ######

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="grey80", fg="hotpink4")
        pswd.place(x=50, y=290)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=320, width=230)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="grey80",
                             fg="hotpink4")
        confirm_pswd.place(x=370, y=290)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=320, width=230)

        ### check button###

        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree the terms & conditions",
                                    font=("times new roman", 12, "bold"), bg="grey80", onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=350)

        ######## buttons #######

        img = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\btn2.png")
        img = img.resize((130, 40))
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="grey80", fg="hotpink4")
        b1.place(x=80, y=385, width=200)

        img1 = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\login.jpg")
        img1 = img1.resize((130, 40))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"),
                    bg="grey80", fg="hotpink4")
        b1.place(x=350, y=385, width=200)

       

 ######## function declaration ###############




    def login(self):
        if self.txtusr.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to our Villa")
        else:
            messagebox.showerror("Invalid","Invalid Username&Password")

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
        if self.var_fname.get == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password doesnt match", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and conditions", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="my_data")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exist,please try another email", parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
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
            messagebox.showinfo("Success", "Register Successfully", parent=self.root)
            self.clear()


    def return_login(self):
        self.root.destroy()


class TheMoonVilla:
    def __init__(self, root):
        self.root = root
        self.root.title("The Moon Villa")
        self.root.geometry("1550x800+0+0")

        # *******************main frame*******************
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # *********************title**************

        lbl_title = Label(self.root, text="THE   MOON   VILLA", font=("times new roman", 40, "bold"),
                          bg="gray10",
                          fg="lightgoldenrod4", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1550, height=50)

        btn_frame = Frame(self.root, bd=4, relief=RIDGE)
        btn_frame.place(x=225, y=50, width=4000, height=40)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=28,
                          font=("times new roman", 16, "bold"), bg="lightgoldenrod4", fg="gray10",
                          activebackground="deepskyblue4", activeforeground="darkslategray1", bd=1, cursor="hand1")
        cust_btn.place(x=0, y=0)

        villa_btn = Button(btn_frame, text="VILLA", width=25,command=self.roombooking,font=("times new roman", 16, "bold"), bg="lightgoldenrod4",
                          fg="gray10", activeforeground="darkslategray1", activebackground="deepskyblue4",
                          bd=1, cursor="hand1")
        villa_btn.place(x=300, y=0)

        details_btn = Button(btn_frame, text="DETAILS", command=self.details_room, width=25,
                             font=("times new roman", 16, "bold"), bg="lightgoldenrod4", fg="gray10",
                             activeforeground="darkslategray1", activebackground="deepskyblue4", bd=1, cursor="hand1")
        details_btn.place(x=600, y=0)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout, width=25,
                            font=("times new roman", 16, "bold"), bg="lightgoldenrod4", fg="gray10",
                            activeforeground="darkslategray1", activebackground="deepskyblue4", bd=1, cursor="hand1")
        logout_btn.place(x=880, y=0)

        # *********** center image image**************

        img3 = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\r1.jpg")
        img3 = img3.resize((1300, 570))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1300, height=500)

        # ^^^^^^^^^^^^^^^logo  IMAGE  1 ^^^^^^^^^^^^^^

        img7 = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\f6.jpg")
        img7 = img7.resize((300, 225))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        lblimg1 = Label(self.root, image=self.photoimg7, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=50, width=228, height=145)

        ##### quote image ################

        img8 = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\qoute.jpg")
        img8 = img8.resize((450, 110))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        lblimg1 = Label(self.root, image=self.photoimg8, bd=4, relief=RIDGE)
        lblimg1.place(x=227, y=90, width=450, height=100)

        ########### quote image 2 ###########

        img9 = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\quote2.jpg")
        img9 = img9.resize((400, 110))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        lblimg1 = Label(self.root, image=self.photoimg9, bd=4, relief=RIDGE)
        lblimg1.place(x=619, y=90, width=400, height=100)

        ##### quote 3 #############

        img10 = Image.open(
            r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\quote5.jpg")
        img10 = img10.resize((400, 110))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        lblimg1 = Label(self.root, image=self.photoimg10, bd=4, relief=RIDGE)
        lblimg1.place(x=1000, y=90, width=400, height=100)

        # ^^^^^^^^^^^^^^^left  IMAGE  1 ^^^^^^^^^^^^^^

        img6 = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\d22.jpg")
        img6 = img6.resize((300, 225))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lblimg1 = Label(main_frame, image=self.photoimg6, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=228, height=200)

        # ^^^^^^^^^^^^^^^left  IMAGE  2  ^^^^^^^^^^^^^^

        img4 = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\d31.jpg")
        img4 = img4.resize((300, 225))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=200, width=228, height=200)

        #### left image 3########

        img5 = Image.open(
            r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\f12.jpg")
        img5 = img5.resize((300, 225))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=2, relief=RIDGE)
        lblimg1.place(x=0, y=363, width=228, height=137)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
