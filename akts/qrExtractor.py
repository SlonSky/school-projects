import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

def extract_QRs(photo):
    img = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # subtract the y-gradient from the x-gradient
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    gradient = cv2.morphologyEx(gradient, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    blurred = cv2.blur(gradient, (3, 3))
    (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    im2, cnts, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for i in range(len(cnts)):
        if len(cnts[i]) < 10:
            cv2.drawContours(thresh, cnts, i, (0, 0, 0), -1)
            continue

        if cv2.contourArea(cnts[i]) < 500:
            cv2.drawContours(thresh, cnts, i, (0, 0, 0), -1)
            continue

        (x, y), (MA, ma), angle = cv2.fitEllipse(cnts[i])
        ratio = max(MA, ma) / min(MA, ma)
        if ratio > 1.2:
            cv2.drawContours(thresh, cnts, i, (0, 0, 0), -1)

    QRs = []

    im2, cnts, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(cnts)):

        x, y, w, h = cv2.boundingRect(cnts[i])
        ratio = ((w * h * 1.0) / (width * height * 1.0))
        minArea = (width * height) * 0.1
        area = w * h

        if ratio < 0.95 and area > 8000 and area < minArea:
            # cv2.drawContours(thresh, cnts, i, (255, 255, 255), -1)
            # cv2.drawContours(img, cnts, i, (0,255,0), 2)
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
            # ims.append(img[y:y + h, x:x + w])

            # cut QR bounding rect from image
            QRs.append(img[y:y + h, x:x + w])
    return QRs

#########################################################3
def pause():
    while cv2.waitKey(10) != ord('q'):
        continue


cv2.namedWindow("picture", cv2.WINDOW_KEEPRATIO)

img = cv2.imread("input_d.jpg")

cv2.imshow("picture", img)

height, width = img.shape[:2]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

pause()

cv2.imshow("picture", gradient)

pause()

gradient = cv2.morphologyEx(gradient, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

cv2.imshow("picture", gradient)
pause()

blurred = cv2.blur(gradient, (3, 3))
(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

cv2.imshow("picture", thresh)
pause()

# while cv2.waitKey(10) != ord('q'):
#     continue

im2, cnts, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(cnts)):
    if len(cnts[i]) < 10:
        cv2.drawContours(thresh, cnts, i, (0, 0, 0), -1)
        continue

    if cv2.contourArea(cnts[i]) < 500:
        cv2.drawContours(thresh, cnts, i, (0, 0, 0), -1)
        continue

    (x, y), (MA, ma), angle = cv2.fitEllipse(cnts[i])
    ratio = max(MA, ma) / min(MA, ma)
    if ratio > 1.2:
        cv2.drawContours(thresh, cnts, i, (0, 0, 0), -1)

cv2.imshow("picture", thresh)
pause()

im2, cnts, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

ims = []
for i in range(len(cnts)):

    x, y, w, h = cv2.boundingRect(cnts[i])
    ratio = ((w * h * 1.0) / (width * height * 1.0))
    minArea = (width * height) * 0.1
    area = w * h  # cv2.contourArea(cnts[i])

    if ratio < 0.95 and area > 8000 and area < minArea:
        cv2.drawContours(thresh, cnts, i, (255, 255, 255), -1)
        # cv2.drawContours(img, cnts, i, (0,255,0), 2)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

        ims.append(img[y:y + h, x:x + w])

cv2.imshow("picture", img)
for i in range(len(ims)):
    cv2.imwrite("qr" + str(i) + ".jpg", ims[i])

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
