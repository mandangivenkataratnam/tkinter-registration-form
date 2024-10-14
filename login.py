from tkinter import * 
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
gmail = Label(root, text="Gmail")
emergency = Label(root, text="Emergency")
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
gmail.grid(row=4, column=2)
emergency.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
gmailvalue = StringVar
emergencyvalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
gmailentry = Entry(root, textvariable=gmailvalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
gmailentry.grid(row=4, column=3)
emergencyentry.grid(row=5, column=3)

checkbtn = Checkbutton(text="remember me?", variable=checkvalue) 
checkbtn.grid(row=6, column=3)

Button(text="Submit", command=getvals).grid(row=7, column=4)

root.mainloop()