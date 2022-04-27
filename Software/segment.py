import cv2

"""
This file is used to perform segmentation on the target image.
"""


def get_threshold(img):
    """
    **Group defined function** \n
    This function performs Otsu thresholding to a given input image.\n
    :param img: A 3D array of the image.
    :return: The segmented image with the non-water pixels having the RGB values of (255, 255, 255).
    """
    row = img.shape[0]
    col = img.shape[1]

    bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh, ans = cv2.threshold(bw, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    for x in range(row):
        for y in range(col):
            if ans[x][y] == 255:
                img[x][y][:] = 255

    return img
