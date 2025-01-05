from tkinter import *
import sqlite3
from tkinter import messagebox as ms
from PIL import Image,ImageTk
import re
root = Tk()
root.title("Welcome to Admin page")
root.geometry("550x200")
image1=Image.open("admin.jpg")
image1=image1.resize((1800,900),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

Name=StringVar()
Email=StringVar()




def insert():
    
    name = Name.get()
    email= Email.get()
    if not name.strip or not email.strip():
       ms.showinfo("Error!","name and email cannot be blank") 
       return
    db = sqlite3.connect('project.db')
    cursor = db.cursor()
    find_user = ('SELECT * FROM registartionpage WHERE Name = ? AND Email=?')
    cursor.execute(find_user,[(Name.get()),(Email.get())])
    result=cursor.fetchall()
    if result:
       msg=""
       print(msg)
       ms.showinfo("message","login successfully")
       from subprocess import call
       call(["python","addstudentdata.py"])
       
       from subprocess import call
       call(["python","updatestudentdata.py"])
       
       from subprocess import call
       call(["python","removestudentdata.py"])

       
    else:
       ms.showinfo("oops!","name or email are not found match")
    
    
# Set the background color of the window
root.configure(bg="pink")

name1_label = Label(root, text="Name", font=("Arial",14,"bold"))
name1_label.place(x=450, y=250)

name1_entry = Entry(root,textvar=Name, font=("Arial",12,"bold"))
name1_entry.place(x=550, y=250, width=300)

Email1_label = Label(root, text="Email id", font=("Arial",14,"bold"))
Email1_label.place(x=450, y=350)

Email1_entry = Entry(root,textvar=Email, font=("Arial", 12))
Email1_entry.place(x=550, y=350, width=300)

add_button = Button(root, text="Add Student", font=("Arial", 12),command=insert)
add_button.place(x=550, y=470, )

update_button = Button(root, text="Update Student", font=("Arial", 12),command=insert)
update_button.place(x=700, y=470, width=150)

remove_button = Button(root, text="Remove Student",font=("Arial", 12),command=insert)
remove_button.place(x=600, y=540, width=150)




root.mainloop()