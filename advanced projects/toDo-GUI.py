from tkinter import *
from tkinter import messagebox
import sqlite3
conn=sqlite3.connect('test.db')
print("Connection is established: Database is created in memory")
#conn.execute("create table tasks(seq_no int primary key,task char(50),priority char(20)); ")
root=Tk()
root.geometry("430x550")
root.title("ToDo")
root.maxsize(height=430,width=530)
#-----------------------------------------------------------------------------------------------
#func to exit the parent window
def exit():
    conn.close()
    root.destroy()

#func to refresh the data on the listbox
def refresh():
    cursor=conn.execute("select * from tasks;")
    #it displays the updated data on the screen
    count=0
    lb1=Listbox(root,selectmode=MULTIPLE,width=70,height=25)
    for record in cursor:
        print(record)
        lb1.insert(count,"{}".format(record))
        count=count+1
        lb1.grid(row=1,column=0,columnspan=6) 
    print("data refreshed succesfully")
#function to delete the selected record in database    
def delete():
    for i in lb1.curselection():
        data_list=lb1.get(i)
        task_id=data_list[1]
        conn.execute("delete from tasks where seq_no='{}';".format(task_id))
        conn.commit()
        print("committed data")
    
    
    
    
#func to ADD NEW TASK in database 
def add_task():
    add_task_window=Tk()
    add_task_window.geometry("500x500")
    
    #function to enter the note in database 
    def save():
        sequence=int(entry_task_sequence.get())
        task=entry_task_description.get()
        priority=entry_task_priority.get()
        if task=="" or priority=="" or sequence=="":
            messagebox.showinfo('ERROR','Please enter the details in all sections!')
        else:
            conn.execute("insert into tasks values({},'{}','{}');".format(sequence,task,priority))
            print("values saved succesfully")
        
        entry_task_sequence.delete(0,END)
        entry_task_description.delete(0,END)
        entry_task_priority.delete(0,END)
    #func to save and exit the add new task window    
    def ok():
        conn.commit()
        cursor=conn.execute("select * from tasks;")
        #it displays the updated data on the screen
        count=0
        lb1=Listbox(root,selectmode=MULTIPLE,width=70,height=25)
        for record in cursor:
            print(record)
            lb1.insert(count,"{}".format(record))
            count=count+1
        lb1.grid(row=1,column=0,columnspan=6) 
        #it destroys the or closes the window.
        add_task_window.destroy()
    
    l1=Label(add_task_window,text="Enter the sequence of new task ")
    l1.pack()
    entry_task_sequence=Entry(add_task_window,bd=3)
    entry_task_sequence.pack()
    
    
    l2=Label(add_task_window,text="Enter new task within 50 characters")
    l2.pack()
    entry_task_description=Entry(add_task_window,bd=3)
    entry_task_description.pack()
    
    l3=Label(add_task_window,text="Set the priority of the task")
    l3.pack()
    entry_task_priority=Entry(add_task_window,bd=3)
    entry_task_priority.pack()
    
    bttn_save=Button(add_task_window,text="SAVE",command=save)
    bttn_save.pack()
    bttn_ok=Button(add_task_window,text="OK",command=ok)
    bttn_ok.pack()
    
    add_task_window.mainloop()
#-----------------------------------------------------------------------------------------
#buttons on the parent window    
bttn_new_task=Button(root,text="New Task",command=add_task,width=13).grid(row=0,column=0)
#bttn_new_task.pack()
bttn_del_task=Button(root,text="Delete",command=delete,width=13).grid(row=0,column=1)
#bttn_del_task.pack()
bttn_exit=Button(root,text="Exit window",command=exit,width=13).grid(row=0,column=2)
#bttn_exit.pack()
bttn_refresh=Button(root,text="REFRESH",command=refresh,width=15).grid(row=0,column=3)
#-----------------------------------------------------------------------------------------
#to display the NOTES 
cursor=conn.execute("select * from tasks;")

count=0
lb1=Listbox(root,selectmode=MULTIPLE,width=70,height=25)
for record in cursor:
    print(record)
    lb1.insert(count,"{}".format(record))
    count=count+1
    
lb1.grid(row=1,column=0,columnspan=6) 

root.mainloop()