from tkinter import *
from time import *

#time updater
def update():
    timeString = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeString)

    dayString = strftime("%A")
    dayLabel.config(text=dayString)

    dateString = strftime("%B %d, %Y")
    dateLabel.config(text=dateString)

    window.after(1000, update)

window = Tk()

timeLabel = Label(window, font=("Arial", 50), fg="red", bg="black")
timeLabel.pack()

dayLabel = Label(window, font=("Arial", 30))
dayLabel.pack()

dateLabel = Label(window, font=("Arial", 30))
dateLabel.pack()

update()


window.mainloop()