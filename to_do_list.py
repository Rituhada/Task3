from tkinter import *
from tkinter import messagebox



def newTask():
    task = my_entry.get()
    if task != "":
       label.insert(END, task)
       my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter task.")

def deleteTask():
    label.delete(ANCHOR)
    
def close():  
    print(newTask)  
    root.destroy()

root=Tk()
root.title("TO-Do-List")
root.iconbitmap(r'to_do_list_rXN_icon.ico')
root.geometry("400x550")
root.config(bg = "#FAEBD7")
root.resizable(False,False)
label=Label(root,text='To-Do-List',font='Consolas 25 bold',padx=20,pady=10, width=10,bg='#FFB6C1',fg='black')
label.pack(side='top', fill=BOTH)

label=Label(root,text='Tasks',font='Consolas 11 bold',bg="#FAEBD7",width=10,fg='black')
label.pack(side='top', fill=BOTH)

frame = Frame(root)
frame.pack(pady=10)
label = Listbox(frame,width=25,height=8,font='Times 18',bd=0,fg='#464646',highlightthickness=0,selectbackground='#a6a6a6',activestyle="none")
label.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    label.insert(END, item)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

label.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=label.yview)

my_entry = Entry(root,font='times 24')
my_entry.pack(pady=10)
button_frame = Frame(root)
button_frame.pack(pady=20)

btn1 = Button(button_frame,text='Add Task',font='times 14 bold',bg='#9ACD32',padx=20, pady=10,command=newTask)
btn1.pack(fill=BOTH, expand=True, side=LEFT)

btn2 = Button(button_frame,text='Delete Task',font='times 14 bold',bg='#FF7F50',padx=20,pady=10,command=deleteTask)
btn2.pack(fill=BOTH, expand=True, side=LEFT)

btn3 =Button(button_frame,text='Exit',font='times 14 bold',bg='#9ACD32',padx=20, pady=10,command = close)
btn3. pack(fill=BOTH, expand=True, side=LEFT)


root.mainloop()
