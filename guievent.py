from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import csv
import os
import random

#to clear all entry fields when button is clicked
def Clear():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    number_entry.delete(0, END)
    mail_entry.delete(0, END)
    father_entry.delete(0, END)
    mother_entry.delete(0, END)
    dob_entry.delete(0, END)
    nation_entry.delete(0, END)
    marry_entry.delete(0, END)
    blood_label1.set("A+")
    add_entry.delete(1.0,END)
    prof_entry.delete(0, END)
    exp_entry.delete(0, END)
    dep_entry.delete(0, END)
    sal_entry.delete(0, END)
    v.set(0)


def quit_win():
    bl = messagebox.askquestion("Question", "Do you want to quit")
    if (bl == 'yes'):
        window.quit()


def insert_data():
    fw = open("Registration_Information.txt", 'a')
    bw = open("Check.txt",'a')
    name = name_entry.get()

    age = age_entry.get()
    if (not (age.isnumeric() and (int(age) in range(1, 100)))):
        messagebox.showerror("Error", 'Please enter a Valid Age')
        raise Exception("Please enter a Valid Age")

    gen_val = v.get()

    gender = ''
    if gen_val == 1:
        gender = 'male'
    else:
        gender = 'female'

    ph_no = number_entry.get()
    if (not (ph_no.isnumeric() and len(ph_no) == 10)):
        messagebox.showerror("Error", 'Please enter a Valid Number')
        raise Exception("Please enter a Valid Number")

    mail = mail_entry.get()
    if (not ("@" in mail)):
        messagebox.showerror("Error", 'Please enter a Valid Mail Id')
        raise Exception("Please Enter Valid Mail Id")

    father=father_entry.get()
    mother=mother_entry.get()
    dob=dob_entry.get()
    nation=nation_entry.get()
    marry=marry_entry.get()
    bg=blood_label1.get()
    add=add_entry.get(1.0,END)
    prof=prof_entry.get()
    exp=exp_entry.get()
    dep=dep_entry.get()
    sal=sal_entry.get()
    check_line = name + "\t" + mail + "\n"
    out_line = name + "\t" + age + "\t" + gender + "\t" + ph_no + "\t" + mail + "\n" + father +"\t" + mother +"\t"+ dob+"\t"+nation+"\t"+marry+"\t"+bg+"\n"+add+"\t"+prof+"\t"+exp+"\t"+dep+"\t"+sal+"\n"
    fw.write(out_line)
    bw.write(check_line)
    bw.close()
    fw.close()
    messagebox.showinfo("Congratulation", 'Record Inserted Successfully')


def Insert_Data():
    flag = 0

    try:
        fr = open("Check.txt", 'r')
        email_set = set()
        for line in fr:
            email_str = line.split("\t")[1]
            email_set.add(email_str.strip())

        if (mail_entry.get() in email_set):
            flag = 1

        fr.close()
    except Exception as e:
        print(e)

    if flag == 1:
        messagebox.showerror("Error", "User Already Exists")
    else:
        insert_data()


window = tkinter.Tk()
window.resizable(0, 0)
window.title('Employee Registration Form')
window.iconbitmap(r'icon.ico')
frame=Frame(window,bg="#d6d6d6")
frame.grid(row=1,column=0,padx=3)
frame2=Frame(window,bg="#d6d6d6")
frame2.grid(row=1,column=1,padx=3,pady=3,sticky=N)
frame3=Frame(window,bg="#d6d6d6")
frame3.grid(row=1,column=1,padx=3,pady=3,sticky=S)


## Create labels for frame1
title=ttk.Label(frame,text="Personal Information")
name_label = ttk.Label(frame,text='Name :')
surname_label = ttk.Label(frame,text='Surname :')
age_label = ttk.Label(frame,text='Age :')
gender_label = ttk.Label(frame,text='Gender :')
father_label = ttk.Label(frame,text="Father's name :")
mother_label = ttk.Label(frame,text="Mother's name :")
birth_label = ttk.Label(frame,text="DOB :")
nationality_label= ttk.Label(frame,text='Nationality :')
marr_label = ttk.Label(frame,text='Marrial status :')
blood_label = ttk.Label(frame,text='Blood group :')
blood_label1= StringVar(frame)
blood_label1.set("Select blood group")

#create labels for frame 2
title2=ttk.Label(frame2,text="Contact Information")
number_label = ttk.Label(frame2,text='Phone Number :')
mail_label = ttk.Label(frame2,text='Email id :')
address_label = ttk.Label(frame2,text='Address :')

