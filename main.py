from inspect import FrameInfo
from re import L
from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import workbook
import pathlib
import _mysql_connector

background = "#06283D"
frameBg = "#EDEDED"
frameFg = "#06283D"


window = Tk()
window.title("Student Registration System")
window.geometry("1250x700+210+100")
window.config(bg=background)


# gender selection
def genderSelection():
    value = radio.get()
    if value == 1:
        gender = "Male"
    else:
        gender = "Female"


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
Label(
    window,
    text="Email: olatunjiolanrewaju228@gmail.com",
    width=10,
    height=3,
    bg="#F0687C",
    anchor="e",
).pack(side=TOP, fill=X)
Label(
    window,
    text="STUDENT REGISTRATION",
    width=10,
    height=2,
    bg="#C36464",
    fg="#FFF",
    font="arial 20 bold",
).pack(side=TOP, fill=X)

# search bar to update
search = StringVar()
Entry(window, textvariable=search, width=15, bd=2, font="arial 20").place(x=820, y=70)
searchIcon = PhotoImage(file="images/search.png")
searchButton = Button(
    window,
    text="Search",
    compound=LEFT,
    image=searchIcon,
    width=123,
    bg="#68DDFA",
    font="arial 13 bold",
)
searchButton.place(x=1060, y=66)

updateIcon = PhotoImage(file="images/update.png")
updateButton = Button(window, image=updateIcon, bg="#C36464")
updateButton.place(x=110, y=64)

# Registration and Date
Label(
    window, text="Matriculation No:", font="arial 13", fg=frameBg, bg=background
).place(x=30, y=150)
Label(window, text="Date:", font="arial 13", fg=frameBg, bg=background).place(
    x=500, y=150
)

matriculationNumber = StringVar()
dateReg = StringVar()

# matriculation_no()
matric_entry = Entry(
    window, textvariable=matriculationNumber, width=15, font="arial 10"
)
matric_entry.place(x=160, y=150)



today = date.today()
currentDate = today.strftime("%d/%m/%Y")
date_entry = Entry(window, textvariable=dateReg, width=15, font="arial 10")
date_entry.place(x=550, y=150)

dateReg.set(currentDate)


# student details
studentInfo = LabelFrame(
    window,
    text="Student Details",
    font=20,
    bd=2,
    width=900,
    bg=frameBg,
    fg=frameFg,
    height=280,
    relief=GROOVE,
)
studentInfo.place(x=30, y=190)

# Name Labels
fNameLabel = Label(
    studentInfo, text="First Name:", font="arial 13", bg=frameBg, fg=frameFg
).place(x=30, y=50)
midNameLabel = Label(
    studentInfo, text="Middle Name:", font="arial 13", bg=frameBg, fg=frameFg
).place(x=30, y=100)
lNameLabel = Label(
    studentInfo, text="Last Name:", font="arial 13", bg=frameBg, fg=frameFg
).place(x=30, y=150)

# Level label
levelLabel = Label(
    studentInfo, text="Level:", font="arial 13", bg=frameBg, fg=frameFg
).place(x=30, y=200)

# Gender Label
genderLabel = Label(
    studentInfo, text="Gender:", font="arial 13", bg=frameBg, fg=frameFg
).place(x=500, y=50)

# Department Label

departmentLabel = Label(
    studentInfo, text="Department:", font="arial 13", bg=frameBg, fg=frameFg
).place(x=500, y=100)

# Date of birth label
dobLabel = Label(
    studentInfo, text="Date of Birth:", font="arial 13", bg=frameBg, fg=frameFg
).place(x=500, y=150)

#  Names Entry
fName = StringVar()
fName_entry = Entry(studentInfo, textvariable=fName, width=20, font="arial 10")
fName_entry.place(x=160, y=50)

midName = StringVar()
midName_entry = Entry(studentInfo, textvariable=midName, width=20, font="arial 10")
midName_entry.place(x=160, y=100)

lName = StringVar()
lName_entry = Entry(studentInfo, textvariable=lName, width=20, font="arial 10")
lName_entry.place(x=160, y=150)

# Level spinbox(Entry)
level_spinbox = Spinbox(
    studentInfo, font="Roboto 10", from_=100, to=500, increment=100, state="r"
)
level_spinbox.place(x=160, y=200)

