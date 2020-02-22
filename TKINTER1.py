import tkinter as tk
def hello():
    print('hello world')
root = tk.Tk()
root.configure(bg="purple")
root.title("Heezus")
menu1 = tk.Menu(root)
#menu=tk.Menu(root)
root.config(menu=menu1)
btn1 = tk.Button(root,text="SWITCH")
btn1.pack(side="bottom")

sub1 = tk.Menu(menu1)

menu1.add_cascade(label="Programs",menu=sub1)
sub1.add_command(label="New")
sub1.add_command(label="New Project")

menu1.add_cascade(label="Edit",menu=sub1)

sub1.add_command(label = "Programs",command = "")
sub1.add_command(label = "Rewrite",command = "")
sub1.add_command(label = "Save",command = hello)
sub1.add_separator()
sub1.add_command(label = "Quit",command = "")

sub5 = tk.Menu(menu1)

menu1.add_cascade(label="Terminal",menu=sub5)
sub1.add_command(label="Exit terminal",)
sub1.add_command(label="Run",command="")
menu1.add_cascade(label="Exit",menu =sub5)
sub2 = tk.Menu(menu1)
menu1.add_cascade(label="About",menu =sub5)
sub2.add_command(label = "About",command = "")

sub4 = tk.Menu(sub2)
sub2.add_cascade(label = "History",menu =sub4)
sub4.add_command(label="origin",command ="")
sub4.add_command(label="Future",command ="")

sub2.add_command(label = "Activities",command = "")
sub2.add_separator()
sub2.add_command(label = "Print",command = "")
sub2.add_command(label = "Quit",command = "")

sub3 = tk.Menu(menu1)
menu1.add_cascade(label="File",menu =sub3)
sub3.add_command(label = "New",command = "")
sub3.add_command(label = "Add",command = "")
sub3.add_command(label = "Save",command = "")




root.mainloop()