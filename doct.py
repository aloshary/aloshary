from tkinter import * 
from tkinter import ttk 
from subprocess import (DEVNULL,PIPE,Popen,run )
def work(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
def pas(): 
  print("medicene")
  work(f"xdg-open load8.gif")
def ana1(): work(f"xdg-open anatomy/u.pdf")
def ana2(): work(f"xdg-open anatomy/u1.pdf")
def ana3(): work(f"xdg-open anatomy/u2.pdf")
def ana4(): work(f"xdg-open anatomy/u3.pdf")
def ana16(): work(f"xdg-open anatomy/u4.pdf")
def ana5(): work(f"xdg-open anatomy/l1.pdf")
def ana6(): work(f"xdg-open anatomy/l2.pdf")
def ana7(): work(f"xdg-open anatomy/l3.pdf")
def ana8(): work(f"xdg-open anatomy/l4.pdf")
def ana9(): work(f"xdg-open anatomy/l5.pdf")
def ana10(): work(f"xdg-open anatomy/l6.pdf")
def ana11(): work(f"xdg-open anatomy/p.pdf")
def ana12(): work(f"xdg-open anatomy/p1.pdf")
def ana13(): work(f"xdg-open anatomy/p2.pdf")
def ana14(): work(f"xdg-open anatomy/p3.pdf")
def ana15(): work(f"xdg-open anatomy/p4.pdf")
def ana17(): work(f"xdg-open 1.pdf")
def ana18(): work(f"xdg-open 1.pdf")
def ana19(): work(f"xdg-open 1.pdf")
def ana20(): work(f"xdg-open 1.pdf")
def ana21(): work(f"xdg-open 1.pdf")
def ana22(): work(f"xdg-open 1.pdf")
def ana23(): work(f"xdg-open 1.pdf")
def ana24(): work(f"xdg-open 1.pdf")
def ana25(): work(f"xdg-open 1.pdf")
def ana26(): work(f"xdg-open 1.pdf")
def ana27(): work(f"xdg-open 1.pdf")
def ana28(): work(f"xdg-open 1.pdf")
def ana29(): work(f"xdg-open 1.pdf")
def ana30(): work(f"xdg-open 1.pdf")
def ana31(): work(f"xdg-open 1.pdf")
def ana32(): work(f"xdg-open 1.pdf")
def ana34(): work(f"xdg-open 1.pdf")
def ana35(): work(f"xdg-open 1.pdf")
def ana36(): work(f"xdg-open 1.pdf")
def ana37(): work(f"xdg-open 1.pdf")
def ana38(): work(f"xdg-open 1.pdf")
def ana39(): work(f"xdg-open 1.pdf")
def ana40(): work(f"xdg-open 1.pdf")
def menu():
    root =Tk()
    root.configure(background= "#555",padx =20,pady =3,cursor="heart")#949fff
    root.grid()
    menu=Menu()
    inp=ttk.Entry(root,width=60)
    logo=PhotoImage(file="/home/kali/Pictures/zalinge.png").subsample(2,1)
    #inp.grid(row=0, column =2,padx =10,pady =0)
    root.title("FACULITY OF MEDICENE")
    style=ttk.Style()
    style.configure("TButton",background="#555",font=("arial",15,"italic"),foreground="black",borderwidth=0)
    style.configure("TLabel",font=("Arial",15,"italic"))
    
    
    but = ttk.Button(root,text ="all refrances")
    but.grid(column=2,row= 15,padx=0,pady=0)
    but.configure(command =pas,width=20)
    l1=ttk.Label(root,text="\n\n   \n\n")
    l1.grid(row=16, column =4,padx =10,pady =0)
    l1.configure(background= "#555",foreground="#949fff") 
    
    l1=ttk.Label(root,text=" \n                PUPLIC OF SUDAN\n   MENISTRY OF HIGH EDUOCATION  \n            FACOLITY OF MEDICENE\n")
    l1.grid(row=0, column =2,padx =10,pady =0)
    l1.configure(background= "#555",foreground="black",font=("times",20,"italic"))
    l1=ttk.Label(root,text=" \n                \n    i  \n            \n")
    l1.grid(row=0, column =4,padx =10,pady =0)
    l1.configure(background= "#555",foreground="cyan",font=("Arial",20),image=logo)
    
    l1=ttk.Label(root,text=" \n                \n    i  \n            \n")
    l1.grid(row=0, column =0,padx =10,pady =0)
    l1.configure(background= "#555",foreground="cyan",font=("Arial",20),image=logo)
    ######################################################################## documents
    but = ttk.Button(root,text ="semster 1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =sem1,width=20,cursor="clock")
    
    but = ttk.Button(root,text ="semster 2")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =sem2,width=20,cursor="man")#,image=logo2)
    
    but = ttk.Button(root,text ="semster 3")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =sem3,width=20,cursor="fleur")#,image=logo2)
    
    but = ttk.Button(root,text ="semster 4")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =sem4,width=20,cursor="exchange")#,image=logo2)
    
    but = ttk.Button(root,text ="semster 5")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =sem5,width=20,cursor="mouse")#,image=logo2)
    
    but = ttk.Button(root,text ="semster 6")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =sem6,width=20,cursor="spider")#,image=logo2)
    
    but = ttk.Button(root,text ="semster 7")
    but.grid(column=1,row= 8,padx=0,pady=0)
    but.config(command =sem7,width=20,cursor="star")
    
    but = ttk.Button(root,text ="semster 8")
    but.grid(column=1,row= 9,padx=0,pady=0)
    but.config(command =sem8,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 9")
    but.grid(column=1,row= 10,padx=0,pady=0)
    but.config(command =sem9,width=20,cursor="target")#,image=logo2)
    
    but = ttk.Button(root,text ="semster 10")
    but.grid(column=1,row= 11 ,padx=0,pady=0)
    but.config(command =sem10,width=20,cursor="trek")#,image=logo2)
    
    but = ttk.Button(root,text ="semster 11")
    but.grid(column=1,row= 12,padx=0,pady=0)
    but.config(command =sem11,width=20,cursor="pirate")#,image=logo2)
    
    but = ttk.Button(root,text ="semster 12")
    but.grid(column=1,row= 13,padx=0,pady=0)
    but.config(command =sem12,width=20,cursor="shuttle")#,image=logo2)
    ###################################################################### videos
    but = ttk.Button(root,text ="semster 1")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =sem1v,width=20,cursor="spraycan")
    
    but = ttk.Button(root,text ="semster 2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =sem2v,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 3")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =sem3v,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 4")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =sem4v,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 5")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =sem5v,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 6")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =sem6v,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 7")
    but.grid(column=2,row= 8,padx=0,pady=0)
    but.config(command =sem7v,width=20)
    
    but = ttk.Button(root,text ="semster 8")
    but.grid(column=2,row= 9,padx=0,pady=0)
    but.config(command =sem8v,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 9")
    but.grid(column=2,row= 10,padx=0,pady=0)
    but.config(command =sem9v,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 10")
    but.grid(column=2,row= 11 ,padx=0,pady=0)
    but.config(command =sem10v,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 11")
    but.grid(column=2,row= 12,padx=0,pady=0)
    but.config(command =sem11v,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 12")
    but.grid(column=2,row= 13,padx=0,pady=0)
    but.config(command =sem12v,width=20)#,image=logo2)
    ##################################################################### records or exam
    but = ttk.Button(root,text ="semster 1")
    but.grid(column=3,row= 2,padx=0,pady=0)
    but.config(command =pas,width=20)
    
    but = ttk.Button(root,text ="semster 2")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 3")
    but.grid(column=3,row= 4,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 4")
    but.grid(column=3,row= 5,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 5")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 6")
    but.grid(column=3,row= 7,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 7")
    but.grid(column=3,row= 8,padx=0,pady=0)
    but.config(command =pas,width=20)
    
    but = ttk.Button(root,text ="semster 8")
    but.grid(column=3,row= 9,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 9")
    but.grid(column=3,row= 10,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 10")
    but.grid(column=3,row= 11 ,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 11")
    but.grid(column=3,row= 12,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    
    but = ttk.Button(root,text ="semster 12")
    but.grid(column=3,row= 13,padx=0,pady=0)
    but.config(command =pas,width=20)#,image=logo2)
    ###################################################################### labels
    l1=ttk.Label(root,text=" documents ")
    l1.grid(row=1, column =1,padx =10,pady =0)
    l1.configure(background= "cyan")
    
    l1=ttk.Label(root,text=" videos ")
    l1.grid(row=1, column =2,padx =10,pady =0)
    l1.configure(background= "cyan")
    
    l1=ttk.Label(root,text=" examinations ")
    l1.grid(row=1, column =3,padx =10,pady =0)
    l1.configure(background= "cyan")
    
    l1=ttk.Label(root,text=" refrances ")
    l1.grid(row=14, column =2,padx =10,pady =0)
    l1.configure(background= "cyan")
    
    l1=ttk.Label(root,text=" 1st YEAR ")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "white",foreground="blue")
    
    l1=ttk.Label(root,text=" 2nd YEAR ")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "white",foreground="blue")
    
    l1=ttk.Label(root,text=" 3rd YEAR ")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "white",foreground="blue")
    
    l1=ttk.Label(root,text=" 4th YEAR ")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "white",foreground="blue")
    
    l1=ttk.Label(root,text=" 5th YEAR ")
    l1.grid(row=10, column =0,padx =10,pady =0)
    l1.configure(background= "white",foreground="blue")
    
    l1=ttk.Label(root,text=" 6th YEAR ")
    l1.grid(row=12, column =0,padx =10,pady =0)
    l1.configure(background= "white",foreground="blue")
    root.mainloop()
def sem1():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 1")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 1\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =ana1,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =ana2,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =ana3,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =ana4,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   CHMISTRY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   BIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n  PHISICS   \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   MATHIMATIC \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem2():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 2")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 2\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white")  
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY 1   \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY 1  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY 1\n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY 2  \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem3():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 3")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 3\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =ana1,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =ana2,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =ana3,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =ana4,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =ana16,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =ana5,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =ana6,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =ana7,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =ana8,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =ana9,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =ana10,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =ana11,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =ana12,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =ana13,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =ana14,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =ana15,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY 2   \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY 2 \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY 2\n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY 3  \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem4():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 4")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 4\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY 3   \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY 3 \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY 3 \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY 4  \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem5():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 5")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 5\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white")  
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem6():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 6")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 6\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem7():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 7")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 7\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem8():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 8")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 8\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
def sem9():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 9")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 9\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem10():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 10")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 10\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem11():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 11")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 11\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem12():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 12")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 12\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    
    ###############################################################################################
