import time
import cv2
from cv2.cv2 import VideoCapture
import os

import Software.main_algo
import Software.segment
import Software.crop

img_path = "../images"
thresh_path = "../thresh"


# Captures the image when the user presses the button
def first_image():
    os.chdir(img_path)
    cam = VideoCapture(0, cv2.CAP_DSHOW)
    cv2.destroyAllWindows()
    success, image = cam.read()
    if (success):
        cv2.imwrite("0.jpg", image)
    else:
        print("error")


# to retake image
def retake_image():
    os.chdir(img_path)
    for file in os.listdir(img_path):
        os.remove(file)


# to crop image
def crop_image(x1, y1, x2, y2):
    global run
    img = Software.crop.cropping(x1, y1, x2, y2)
    thresh = Software.segment.get_threshold(img)
    os.chdir(thresh_path)
    cv2.imwrite("0_thresh.jpg", thresh)
    run = True


# to get the first image
def get_image():
    os.chdir(thresh_path)
    img = cv2.imread("0_thresh.jpg")
    return img


# to capture image every interval
def image_capture(interval):
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


# deletes the images in the folder after the observation is stopped
def delete_images():
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

