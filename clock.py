import tkinter as tk
import time 

# test git
def main():
    def tick():
        now = time.strftime('%H:%M:%S')
        label.config(text=now)
        label.after(200, tick)
        
    window = tk.Tk()
    window.title("Python-Clock")
    window['width'] = window.winfo_screenwidth()
    window['height'] = window.winfo_screenheight()

    window.configure(bg='black')
    window.resizable(0, 0)
    
    label = tk.Label(window, text='00:00:00', font=('Arial', 250, 'bold'), fg='white', bg='black')
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    tick()
    
    window.mainloop()

if __name__ == "__main__":
    main()