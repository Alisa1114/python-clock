import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import time

root = tk.Tk()
root.title("Python-Clock")
# root['width'] = root.winfo_screenwidth()
# root['height'] = root.winfo_screenheight()
root.geometry('1600x900')
root.configure(bg='black')
root.resizable(0, 0)


def tick():
    now = time.strftime('%H:%M:%S')
    clock.config(text=now)
    clock.after(200, tick)


def countdown():
    total_time = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(
        second.get())
    while total_time > -1:
        mins, secs = divmod(total_time, 60)
        hours, mins = divmod(mins, 60)
        hour.set(str(hours))
        minute.set(str(mins))
        second.set(str(secs))
        root.update()
        time.sleep(1)
        total_time -= 1
    messagebox.showinfo("Time Countdown", "Time's Up")


customed_style = ttk.Style()
customed_style.configure('Custom.TNotebook.Tab',
                         padding=[12, 12],
                         font=('Helvetica', 20))
notebook = ttk.Notebook(root, style='Custom.TNotebook')
clock_f = tk.Frame()
cntdown_timer_f = tk.Frame()

# clock
clock = tk.Label(clock_f,
                 text='00:00:00',
                 font=('Arial', 100, 'bold'),
                 fg='white',
                 bg='black')
clock.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
tick()

# countdown timer
hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()
hour.set("00")
minute.set("00")
second.set("00")
h_Entry = tk.Entry(cntdown_timer_f,
                   width=3,
                   font=("Arial", 50, ""),
                   textvariable=hour)
h_Entry.place(relx=0.5 - 0.1, rely=0.5, anchor=tk.CENTER)
m_Entry = tk.Entry(cntdown_timer_f,
                   width=3,
                   font=("Arial", 50, ""),
                   textvariable=minute)
m_Entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
s_Entry = tk.Entry(cntdown_timer_f,
                   width=3,
                   font=("Arial", 50, ""),
                   textvariable=second)
s_Entry.place(relx=0.5 + 0.1, rely=0.5, anchor=tk.CENTER)
start_btn = tk.Button(cntdown_timer_f,
                      text='Start',
                      font=('Arial', 20),
                      bd='5',
                      command=countdown)
start_btn.place(relx=0.5, rely=0.5 + 0.3, anchor=tk.CENTER)

notebook.add(clock_f, text='Clock')
notebook.add(cntdown_timer_f, text='Countdown Timer')
notebook.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()