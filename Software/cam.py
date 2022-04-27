import time
import cv2
from cv2.cv2 import VideoCapture
import os

import Software.main_algo
import Software.segment
import Software.crop

"""
This file is used for the operations of the webcam and image acquisition.
"""

img_path = "../images"
thresh_path = "../thresh"


def first_image():
    """
    **Group defined function** \n
    This function is used to capture the first image when the user presses the button.
    """
    os.chdir(img_path)
    cam = VideoCapture(0, cv2.CAP_DSHOW)
    cv2.destroyAllWindows()
    success, image = cam.read()
    if (success):
        cv2.imwrite("0.jpg", image)
    else:
        print("error")


def retake_image():
    """
    **Group defined function** \n
    This is a function that will delete the first image taken by the user.
    """
    os.chdir(img_path)
    for file in os.listdir(img_path):
        os.remove(file)


def crop_image(x1, y1, x2, y2):
    """
    **Group defined function** \n
    This function is used to crop an image and perform Otsu thresholding. \n
    :param x1: x coordinate of the top left corner of the crop box.
    :param y1: y coordinate of the top left corner of the crop box.
    :param x2: x coordinate of the bottom right corner of the crop box from the top left corner.
    :param y2: y coordinate of the bottom right corner of the crop box from the top left corner.
    """
    global run
    img = Software.crop.cropping(x1, y1, x2, y2)
    thresh = Software.segment.get_threshold(img)
    os.chdir(thresh_path)
    cv2.imwrite("0_thresh.jpg", thresh)
    run = True


def get_image():
    """
    **Group defined function** \n
    This function is used to read the first image after segmentation.\n
    :return: 3D array of the first image.
    """
    os.chdir(thresh_path)
    img = cv2.imread("0_thresh.jpg")
    return img


def image_capture(interval):
    """
    **Group defined function** \n
    This function is used to capture an image at every time interval.\n
    :param interval: An integer value representing the time interval to take an image.
    """
    global run
    os.chdir(img_path)
    name = 1
    interval = int(interval)
    time.sleep(interval)
    cam = VideoCapture(0, cv2.CAP_DSHOW)
    cv2.destroyAllWindows()
    while run:
        elapsed = 0
        success, image = cam.read()
        start = time.time()
        if success:
            os.chdir(img_path)
            cv2.imwrite(str(name) + ".jpg", image)
            img = cv2.imread(str(name) + ".jpg")
            img = Software.crop.recrop(img)
            thresh = Software.segment.get_threshold(img)
            os.chdir(thresh_path)
            cv2.imwrite(str(name) + "_thresh.jpg", thresh)
            var = cv2.imread(str(name) + "_thresh.jpg")
            Software.main_algo.start_program(var)
        else:
            print("error")
        while (elapsed < interval) and run:
            elapsed = time.time() - start
        name = name + 1


def delete_images():
    """
    **Group defined function** \n
    This function is used to delete the images in the folder after the observation is stopped.
    """
    global run
    run = False
    global img_path
    global thresh_path
    os.chdir(img_path)
    for file in os.listdir(img_path):
        os.remove(file)
    os.chdir(thresh_path)
    for file in os.listdir(thresh_path):
        os.remove(file)

