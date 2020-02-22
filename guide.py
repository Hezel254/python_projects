from tkinter.constants import *
from tkinter import *
root=Tk()
root.title('frame')
root.configure(bg='brown')
fra=Frame(root,relief=RIDGE,borderwidth=2)
fra.pack(fill=BOTH,expand=1)
label=Label(fra,text='hello world')
label.pack(fill=X,expand=1)
btn=Button(fra,text='Exit',command=exit)

root.mainloop()