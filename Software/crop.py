import cv2
import os

x_top = 0
y_top = 0
x_bot = 0
y_bot = 0

# -- FUNCTION DEFINITION --#


# cropping mechanism
def cropping(x1, y1, x2, y2):
    global x_top, y_top, x_bot, y_bot

    os.chdir("../images")
    # insert while loop to change crop image
    img = cv2.imread("0.jpg")
    x_top = x1
    y_top = y1
    x_bot = x2
    y_bot = y2

    cropped = img[y_top:y_bot, x_top:x_bot]

    return cropped


# recropping mechanism
def recrop(img):
    cropped = img[y_top:y_bot, x_top:x_bot]
    return cropped
