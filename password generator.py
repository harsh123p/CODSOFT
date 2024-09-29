import code 
from tkinter import *
import random 
root = Tk()
root.geometry("500x350")
passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate():
    passchar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','K','L','M','N','O','P'
                ,'Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','*','_','-','=','+']
    
    password = ""
    for i in range(passlen.get()):
        password = password + random.choice(passchar)
    passstr.set(password)


Label(root,text="Password Generator ",font="Calibri 26 bold ",bg= "white").pack()
Label(root.config(bg="green"))
Label(root,text="Enter password length ",font="Elephant 13 ",bg= "white").pack(pady=3)
Entry(root,textvariable=passlen).pack(pady=3)
Button(root,text="Generate Password ",font="Elephant 13",bg="white",command=generate).pack(pady=7)
Entry(root,textvariable=passstr).pack(pady=3)

root.mainloop()