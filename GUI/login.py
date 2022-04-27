import webbrowser
import mysql.connector
from subprocess import call
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

"""
This file is used to design and implement the functionalities of the login page in the GUI.
"""


def mainPage(tk):
    """
    **Group defined function** \n
    This function is used to destroy the current page and to open the home/main page. \n
    :param tk: !!!
    """
    tk.destroy()
    import GUI.main_page as main_page
    main_page.main()


def callWeb():
    """
    **Group defined function** \n
    This function is used to open the web application.
    """
    webbrowser.open_new(r"local/webapp/index.php")


def Ok():
    """
    **Group defined function** \n
    This function contains the designs of the GUI (Buttons, Bars, Images, Window Dimension etc.)
    inclusive of its functionalities. Moreover, it includes the functionalities of the login system
    which is linked to the database.\n
    """
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hfyql1ju_segp")
    mycursor = mysqldb.cursor()
    username = username_login_entry.get()
    password = password__login_entry.get()

    sql = "select * from registration where username = %s and password = %s"
    mycursor.execute(sql, [(username), (password)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", "Login Success")
        window.destroy()
        call(["python", "GUI/main_page.py"])
        return True
    else:
        messagebox.showinfo("", "Incorrect Username and Password")
        return False

# --------------------------------------TOP BAR---------------------------------------------------
# define window as GUI window, set minimum dimension
window = Tk()
window.minsize(500, 350)
window.maxsize(1000, 550)
window.title("Water Analysis Grp9A")
window.configure(bg="white")
style = ttk.Style()
style.configure("BW.TLabel", background="white")

# empty space for arranging elements
empty = Label(window,
              text="                                                                                             ",
              background="white")
empty.grid(row=0, column=0)

# top bar with logo
logo = PhotoImage(file="GUI/Assets/Group 2.png")
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
logo2 = PhotoImage(file="GUI/Assets/logo 2.png")
right_logo = Label(window,
                   text="",
                   image=logo2,
                   compound=CENTER,
                   background="white")
right_logo.grid(row=0, column=3)

# --------------------------------------MAIN BUTTONS---------------------------------------------------
Label(window, text="Please enter login details", background="white", font=("Poppins", 10)).grid(row=1, column=1)
Label(window, text="", background="white").grid(row=2)
Label(window, text="Username", background="white", font=("Poppins", 10), ).grid(row=3, column=1)
username_login_entry = Entry(window, textvariable="username")
username_login_entry.grid(row=4, column=1)
Label(window, text="", background="white").grid(row=5, column=1)
Label(window, text="Password", background="white", font=("Poppins", 10)).grid(row=6, column=1)
password__login_entry = Entry(window, textvariable="password", show='*')
password__login_entry.grid(row=7, column=1)
Label(window, text="", background="white", font=("Poppins", 10)).grid(row=8, column=1)
login_button_image = PhotoImage(file="GUI/Assets/login_button.png")
login_button = Button(window,
                      image=login_button_image,
                      background="white",
                      borderwidth=0,
                      activeforeground="white",
                      activebackground="white",
                      font=("Poppins", 10),
                      command=lambda: Ok())
login_button.grid(row=9, column=1)

# to run this page
window.mainloop()
