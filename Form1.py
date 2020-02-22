import tkinter as tk
root = tk.Tk()
root.title("FORM DATA")
root.configure(bg="pink")
menu1 = tk.Menu(root)
root.config(menu = menu1)
sub1 = tk.Menu(menu1)
first = tk.Label(root,text="First name",fg='magenta').grid(row=0,column=0)
last = tk.Label(root,text="Last name",fg = "magenta").grid(row=1,column = 0)
agp = tk.Label(root,text="AGP",fg = "magenta").grid(row=2,column=0)
academic_level = tk.Label(root,text = "Academic level",fg ="magenta").grid(row=3,column=0)
ent1 = tk.Entry(root,bg='red',).grid(row=0,column=1)
ent2 = tk.Entry(root,bg="red").grid(row=1,column=1)
ent3 = tk.Entry(root,bg="red").grid(row=2,column=1)
ent4 = tk.Entry(root,bg="red").grid(row=3,column=1)
root.mainloop()


