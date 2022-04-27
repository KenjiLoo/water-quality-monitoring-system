import webbrowser
from tkinter import *
from tkinter import ttk
import os
import mysql.connector
import GUI.time_setting as time_setting
from Software.cam import delete_images

"""
This file is used to design and implement the functionalities of the final page in the GUI.
"""

dir = os.path.dirname(os.path.abspath(__file__))


def homePage(tk):
    """
    **Group defined function** \n
    This function destroys the current window and opens the home/main page.\n
    :param tk: Tkinter Object declared before function call, used in this function for destroy() method
    """
    tk.destroy()
    import GUI.main_page as main_page
    main_page.main()


def cameraPage(tk):
    """
    **Group defined function** \n
    This function destroys the current window and opens the camera page.\n
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


def stopProgram(tk):
    """
    **Group defined function** \n
    This function is used to terminate the program where it stops all threads, delete past images
    and returns to the home page.\n
    :param tk: Tkinter Object declared before function call, used in this function for destroy() method
    """
    print('----------------------------------')
    print("Software is terminating...")
    delete_images()
    time_setting.stopThread()
    print("Software has terminated")
    homePage(tk)


def main():
    """
    **Group defined function** \n
    This function contains the designs of the GUI (Buttons, Bars, Images, Window Dimension etc.)
    inclusive of its functionalities.\n
    """
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
            # if str(i)[1] == '':
            id_list.append(str(i)[0])
            # else:
            #     id_list.append((str(i)[0])+(str(i)[1]))

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