# Department combobox(Entry)
department_combobox = Combobox(
    studentInfo,
    values=[
        "Computer Science",
        "Cyber Security",
        "Information and Communication Technology",
        "Software Engineering",
    ],
    font="Roboto 10",
    width=20,
    state="r",
)
department_combobox.current(0)
department_combobox.place(x=620, y=100)

dateOfBirth = StringVar()
dateOfBirth_entry = Entry(
    studentInfo, textvariable=dateOfBirth, width=20, font="arial 10"
)
dateOfBirth_entry.place(x=620, y=150)

# Radio butons for gender
radio = IntVar()
radioBtn1 = Radiobutton(
    studentInfo,
    text="Male",
    variable=radio,
    value=1,
    bg=frameBg,
    fg=frameFg,
    command=genderSelection,
)
radioBtn1.place(x=570, y=50)

radioBtn2 = Radiobutton(
    studentInfo,
    text="Female",
    variable=radio,
    value=2,
    bg=frameBg,
    fg=frameFg,
    command=genderSelection,
)
radioBtn2.place(x=630, y=50)


# Course Information Collection

# Coure Information Frame
courseInfoFrame = LabelFrame(
    window,
    text="Course Information",
    font=20,
    bd=2,
    width=900,
    bg=frameBg,
    fg=frameFg,
    height=110,
    relief=GROOVE,
)
courseInfoFrame.place(x=30, y=480)

# Label for registration Status
registeredLabel = Label(
    courseInfoFrame, text="Registration Status", font="arial 13", bg=frameBg, fg=frameFg
).place(x=30, y=20)

regStatusVar = StringVar(value="Not Registered")

# check button for registration label
registeredCheck = Checkbutton(
    courseInfoFrame,
    text="Currently Registered",
    variable=regStatusVar,
    onvalue="Registered",
    offvalue="Not Registered",
    font="arial 10",
    bg=frameBg,
    fg=frameFg,
).place(x=35, y=40)

# No  Of Courses
num_courses_label = Label(
    courseInfoFrame,
    text="No of Completed Courses",
    font="arial 13",
    bg=frameBg,
    fg=frameFg,
).place(x=300, y=20)
num_courses_spinbox = Spinbox(
    courseInfoFrame, from_=0, to="infinity", font="arial 10", bg=frameBg, fg=frameFg
).place(x=310, y=45)

# No of Semester Label
num_semesters_label = Label(
    courseInfoFrame, text="No of Semesters", font="arial 13", bg=frameBg, fg=frameFg
).place(x=600, y=20)
num_semesters_spinbox = Spinbox(
    courseInfoFrame, from_=0, to="infinity", font="arial 10", bg=frameBg, fg=frameFg
).place(x=610, y=45)

# Terms & Condition Frame
termsFrame = LabelFrame(
    window,
    text="Terms & conditions",
    font=13,
    bd=2,
    width=900,
    bg=frameBg,
    fg=frameFg,
    height=60,
    relief=GROOVE,
)
termsFrame.place(x=30, y=600)

accept_terms_var = StringVar(value="Not Accepted")
terms_check = Checkbutton(
    termsFrame,
    text="I accept the terms and conditions.",
    variable=accept_terms_var,
    onvalue="Accepted",
    offvalue="Not Accepted",
    font="arial 10",
    bg=frameBg,
    fg=frameFg,
).place(x=10, y=6)

# Image Icon
imageFrame = Frame(window, bd=3, bg="black", width=200, height=200, relief=GROOVE)
imageFrame.place(x=1000, y=150)
img = PhotoImage(file="Images/upload-photo.png")
imgLabel = Label(imageFrame, bg="black", image=img).place(x=0, y=0)

# Buttons

uploadBtn = Button(
    window, text="Upload", width=19, height=2, font="arial 12 bold", bg="lightblue"
).place(x=1000, y=370)
saveBtn = Button(
    window, text="Save", width=19, height=2, font="arial 12 bold", bg="lightgreen"
).place(x=1000, y=450)
resetBtn = Button(
    window, text="Reset", width=19, height=2, font="arial 12 bold", bg="lightpink"
).place(x=1000, y=530)
exitBtn = Button(
    window, text="Exit", width=19, height=2, font="arial 12 bold", bg="grey"
).place(x=1000, y=610)


if __name__ == "__main__":
    window.mainloop()
