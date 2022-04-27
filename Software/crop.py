import cv2
import os

"""
This file is used to perform operations regarding the cropping on a target image.
"""

x_top = 0
y_top = 0
x_bot = 0
y_bot = 0


def cropping(x1, y1, x2, y2):
    """
    **Group defined function** \n
    This function is used to perform the cropping mechanism.\n
    :param x1: x coordinate of the top left corner of the crop box.
    :param y1: y coordinate of the top left corner of the crop box.
    :param x2: x coordinate of the bottom right corner of the crop box from the top left corner.
    :param y2: y coordinate of the bottom right corner of the crop box from the top left corner.
    :return: Cropped image.
    """
    global x_top, y_top, x_bot, y_bot

    os.chdir("../images")
    img = cv2.imread("0.jpg")

    x_top = x1
    y_top = y1
    x_bot = x2
    y_bot = y2

    cropped = img[y_top:y_bot, x_top:x_bot]

    return cropped


def recrop(img):
    """
    **Group defined function** \n
    This function is used to automatically crop the image based on the user's initial input.\n
    :param img: Target Image.
    :return: Cropped Image.
    """
    cropped = img[y_top:y_bot, x_top:x_bot]
    return cropped
