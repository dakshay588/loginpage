from logging import root
from tkinter import*
from tkinter import messagebox
class login_page:
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1199x600+100+50")


        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)
        titel=Label(Frame_login,text="login here",font=("impact",35,"bold"),fg="grey",bg="white").place(x=90,y=30)

        lbl_user=Label(Frame_login,text="username",font=("Goudy old style",13,"bold"),fg="grey",bg="white").place(x=90,y=150)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_user.place(x=90,y=170,width=350,height=35)


        lbl_pass=Label(Frame_login, text="password", font=("Goudy old style", 13, "bold"), fg="grey",
                         bg="white").place(x=90, y=210)
        self.txt_pass=Entry(Frame_login, font=("times new roman", 15), bg="lightgrey")
        self.txt_pass.place(x=90, y=240, width=350, height=35)


        forget_btn=Button(Frame_login,text="forgot password?",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
        login_btn=Button(self.root,command=self.login_function,text="login", fg="white", bg="#d77337",
                        font=("times new roman", 12)).place(x=300, y=470,width=180, height=40)


    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("ERROR","ALL FEILD ARE REQUIRED",parent=self.root)
        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="innolabz":
            messagebox.showerror("Error","invalid username or password",parent=self.root)
        else:
            messagebox.showinfo("welcome",f"welcome {self.txt_user.get()}\nyour password: {self.txt_pass.get()}",parent=self.root)






root=Tk()
obj=login_page(root)
root.mainloop()
