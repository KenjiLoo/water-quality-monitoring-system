import cv2
from datetime import datetime
import Software.colour
import Software.cam
import numpy as np
import os
import mysql.connector
from tkinter import messagebox

# -- FUNCTION DEFINITION --#

# gets the latest image from the image folder
def get_latest_image(dirpath, valid_extensions=('jpg','jpeg','png')):
    """
    Get the latest image file in the given directory
    """

    # get filepaths of all files and dirs in the given dir
    valid_files = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    # filter out directories, no-extension, and wrong extension files
    valid_files = [f for f in valid_files if '.' in f and \
        f.rsplit('.',1)[-1] in valid_extensions and os.path.isfile(f)]

    if not valid_files:
        raise ValueError("No valid images in %s" % dirpath)

    return max(valid_files, key=os.path.getmtime)

# converts the image to binary data to be posted as a BLOB
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

# background removal
def remove_background(img):
    row = img.shape[0]
    col = img.shape[1]
    size = row * col

    h = img[:, :, 0].ravel()
    s = img[:, :, 1].ravel()
    v = img[:, :, 2].ravel()

    output1 = [idx for idx, element in enumerate(h) if element == 0]
    output2 = [idx for idx, element in enumerate(s) if element == 0]
    output3 = [idx for idx, element in enumerate(v) if element == 255]

    h_set = set(output1)
    s_set = set(output2)
    c_set = set(output3)

    if (h_set & s_set & c_set):
        index = h_set & s_set & c_set
        count = len(index)
    else:
        print("No common elements")

    img = np.reshape(img, (size, 3))

    result = np.zeros([(size - count), 3])
    y = 0
    for x in range(size):
        if x in index:
            continue
        else:
            result[y, 0] = img[x, 0]
            result[y, 1] = img[x, 1]
            result[y, 2] = img[x, 2]
            y += 1

    new_size = int((size - count) ** 0.5)
    remainder = (size - count) % (new_size * new_size)
    if (remainder != 0):
        new_size += 1
        remainder = new_size ** 2 - (size - count)
        result.resize((new_size * new_size, 3))
        rgb = Software.colour.get_colour(img)
        val = Software.colour.rgb2hsv(rgb)
        for x in range(remainder):
            result[y, 0] = val[0]
            result[y, 1] = val[1]
            result[y, 2] = val[2]
            y += 1
    result = np.reshape(result, (new_size, new_size, 3))
    result = result.astype(int)
    cv2.imwrite("hist.png", result)
    result = cv2.imread("hist.png")
    return result

# compares the new image to the first image
def comparison(img2):
    global img1
    img1_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    img1_hsv = remove_background(img1_hsv)
    img2_hsv = remove_background(img2_hsv)

    hist_img1 = cv2.calcHist([img1_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_img2 = cv2.calcHist([img2_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    bhatta = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_BHATTACHARYYA)

    now = datetime.now()
    dt_object = now.strftime("%d-%m-%Y %H:%M:%S")
    percentage = round(bhatta * 100, 2)
    print('----------------------------------')
    print('RESULTS AS OF:', dt_object)
    print('Changes from the initial sample is', percentage, '%')

    return bhatta

# reads the rgb value of the background
def rgb_background(img):
    row = img.shape[0]
    col = img.shape[1]
    size = row * col

    b = img[:, :, 0].ravel()
    g = img[:, :, 1].ravel()
    r = img[:, :, 2].ravel()

    output1 = [idx for idx, element in enumerate(b) if element == 255]
    output2 = [idx for idx, element in enumerate(g) if element == 255]
    output3 = [idx for idx, element in enumerate(r) if element == 255]

    b_set = set(output1)
    g_set = set(output2)
    r_set = set(output3)

    if (b_set & g_set & r_set):
        index = b_set & g_set & r_set
        count = len(index)
    else:
        print("No common elements")

    img = np.reshape(img, (size, 3))

    result = np.zeros([(size - count), 3])
    y = 0
    for x in range(size):
        if x in index:
            continue
        else:
            result[y, 0] = img[x, 0]
            result[y, 1] = img[x, 1]
            result[y, 2] = img[x, 2]
            y += 1

    new_size = int((size - count) ** 0.5)
    remainder = (size - count) % (new_size * new_size)
    if (remainder != 0):
        new_size += 1
        remainder = new_size ** 2 - (size - count)
        result.resize((new_size * new_size, 3))
        rgb = Software.colour.get_colour(img)
        val = (rgb[2], rgb[1], rgb[0])
        for x in range(remainder):
            result[y, 0] = val[0]
            result[y, 1] = val[1]
            result[y, 2] = val[2]
            y += 1
    result = np.reshape(result, (new_size, new_size, 3))
    result = result.astype(int)
    cv2.imwrite("rgb.png", result)
    result = cv2.imread("rgb.png")
    return result

# opens camera and capture image
def get_image():
    global img1
    img1 = Software.cam.get_image()

# starts the image processing algorithm
def start_program(img2):
    global img1
    bhatta = comparison(img2)
    if bhatta >= threshold:
        print("Water is dirty")
    else:
        print("Water is clean")

    colour_img = rgb_background(img2)
    color = Software.colour.list_colour(colour_img)
    img1 = img2

    # mysql connection
    img_path = "../images"
    percentage = round(bhatta * 100, 2)
    image_non_bin = get_latest_image(img_path)
    image = convertToBinaryData(image_non_bin)

    similarity_percentage = percentage
    colour = color

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hfyql1ju_csv_db_7")
    mycursor = mysqldb.cursor()

    #GET LATEST ID AND POST AN INCREMENT
    sql_select_Query = "select id from results"
    mycursor.execute(sql_select_Query)
    get_id = mycursor.fetchall()

    id_list = []
    for row in get_id:
        for i in row:
            id_list.append(str(i)[0])
    id = int(id_list[-1]) + 1

    try:
        sql = "INSERT INTO results(id, difference_percentage, colour,image) VALUES (%s, %s, %s, %s)"
        val = (id, similarity_percentage, colour, image)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "pushed to database")
    except Exception as e:
        print(e)
        print("failed pushing")
        mysqldb.rollback()
        mysqldb.close()

threshold = 0.568
img1 = []
