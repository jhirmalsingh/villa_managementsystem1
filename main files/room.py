from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import  datetime
from tkinter import messagebox
import mysql.connector


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("The Moon Villa")
        self.root.geometry("1123x475+231+220")

        #  ##### varaibles ####

        self.var_contact = StringVar()
        self.var_eventdate = StringVar()
        # self.var_totalrooms = StringVar()
        self.var_eventtype = StringVar()
        self.var_timeofeventstarts = StringVar()
        self.var_timeofeventends = StringVar()
        self.var_meal = StringVar()
        self.var_eventduration = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal= StringVar()
        self.var_total= StringVar()



####### title######

        lb1_title = Label(self.root, text=" VILLA BOOKING DETAILS", font=("times new roman", 16, "bold"), bg="gray10",
                          fg="lightgoldenrod4", bd=4)
        lb1_title.place(x=0, y=0, width=1295, height=30)


##### label frame #####

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Villa Booking Details",font=("times new roman",14,"bold"),fg="darkgray",bg="mediumorchid4",padx=2)
        labelframeleft.place(x=5,y=30,width=417,height=442)



    #     ####  labels and entrys#####

        # Customer contact

        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=("arial", 12, "bold"),fg="black",bg="mediumorchid4", pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, font=("arial", 11, "bold"), width=27)
        enty_contact.grid(row=0, column=1, sticky=W)

        # ## fetch data button

        btnFetchData = Button(labelframeleft, command=self.Fetch_contact,text="Fetch Data", font=("arial",9, "bold"),
                              bg="chocolate4", fg="darkgrey", width=8)
        btnFetchData.place(x=347, y=4)

        # # Event Date

        event_date = Label(labelframeleft, font=("arial", 12, "bold"), text="Event Date:",fg="black",bg="mediumorchid4", padx=2, pady=6)
        event_date.grid(row=1, column=0, sticky=W)

        txtevent_date = ttk.Entry(labelframeleft, textvariable=self.var_eventdate, font=("arial", 11, "bold"),
                                     width=29)
        txtevent_date.grid(row=1, column=1)

        # # Event type

        label_eventtype = Label(labelframeleft, font=("arial", 12, "bold"), text="Event Type:",fg="black",bg="mediumorchid4", padx=2, pady=6)
        label_eventtype.grid(row=2, column=0, sticky=W)

        combo_eventtype = ttk.Combobox(labelframeleft, textvariable=self.var_eventtype, font=("arial", 11, "bold"),
                                      width=27, state="readonly")
        combo_eventtype["value"] = ("Marriage", "Party")
        combo_eventtype.current(0)
        combo_eventtype.grid(row=2, column=1)

        # #####  time of event starts

        lbltimeofeventstarts= Label(labelframeleft, font=("arial", 12, "bold"),bg="mediumorchid4",fg="black", text="Time Of Event Starts:", padx=2, pady=6)
        lbltimeofeventstarts.grid(row=3, column=0, sticky=W)

        txttimeofeventstarts = ttk.Entry(labelframeleft, textvariable=self.var_timeofeventstarts, font=("arial", 11, "bold"),
                                     width=29)
        txttimeofeventstarts.grid(row=3, column=1)


        # #####  time of event ends

        lbltimeofeventends= Label(labelframeleft, font=("arial", 12, "bold"),bg="mediumorchid4",fg="black",text="Time Of Event Ends:", padx=2, pady=6)
        lbltimeofeventends.grid(row=4, column=0, sticky=W)

        txttimeofeventends = ttk.Entry(labelframeleft, textvariable=self.var_timeofeventends, font=("arial", 11, "bold"),
                                     width=29)
        txttimeofeventends.grid(row=4, column=1)



     ######### meal ###########

        label_meal = Label(labelframeleft, font=("arial", 12, "bold"), text="Meal:",fg="black", bg="mediumorchid4", padx=2,
                            pady=6)
        label_meal.grid(row=5, column=0, sticky=W)

        combo_meal = ttk.Combobox(labelframeleft, textvariable=self.var_meal, font=("arial", 11, "bold"),
                                   width=27, state="readonly")
        combo_meal["value"] = ("Breakfast", "Lunch","Dinner")
        combo_meal.current(0)
        combo_meal.grid(row=5, column=1)

        ######### Event Duration ###########

        label_eventduration = Label(labelframeleft, font=("arial", 12, "bold"), text="Event Duration:",fg="black", bg="mediumorchid4", padx=2,
                           pady=6)
        label_eventduration.grid(row=6, column=0, sticky=W)

        combo_meal = ttk.Combobox(labelframeleft, textvariable=self.var_eventduration, font=("arial", 11, "bold"),
                                  width=27, state="readonly")
        combo_meal["value"] = ("Morning", "Evening", "Night")
        combo_meal.current(0)
        combo_meal.grid(row=6, column=1)

