import webbrowser
from tkinter import *
from tkinter import ttk
import os
import argparse

"""
This file is used to design and implement the functionalities of the main page in the GUI.
"""


dir = os.path.dirname(os.path.abspath(__file__))


def cameraPage(tk):
    """
    **Group defined function** \n
    This function is used to destroy the current page and to open the camera page.\n
    :param tk: Tkinter Object declared before function call, used in this function for destroy() method
    """
    tk.destroy()
    import GUI.camera as camera
    camera.main()


def callWeb():
    """
    **Group defined function** \n
    This function is used to open the web application.\n
    """
    webbrowser.open_new(r"localhost/WebApp/index.php")


def main():
    """
    **Group defined function** \n
    This function contains the designs of the GUI (Buttons, Bars, Images, Window Dimension etc.)
    inclusive of its functionalities.\n
    """
    # --------------------------------------TOP BAR---------------------------------------------------
    # define window as GUI window, set minimum dimension
    os.chdir(dir)

    window = Tk()
    window.minsize(850, 400)

    window.title("Water Analysis Grp9A")
    window.configure(bg="white")
    style = ttk.Style()
    style.configure("BW.TLabel", background="white")

    # empty space for arranging elements
    empty = Label(window,
                  text="                                                                                                         ",
                  background="white")
    empty.grid(row=0, column=0)

    # top bar with logo
    logo = PhotoImage(file="Assets/Group 2.png")
    title_logo = Label(window,
                       text="",
                       image=logo,
                       compound=CENTER,
                       background="white")
    title_logo.grid(row=0, column=1)

    # empty space between title logo and the app logo
    empty2 = Label(window, text="                                                                          ",
                   background="white")
    empty2.grid(row=0, column=2)

    # top bar right side logo
    logo2 = PhotoImage(file="Assets/logo 2.png")
    right_logo = Label(window,
                       text="",
                       image=logo2,
                       compound=CENTER,
                       background="white")
    right_logo.grid(row=0, column=3)

    # --------------------------------------MAIN BUTTONS---------------------------------------------------
    # button 1
    button1_image = PhotoImage(file="Assets/button1.png")
    button1 = Button(window,
                     image=button1_image,
                     background="white",
                     borderwidth=0,
                     activeforeground="white",
                     activebackground="white",
                     command=lambda: callWeb())
    button1.grid(row=1, column=0)

    # button 2
    button2_image = PhotoImage(file="Assets/button2.png")
    button2 = Button(window,
                     image=button2_image,
                     background="white",
                     borderwidth=0,
                     activeforeground="white",
                     activebackground="white",
                     command=lambda: cameraPage(window))
    button2.grid(row=1, column=1)

    # button 3
    button3_image = PhotoImage(file="Assets/button3.png")
    button3 = Button(window,
                     image=button3_image,
                     background="white",
                     borderwidth=0,
                     activeforeground="white",
                     activebackground="white",
                     command=lambda: callWeb())
    button3.grid(row=1, column=2)

    # to run the window
    window.mainloop()


main()
