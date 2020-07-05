from tkinter import *
import time
root = Tk()
def tick():
    time2 = time.strftime('%H:%M:%S')
    clock.config(text=time2)
    clock.after(200,tick)
clock=Label(root,font=('Digital Clock',100,'bold'),bg = 'blue')
clock.pack(fill =BOTH,expand=1)
tick()
root.mainloop()