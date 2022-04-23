import webbrowser
from tkinter import *
from tkinter import ttk
import os
import mysql.connector
import time_setting
from Software.cam import delete_images

dir = "../GUI"

# -- FUNCTION DEFINITION --#

# opens the homepage
def homePage(tk):
    tk.destroy()
    import main_page
    main_page.main()

# opens the camera page
def cameraPage(tk):
    tk.destroy()
    import camera
    camera.main()

# opens the web app
def callWeb():
    webbrowser.open_new(r"localhost/webapp/index.php")

# to terminate the program
def stopProgram(tk):
    print('----------------------------------')
    print("Software is terminating...")
    delete_images()
    time_setting.stopThread()
    print("Software has terminated")
    homePage(tk)

# the main algorithm that runs in this page
def main():
    # --------------------------------------TOP BAR---------------------------------------------------
    # define window as GUI window, set minimum dimension
    window = Tk()
    window.minsize(850, 450)
    window.maxsize(1000, 550)
    window.title("Water Analysis Grp9A")
    window.configure(bg="white")
    style = ttk.Style()
    style.configure("BW.TLabel", background="white")

    # set blue bar
    os.chdir(dir)
    blue_bar_image = PhotoImage(file="Assets/blue_bar.png")
    blue_bar = Button(window,
                      text="",
                      compound=RIGHT,
                      image=blue_bar_image,
                      background="#81D3F9",
                      activeforeground="white",
                      activebackground="white",
                      borderwidth=0,
                      font=("Poppins", 10),
                      command=lambda: cameraPage(window))
    blue_bar.grid(row=0, columnspan=4)

    # --------------------------------------WORDS---------------------------------------------------
    # success wording
    success_image = PhotoImage(file="Assets/success_wording.png")
    success = Label(window, image=success_image, background="white")
    success.grid(row=1, column=0, pady=(100, 10))

    # id display
    # GET LATEST ID AND POST AN INCREMENT
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hfyql1ju_csv_db_7")
    mycursor = mysqldb.cursor()
    sql_select_Query = "select id from results"
    mycursor.execute(sql_select_Query)
    get_id = mycursor.fetchall()

    id_list = []
    for row in get_id:
        for i in row:
            id_list.append(str(i)[0])
    id_val = int(id_list[-1]) + 1

    disp_string = "ID: "
    id_string = disp_string + str(id_val)
    id = Label(window,
               text=id_string,
               compound=CENTER,
               font=("Arial", 20),
               background="white")
    id.grid(row=2, column=0)

    # --------------------------------------BUTTONS---------------------------------------------------
    # empty space
    empty = Label(window, text="", background="white")
    empty.grid(row=3)
    empty2 = Label(window, text="", background="white")
    empty2.grid(row=4)
    empty3 = Label(window, text="", background="white")
    empty3.grid(row=5)

    # button 1
    button1_image = PhotoImage(file="Assets/button1_4.png")
    button1 = Button(window,
                     image=button1_image,
                     background="white",
                     activeforeground="white",
                     activebackground="white",
                     borderwidth=0,
                     command=lambda: callWeb())
    button1.grid(row=6, column=0)


    # button 3
    button3_image = PhotoImage(file="Assets/button2_5.png")
    button3 = Button(window,
                     image=button3_image,
                     background="white",
                     activeforeground="white",
                     activebackground="white",
                     borderwidth=0,
                     command=lambda: stopProgram(window))
    button3.grid(row=6, column=2)

    # to run the window
    window.mainloop()
