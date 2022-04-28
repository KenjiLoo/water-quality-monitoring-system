from tkinter import *
from tkinter import ttk
import cv2
import sys
import os
from Software.cam import retake_image, crop_image

"""
This file is used to design and implement the functionalities of the cropping page in the GUI.
"""

sys.path.insert(0, 'SEGP9A/Software')
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


def timeSettingPage(tk):
    """
    **Group defined function** \n
    This function is used to destroy the current page and to open the time interval page.\n
    :param tk: Tkinter Object declared before function call, used in this function for destroy() method
    """
    tk.destroy()
    import GUI.time_setting as time_setting
    time_setting.main()


def retakeImage(tk):
    """
    **Group defined function** \n
    This function is used to open the camera page to retake an image.\n
    :param tk: Tkinter Object declared before function call, used in this function for destroy() method
    """
    retake_image()
    cameraPage(tk)


def start_crop(tk):
    """
    **Group defined function** \n
    This function is used to facilitate the cropping mechanism.\n
    :param tk: Tkinter Object declared before function call, used in this function for destroy() method
    """
    crop_image(x_top, y_top, x_bot, y_bot)
    os.chdir(dir)
    timeSettingPage(tk)


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
    window.geometry('1150x180')
    window.configure(bg="white")
    style = ttk.Style()
    style.configure("BW.TLabel", background="white")

    # set blue bar
    blue_bar_image = PhotoImage(file="Assets/blue_bar.png")
    blue_bar = Button(window, text="< Retake",
                      compound=RIGHT,
                      image=blue_bar_image,
                      background="#81D3F9",
                      activeforeground="white",
                      activebackground="white",
                      borderwidth=0,
                      font=("IBM Plex Sans", 10),
                      command=lambda: retakeImage(window))
    blue_bar.pack(fill=BOTH)

    # --------------------------------------CAMERA FRAME---------------------------------------------------
    Label(window, text="Cropping the Image", background="white", font=("Poppins", 16)).pack()
    Label(window, text="1. Using the mouse, draw a rectangle over the desired region", background="white",
          font=("Poppins", 10)).pack()
    Label(window, text="2. Press ENTER when completed", background="white", font=("Poppins", 10)).pack()
    Label(window, text="3. To reselect the region, draw a rectangle again", background="white", font=("Poppins", 10)).pack()

    def select_ROI(window):
        """
        **Group defined function** \n
        This is a function that gets the coordinates of the box drawn by the user on the image.\n
        :param window: a Tkinter Object 
        """
        global x_top, y_top, x_bot, y_bot

        os.chdir("../images")

        img = cv2.imread("0.jpg")
        dimension = cv2.selectROI("Crop Image", img)
        x_top = int(dimension[0])
        y_top = int(dimension[1])
        x_bot = x_top + int(dimension[2])
        y_bot = y_top + int(dimension[3])

        cv2.destroyWindow("Crop Image")
        start_crop(window)


    save_button_image = PhotoImage(file="Assets/save_button.png")
    save_button = Button(window,
                         image=save_button_image,
                         background="white",
                         activeforeground="white",
                         activebackground="white",
                         borderwidth=0,
                         command=lambda: select_ROI(window))
    save_button.pack()

    # runs the page
    window.mainloop()
