from tkinter import *
import tkinter.messagebox
import datetime
global entry1
global entry2
global entry3
global entry4
global entry5
global entry6
global entry7
global entry8
global entry9
def del_user_func():
    global entry8,entry9
    root6 = Tk()
    root6.geometry("1300x700")
    frame1 = Frame(root6)
    frame2 = Frame(root6)
    frame1.pack()
    frame2.pack()

    label1 = Label(frame1, text="Enter the user name")
    label2=Label(frame1,text="Enter the user mailid")
    entry8 = Entry(frame1)
    entry9=Entry(frame1)

    label1.grid(row=0, column=0)
    label2.grid(row=1,column=0)
    entry8.grid(row=0, column=1)
    entry9.grid(row=1,column=1)

    button = Button(frame2, text="del user", command=obj1.del_user)
    button2 = Button(frame2, text="back", command=root6.destroy)
    button2.pack()
    button.pack()
    root6.mainloop()

def del_book_func():
    global entry7
    global entry9
    root5=Tk()
    root5.geometry("1300x700")
    frame1=Frame(root5)
    frame2=Frame(root5)
    frame1.pack()
    frame2.pack()

    label1=Label(frame1,text="Enter the book name")
    label2=Label(frame1,text="Enter the author name")
    entry7=Entry(frame1)
    entry9=Entry(frame1)

    label1.grid(row=0,column=0)
    entry7.grid(row=0,column=1)
    label2.grid(row=1,column=0)
    entry9.grid(row=1,column=1)

    button=Button(frame2,text="del book",command=obj1.del_books)
    button2 = Button(frame2, text="back", command=root5.destroy)
    button.pack()
    button2.pack()
    root5.mainloop()

def add_book_func():
    global entry4,entry5,entry6
    root4=Tk()
    root4.geometry("1300x700")
    frame1=Frame(root4)
    frame2=Frame(root4)
    frame1.pack()
    frame2.pack()

    label1=Label(frame1,text="Enter the book name")
    label2=Label(frame1,text="enter the author name")
    label3=Label(frame1,text="Enter the number of copies")
    entry4=Entry(frame1)
    entry5=Entry(frame1)
    entry6=Entry(frame1)

    label1.grid(row=0,column=0)
    entry4.grid(row=0,column=1)
    label2.grid(row=1,column=0)
    entry5.grid(row=1,column=1)
    label3.grid(row=2,column=0)
    entry6.grid(row=2,column=1)

    button=Button(frame2,text="add book",command=obj1.add_books)
    button2 = Button(frame2, text="back", command=root4.destroy)
    button2.pack()
    button.pack()
    root4.mainloop()

def return_book_func():
    root3=Tk()
    root3.geometry("1300x700")
    global entry8
    root3.title("Book return")
    frame2 = Frame(root3)
    frame3 = Frame(root3)
    frame2.pack()
    frame3.pack()

    label1=Label(frame2,text="Enter the book name")
    entry8=Entry(frame2)

    label1.grid(row=0,column=0)
    entry8.grid(row=0,column=1)

    button=Button(frame3,text="return book",command=obj.book_return)
    button2 = Button(frame3, text="back", command=root3.destroy)
    button2.pack()
    button.pack()
    root3.mainloop()
def change_password_func():
    root2=Tk()
    root2.geometry("1300x700")
    global entry5,entry6,entry7,entry9
    root2.title("Change password")
    frame2=Frame(root2)
    frame3=Frame(root2)
    frame2.pack()
    frame3.pack()

    label1=Label(frame2,text="Enter the user name")
    label2=Label(frame2,text="Enter the old password")
    label3=Label(frame2,text="enter the new password")
    label4=Label(frame2,text="enter the mail id")

    entry5=Entry(frame2)
    entry6=Entry(frame2)
    entry7=Entry(frame2)
    entry9=Entry(frame2)

    label1.grid(row=0,column=0)
    entry5.grid(row=0,column=1)
    label2.grid(row=1,column=0)
    entry6.grid(row=1,column=1)
    label3.grid(row=2,column=0)
    entry7.grid(row=2,column=1)
    label4.grid(row=3,column=0)
    entry9.grid(row=3,column=1)

    button=Button(frame3,text="change password",command=obj.change_password)
    button2=Button(frame3,text="back",command=root2.destroy)
    button.pack()
    button2.pack()
    root2.mainloop()

