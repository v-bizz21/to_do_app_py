#First attemp to to do list desktop app using tkinter
import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To do app")

def add_task():
    task = entry_tasks.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_tasks.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attenzione!", message = "Inserire attività")

def delete_task():
    try:
        #we need the index of the tasks
        task_index  = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Attenzione!", message = "Selezionare attività")

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Attenzione!", message = "file non trovato!")

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    print(tasks)
    pickle.dump(tasks, open("tasks.dat", "wb"))

#creating GUI

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height = 10, width = 50)
listbox_tasks.pack(side = tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side = tkinter.RIGHT, fill = tkinter.Y)

listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)
scrollbar_tasks.config(command = listbox_tasks.yview)

entry_tasks = tkinter.Entry(root, width = 50)
entry_tasks.pack()

button_add_tasks = tkinter.Button(root, text = "Add task", width = 48, command = add_task)
button_add_tasks.pack()

button_delete_tasks = tkinter.Button(root, text = "delete task", width = 48, command = delete_task)
button_delete_tasks.pack()

button_load_tasks = tkinter.Button(root, text = "load task", width = 48, command = load_task)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text = "Save task", width = 48, command = save_task)
button_save_tasks.pack()

root.mainloop()
