import cv2


# -- FUNCTION DEFINITION --#

# performs otsu thresholding
def get_threshold(img):
    row = img.shape[0]
    col = img.shape[1]

    bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh, ans = cv2.threshold(bw, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    for x in range(row):
        for y in range(col):
            if ans[x][y] == 255:
                img[x][y][:] = 255

    return img