def new_window2():
    root3=Tk()
    root3.geometry("1300x700")
    root3.title("welcome admin")
    frame1=Frame(root3)
    frame1.pack()

    button1=Button(frame1,text="add book",command=add_book_func)
    button2=Button(frame1,text="del book",command=del_book_func)
    button3=Button(frame1,text="del user",command=del_user_func)
    button4=Button(frame1,text="back",command=root3.destroy)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()

    root3.mainloop()

def new_window():
    root1=Tk()
    root1.geometry("1300x700")
    global entry4
    root1.title("Welcome to library")
    frame4=Frame(root1)
    frame1=Frame(root1)
    frame1.pack()
 #   photo3=PhotoImage(file="200.png")
  #  photo4=Label(frame4,image=photo3)
   # photo4.pack()
    frame2=Frame(root1)
    frame2.pack()
    label1=Label(frame1,text="Enter book name/author name")
    entry4=Entry(frame1)

    label1.grid(row=0,column=0)
    entry4.grid(row=0,column=1)
    button = Button(frame2, text="search by author", command=obj.book_search_by_author)
    button2 = Button(frame2, text="Search by name", command=obj.book_search_by_name)
    button3=Button(frame2,text="Change password",command=change_password_func)
    button4=Button(frame2,text="Return book",command=return_book_func)
    button5=Button(frame2,text="back to log in page",command=root1.destroy)

    button.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()

    root1.mainloop()

