from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class LoginSystem:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x760+40+60")
        self.root.attributes("-fullscreen",False)
        self.root.title("Parth Billing Software")
        self.root.config(bg = "#fafafa")

        self.username = StringVar()
        self.password = StringVar()

        self.phone_image = ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image = Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        self.login_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white").place(x=650,y=90,width=350,height=460)

        title=Label(self.login_frame,text="Login System",font= ("Times New Roman",40,"bold"),bg="white").place(x=670,y=110)

        lbl_user = Label(self.login_frame,text = "Username",font=("Andalus",15),bg="white",fg="#767171").place(x=700,y=180)
        txt_username = Entry(self.login_frame,textvariable = self.username,font=("Times New Roman",15),bg="lightgrey",fg="black").place(x=700,y=215,width=230)

        lbl_pass = Label(self.login_frame,text = "Password",font=("Andalus",15),bg="white",fg="#767171").place(x=700,y=265)
        txt_pass = Entry(self.login_frame,textvariable = self.password,show="*",font=("Times New Roman",15),bg="lightgrey",fg="black").place(x=700,y=295,width=230)

        btn_login = Button(self.login_frame,command=self.login,text="Login",font=("Arial Rounded MT Bold",15),bg="lightblue",fg="white").place(x=670,y=345,width=310)
        btn_forget = Button(self.login_frame,command=self.forget,text="Forget Password?",font=("Arial Rounded MT Bold",15),bg="lightblue",fg="white").place(x=670,y=425,width=310)

    def login(self):
        pass

    def forget(self):
        pass

if __name__ == "__main__":
    root=Tk()
    obj = LoginSystem(root)
    root.mainloop()
