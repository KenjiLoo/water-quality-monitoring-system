from collections import Counter
import pandas as pd

"""
This file is used to perform any operations regarding the colours of the image
such as RGB to HSV conversion and determining the most prominent colour.
"""


index = ["color", "color_name", "R", "G", "B"]
csv_file = pd.read_csv('../coloursfull.csv', names=index, header=None)


def getColorName(rgb):
    """
    **Adapted code from:** *https://data-flair.training/blogs/project-in-python-colour-detection/*\n
    This function is used to determine the name of the colour based on the RGB values through a minimum distance
    calculation with a csv file containing colour data.\n
    :param rgb: A tuple of RGB values.
    :return: The colour name.
    """
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


def list_colour(img):
    """
    **Group defined function** \n
    This function is used to get the two most occurring RGB values and get the respective colour names.\n
    :param img: A 3D array of the image.
    :return: A string representing the colour name.
    """
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


def get_colour(img):
    """
    **Group defined function** \n
    This function is used to get the most common RGB value in the image.\n
    :param img: A 3D array of the image.
    :return: A tuple of the most common RGB values.
    """
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


def declare_h(dif, div, max_value):
    """
    **Group defined function** \n
    This function is used to calculate the hue when converting from RGB to HSV.\n
    :param dif: The difference between the highest and lowest value in the RGB tuple.
    :param div: The RGB tuple.
    :param max_value: The highest value in the RGB tuple.
    :return: The hue.
    """
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


def declare_s(max_value, dif):
    """
    **Group defined function** \n
    This function is used to calculate the saturation when converting from RGB to HSV.\n
    :param max_value: The highest value in the RGB tuple.
    :param dif: The difference between the highest and lowest value in the RGB tuple.
    :return: The saturation.
    """
    if max_value == 0:
        return 0
    else:
        return (dif / max_value) * 100


def rgb2hsv(colour):
    """
    **Group defined function** \n
    This function is used to convert RGB values to HSV.\n
    :param colour: A tuple representing the colour's RGB values.
    :return: A tuple of the converted HSV values.
    """
    div = tuple(float(value) / 255 for value in colour)
    max_value = max(div)
    min_value = min(div)
    dif = max_value - min_value

    h = declare_h(dif, div, max_value)

    s = declare_s(max_value, dif)

    v = max_value * 100

    return (h, s, v)
