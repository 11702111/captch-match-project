entry1n=''
zs=''
JH=''
Ts=''
T1s=''
buttonn=''
words=''
ran=''
master1=''
captchan=''
images=''
master3=''
end=''
from tkinter import *
import random
import sys
import pickle
from goto import with_goto  
def find():
    f=open("D:\\python\\data.txt","rb")
    end=False
    while not end:
        try:
            l=pickle.load(f)
            if(l[0]==entry.get() and l[-1]==entry1.get()):
                print("SUCESSFUL LOGIN CORRECT USERNAME AND PASSWORD")
                master.destroy()
                sys.exit()
            else:
                T = Text(master, height=1, width=30)
                T.place(x=25,y=155)
                T.insert(END, "INCORRECT USERNAME/PASSWORD ")
        except EOFError:
            end=True
def rancall():
         global ran
         ran=random.randint(0,8)
def qwe():
    import tkinter
    import random
    import sys
    import pickle
    global entry1n
    global zs
    global buttonn
    global words
    global ran
    global master1
    global captchan
    global images
    master.destroy()
    ran=random.randint(0,8)
    master1=Tk()
    master1.title('FORGOT PASSWORD')
    framen=tkinter.Frame(master1)
    framen.config(height=55,width=280,relief=RIDGE,bg="#e7e7e7")
    framen.place(x=10,y=10)
    master1.geometry("300x400")
    captcha1n=tkinter.Label(framen,text="REG NO")
    captcha1n.place(x=30,y=20)
    zs=StringVar()
    entryn=tkinter.Entry(framen,textvariable=zs)
    entryn.place(x=100,y=20)

    frame1n=tkinter.Frame(master1)
    frame1n.config(height=315,width=280,relief=RIDGE,bg="#e7e7e7")
    frame1n.place(x=10,y=75)
    l2=PhotoImage(file="C:\\Users\\hp\\Desktop\\captcha\\2.png")
    l3=PhotoImage(file="C:\\Users\\hp\\Desktop\\captcha\\3.png")
    l4=PhotoImage(file="C:\\Users\\hp\\Desktop\\captcha\\4.png")
    l5=PhotoImage(file="C:\\Users\\hp\\Desktop\\captcha\\5.png")
    l6=PhotoImage(file="C:\\Users\\hp\\Desktop\\captcha\\6.png")
    l7=PhotoImage(file="C:\\Users\\hp\\Desktop\\captcha\\7.png")
    l8=PhotoImage(file="C:\\Users\\hp\\Desktop\\captcha\\8.png")
    l9=PhotoImage(file="C:\\Users\\hp\\Desktop\\captcha\\9.png")
    l10=PhotoImage(file="C:\\Users\\hp\\Desktop\\captcha\\10.png")
    o2=l2.subsample(24,24)
    o3=l3.subsample(24,24)
    o4=l4.subsample(24,24)
    o5=l5.subsample(24,24)
    o6=l6.subsample(24,24)
    o7=l7.subsample(24,24)
    o8=l8.subsample(24,24)
    o9=l9.subsample(24,24)
    o10=l10.subsample(24,24)

    images=[o2,o3,o4,o5,o6,o7,o8,o9,o10]
    words=["61ItF","83BHa","34JSg","96EMb","20ANh","07GQc","45DPr","58KQi","79FRl"]
 
    captchan=tkinter.Label(frame1n,image=images[ran])
    captchan.place(x=55,y=10)
    entry1n=tkinter.Entry(frame1n )
    entry1n.insert(END, 'ENTER HERE')
    entry1n.place(x=55,y=110)
    frame3n=tkinter.Frame(master1)

    v=StringVar()
    v.set(0)
    cb=tkinter.Checkbutton(frame3n,text="I AM NOT A ROBOT",fg="blue",variable=v,anchor="e")
    cb.place(x=15,y=35)
    i = PhotoImage(file="C:\\Users\\hp\\Desktop\\my1.png")
    o2=i.subsample(8,8)
    sn=tkinter.Label( frame3n, image=o2,anchor="s")
    sn.place(x=175,y=15)
    frame3n.config(height=90,width=250)
    frame3n.place(x=20,y=230)
    buttonn=tkinter.Button(frame1n,command=check,text="SUBMIT",state=DISABLED)
    buttonn.place(x=200,y=260)
    cb.config(command=process)
    button1n=tkinter.Button(frame1n,text="BACK TO LOGIN PAGE")
    button1n.place(x=20,y=260)
    master1.config(bg="white")
    master1.mainloop()
