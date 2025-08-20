import sqlite3
import PIL
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,messagebox
from backup import BackUP


class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x760+40+60")
        self.root.attributes("-fullscreen", False)
        self.root.title("Parth Billing Software")
        self.root.config(bg="white")

        # TITLE
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Parth Billing Software", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # LOGOUT BUTTON
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow",
                            command=self.backup, cursor="hand2")
        btn_logout.place(x=1200, y=10, height=50, width=150)

        # CLOCK
        self.label_clock = Label(self.root,
                                 text="Welcome\t\t Date : DD-MM-YYYY\t Time : HH:MM:SS",
                                 font=("times new roman", 15), bg="#5d636d", fg="white")
        self.label_clock.place(x=0, y=70, relwidth=1, height=30)

        # Product Frame
        self.var_search=StringVar()
        ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        ProductFrame1.place(x=6, y=110, width=410, height=550)

        titleLabel = Label(ProductFrame1, text="All Products", font=("goudy old style", 20, "bold"),
                           bg="#262626", fg="white")
        titleLabel.pack(side=TOP, fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show all",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
        
        #Supplier Frame
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=395,height=375)

        scroll_x = Scrollbar(ProductFrame3,orient=HORIZONTAL)
        scroll_y = Scrollbar(ProductFrame3,orient=VERTICAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.product_Table.xview)
        scroll_y.config(command=self.product_Table.yview)


        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="Quantity")
        self.product_Table.heading("status",text="Status")
        

        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=100)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)


        self.product_Table.pack(fill=BOTH,expand=1)

        #self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="Note:'Enter 0 Quantity to remove product from cart.",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=600,height=70)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_name=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)


        #=====Cal Cart Frame======================================
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=600,height=360)


            #=====Calculator Frame==============================================
        Cal_Frame=Frame(Cal_Cart_Frame,bd=2,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=235,height=340)

            #=====Cart Frame==============================================

        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=240,y=10,width=357,height=340)
        cartTitle=Label(cart_Frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)


        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.pack(side=BOTTOM,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        self.CartTable.heading("status",text="Status")
        self.CartTable["show"]="headings"
        self.CartTable.column("pid",width=15)
        self.CartTable.column("name",width=60)
        self.CartTable.column("price",width=30)
        self.CartTable.column("qty",width=30)
        self.CartTable.column("status",width=20)
        self.CartTable.pack(fill=BOTH,expand=1)
        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)

        #=====ADD Cart Widgets Frame=========================================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=600,height=110)

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow").place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow").place(x=230,y=35,width=150,height=22)

        
        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock [9999]",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add | Update Cart",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)


    def backup(self):
        self.new_obj = BackUP.bckup()
        

    def show(self):
        con=sqlite3.connect(database=r'C:\Users\parth\OneDrive\Desktop\PBS\pbs.db')
        cur=con.cursor()
        try:
            #self.product_Table=ttk.Treeview(ProductFrame,colums=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrolly.set)
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def search(self):   
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("ERROR","Search input should be required",parent=self.root)
            else:
                cur.execute("SELECT pid,name,price,qty,status from Product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if(len(rows)!=0):
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("ERROR","No record found!!!",parent=self.root)
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  ",{str(error)},parent=self.root)


    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")

    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error',"Please select product from the list",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror('Error',"Quantity is Required",parent=self.root)
        else:
            price_cal=int(self.var_qty.get())*float(self.var_price.get())
            price_cal=float(price_cal)
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get()]
            #=====update cart==========================================
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product already present\nDo you want to update| Remove from the Cart List",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_qty.get() #qty        
            else:
                self.cart_list.append(cart_data)
            self.show_cart()  
            self.bill_updates()

    def bill_updates(self):
        bill_amnt=0
        net_pay=0
        for row in self.cart_list:
            bill_amnt=bill_amnt+float(row[2])

        net_pay=bill_amnt-((bill_amnt*5)/100)
        self.lbl_amnt.config(text=f'Bill Amnt\n{str(bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(net_pay)}')    
        self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")





    def show_cart(self):
      try:
         self.product_Table.delete(*self.CartTable.get_children())
         for row in self.cart_list:
            self.CartTable.insert('',END,values=row)
      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def bill_middle(self):
        con=sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            for row in self.cart_list:
                    pid=row[0]   
                    name=row[1]
                    qty=int(row[4])-int(row[3])
                    if int(row[3])==int(row[4]):
                        status='Inactive'
                    if int(row[3])!=int(row[4]):
                        status='Active'

                    price=float(row[2])*int(row[3])
                    price=str(price)
                    self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                #=========Update qty in product table======================================================
                    cur.execute('Update Product set qty=?,status=?, where pid=?',(
                    qty,
                    status,
                    pid
                    ))   
                    con.commit()
            con.close()    
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')
    
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl.clock.after(200,self.update_date_time)


if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
