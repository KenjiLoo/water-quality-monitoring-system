from tkinter import *
from tkinter import ttk
import threading
import sys
from Software.cam import image_capture

"""
This file is used to design and implement the functionalities of the time interval page in the GUI.
"""

sys.path.insert(0, 'SEGP9A/Software')
global thread


def imageCroppingPage(tk):
    """
    **Group defined function** \n
    This function is used to destroy the current page and to open the image cropping page.\n
    :param tk: !!!
    """
    tk.destroy()
    import GUI.image_cropping as image_cropping
    image_cropping.main()


def finalPage(tk):
    """
    **Group defined function** \n
    This function is used to destroy the current page and to open the final page.\n
    :param tk: !!!
    """
    tk.destroy()
    import GUI.final_page as final_page
    final_page.main()


def timeInterval(tk, minute, second):
    """
    **Group defined function** \n
    This function is used to facilitate the time interval settings.\n
    :param tk: !!!
    :param minute: A numerical value representing the minutes of the time interval.
    :param second: A numerical value representing the seconds of the time interval.
    """
    min = int(minute.get())
    sec = int(second.get())
    interval = (min * 60) + sec
    global thread
    import Software.main_algo
    Software.main_algo.get_image()
    thread = threading.Thread(target=image_capture, args=(interval,), daemon=True)
    thread.start()
    finalPage(tk)


def stopThread():
    """
    **Group defined function** \n
    This function is used to stop the threading.\n
    """
    global thread
    thread.join()


def getMin(minute):
    """
    **Group defined function** \n
    This function is used to get the value in the "Minutes" textbox.\n
    :param minute: A string variable of the minutes of the time interval.
    """
    minute.get()


def getSec(second):
    """
    **Group defined function** \n
    This function is used to get the value in the "Seconds" textbox.\n
    :param second: A string variable of the seconds of the time interval.
    """
    second.get()


def main():
    """
    **Group defined function** \n
    This function contains the designs of the GUI (Buttons, Bars, Images, Window Dimension etc.)
    inclusive of its functionalities.\n
    """
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
