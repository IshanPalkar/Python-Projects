import random
import tkinter as tk
rel = ["Brother","sister","wife","daughter","son","mother","grandpa","enemy"]

def cal():
    choice=random.choice(rel)
    l.configure(text=f"Your friend was your {choice}")

font = ("verdana",15,"bold")

root = tk.Tk()
root.geometry("400x300")
root.title("Funny Game")
name1=tk.StringVar
root.configure(bg="black")
e1=tk.Entry(root,textvariable=name1)
e1.place(x=20,y=40)
e2=tk.Entry(root)
e2.place(x=220,y=40)

l=tk.Label(root,text='Find relation between you and your friend from the past life:)',font=font,fg="white",bg="black")
l.place(x=10,y=80)
b=tk.Button(root,text="Find relation",fg="white",bg="blue",command=cal)
b.place(x=150,y=250)

root.mainloop()