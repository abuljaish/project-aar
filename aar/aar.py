#AAR Virtual Assistant v1.5

'''

proud to be student of :
SCHOOL OF EXCELLENCE ROHINI SECTOR-23 NEW DELHI


created by:

1.) Abul Jaish

2.) Abhishek

3.) Rishi

and lead by Abul Jaish under the guidence of Deepanshu Goyal (C.S lecturer) and Rahul Bhatia (C.S TGT) of School of excellence rohini sector-23.



This programme is made with python and tkinter with many more important modules )


'''



from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from pytube import YouTube
import sys
from PIL import Image,ImageTk
from time import strftime
from tkinter.filedialog import *
import pyautogui
import os
import webbrowser
import calendar
import qrcode
import random


window = Tk()
window.title('AAR The Virtual Assistant')


   
window.maxsize(1120,655)
render = PhotoImage(file = './rescources/bgimg.png')
pht = Label(window,image = render)
pht.grid(row=0, column=0)

window.wm_iconbitmap('./rescources/aar.ico')
photo1=PhotoImage(file="./rescources/aarpad.png")

photo2=PhotoImage(file="./rescources/clock.png")

photo3=PhotoImage(file="./rescources/logo.png")

photo4=PhotoImage(file="./rescources/ss.png")

photo5=PhotoImage(file="./rescources/sm.png")


photo6=PhotoImage(file="./rescources/syll.png")
photo7=PhotoImage(file="./rescources/cw.png")


photo8=PhotoImage(file="./rescources/snv.png")



photo9=PhotoImage(file="./rescources/ncert.png")


photo10=PhotoImage(file="./rescources/cln.png")



photo11=PhotoImage(file="./rescources/about.png")

photo12=PhotoImage(file="./rescources/ludo.png")



photo13=PhotoImage(file="./rescources/shutdown.png")

