## Alarm Clock Maker ###

## Importing all the Necessary Libraries and Modules

from tkinter import *
import datetime 
import time
import winsound

# Tkinter module belongs to a standard library of GUI in Python.--
# It helps us to create a dialog box with any information that we want to provide or get from the users.

# Datetime and time modules in python help us to work 
# with the dates and time of the current day when the user is operating python and to manipulate it too.

# Winsound module provides access to the basic sound playing machinery provided by Windows platforms. 
# This is useful to generate the sound immediately when a function is called.

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        #Get the current time using current_time which takes the argument of datetime.datetime.now()
        current_time = datetime.datetime.now()
        #now is used to print the time and date is used to print the current date by string conversion using strftime().
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break
## Define another function here named actual_time() which takes in the user value for setting the alarm in the string format. The same 
# argument of (set_alarm_timer) as alarm before to execute the while loop which we further use while making GUI
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
## If loop suggests that if the user input time set_alarm_timer matches with the while loop ongoing time now,
#  the message is printed as” Time to Wake up”.

clock = Tk()
# To Initialize tkinter, we pass a command under the name clock as Tk()
clock.title("Alarm Clock for Kamlesh ")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
## The second heading is given above the user input boxes for the labeling to be “Hour Min Sec” using addTime
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
#Just to make the dialog box look funkier, adding another label as “when to wake you up” using setYourAlarm.
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)


#Finally make the input boxes such as hourTime, minTime, and secTime which takes the entry of the time the user wants to set the alarm on in 24-hour format.
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)


##Clock.mainloop() is the basic and the last command was given to compile all the previous commands with their basic settings of color, font, width, axis, etc. and displays the window as soon as the program is run
clock.mainloop()
#Execution of the window.