from cProfile import label
from email.mime import image
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from customer import Cust_Win
from details import DetailsRoom
from room import Roombooking


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
                          activebackground="gold4", activeforeground="darkslategray1", bd=1, cursor="hand1")
        cust_btn.place(x=0, y=0)

        villa_btn = Button(btn_frame, text="VILLA", width=25,command=self.roombooking,font=("times new roman", 16, "bold"), bg="lightgoldenrod4",
                          fg="gray10", activeforeground="darkslategray1", activebackground="gold4",
                          bd=1, cursor="hand1")
        villa_btn.place(x=300, y=0)

        details_btn = Button(btn_frame, text="DETAILS", command=self.details_room, width=25,
                             font=("times new roman", 16, "bold"), bg="lightgoldenrod4", fg="gray10",
                             activeforeground="darkslategray1", activebackground="gold4", bd=1, cursor="hand1")
        details_btn.place(x=600, y=0)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout, width=25,
                            font=("times new roman", 16, "bold"), bg="lightgoldenrod4", fg="gray10",
                            activeforeground="darkslategray1", activebackground="gold4", bd=1, cursor="hand1")
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
    root = Tk()
    obj = TheMoonVilla(root)
    root.mainloop()
