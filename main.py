from inspect import FrameInfo
from re import L
from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl,xlrd
from openpyxl import workbook
import pathlib
import _mysql_connector

background="#06283D"
frameBg = "#EDEDED"
frameFg="#06283D"



window=Tk()
window.title("Student Registration System")
window.geometry("1250x700+210+100")
window.config(bg=background)



#gender selection
def genderSelection():
    value=radio.get()
    if value ==1:
        gender="Male"
    else:
        gender="Female"

# file=pathlib.Path('Student_data.xlsx')
# if file.exists():
#     pass
# else:
#     file = workbook()
#     sheet = file.active
#     sheet['A1']="Matriculation No."
#     sheet['B1']="First Name"
#     sheet['C1']="Middle Name"
#     sheet['D1']="Last Name"
#     sheet['E1']="Level"
#     sheet['F1']="Department"
#     sheet['G1']="Gender"
#     sheet['H1']="Date of Birth"
#     sheet['I1']="Date of Registration"
#     sheet['J1']=""
#     sheet['K1']=""
#     sheet['L1']=""

#     file.save('Student_data.xlsx')
    
    
    
# top frames
Label(window, text="Email: olatunjiolanrewaju228@gmail.com", width=10,height=3,bg="#F0687C", anchor='e').pack(side=TOP,fill=X)
Label(window, text="STUDENT REGISTRATION", width=10,height=2,bg="#C36464",fg="#FFF", font='arial 20 bold').pack(side=TOP,fill=X)

#search bar to update
search = StringVar()
Entry(window,textvariable=search,width=15,bd=2,font="arial 20").place(x=820, y=70)
# searchIcon = PhotoImage(file="images/search.png")
# searchButton = Button(window,text='Search',compound=LEFT, image=searchIcon,wdith=123,bg="#68DDFA", font="arial 13 bold")
# searchButton.place(x=1060, y=66)

# updateIcon= PhotoImage(file="images/update.png")
# updateButton = Button(window, image=updateIcon, bg="#C36464")
# updateButton.place(x=110,y=64)

#Registration and Date
Label(window,text="Matriculation No:", font="arial 13", fg=frameBg,bg=background).place(x=30,y=150)
Label(window,text="Date:", font="arial 13", fg=frameBg,bg=background).place(x=500,y=150)

matriculationNumber = StringVar()
dateReg = StringVar()

matric_entry = Entry(window,textvariable= matriculationNumber, width=15,font="arial 10")
matric_entry.place(x=160, y=150)

#matriculation_no()

today = date.today()
currentDate = today.strftime("%d/%m/%Y")
date_entry = Entry(window,textvariable=dateReg,width=15, font="arial 10")
date_entry.place(x=550,y=150)

dateReg.set(currentDate)


#student details
studentInfo = LabelFrame(window,text="Student Details", font=20,bd=2,width=900, bg=frameBg,fg=frameFg,height=250,relief=GROOVE)
studentInfo.place(x=30,y=200)

Label(studentInfo,text="First Name:",font="arial 13",bg=frameBg,fg=frameFg).place(x=30,y=50)
Label(studentInfo,text="Middle Name:", font="arial 13", bg=frameBg,fg=frameFg).place(x=30,y=100)
Label(studentInfo,text="Last Name:",font="arial 13", bg=frameBg, fg=frameFg).place(x=30,y=150)

Label(studentInfo,text="Level:",font="arial 13",bg=frameBg, fg=frameFg).place(x=500,y=50)
Label(studentInfo,text="Department",font="arial 13",bg=frameBg,fg=frameFg).place(x=500,y=100)
Label(studentInfo,text="Date of Birth:",font="arial 13",bg=frameBg,fg=frameFg).place(x=500,y=150)

fName=StringVar()
fName_entry = Entry(studentInfo,textvariable=fName,width=20,font="arial 10")
fName_entry.place(x=160,y=50)

radio=IntVar()
radioBtn1 = Radiobutton(studentInfo,text="Male", variable=radio,value=1,bg=frameBg,fg=frameFg,command=genderSelection)
radioBtn1.place(x=150,y=150)

radioBtn2 = Radiobutton(studentInfo,text="Female",variable=radio,value=2,bg=frameBg,fg=frameFg,command=genderSelection)
radioBtn2.place(x=200,y=150)



window.mainloop() 