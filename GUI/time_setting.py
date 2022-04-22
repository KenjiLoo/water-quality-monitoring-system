from tkinter import *
from tkinter import ttk
import threading
import sys
from Software.cam import image_capture

sys.path.insert(0, 'SEGP9A/Software')


# -- FUNCTION DEFINITION --#

# change to the cropping page
def imageCroppingPage(tk):
    tk.destroy()
    import image_cropping
    image_cropping.main()

# change to the final page
def finalPage(tk):
    tk.destroy()
    import final_page
    final_page.main()

# facilitates the time interval setting
def timeInterval(tk, minute, second):
    min = int(minute.get())
    sec = int(second.get())
    interval = (min * 60) + sec
    global thread
    import Software.main
    Software.main.get_image()
    thread = threading.Thread(target=image_capture, args=(interval,), daemon=True)
    thread.start()
    finalPage(tk)

# stop the threading
def stopThread():
    global thread
    thread.join()

# get the minutes in the time interval function
def getMin(minute):
    minute.get()

# get the second in the time interval function
def getSec(second):
    second.get()

# main algorithm that's running in this page
def main():
    # --------------------------------------TOP BAR---------------------------------------------------
    # define window as GUI window, set minimum dimension
    window = Tk()
    window.title("Water Analysis Grp9A")
    window.configure(bg="white")
    window.minsize(855, 450)
    style = ttk.Style()
    style.configure("BW.TLabel", background="white")

    # set blue bar
    blue_bar_image = PhotoImage(file="Assets/blue_bar.png")
    blue_bar = Button(window, text="< Recrop",
                      compound=RIGHT,
                      image=blue_bar_image,
                      background="#81D3F9",
                      activeforeground="white",
                      activebackground="white",
                      borderwidth=0,
                      font=("Poppins", 10),
                      command=lambda: imageCroppingPage(window))
    blue_bar.pack(fill=BOTH)

    # --------------------------------------SET TIME INTERVAL---------------------------------------------------

    Label(window, text="", background="white").pack()
    Label(window, text="TIME INTERVAL", background="white", font=("Poppins", 10), ).pack()
    Label(window, text="Minimum: 10 seconds", background="white", font=("Poppins", 10), ).pack()
    Label(window, text="(minutes)", background="white", font=("Poppins", 10), ).pack()
    minute = StringVar(value=0)
    time_interval = Spinbox(window, from_=0, to=60, textvariable=minute, command=getMin(minute))
    time_interval.pack()
    Label(window, text="(seconds)", background="white", font=("Poppins", 10), ).pack()
    second = StringVar(value=0)
    time_interval_seconds = Spinbox(window, from_=0, to=59, textvariable=second, command=getSec(second))
    time_interval_seconds.pack()
    Label(window, text="", background="white").pack()
    set_button_image = PhotoImage(file="Assets/set_button.png")
    set_button = Button(window,
                        image=set_button_image,
                        background="white",
                        borderwidth=0,
                        activeforeground="white",
                        activebackground="white",
                        font=("Poppins", 10),
                        command=lambda: timeInterval(window, minute, second))
    set_button.pack()

    # to run the window
    window.mainloop()