#create labels for frame 3
title3=ttk.Label(frame3,text="Professional Information")
prof_label = ttk.Label(frame3,text='Profession :')
exp_label = ttk.Label(frame3,text='Experience :')
dept_label=ttk.Label(frame3,text='Department :')
salary_label=ttk.Label(frame3,text='Salary :')

val_x = 10
val_y = 5

#add labels to frame 1 grid
title.grid(row=0,column=1,columnspan=2)
name_label.grid(row=1, column=1, sticky=W, pady=val_y, padx=val_x)
age_label.grid(row=2, column=1, sticky=W, pady=val_y, padx=val_x)
gender_label.grid(row=3, column=1, sticky=W, pady=val_y, padx=val_x)
father_label.grid(row=5, column=1, sticky=W, pady=val_y, padx=val_x)
mother_label.grid(row=6, column=1, sticky=W, pady=val_y, padx=val_x)
birth_label.grid(row=7, column=1, sticky=W, pady=val_y, padx=val_x)
nationality_label.grid(row=8, column=1, sticky=W, pady=val_y, padx=val_x)
marr_label.grid(row=9, column=1, sticky=W, pady=val_y, padx=val_x)
blood_label.grid(row=10, column=1, sticky=W, pady=val_y, padx=val_x)

#add labels to frame 2 grid
title2.grid(row=0,column=1,columnspan=2)
number_label.grid(row=1, column=1, sticky=W, pady=val_y, padx=val_x)
mail_label.grid(row=2, column=1, sticky=W, pady=val_y, padx=val_x)
address_label.grid(row=3, column=1, sticky=W, pady=val_y, padx=val_x)

#add labels to frame 3 grid
title3.grid(row=0,column=1,columnspan=2)
prof_label.grid(row=1, column=1, sticky=W, pady=val_y, padx=val_x)
exp_label.grid(row=2, column=1, sticky=W, pady=val_y, padx=val_x)
dept_label.grid(row=3, column=1, sticky=W, pady=val_y, padx=val_x)
salary_label.grid(row=4, column=1, sticky=W, pady=val_y, padx=val_x)

#create entry fields for frame 1
name_entry = Entry(frame)
age_entry = Entry(frame)
v = IntVar()
gender1 = ttk.Radiobutton(frame,text='Male', value=1, variable=v)
gender2 = ttk.Radiobutton(frame,text='female', value=2, variable=v)
father_entry= Entry(frame)
mother_entry= Entry(frame)
dob_entry = Entry(frame)
nation_entry = Entry(frame)
marry_entry = Entry(frame)
items=["A+","A-","B+","B-","O+","O-","AB+","AB-"]
o1=ttk.OptionMenu(frame,blood_label1,*items)

#Entry fields for frame 2
number_entry = Entry(frame2)
mail_entry = Entry(frame2)
add_entry = Text(frame2,height=2,width=15,borderwidth=1)

#Entry fields for frame 3
prof_entry=Entry(frame3)
exp_entry=Entry(frame3)
dep_entry=Entry(frame3)
sal_entry=Entry(frame3)

val_x = 3
val_y = 3

#Add entry fields to their respective frame grids
name_entry.grid(row=1, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
age_entry.grid(row=2, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
gender1.grid(row=3, column=2, padx=(2, 15), sticky=W)
gender2.grid(row=4, column=2, padx=(2, 15), sticky=W)
father_entry.grid(row=5, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
mother_entry.grid(row=6, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
dob_entry.grid(row=7, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
nation_entry.grid(row=8, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
marry_entry.grid(row=9, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
o1.grid(row=10, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)

number_entry.grid(row=1, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
mail_entry.grid(row=2, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
add_entry.grid(row=3,column=2,padx=(2,15),ipadx=val_x,ipady=val_y)

prof_entry.grid(row=1, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
exp_entry.grid(row=2, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
dep_entry.grid(row=3, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
sal_entry.grid(row=4, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)

#Buttons
submit = ttk.Button(text='Submit', command=Insert_Data, width=17, )
submit.grid(row=8, column=0, sticky=E + W, padx=2, ipadx=3, ipady=3)

clear = ttk.Button(text='Clear', command=Clear, )
clear.grid(row=8, column=1, sticky=E + W, pady=5, padx=(2, 15), ipadx=3, ipady=3)

exit = ttk.Button(text='Exit', command=quit_win, )
exit.grid(row=9, column=0, columnspan=2, sticky=W + E, padx=(2, 15), pady=(0, 15), ipadx=3, ipady=3)

#add image
file_path = r"images\\AB2.png"
photo = PhotoImage(file=file_path)
img_lb = Label(image=photo)
img_lb.image = photo
img_lb.grid(row=0, column=0, columnspan=2)

mainloop()
