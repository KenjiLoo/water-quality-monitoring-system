from collections import Counter
import pandas as pd
import cv2
import numpy as np

index = ["color", "color_name", "R", "G", "B"]
csv_file = pd.read_csv('../coloursfull.csv', names=index, header=None)

# -- FUNCTION DEFINITION --#

# function to calculate minimum distance from all colors and get the most matching color
def getColorName(rgb):
    R = rgb[0]
    G = rgb[1]
    B = rgb[2]
    minimum = 10000

    for i in range(len(csv_file)):
        d = abs(R - int(csv_file.loc[i, "R"])) + abs(G - int(csv_file.loc[i, "G"])) + abs(B - int(csv_file.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            cname = csv_file.loc[i, "color_name"]

    return cname


# gets the names of the two most common colours
def list_colour(img):
    name = []
    rgb_number = []

    (row, col, dim) = img.shape
    for x in range(row):
        for y in range(col):
            R = img[x][y][2]
            G = img[x][y][1]
            B = img[x][y][0]

            rgb_number.append((R, G, B))

    rgb_common = Counter(rgb_number).most_common(2)
    name.append(getColorName(rgb_common[0][0]))
    name.append(getColorName(rgb_common[1][0]))
    print("Colours are:")
    print('-', name[0])
    if name[0] != name[1]:
        print('-', name[1])

    string = ' '.join([str(item) for item in name])
    return string


# gets the most common RGB value
def get_colour(img):
    rgb_number = []

    (size, dim) = img.shape
    for x in range(size):
        if img[x][2] != 255 & img[x][1] != 255 & img[x][0] != 255:
            R = img[x][2]
            G = img[x][1]
            B = img[x][0]
            rgb_number.append((R, G, B))

    rgb_common = Counter(rgb_number).most_common(1)
    return rgb_common[0][0]


# calculates H value
def declare_h(dif, div, max_value):
    if dif == 0:
        return 0
    elif max_value == div[2]:
        return (((div[1] - div[0]) / dif) * 60 + 360) % 360
    elif max_value == div[1]:
        return (((div[0] - div[2]) / dif) * 60 + 120) % 360
    elif max_value == div[0]:
        return (((div[2] - div[1]) / dif) * 60 + 240) % 360
    else:
        pass
        # error


# calculates S value
def declare_s(max_value, dif):
    if max_value == 0:
        return 0
    else:
        return (dif / max_value) * 100


# converts rgb values to hsv
def rgb2hsv(colour):
    div = tuple(float(value) / 255 for value in colour)
    max_value = max(div)
    min_value = min(div)
    dif = max_value - min_value

    # getting H value (It is supposed to be a function)
    h = declare_h(dif, div, max_value)

    # getting S value
    s = declare_s(max_value, dif)

    # checking the colours
    v = max_value * 100

    return (h, s, v)