photo15=PhotoImage(file='./rescources/aboutus.png')
photo16=PhotoImage(file="./rescources/weburl.png")
window.configure(bg="#285466")
def aarpad():
    window2 = Tk()
    window2.title("AAR Pad ,Writing Pad")
    window2.wm_iconbitmap('./rescources/aar.ico')
    window2.geometry("900x600")
    window.configure(bg='black')

    
    
    def saveFile():
        new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
        if new_file is None:
            return
        text = str(entry.get(1.0, END))
        new_file.write(text)
        new_file.close()



    b1 = Button(window2, text="Save", bg = "black",fg='cyan', command = saveFile).pack()
    lbl=Label(window2,text= 'Note: After Clicking on Save Buttton Please put " .txt " after the name of the file').pack()
    entry = ScrolledText(window2, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
    entry.pack(fill=BOTH, expand=True)
    entry.focus_set()


def clock():
    def tick():
        time_string = strftime("%H:%M:%S")
        clock.config(text=time_string)
        clock.after(200,tick)
    
    times = Tk()
    times.wm_iconbitmap('./rescources/aar.ico')
    times.title("AAR Clock")
    clock = Label(times, font = ("OCR A Extended",100,"bold"), bg="black", fg='cyan') 
    clock.pack()
    tick()


def logo():
 
    aarlog = Tk()
    aarlog.title("AAR Logo Maker")
    
    aarlog.wm_iconbitmap('./rescources/aar.ico')
    
    aarlog.configure(background='black')
    
    label1=Label(aarlog, text="Please take screenshot of your Logo as there is some issue with save button,sorry for inconvinience",font='Helvetica 18 bold',bg='black', fg='cyan').pack()
    label1=Label(aarlog, text="Developed By Team AAR Abul Jaish Abhishek Mishra and Rishi Singh Rajawat                                    ",font='Helvetica 18 bold',bg='black',fg='cyan').pack()


    label1=Label(aarlog, text="Enter Your name/Company name ",font='Broadway 18 bold',bg='cyan', fg='black').pack()
    def returnEntry(arg=None):
 
        result = myEntry.get()
        resultLabel.config(text=result)
        myEntry.delete(0,END)



    myEntry = Entry(aarlog, width=20)
    myEntry.focus()
    myEntry.bind("<Return>",returnEntry)
    myEntry.pack()


 
    enterEntry = Button(aarlog, text= "Enter", command=returnEntry, bg='black', fg='cyan')
    enterEntry.pack(fill=X)


 
    otherlabel=Label(aarlog, text="welcome")
    resultLabel = Label(aarlog, text = "")
    resultLabel.pack(fill=X)
    resultLabel.config(font=("shutdown!",300),fg='cyan',bg='black')





def ss():

    ss=Tk()
    ss.title("AAR Click")
    ss.wm_iconbitmap('./rescources/aar.ico')
    

    canvas1 = Canvas(ss, width = 300, height = 300)
    canvas1.pack()

    sslabel = Label(ss, text="Developed by AAR Team").pack()

    def takeScreenshot():
    
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\Public\Pictures\AARscreenshot.png')
        myScreenshot.show('AARscreenshot.png')

    sslabel = Label(ss, text=r"Path of Saved ScreenShot: C:\Users\Public\Pictures").pack()

    sslabel2 = Label(ss, text="NOTE: This AAR app will take screenshot and when you take another screenshot it will overwrite the first screenshot so after taking Screenshot Please move it in other directories")
    sslabel2.pack()

                
    myButton = Button(ss,text='Take Screenshot', command=takeScreenshot, bg='black',fg='cyan',font= 20)
    canvas1.create_window(150,150,  window=myButton)



    


    
def support_material():
    os.system("start \"\" http://www.edudel.nic.in/welcome_folder/support_material_2019_20.htm")


    

    
def syll():
    os.system("start \"\" http://www.edudel.nic.in/asg_file/classwise_distribution_new.htm")


    

    
def cw():
    os.system("start \"\" https://clicksworthy.blogspot.com/")




    
def snv():
    survol=Tk()
    survol.title("Surface Area Of 3d Objects")
    survol.wm_iconbitmap('./rescources/aar.ico')



    
    
    label1=Label(survol,bg="black", fg='cyan',width=34,text="Surface Area of 3D Shapes",font="Courier 26").pack()


    

    
    l2=Label(survol,bg="cyan",fg='black',width=100,text="Developed by Team Abul Jaish Abhishek Mishra and Rishi Singh").pack()




    label1=Label(survol,text="Cube",font="Andalus 25",bg="black", fg='cyan',width=39).pack()
    l1=Label(survol,bg="cyan",width=100,text="Total Surface area: 6a^2").pack()
    l2=Label(survol,bg="cyan",width=100,text="Volume: a^3").pack()



    label1=Label(survol,text="Cuboid",font="Andalus 25",bg="black", fg='cyan',width=39).pack()
    l1=Label(survol,bg="cyan",width=100,text="Total Surface area: 2(lb+bh+hl)").pack()
    l2=Label(survol,bg="cyan",width=100,text="Volume: l * b * h").pack()



    label1=Label(survol,text="Cylinder",font="Andalus 25",bg="black", fg='cyan',width=39).pack()
    l1=Label(survol,bg="cyan",width=100,text="Total Surface area: 2 π r(r+h)").pack()
    l2=Label(survol,bg="cyan",width=100,text="Volume: π r^2 h").pack()


    label1=Label(survol,text="Cone",font="Andalus 25",bg="black", fg='cyan',width=39).pack()
    l1=Label(survol,bg="cyan",width=100,text="Total Surface area: π r(r+l)").pack()
    l2=Label(survol,bg="cyan",width=100,text="Volume: 4/3π r3").pack()



    label1=Label(survol,text="Sphere",font="Andalus 25",bg="black", fg='cyan',width=39).pack()
    l1=Label(survol,bg="cyan",width=100,text="Total Surface area: 4 π r^2	").pack()
    l2=Label(survol,bg="cyan",width=100,text="Volume: 4/3π r^3").pack()


    label1=Label(survol,text="Hemisphere",font="Andalus 25",bg="black", fg='cyan',width=39).pack()
    l1=Label(survol,bg="cyan",width=100,text="Total Surface area: 3 π r^2").pack()
    l2=Label(survol,bg="cyan",width=100,text="Volume: 2/3π r^3 	").pack()






def ncert():
    os.system("start \"\" https://epathshala.nic.in//process.php?id=students&type=eTextbooks&ln=en")


'''def ncert():
    ncert=Tk()
    ncert.wm_iconbitmap('./images/aar.ico')
    ncert.title("Read Ncert Books")

    def np():
        os.system("start \"\" http://ncert.nic.in/textbook/textbook.htm?jesc1=0-16")

    def nf():
        os.system("start \"\" https://epathshala.nic.in//process.php?id=students&type=eTextbooks&ln=en")

    label1=Label(ncert,bg="#c1db84",width=100,text="There are two choices of books You can read, one is PDF and other is FlipBook Please choose which one you want to read").pack()
    label1=Label(ncert,bg="#c1db84",width=100,text="Sorry For Inconvinienece but the choice buttons are on Home Page in Red Color").pack()
    label1=Label(ncert,bg="#c1db84",width=100,text="Created by ABUL JAISH, Rishi Singh and Abhishek Mishra").pack()

    #NCERT BOOK
    btn2=Button(ncert,image=pht1,command = np).grid(row=0,column=2)

    #NCERT FlipBook
    btn2=Button(ncert,image=pht2,command = nf).grid(row=0,column=1)'''
  
def call():
  
    cln=calendar.calendar(2021)

    clnaar=Tk()
    clnaar.geometry('600x650')
    clnaar.configure(bg='black')
    clnaar.wm_iconbitmap('./rescources/aar.ico')

    clnaar.title('AAR Calender')

    lblcln=Label(clnaar,text='CALENDAR 2021',bg='cyan',fg='black',font=('eras bold itc',28,'bold'),width=50).pack()
    lblcln1=Label(clnaar,text=cln,bg='black',fg='cyan',font=('courier 10 bold')).pack()
  
    
    
def about():
    about=Tk()
    about.title("About AAR")
    about.wm_iconbitmap('./rescources/aar.ico')
    
    canvas2 = Canvas(about, width = 1, height = 1)
    canvas2.grid(row=0,column=0)

    #photo_about = PhotoImage(file = './images/aboutus.png')
    #aboutlbl = Label(about,image=photo_about)
    #aboutlbl.grid(row=0,column=0)

    btn_about=Button(image=photo15,command=about,bg='#48465C', bd=0).grid(row=0,column=0)
    canvas2.create_window(150, 150, about=btn_about)


    
    
    
    '''aboutlabel=Label(about,bg="#0095B6",width="100",text="AAR Virtual assistant",font="Algerian 30").pack()

    
    aboutlabel=Label(about,text="About Us",font="Algerian 30").pack()

                
    aboutlabel=Label(about,text="This programme is created by Abul Jaish, Rishi Singh and Abhishek Mishra under guidance of Deeepanshu Goyal and Rahul Bhatia of SOE Rohini sec-23",font="Arial 15").pack()

    
    aboutlabel=Label(about,text="This multifunctioned programme is made in python to help student in their work  ",font="arial 15").pack()

    
    aboutlabel=Label(about,bg="#0095B6",width="130",text="Have any queries Contact us on peaceindia86@gmail.com",font="Arial 15").pack()'''



def ludo():
    ludo = Tk()
    ludo.geometry('400x400')
    ludo.title('AAR Dice, A dice rolling game')
    ludo.wm_iconbitmap('./rescources/aar.ico')
    ludo.configure(bg='black')
    labelludo1=Label(ludo,bg="cyan",width=100,text="Developed by ABUL JAISH, Rishi Singh and Abhishek Mishra").pack()
    labelludo2 = Label(ludo, text='', font=('Helvetica', 260))
    def roll_dice():
        dice = ['\u2680','\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        labelludo2.configure(text=f'{random.choice(dice)}')
        labelludo2.pack()
    button = Button(ludo, text='roll dice', foreground='cyan',background='black', command=roll_dice).pack() 
def shutdown():
    return os.system("shutdown /s /t 1")

    
def weburl():
    weburl=Tk()
    weburl.title("AAR Search Bar")
    weburl.wm_iconbitmap('./rescources/aar.ico')
    weburl.configure(bg='black')
    weburl.maxsize(400,200)


    def search():
        url=entryurl.get()
    
        webbrowser.open(url)

    lblurl1=Label(weburl,text="Enter URL here :   ",font=("arial",15,"bold"),bg='black',fg='cyan')
    lblurl1.grid(row=0,column=0)
    entryurl=Entry(weburl,width=35)
    entryurl.grid(row=0,column=1)
    btnurl=Button(weburl,text="Search",command=search,bg="cyan",fg="black",font=("arial",14,"bold"))
    btnurl.grid(row=1,column=0,columnspan=2,pady=10)
    weburl.mainloop()
    
btn = Button(window,
             image = photo1,
             command=aarpad, bd=0, bg='#48465C').place(x=50, y=170)
btn2=Button(
    image=photo2,
    command = clock, bg='#48465C', bd=0).place(x=200, y=170)


btn3=Button(
    image=photo3,
    command = logo, bg='#48465C', bd=0).place(x=350, y=170)


btn4=Button(
    image=photo4,
    command = ss, bg='#48465C', bd=0).place(x=500, y=170)

btn5=Button(
    image=photo5,
    command = support_material, bg='#48465C', bd=0).place(x=650, y=170)

btn6=Button(
    image=photo6,
    command = syll, bg='#48465C', bd=0).place(x=800, y=170)

btn7=Button(
    image=photo7,
    command = cw, bg='#48465C', bd=0).place(x=950, y=170)


btn8=Button(
    image=photo8,
    command = snv, bg='#48465C', bd=0).place(x=50, y=320)



btn9=Button(
    image=photo9,
    command = ncert, bg='#48465C', bd=0).place(x=200, y=320)

btn10=Button(
    image=photo10,
    command = call, bg='#48465C', bd=0).place(x=350, y=320)



btn12=Button(
    image=photo12,
    command = ludo, bg='#48465C', bd=0).place(x=500, y=320)

btn11=Button(
    image=photo11,
    command = about, bg='#48465C', bd=0).place(x=800, y=320)


btn13=Button(image=photo13,command = shutdown,
              bg='#48465C', bd=0).place(x=950, y=320)

btn14=Button(image=photo16,command = weburl,
              bg='#48465C', bd=0).place(x=650, y=320)
Button(text=X,command=window.destroy,fg='white',bg='red',width=3,font=("arial",10,"bold")).place(x=1083,y=10)
Label(text='Close',fg='cyan',bg='black').place(x=1082,y=40)
def disable():
    pass
window.protocol("WM_DELETE_WINDOW", disable)




exit=input("press Enter to exit: ")


window.mainloop
