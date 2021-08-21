#PLAGIARISM DETECTOR

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile


root = Tk()
root.title('PLAGIARISM DETECTOR')
root.geometry("1250x640")
root.configure(bg='black')

def original_file():
    org_file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if org_file is not None:
        org_content = org_file.readlines()
        global str1
        str1 = ''.join(org_content)

def checking_file():
    check_file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if check_file is not None:
        check_content = check_file.readlines()
        global str2
        str2 = ''.join(check_content)

def origi_box():
    original_box.delete(0, END)

def doub_box():
    doubt_box.delete(0, END)

def full_reset():
    original_box.delete(0, END)
    doubt_box.delete(0, END)


def checker():
    para1=original_box.get()
    lower_para1 = para1.lower()
    para_org_li1=lower_para1.split()

    para2=doubt_box.get()
    lower_para2 = para2.lower()
    para_org_li2=lower_para2.split()

    if para_org_li1==para_org_li2:
        messagebox.showinfo('RESULT', " The Paragraph is PLAGIARISED ❌❌")
    else:
        messagebox.showinfo('RESULT', " The Paragraph is NOT PLAGIARISED ✔✔")


def upload_checker():
    real = str1.lower()
    real_list = real.split('.')

    fake = str2.lower()
    fake_list = fake.split('.')

    final_list = []
    for x in real_list:
        for y in fake_list:
            if x==y:
                final_list.append(x)
                percent = (len(final_list)/len(real_list))*100
                messagebox.showinfo('RESULT', f"PLAGIARISED. PLAGIARISM PERCENTAGE = {percent} %")
            else:
                messagebox.showinfo('RESULT', "NOT PLAGIARISED ✔✔")



mylabel1 = Label(root, text='PLAGIARISM DETECTOR', font=("Arial Bold", 20, 'underline') , fg='cyan', bg='black')
mylabel1.pack()

mylabel2 = Label(root, text='', bg='black')
mylabel2.pack()

mylabel3 = Label(root, text='Enter [ TEXT ] Original Content :- ', font=('Arial', 15), bg='black', fg='white')
mylabel3.place(x=135, y=55)

mylabel4 = Label(root, text='Enter [ TEXT ] Content to be Checked :- ', font=('Arial', 15), bg='black', fg='white')
mylabel4.place(x=135, y=130)

mylabel5 = Label(root, text='Made for ICEM Pune', bg='black', fg='white')
mylabel5.place(x=570, y=620)

mylabel6 = Label(root, text='========================================================================', font=('Arial', 15), bg='black', fg='white')
mylabel6.place(x=130, y=190)

mylabel7 = Label(root, text='Upload .txt File to Check for PLAGIARISM', font=('Arial', 20), bg='black', fg='white')
mylabel7.place(x=135, y=210)

mylabel6 = Label(root, text='========================================================================', font=('Arial', 15), bg='black', fg='white')
mylabel6.place(x=130, y=245)

mylabel7 = Label(root, text='Upload Original .txt File', font=('Arial', 15), bg='black', fg='white')
mylabel7.place(x=135, y=270)

mylabel7 = Label(root, text='Upload .txt File to Checked', font=('Arial', 15), bg='black', fg='white')
mylabel7.place(x=135, y=315)


original_box = Entry(root, bg='misty rose', fg='black')
original_box.place(x=140, y=90, width=500, height=27)

doubt_box = Entry(root, bg='misty rose', fg='black')
doubt_box.place(x=140, y=165, width=500, height=27)


button1 = Button(root, text='CLEAR TEXT', fg='white', bg='red', width=40, font='sans 10 bold', command=origi_box).place(x=650, y=90)

button2 = Button(root, text='CLEAR TEXT', fg='white', bg='red', width=13, font='sans 10 bold', command=doub_box).place(x=645, y=165)

button3 = Button(root, text='CHECK TEXT', fg='white', bg='red', width=13, font='sans 10 bold', command=checker).place(x=870, y=165)

button4 = Button(root, text='RESET', fg='white', bg='red', width=13, font='sans 10 bold', command=full_reset).place(x=760, y=165)

button5 = Button(root, text='UPLOAD FILE', fg='white', bg='red', width=13, font='sans 10 bold', command=original_file).place(x=400, y=270)

button6 = Button(root, text='UPLOAD FILE', fg='white', bg='red', width=13, font='sans 10 bold', command=checking_file).place(x=400, y=317)

button5 = Button(root, text='CHECK UPLOADED FILE', fg='white', bg='red', width=58, height=4, font='sans 10 bold', command=upload_checker).place(x=520, y=270)


root.mainloop()