##########Paid Tax

        lbleventtype = Label(labelframeleft, font=("arial", 12, "bold"),text="Paid Tax:",fg="black", bg="mediumorchid4", padx=2, pady=6)
        lbleventtype.grid(row=7, column=0, sticky=W)

        txteventtype = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=("arial", 11, "bold"), width=29)
        txteventtype.grid(row=7, column=1)

             #  Sub Total

        lbleventtype=Label(labelframeleft,font=("arial",12, "bold"),text= "Sub Total:", bg="mediumorchid4",fg="black",padx=2,pady=6)
        lbleventtype.grid(row=8,column=0,sticky=W)

        txteventtype=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("arial",11,"bold"),width=29)
        txteventtype.grid(row=8,column=1)

            #   Total Cost

        lblIdNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="Total Cost:", bg="mediumorchid4" ,fg="black",padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_total,
                                    font=("arial", 11, "bold"), width=29)
        txtIdNumber.grid(row=9, column=1)

        ####    Bill Button

        btnBill =Button(labelframeleft, text="Bill",command=self.total, font=("arial", 10, "bold"), bg="chocolate4", fg="gray69", width=13)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # # btns #############3

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE,bg="hotpink3")
        btn_frame.place(x=0,y=381,width=410,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="chocolate4",fg="gray69",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="chocolate4",fg="gray69",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="chocolate4",fg="gray69",width=10)
        btnDelete.grid(row=0,column=2,padx=2)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="chocolate4",fg="gray69",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        # #### logo #####3
        img23 = Image.open(r"C:\Users\Vibhu Bhardwaj.SumitSharma-PC\Documents\Hostel managemnt System\images\log.jpg")
        img23 = img23.resize((700, 500))
        self.photoimg23 = ImageTk.PhotoImage(img23)

        lblimg = Label(self.root, image=self.photoimg23, bd=0, relief=RIDGE)
        lblimg.place(x=616, y=37, width=500, height=300)

        #########   tabel frame search system

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                                     font=("arial", 12, "bold"), padx=0)
        Table_Frame.place(x=420, y=260, width=700, height=450)

        lblSearchBy = Label(Table_Frame, font=("arial", 11, "bold"), text="Search By:", bg="chocolate4", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 11, "bold"), width=20,
                                        state="readonly")
        combo_search["value"] = ("Contact", "eventdate")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 12, "bold"), width=20)
        txtsearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search",command=self.search, font=("arial", 10, "bold"), bg="chocolate4", fg="gray69", width=13)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All",command=self.fetch_data, font=("arial", 10, "bold"), bg="chocolate4", fg="gray69", width=13)
        btnShowAll.grid(row=0, column=4, padx=1)

        ########     Show data Table

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=35, width=700, height=155)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table,column=("contact", "eventdate", "eventtype", "timeofeventstarts","timeofeventends","meal","eventduration"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("eventdate", text="Event Date")
        # self.room_table.heading("totalrooms", text="Total Rooms")
        self.room_table.heading("eventtype", text="Event Type")
        self.room_table.heading("timeofeventstarts", text="Time Of Event Starts")
        self.room_table.heading("timeofeventends", text="Time Of Event Ends")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("eventduration", text="Event Duration")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("eventdate", width=100)
        # self.room_table.column("totalrooms", width=100)
        self.room_table.column("eventtype", width=100)
        self.room_table.column("timeofeventstarts", width=100)
        self.room_table.column("timeofeventends", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("eventduration", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_contact.get()=="" or self.var_eventdate.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="my_data")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_eventdate.get(),
                                                                                    # self.var_totalrooms.get(),
                                                                                    self.var_eventtype.get(),
                                                                                    self.var_timeofeventstarts.get(),
                                                                                    self.var_timeofeventends.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_eventduration.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Villa Details has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]


        self.var_contact.set(row[0])
        self.var_eventdate.set(row[1])
        # self.var_totalrooms
        self.var_eventtype.set(row[2])
        self.var_timeofeventstarts.set(row[3])
        self.var_timeofeventends.set(row[4])
        self.var_meal.set(row[5])
        self.var_eventduration.set(row[6])
        self.var_paidtax.set(row[7])
        self.var_actualtotal.set(row[8])
        self.var_total.set(row[9])

######## update #############

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set eventdate=%s,eventtype=%s,timeofeventstarts=%s,timeofeventends=%s,meal=%s,eventduration=%s where contact=%s",(
                                                                                                                        self.var_eventdate.get(),
                                                                                                                        self.var_eventtype.get(),
                                                                                                                        self.var_timeofeventstarts.get(),
                                                                                                                        self.var_timeofeventends.get(),
                                                                                                                        self.var_meal.get(),
                                                                                                                        self.var_eventduration.get(),
                                                                                                                        self.var_contact.get()

                    ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Villa details has been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("The Moon Villa", "Do you want to delete this customer", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
            my_cursor = conn.cursor()
            query = "delete from room where contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_contact.set(""),
        self.var_eventdate.set(""),
        # self.var_eventtype.set(""),
        self.var_timeofeventstarts.set(""),
        self.var_timeofeventends.set(""),
        # self.var_meal.set(""),
        # self.var_eventduration.set(""),
        self.var_paidtax.set(""),
        self.var_total.set(""),
        self.var_actualtotal.set("")
        #     x = random.randint(1000, 9999)
        #     self.var_ref.set(str(x))

        ######### all data fetch #########

    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row == None:
                    messagebox.showerror("Error", "This number doesn't exist", parent=self.root)
            else:
                conn.commit()
                conn.close()


                ########## data frame ########

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2,bg="mediumpurple1")
                showDataframe.place(x=422, y=50, width=190, height=200)

                lblName = Label(showDataframe, text="Name:", font=("arial", 12, "bold"),bg="mediumpurple1")
                lblName.place(x=0, y=10)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"),bg="mediumpurple1")
                lbl.place(x=70, y=10)


                ######## gender #######

                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"),bg="mediumpurple1")
                lblGender.place(x=0, y=40)

                lbl2= Label(showDataframe, text=row, font=("arial", 12, "bold"),bg="mediumpurple1")
                lbl2.place(x=70, y=40)


############# email ####################

                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail = Label(showDataframe, text="Email:", font=("arial", 12, "bold"),bg="mediumpurple1")
                lblEmail.place(x=0, y=70)

                lbl3= Label(showDataframe, text=row, font=("arial", 12, "bold"),bg="mediumpurple1")
                lbl3.place(x=60, y=70)


############ nationality ################

                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"),bg="mediumpurple1")
                lblNationality.place(x=0, y=100)

                lbl4 = Label(showDataframe, text=row, font=("arial", 12, "bold"),bg="mediumpurple1")
                lbl4.place(x=90, y=100)


                ################# adddress ##############


                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"),bg="mediumpurple1")
                lblAddress.place(x=0, y=130)

                lbl5 = Label(showDataframe, text=row, font=("arial", 12, "bold"),bg="mediumpurple1")
                lbl5.place(x=85, y=130)


    ###########search system###########

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="my_data")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(
            self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
     if(self.var_meal.get()=="Breakfast" and self.var_eventtype.get()=="Marriage"):
         q1=float(5000)
         q2=float(10000)
         q3=float(q1+q2)
         Tax="Rs."+str("%.2f"%((q3)*0.1))
         ST="Rs."+str("%.2f"%((q3)))
         TT="Rs."+str("%.2f"%(q3+((q3)*0.1)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)

     elif (self.var_meal.get() == "Lunch" and self.var_eventtype.get() == "Marriage"):
        q1 = float(10000)
        q2 = float(10000)
        q3 = float(q1 + q2)
        Tax = "Rs." + str("%.2f" % ((q3) * 0.1))
        ST = "Rs." + str("%.2f" % ((q3)))
        TT = "Rs." + str("%.2f" % (q3 + ((q3) * 0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

     elif (self.var_meal.get() == "Dinner" and self.var_eventtype.get() == "Marriage"):
         q1 = float(15000)
         q2 = float(20000)
         q3 = float(q1 + q2)
         Tax = "Rs." + str("%.2f" % ((q3) * 0.1))
         ST = "Rs." + str("%.2f" % ((q3)))
         TT = "Rs." + str("%.2f" % (q3 + ((q3) * 0.1)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)

     elif (self.var_meal.get() == "Breakfast" and self.var_eventtype.get() == "Party"):
         q1 = float(3000)
         q2 = float(5000)
         q3 = float(q1 + q2)
         Tax = "Rs." + str("%.2f" % ((q3) * 0.1))
         ST = "Rs." + str("%.2f" % ((q3)))
         TT = "Rs." + str("%.2f" % (q3 + ((q3) * 0.1)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)


     elif (self.var_meal.get() == "Lunch" and self.var_eventtype.get() == "Party"):
         q1 = float(5000)
         q2 = float(5000)
         q3 = float(q1 + q2)
         Tax = "Rs." + str("%.2f" % ((q3) * 0.1))
         ST = "Rs." + str("%.2f" % ((q3)))
         TT = "Rs." + str("%.2f" % (q3 + ((q3) * 0.1)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)


     elif (self.var_meal.get() == "Dinner" and self.var_eventtype.get() == "Party"):
         q1 = float(6000)
         q2 = float(10000)
         q3 = float(q1 + q2)
         Tax = "Rs." + str("%.2f" % ((q3) * 0.1))
         ST = "Rs." + str("%.2f" % ((q3)))
         TT = "Rs." + str("%.2f" % (q3 + ((q3) * 0.1)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
