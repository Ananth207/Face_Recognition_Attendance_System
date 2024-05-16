from tkinter import *
import face_capture
import face_recognise
import delete_entry
import cv2
import attendance
import database_management
import mysql.connector as sqlator

root = Tk()
text = ""
root.title("Attendance System")
root.columnconfigure(1, weight=1)
root.columnconfigure(0, weight=3)
def display_table():
    # Displaying table
    window = Toplevel(root)
    current_time, current_date, table_name = attendance.get_address()
    given_date = date.get()
    if given_date != '':
        table = 'Attendance_for_' + given_date
    else:
        table = table_name

    window.title(table)
    db_connector = sqlator.connect(host = "localhost", user = "root", passwd = "Arjun$207", database = "PyProj")
    if db_connector.is_connected():
        print('Successfully connected to MySQL database')
    cursor = db_connector.cursor()


    sql = "SELECT * FROM " + table #+ " limit 0,10"
    cursor.execute(sql)
    students = cursor.fetchall()
    labels = ["ID", "Name", "Attendance", "Time of Attendance"]
    for y in range(4):
        e = Label(window, text=labels[y])
        e.grid(row=0, column=y)
    i = 1
    col = 4
    iteration = 0
    for student in students:
        for j in range(col):

            e = Label(window,width=10, text=student[j])
            e.grid(row=i, column=j)
        i = i + 1


def details_recorded():
    i = int(id.get())
    n = name.get()
    a = int(age.get())
    face_capture.capture_face(i,n,a)
    global text
    text = "Your details has been recorded"
    mesLabel.config(text = text)
    name.delete(0,END)
    age.delete(0, END)
    id.delete(0, END)

def delete_record():
    i = int(id.get())
    delete_entry.delete_entry(i)

def temp():

    face_recognise.recognise_face(False)

def attendance_text():
    global text
    text = attendance.record_attendance()
    mesLabel.config(text=text)

nameLabel = Label(root, text="Name :", width = 40)
nameLabel.grid(row = 0, column = 0, sticky=NSEW)

name = Entry(root, width=50)
name.grid(row = 0, column = 1, sticky=NSEW)

ageLabel = Label(root, text="Age :")
ageLabel.grid(row = 1, column = 0, sticky=NSEW)

age = Entry(root, width=50)
age.grid(row = 1, column = 1, sticky=NSEW)

idLabel = Label(root, text="User ID:")
idLabel.grid(row = 2, column = 0, sticky=NSEW)

id = Entry(root, width=50)
id.grid(row = 2, column = 1, sticky=NSEW)

# add empty label in row 0 and column 0
l0 = Label(root, text='')
l0.grid(column=0, row=5, columnspan =2)


dateLabel = Label(root, text="Date: (dd_mm_yyyy)")
dateLabel.grid(row = 6, column = 0, sticky=NSEW)

date = Entry(root, width=50)
date.grid(row = 6, column = 1, sticky=NSEW)

myButton = Button(root, text = "Click to record details", command = details_recorded)
myButton.grid(row = 3, column =0, sticky=NSEW)

recogniseButton = Button(root, text = "recognise", command = temp)
recogniseButton.grid(row = 3, column =1, sticky=NSEW)

recordAttendanceButton = Button(root, text = "Record Attendance", command = attendance_text)
recordAttendanceButton.grid(row = 4, column =0, sticky=NSEW)

deleteRecordButton = Button(root, text = "Delete Record", command = delete_record)
deleteRecordButton.grid(row = 4, column =1, sticky=NSEW)

exitButton = Button(root, text = "Exit", command = root.destroy)
exitButton.grid(row = 8, column =0, sticky=NSEW)

displayButton = Button(root, text = "Display", command = display_table)
displayButton.grid(row = 8, column =1, sticky=NSEW)

mesLabel = Label(root, text = "")
mesLabel.grid(row = 9, column =0, columnspan = 2, sticky=NSEW)

root.mainloop()