def check():
    global entry1n
    global words
    global ran
    global master1
    global captchan
    global images
    if entry1n.get() == words[ran]:
       master1.destroy()
       password()
    else:
        rancall()
        captchan["image"]=images[ran]
def process():
     global buttonn
     buttonn['state']='normal'
def password():
    import tkinter
    global zs
    global Ts
    global T1s
    global master3
    global end
    master3=Tk()
    master3.geometry("300x280")
    framez=tkinter.Frame(master3)
    Tz = tkinter.Text(master3, height=1, width=34)
    Tz.place(x=10,y=10)
    Tz.insert(END,"REGISTRATION NUMBER IS "+zs.get())
    framez.config(height=80,width=280,relief=RIDGE,bg="#e7e7e7")
    framez.place(x=10,y=40)
    T = tkinter.Text(framez, height=1, width=18)
    T.place(x=60,y=15)
    T.insert(END, "ENTER NEW PASSWORD")
    Ts=StringVar()
    ez=tkinter.Entry(framez,width=39,textvariable=Ts)
    ez.place(x=20,y=45)

    framez1=tkinter.Frame(master3)
    framez1.config(height=80,width=280,relief=RIDGE,bg="#e7e7e7")
    framez1.place(x=10,y=140)
    T1 =tkinter.Text(framez1, height=1, width=18)
    T1.place(x=60,y=15)
    T1.insert(END, "CONFIRM PASSWORD")
    T1s=StringVar()
    ez1=tkinter.Entry(framez1,width=39,textvariable=T1s)
    ez1.place(x=20,y=45)

    buttonz=tkinter.Button(master3,text="SUBMIT",state=NORMAL , command=tut1)
    buttonz.config(width=15)
    buttonz.place(x=170,y=240)

    mainloop()
def tut1():
    global T1s
    global Ts
    if (T1s.get() == Ts.get()):
        tut()
    else :
        print ("CONFIRM PASSWORD DOES MOT MATCH WITH PASSWORD",Ts.get(),T1s.get())
    
    
def tut():
    global master3
    global Ts
    global zs
    global JH
    f=open("D:\\python\\data.txt","ab")
    t=[zs.get(),Ts.get()]
    pickle.dump(t,f)
    pickle.dump("\n",f)
    JH=str(" NOW YOU ARE OUR USER YOUR REGISTRATION IS " +zs.get()+" AND PASSWORD IS "+Ts.get())
    print(JH)
    master3.destroy()
    f.close()
    
    
    
master=Tk()
master.title('LOGIN PAGE')
master.geometry("300x220")


frame=Frame(master)
frame.config(height=55,width=280,relief=RIDGE,bg="#e7e7e7")
frame.place(x=10,y=10)
captcha1=Label(frame,text="REG NO")
captcha1.place(x=30,y=20)
regno1=StringVar()
entry=Entry(frame,textvariable=regno1)
entry.place(x=130,y=20)


frame3=Frame(master)
frame3.config(height=55,width=280,relief=RIDGE,bg="#e7e7e7")
frame3.place(x=10,y=85)
captcha1=Label(frame3,text="PASSWORD")
captcha1.place(x=30,y=20)
password1=StringVar()
entry1=Entry(frame3,textvariable=password1)
entry1.place(x=130,y=20)

but=Button(master,text="LOG IN",command=find)
but.config(height=1,width=10)
but.place(x=190,y=185)

fp=Button(master,text="SIGN UP",command=qwe)
fp.config(height=1,width=10)
fp.place(x=20,y=185)



master.mainloop()
