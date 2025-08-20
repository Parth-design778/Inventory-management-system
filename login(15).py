    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
               messagebox.showerror('Error',"All fields are required",parent=self.root)
            else:   
               cur.execute("select utype from employee where eip=? AND pass=?",(self.employee_id.get(),self.password.get()))
               user=cur.fetchone()
               if user==None:
                  messagebox.showerror('Error',"INVALID USERNAME/PASSWORD",parent=self.root)
               else:
                    #print(user)
                    if user[0]=="Admin":
                       self.root.destroy()
                       os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
           if self.employee_id.get()==""
            messagebox.showerror('Error',"Employee ID must be required",parent=self.root)
           else:
               cur.execute("select email from employee where eip=?",(self.employee_id.get(),))
               email=cur.fetchone()
               if email==None:
                  messagebox.showerror('Error',"Invalid Employee ID,try again",parent=self.root)
               else:
                   #=======Forget Window============================================
                   self.var_otp=StringVar()
                   self.var_new_pass=StringVar()
                   self.var_conf_pass=StringVar()
                   #call send_email_function()
                   self.forget_win=Toplevel(self.root)
                   self.forget_win.title('RESET PASSWORD')
                   self.forget_win.geometry('400x350+500+100')
                   self.forget_win.focus_force()

                   title=Label(self.forget_win,text='Reset Password',font=('goudy old style',15),bg="#3f51b5",fg="white").pack(side=TOP,fill=X) 
                   lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registration Email",font=("times new roman",15)).place(x=20,y=60)
                   self.btn_reset=Button(self.forget_win,text="SUBMIT",font=("times new roman",15),bg='lightblue')
                   self.btn_reset.place(x=280,y=100,width=100,height=30)   
  
                  
                   lbl_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                   txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg='lightyellow').place(x=20,y=190,width=250,height=30)
                  

                   lbl_c_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                   txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg='lightyellow').place(x=20,y=255,width=250,height=30)
                  
                   self.btn_update=Button(self.forget_win,text="update",state=DISABLED,font=("times new roman",15),bg='lightblue')
                   self.btn_update.place(x=150,y=300,width=100,height=30)   
  
                 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


root=Tk()
obj=Login_System(root)
root.mainloop()


     