class user():
    def __init__(self):
      '''  self.user_name=input("Enter the name of the user")
        self.mail_id=input("Enter the user mail id")
        self.user_password=input("Enter the password")'''
    def data_storing(self):
        self.user_name = entry1.get()
        self.mail_id = entry3.get()
        self.user_password = entry2.get()
        fh=open("login_details.txt","a")
        fh.write(self.user_name+" ")
        fh.write(self.mail_id+" ")
        fh.write(self.user_password+"\n")
        tkinter.messagebox.showinfo("msg","sign up successful \n log in to enter")
        fh.close()
    def membere_data(self):
        fh = open("login_details.txt", "a")
        fh.write(self.user_name + " ")
        fh.write(self.mail_id + " ")
        fh.write(self.user_password + "\n")
        fh.close()
        fh = open("member_details.txt", "a")
        fh.write(self.user_name + " ")
        fh.write(self.mail_id + " ")
        fh.write(self.user_password + "\n")
        fh.close()
    def user_login(self):
        fh=open("login_details.txt","r")
        self.user_name=entry1.get()
        self.mail_id=entry3.get()
        self.user_password=entry2.get()
        content=fh.readlines()
        fh.close()
        flag= False
        for i in content:
            p9=i.split()
            flag=False
            if self.user_name == p9[0] and self.mail_id == p9[1] and self.user_password == p9[2]:
               new_window()
               flag=True
               break
        if flag == False:
            tkinter.messagebox.showinfo("msg","log in details not found log in with proper name and password")
    def book_search_by_name(self):
        self.book_search_name=entry4.get()
        fh = open("book_details.txt", "r")
        content3 = fh.readlines()
        fh.close()
        flag3 = False
        for i in content3:
            p3 = i.split()
            if self.book_search_name == p3[0]:
                flag3 = True
                break
        if flag3 == True:
            tkinter.messagebox.showinfo("msg","The book is found")
            answer = tkinter.messagebox.askyesno("msg", "Do you want to take the book")
            if answer == True:
                self.book_issue2()
        else:
            tkinter.messagebox.showinfo("msg","Book not found")
    def book_search_by_author(self):
        self.book_search_author = entry4.get()
        fh = open("book_details.txt", "r")
        content3 = fh.readlines()
        fh.close()
        flag3 = False
        for i in content3:
            p3 = i.split()
            if self.book_search_author == p3[1]:
                flag3= True
                break
        if flag3 == True:
            tkinter.messagebox.showinfo("msg","The book is found")
            answer=tkinter.messagebox.askyesno("msg","Do you want to take the book")
            if answer==True:
                self.book_issue()
        else:
            tkinter.messagebox.showinfo("msg","The book is not found")
    def change_password(self):
        self.user_name1=entry5.get()
        self.old_password=entry6.get()
        self.old_mail=entry9.get()
        flag=0
        fh=open("login_details.txt","r")
        content4=fh.readlines()
        fh.close()
        fh=open("login_details.txt","w")
        for i in content4:
            p4=i.split()
            if p4[0] ==self.user_name1 and p4[2] ==self.old_password and p4[1]==self.old_mail:
                p4[2]=entry7.get()
                flag=1
            fh.write(p4[0]+" "+p4[1]+" "+p4[2]+"\n")
        fh.close()
        if flag==0:
            tkinter.messagebox.showinfo("msg","invalid user details")
        else:
            tkinter.messagebox.showinfo("msg","password successfully changed")
    def book_issue(self):
        fh=open("book_issue_details.txt","r")
        flag6=0
        for i in fh:
            p6=i.split()
            if p6[0]==entry1.get()and p6[4]==entry3.get():
                flag6=1
                break
        fh.close()
        if flag6==0:
            self.new_book = self.book_search_author
            fh = open("book_details.txt", "r")
            content4 = fh.readlines()
            fh.close()
            fh = open("book_details.txt", "w")
            for i in content4:
                p4 = i.split()
                a = p4[2]
                if p4[1] == self.new_book and int(p4[2]) > 0:
                    bk = p4[1]
                    ck = p4[0]
                    a = int(p4[2]) - 1
                    a = str(a)
                fh.write(p4[0] + " " + p4[1] + " " + a + "\n")
            fh.close()
            tkinter.messagebox.showinfo("msg", "Book issued successfully")
            today = datetime.date.today()
            submission_date = datetime.date(today.year, today.month + 1, today.day)
            fh = open("book_issue_details.txt", "a")
            fh.write(entry1.get() + " " + ck + " " + bk + " " + str(submission_date) +" "+entry2.get()+ "\n")
            fh.close()
        else:
            tkinter.messagebox.showinfo("msg","You must have to return the previous book before issueing new books ")
    def book_issue2(self):
        fh = open("book_issue_details.txt", "r")
        flag6 = 0
        for i in fh:
            p6=i.split()
            if p6[0] == entry1.get()and p6[4]==entry3.get():
                flag6 = 1
                break
        fh.close()
        if flag6==0:
            self.new_book = self.book_search_name
            fh = open("book_details.txt", "r")
            content4 = fh.readlines()
            fh.close()
            fh = open("book_details.txt", "w")
            for i in content4:
                p4 = i.split()
                a = p4[2]
                if p4[0] == self.new_book and int(p4[2]) > 0:
                    bk = p4[1]
                    ck = p4[0]
                    a = int(p4[2]) - 1
                    a = str(a)
                fh.write(p4[0] + " " + p4[1] + " " + a + "\n")
            fh.close()
            tkinter.messagebox.showinfo("msg", "Book issued successfully")
            today = datetime.date.today()
            submission_date = datetime.date(today.year, today.month + 1, today.day)
            fh = open("book_issue_details.txt", "a")
            fh.write(entry1.get() + " " + ck + " " + bk + " " + str(submission_date)+" "+entry3.get() + "\n")
            fh.close()
        else:
            tkinter.messagebox.showinfo("msg", "You must have to return the previous book before issueing new books ")
    def book_return(self):
        self.book_name=entry8.get()
        self.user_name2=entry1.get()
        fh=open("book_issue_details.txt","r")
        content9 = fh.readlines()
        fh.close()
        fh=open("book_issue_details.txt","w")
        for i in content9:
            p9=i.split()
            if p9[0]==self.user_name2 and p9[1]==self.book_name and p9[4]==entry3.get():
                continue
            fh.write(p9[0]+" "+p9[1]+" "+p9[2]+" "+p9[3]+" "+p9[4]+"\n")
        fh.close()
        fh = open("book_details.txt","r")
        content8 = fh.readlines()
        fh.close()
        fh=open("book_details.txt","w")
        for i in content8:
            p8=i.split()
            ab=p8[2]
            if p8[0]==self.book_name:
                ab=int(p8[2])+1
                ab=str(ab)
            fh.write(p8[0]+" "+p8[1]+" "+ab+"\n")
        fh.close()
        tkinter.messagebox.showinfo("msg","book return successfull")
