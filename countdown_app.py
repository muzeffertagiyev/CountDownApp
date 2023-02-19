from tkinter import *
import tkinter.messagebox as msgb
import time
from playsound import playsound


root = Tk()
root.title('Countdown Timer')
root.geometry("300x400")

do_tick = False

def countdown():
    try:
        start_time = time.time()
        times = int(hours.get())*3600 + int(minutes.get())*60 + int(seconds.get())
        if times > 0:
            while times > -1:
                minute, second = (times//60, times%60)

                hour = 0
                if minute > 60:
                    hour, minute = (minute // 60,minute % 60 )
                
                if hour < 10:
                    hour = f"0{hour}"
                if minute < 10 :
                    minute = f"0{minute}"
                if second < 10:
                    second = f"0{second}"

                seconds.set(second)
                minutes.set(minute)
                hours.set(hour)
                
                root.update()
                time.sleep(1)

                if times == 0:
                    playsound('time_is_out_bell.wav')
                    msgb.showinfo(title='Info', message="Time is out,set a new time")
                    hours.set('00')
                    minutes.set('00')
                    seconds.set('00')

                if do_tick:
                    elapsed_time = time.time() - start_time
                    times = int(times - elapsed_time)
                    break
                    
                times -= 1
        else:
            msgb.showwarning(title='Warning', message='Please add time')
    except:
        msgb.showwarning(title='Warning', message='Invalid input,please add only numbers')
    
def start():
    global do_tick
    do_tick = False
    countdown()

def stop():
    global do_tick
    do_tick = True

def reset():
    answer = msgb.askokcancel(title='Confirmation', message='Do you want to reset?')
    if answer:
        global do_tick
        do_tick = True
        hours.set("00")
        minutes.set("00")
        seconds.set("00")

heading = Label(root,text='Timer', font=("Courier 30 bold"),fg='#ea3548')
heading.pack()

def clock():
    text = 'Current time: '
    clock_time = time.strftime("%H:%M:%S %p")
    text += clock_time
    current_time.config(text=text)
    current_time.after(1000,clock)

current_time = Label(root,text="", bg='papaya whip')
current_time.pack(pady=20)
clock()

hours = StringVar()
Entry(root,textvariable=hours, width=2, font=("arial 50"),bd=4).place(x=30, y=270)
hours.set("00")
Label(root,text='Hours').place(x=30, y=350)

minutes = StringVar()
Entry(root,textvariable=minutes, width=2,font=("arial 50"), bd=4).place(x=110, y=270)
minutes.set("00")
Label(root,text='Minutes').place(x=110, y=350)

seconds = StringVar()
Entry(root,textvariable=seconds, width=2, font=("arial 50"), bd=4).place(x=190, y=270)
seconds.set("00")
Label(root,text="Seconds").place(x=190, y=350)

start_button = Button(root,text="Start",font=("Courier 20"),command=start)
start_button.pack()

stop_button = Button(root, text='Stop',font=("Courier 20"), command=stop)
stop_button.pack()

reset_button = Button(root, text='Reset',font=("Courier 20"), command=reset) 
reset_button.pack()

root.mainloop()