def sem1v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 1")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 1\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =ana1,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =ana2,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =ana3,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =ana4,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   CHMISTRY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   BIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n  PHISICS   \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   MATHIMATIC \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem2v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 2")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 2\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white")  
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY 1   \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY 1  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY 1\n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY 2  \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem3v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 3")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 3\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =ana1,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =ana2,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =ana3,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =ana4,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =ana16,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =ana5,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =ana6,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =ana7,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =ana8,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =ana9,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =ana10,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =ana11,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =ana12,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =ana13,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =ana14,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =ana15,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY 2   \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY 2 \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY 2\n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY 3  \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem4v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 4")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 4\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY 3   \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY 3 \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY 3 \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY 4  \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem5v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 5")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 5\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white")  
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem6v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 6")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 6\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem7v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 7")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 7\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem8v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 8")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 8\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
def sem9v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 9")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 9\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem10v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 10")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 10\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem11v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 11")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 11\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
def sem12v():
    root=Tk()
    root.configure(background= "black",padx=20 ,pady=20)
    root.title("F-O-M  SEMISTER 12")
    style=ttk.Style()
    #style.configure("TButton",background="brown")
    l1=ttk.Label(root,text="\nsemister 12\n")
    l1.grid(row=0, column =16,padx =10,pady =0)
    l1.configure(background= "black",foreground="white") 
    inp=ttk.Entry(root,width=100)
    #inp.grid(row=0, column =2,padx =10,pady =0) 
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 1,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 2
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 2,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 3
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 3,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 4
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 4,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 5
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 5,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    ######################################## course 6
    but = ttk.Button(root,text ="lec1")
    but.grid(column=1,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 6,padx=0,pady=0)
    but.config(command =pas,width=7)
    ##############course 7
    but = ttk.Button(root,text="lec1")
    but.grid(column=1,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec2")
    but.grid(column=2,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec3")
    but.grid(column=3,row=7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec4")
    but.grid(column=4,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec5")
    but.grid(column=5,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec6")
    but.grid(column=6,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec7")
    but.grid(column=7,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec8")
    but.grid(column=8,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec9")
    but.grid(column=9,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec10")
    but.grid(column=10,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec11")
    but.grid(column=11,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec12")
    but.grid(column=12,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec13")
    but.grid(column=13,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    
    but = ttk.Button(root,text ="lec14")
    but.grid(column=14,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec15")
    but.grid(column=15,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)#,image=logo2)
    
    but = ttk.Button(root,text ="lec16")
    but.grid(column=16,row= 7,padx=0,pady=0)
    but.config(command =pas,width=7)
    ########## label
    l1=ttk.Label(root,text="\n   ANATOMY    \n")
    l1.grid(row=1, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   PHYIOLOGY  \n")
    l1.grid(row=2, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n BIOCHEMISTRY \n")
    l1.grid(row=3, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n   COMUNITY   \n")
    l1.grid(row=4, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=5, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=6, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\nnot defind yet\n")
    l1.grid(row=7, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    l1=ttk.Label(root,text="\n\n\n\n\n\n\n\n")
    l1.grid(row=8, column =0,padx =10,pady =0)
    l1.configure(background= "black",foreground="blue")
    
    

    
menu()
    
