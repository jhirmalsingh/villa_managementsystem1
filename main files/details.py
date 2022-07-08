import random
from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk


class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("The Moon Villa")
        self.root.geometry("1123x475+231+220")


        self.var_event = StringVar()
        self.var_roomtype = StringVar()
        self.var_noofguests = StringVar()
        self.var_halltype = StringVar()
        self.var_decoration = StringVar()

        #### title #####

        lbl_title = Label(self.root, text=" ADD  EVENT  DETAILS", font=("times new roman", 20, "bold"), bg="gray10",
                          fg="lightgoldenrod4")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # #### logo ####
        #
        # img2 = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\h1.jpg")
        # img2 = img2.resize((100, 40))
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        #
        # lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        # lblimg.place(x=5, y=2, width=100, height=40)

        # ######image######
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\w12.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=40, relwidth=1, relheight=1)

        
        # img2=Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\d31.jpg")
        # img2=img2.resize((100,30))
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        # lblimg.place(x=0,y=0,width=90,height=45)

        ### label frame ######

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Add Event Details", font=("arial", 12, "bold"),
                                    bg="antiquewhite2",
                                    padx=2, pady=6)
        labelframeleft.place(x=5, y=50, width=520, height=350)
        # labelframeleft = Label(self.root, image=self.bg1)
        # self.bg1 = ImageTk.PhotoImage(
        #     file=r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\d2.jpg")

        # ####   Event  ####

        lbl_event = Label(labelframeleft, font=("arial", 12, "bold"), text="Event:", bg="antiquewhite2", padx=2, pady=6)
        lbl_event.grid(row=1, column=0)
        combo_event = ttk.Combobox(labelframeleft, textvariable=self.var_event, font=("arial", 12, "bold"), width=20,
                                   state="readonly")
        combo_event["value"] = ("Outdoor", "Indoor", "Both")
        combo_event.current(0)
        combo_event.grid(row=1, column=1)

        # lbl_event = Label(labelframeleft, text="Event", font=("arial", 12, "bold"),bg="antiquewhite2", padx=2, pady=6)
        # lbl_event.grid(row=0, column=0, sticky=W, padx=20)
        #
        # self.var_event = StringVar()
        # enty_event = ttk.Entry(labelframeleft, textvariable=self.var_event, font=("arial", 13, "bold"), width=20)
        # enty_event.grid(row=0, column=1, sticky=W)

        #           # Room Type

        lbl_roomtype = Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type", bg="antiquewhite2", padx=2,
                             pady=6)
        lbl_roomtype.grid(row=2, column=0)
        combo_roomtype = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("arial", 12, "bold"),
                                      width=20,
                                      state="readonly")
        combo_roomtype["value"] = ("Bridal Room", "Guest Room", "Both")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=2, column=1)

        # No OF gUESTS

        lbl_noofguests = Label(labelframeleft, text="No of Guests", font=("arial", 12, "bold"), bg="antiquewhite2",
                               padx=2, pady=6)
        lbl_noofguests.grid(row=3, column=0, sticky=W, padx=20)

        self.var_noofguests = StringVar()
        enty_noofguests = ttk.Entry(labelframeleft, textvariable=self.var_noofguests, font=("arial", 13, "bold"),
                                    width=22)
        enty_noofguests.grid(row=3, column=1, sticky=W)

        #           # Hall Type

        lbl_halltype = Label(labelframeleft, font=("arial", 12, "bold"), text="Hall Type", bg="antiquewhite2", padx=2,
                             pady=6)
        lbl_halltype.grid(row=4, column=0)
        combo_halltype = ttk.Combobox(labelframeleft, textvariable=self.var_halltype, font=("arial", 12, "bold"),
                                      width=20,
                                      state="readonly")
        combo_halltype["value"] = ("Air Conditioner", "Non Air Conditioner")
        combo_halltype.current(0)
        combo_halltype.grid(row=4, column=1)

        ######### decoration ##########

        lbl_decoration = Label(labelframeleft, font=("arial", 12, "bold"), text="Decoration", bg="antiquewhite2",
                               padx=2, pady=6)
        lbl_decoration.grid(row=5, column=0)
        combo_decoration = ttk.Combobox(labelframeleft, textvariable=self.var_decoration, font=("arial", 12, "bold"),
                                        width=20,
                                        state="readonly")
        combo_decoration["value"] = ("Luxary", "Normal")
        combo_decoration.current(0)
        combo_decoration.grid(row=5, column=1)

        ####  btns #####

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=10, y=200, width=435, height=38)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="coral3",
                        fg="darkgreen",
                        width=15)
        btnAdd.grid(row=0, column=0, padx=1)

        # btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 11, "bold"), bg="coral3",
        #                    fg="darkgreen", width=10)
        # btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 11, "bold"), bg="coral3",
                           fg="darkgreen", width=15)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 11, "bold"), bg="coral3",
                          fg="darkgreen", width=15)
        btnReset.grid(row=0, column=3, padx=1)

        #### table frame search system #############

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Event Details", font=("arial", 11, "bold"),
                                 bg="antiquewhite2",
                                 padx=2, pady=6)
        # self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\o1.jpg")
        # Table_Frame = Label(self.root, image=self.bg1)
        Table_Frame.place(x=550, y=50, width=570, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.details_table = ttk.Treeview(Table_Frame, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        self.details_table = ttk.Treeview(Table_Frame,
                                          column=("event", "roomtype", "noofguests", "halltype", "decoration"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        self.details_table.heading("event", text="Event")
        self.details_table.heading("roomtype", text="Room Type")
        self.details_table.heading("noofguests", text="No Of Guests")
        self.details_table.heading("halltype", text="Hall Type")
        self.details_table.heading("decoration", text="Decoration")

        self.details_table["show"] = "headings"

        self.details_table.column("event", width=100)
        self.details_table.column("roomtype", width=100)
        self.details_table.column("noofguests", width=100)
        self.details_table.column("halltype", width=100)
        self.details_table.column("decoration", width=100)

        self.details_table.pack(fill=BOTH, expand=1)
        self.details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_event.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s,%s,%s)", (

                    self.var_event.get(),
                    self.var_roomtype.get(),
                    self.var_noofguests.get(),
                    self.var_halltype.get(),
                    self.var_decoration.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", " New details added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.details_table.delete(*self.details_table.get_children())
            for i in rows:
                self.details_table.insert("", END, values=i)
                conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.details_table.focus()
        content = self.details_table.item(cursor_row)
        row = content["values"]

        self.var_event.set(row[0]),
        self.var_roomtype.set(row[1]),
        self.var_noofguests.set(row[2]),
        self.var_halltype.set(row[3]),
        self.var_decoration.set(row[4])

    # def update(self):
    #     if self.var_floor.get() == "":
    #         messagebox.showerror("Error", "Please enter event", parent=self.root)
    #     else:
    #         conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
    #         my_cursor = conn.cursor()
    #         my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s", (
    #                                                                                        self.var_floor.get(),
    #                                                                                        self.var_RoomType.get(),
    #                                                                                        self.var_roomNo.get(),
    #                                                                                       ))
    #         conn.commit()
    #         self.fetch_data()
    #         conn.close()
    #         messagebox.showinfo("Update", " New Room details has been updated successfully", parent=self.root)

    # def mDelete(self):
    #     mDelete = messagebox.askyesno("The Moon Villa", "Do you want to delete this Detail", parent=self.root)
    #     if mDelete > 0:
    #         conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
    #         my_cursor = conn.cursor()
    #         query = "delete from details where event=%s"
    #         value = (self.var_event.get(),)
    #         my_cursor.execute(query, value)
    #     else:
    #         if not mDelete:
    #             return
    #     conn.commit()
    #     self.fetch_data()
    #     conn.close()

    def mDelete(self):
        mDelete = messagebox.askyesno("The Moon Villa", "Do you want to delete this detail", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
            my_cursor = conn.cursor()
            query = "delete from details where event=%s"
            value = (self.var_event.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        # self.var_event.set(""),
        # self.var_roomtype.set(""),
        self.var_noofguests.set(""),
        # self.var_halltype.set(""),
        # self.var_decoration.set("")


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()