class admin():
    def __init__(self):
        self.admin_name=0
    def user_login(self):
        self.admin_name=entry1.get()
        self.admin_password=entry2.get()
        if self.admin_name == "amlan" and self.admin_password == "raj":
            tkinter.messagebox.showinfo("msg","Welcome to library , admin")
            new_window2()
        else:
            tkinter.messagebox.showinfo("msg","you are not an admin plz provide correct information")
    def add_books(self):
        self.book_name=entry4.get()
        self.book_author=entry5.get()
        self.book_quantity=entry6.get()
        fh=open("book_details.txt","a")
        fh.write(self.book_name+" ")
        fh.write(self.book_author+" ")
        fh.write(self.book_quantity+"\n")
        fh.close()
        tkinter.messagebox.showinfo("msg","Book successfully added")
    def del_books(self):
        self.book_name2=entry7.get()
        self.author_name2=entry9.get()
        fh=open("book_details.txt","r")
        content4=fh.readlines()
        fh.close()
        fh=open("book_details.txt","w")
        for i in content4:
            p4=i.split()
            if p4[0]==self.book_name2 and p4[1]==self.author_name2:
                continue
            fh.write(p4[0]+" "+p4[1]+" "+p4[2]+"\n")
        fh.close()
        tkinter.messagebox.showinfo("msg","Book removed successfully")
    def del_user(self):
        self.user_name2 = entry8.get()
        self.user_mail2=entry9.get()
        fh = open("login_details.txt", "r")
        content5 = fh.readlines()
        fh.close()
        fh = open("login_details.txt", "w")
        for i in content5:
            p5 = i.split()
            if p5[0] == self.user_name2 and p5[2]==self.user_mail2:
                continue
            fh.write(p5[0] + " " + p5[1] + " " + p5[2] + "\n")
        fh.close()
        tkinter.messagebox.showinfo("msg","User has been removed successfully")




root=Tk()
root.geometry("1300x700")
root.title("Log in page")
frame3=Frame(root)
frame3.pack()
frame1 = Frame(root)
frame1.pack()
frame2= Frame(frame1)

label1 = Label(frame1, text="Enter your Name ")
label2 = Label(frame1, text="Enter the password")
label3= Label(frame1, text="Enter mail id")
photo=PhotoImage(file="110.png")
photo1=Label(frame3,image=photo)
photo1.pack()

entry1 = Entry(frame1)
entry2 = Entry(frame1,show="*")
entry3= Entry(frame1)
obj=user()
obj1=admin()

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)
label3.grid(row=2,sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2,column=1)
frame2.grid(row=3, column=1)
bottam2= Button(frame2,text="Sign Up",command=obj.data_storing)
bottam1 = Button(frame2, text="Log in",command=obj.user_login)
bottam3=Button(frame2,text="admin log in",command=obj1.user_login)

bottam1.pack(side=LEFT)
bottam2.pack(side = LEFT)
bottam3.pack()

root.mainloop()

