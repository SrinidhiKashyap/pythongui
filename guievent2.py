from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import os
import random


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
    name = name_entry.get()

    if(len(name)==0):
        messagebox.showerror("Error", 'Please enter a Valid Name')
        raise Exception("Please enter a Valid Name")

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

    out_line = name + "\t" + age + "\t" + gender + "\t" + ph_no + "\t" + mail + "\t" + father +"\t" + mother +"\t"+ dob+"\t"+nation+"\t"+marry+"\t"+bg+"\t"+add+"\t"+prof+"\t"+exp+"\t"+dep+"\t"+sal+"\n"
    fw.write(out_line)
    fw.close()
    messagebox.showinfo("Congratulation", 'Record Inserted Successfully')


def Insert_Data():
    flag = 0

    try:
        fr = open("Registration_Information.txt", 'r')
        email_set = set()
        for line in fr:
            email_str = line.split("\t")[4]
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
#window.geometry('300x600')
window.resizable(0, 0)
window.title('Student Registration Form')

frame=Frame(window,bg="#d6d6d6")
frame.grid(row=0,column=3,padx=3)
frame2=Frame(window,bg="#d6d6d6")
frame2.grid(row=0,column=4,padx=3,pady=3,sticky=N)
frame3=Frame(window,bg="#d6d6d6")
frame3.grid(row=0,column=4,padx=3,pady=3,sticky=S)


## Create a Labels
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

title2=ttk.Label(frame2,text="Contact Information")
number_label = ttk.Label(frame2,text='Phone Number :')
mail_label = ttk.Label(frame2,text='Email id :')
address_label = ttk.Label(frame2,text='Address :')


title3=ttk.Label(frame3,text="Education")
tenth_label = ttk.Label(frame3,text='10th % :')
twelwe_label = ttk.Label(frame3,text='12th % :')
board_label=ttk.Label(frame3,text='Board :')
stream_label=ttk.Label(frame3,text='Stream :')

#desc_label=ttk.Label(frame2,text='Designation :')




val_x = 10
val_y = 5

title.grid(row=0,column=1,columnspan=2)
name_label.grid(row=1, column=1, sticky=W, pady=val_y, padx=val_x)
age_label.grid(row=2, column=1, sticky=W, pady=val_y, padx=val_x)
gender_label.grid(row=3, column=1, sticky=W, pady=val_y, padx=val_x)
father_label.grid(row=5, column=1, sticky=W, pady=val_y, padx=val_x)
mother_label.grid(row=6, column=1, sticky=W, pady=val_y, padx=val_x)
birth_label.grid(row=7, column=1, sticky=W, pady=val_y, padx=val_x)
nationality_label.grid(row=8, column=1, sticky=W, pady=val_y, padx=val_x)
#marr_label.grid(row=9, column=1, sticky=W, pady=val_y, padx=val_x)
blood_label.grid(row=10, column=1, sticky=W, pady=val_y, padx=val_x)


title2.grid(row=0,column=1,columnspan=2)
number_label.grid(row=1, column=1, sticky=W, pady=val_y, padx=val_x)
mail_label.grid(row=2, column=1, sticky=W, pady=val_y, padx=val_x)
address_label.grid(row=3, column=1, sticky=W, pady=val_y, padx=val_x)
#desc_label.grid(row=3, column=1, sticky=W, pady=val_y, padx=val_x)

title3.grid(row=0,column=1,columnspan=2)
tenth_label.grid(row=1, column=1, sticky=W, pady=val_y, padx=val_x)
twelwe_label.grid(row=3, column=1, sticky=W, pady=val_y, padx=val_x)
board_label.grid(row=2, column=1, sticky=W, pady=val_y, padx=val_x)
stream_label.grid(row=4, column=1, sticky=W, pady=val_y, padx=val_x)


name_entry = Entry(frame)
age_entry = Entry(frame)

v = IntVar()
gender1 = ttk.Radiobutton(frame,text='Male', value=1, variable=v)
gender2 = ttk.Radiobutton(frame,text='female', value=2, variable=v)

number_entry = Entry(frame2)
mail_entry = Entry(frame2)
add_entry = Text(frame2,height=2,width=15,borderwidth=1)
#desc_entry = Entry(frame2)

father_entry= Entry(frame)
mother_entry= Entry(frame)
dob_entry = Entry(frame)
nation_entry = Entry(frame)
marry_entry = Entry(frame)
o1=ttk.OptionMenu(frame,blood_label1,0,"A+","A-","B+","B-","O+","O-","AB+","AB-")
board1= StringVar()
board1.set("Select board")
stream=StringVar()
stream.set("Select stream")

tenth_entry=Entry(frame3)
twelwe_entry=Entry(frame3)
board_entry=Entry(frame3)
sal_entry=Entry(frame3)

val_x = 3
val_y = 3

name_entry.grid(row=1, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
age_entry.grid(row=2, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
#marr_entry.grid(row=3, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
father_entry.grid(row=5, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
mother_entry.grid(row=6, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
dob_entry.grid(row=7, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
nation_entry.grid(row=8, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
#marry_entry.grid(row=9, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
o1.grid(row=10, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
gender1.grid(row=3, column=2, padx=(2, 15), sticky=W)
gender2.grid(row=4, column=2, padx=(2, 15), sticky=W)


number_entry.grid(row=1, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
mail_entry.grid(row=2, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
add_entry.grid(row=3,column=2,padx=(2,15),ipadx=val_x,ipady=val_y)



tenth_entry.grid(row=1, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
twelwe_entry.grid(row=3, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
b1=ttk.OptionMenu(frame3,board1,0,"ICSE","CBSE","State board")
board1.set("Select board")
b1.grid(row=2, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
s1=ttk.OptionMenu(frame3,stream,0,"Science","Commerce","Others")
s1.grid(row=4, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)

submit = ttk.Button(text='Submit', command=Insert_Data, width=17, )
submit.grid(row=8, column=3, sticky=E + W, padx=2, ipadx=3, ipady=3)

clear = ttk.Button(text='Clear', command=Clear, )
clear.grid(row=8, column=4, sticky=E + W, pady=5, padx=(2, 15), ipadx=3, ipady=3)

exit = ttk.Button(text='Exit', command=quit_win, )
exit.grid(row=9, column=3, columnspan=2, sticky=W + E, padx=(2, 15), pady=(0, 15), ipadx=3, ipady=3)

file_path = r"images\\AB1.png"

photo = PhotoImage(file=file_path)

img_lb = Label(image=photo)
img_lb.image = photo
img_lb.grid(row=0, column=0, columnspan=3)

window.mainloop()
