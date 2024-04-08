import cv2
import numpy as np
def pause():
  while cv2.waitKey(10) != ord('q'):
    continue

###############################
def extract_workspace(markerTop, markerBottom, image):
    #######
    #    m# <- top marker
    #     #
    #m    # <- bottom marker
    #######
    top_rect = get_marker_rect(markerTop, image)
    bottom_rect = get_marker_rect(markerBottom, image)

    if (top_rect or bottom_rect) is False:
        return False


    res = image.copy()
    res = cv2.cvtColor(res, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(res, (top_rect['top_left']['x'],top_rect['top_left']['y']), (top_rect['bottom_right']['x'],top_rect['bottom_right']['y']), (0, 255, 0), 3)
    cv2.rectangle(res, (bottom_rect['top_left']['x'], bottom_rect['top_left']['y']),(bottom_rect['bottom_right']['x'], bottom_rect['bottom_right']['y']), (0, 255, 0), 3)
    cv2.imwrite("demo/sift.jpg", res)

    top_left = {
        'x': bottom_rect['top_left']['x'],
        'y': top_rect['bottom_right']['y']
    }

    bottom_right = {
        'x': top_rect['bottom_right']['x'],
        'y': bottom_rect['top_left']['y']
    }

    # return top_left, bottom_right
    return image[top_left['y']:bottom_right['y'], top_left['x']:bottom_right['x']]

def get_marker_rect(marker, image):

    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(marker, None)
    kp2, des2 = sift.detectAndCompute(image.copy(), None)

    # find matches
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    MIN_MATCH_COUNT = 10
    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        h, w = marker.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)

        # top left point
        x1 = int(dst[0][0][0])
        y1 = int(dst[0][0][1])

        # bottom right point
        x2 = int(dst[2][0][0])
        y2 = int(dst[2][0][1])

        return {'top_left': {'x': x1, 'y': y1}, 'bottom_right': {'x': x2, 'y': y2}}
    else:
        return False
#########################################
def extract_QRs(img):
    height, width = img.shape[:2]

    gray = img.copy()#cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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

        if cv2.contourArea(cnts[i]) < (width * height) / 10119.168:
            cv2.drawContours(thresh, cnts, i, (0, 0, 0), -1)
            continue

        (x, y), (MA, ma), angle = cv2.fitEllipse(cnts[i])
        ratio = max(MA, ma) / min(MA, ma)
        if ratio > 2:
            cv2.drawContours(thresh, cnts, i, (0, 0, 0), -1)

    im2, cnts, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    QRBounds = []
    QRImages = []

    for i in range(len(cnts)):

        x, y, w, h = cv2.boundingRect(cnts[i])
        ratio = ((w * h * 1.0) / (width * height * 1.0))
        minArea = (width * height) * 0.1
        area = w * h  # cv2.contourArea(cnts[i])

        if ratio < 0.95 and area > (width * height) / 632.4 and area < minArea:
            cv2.drawContours(thresh, cnts, i, (255, 255, 255), -1)
            # cv2.drawContours(img, cnts, i, (0,255,0), 2)

            cv2.rectangle(res, (x, y), (x + w, y + h), (0, 255, 0), 3)

            QRBounds.append([x+2,y+2,w-2,h-2])
            QRImages.append(img[y+2:y + h-2, x+2:x + w - 2])
    cv2.imshow("picture", cv2.cvtColor(img, cv2.COLOR_GRAY2BGR))
    return QRBounds, QRImages

def rescale(img):
    NOMINAL_WIDTH = 1000
    size = img.shape[:2]
    scale = size[0] / NOMINAL_WIDTH
    return cv2.resize(img, (int(size[1] / scale), int(size[0] / scale)))
#########################################3
def extract_answers(QRs, photo):
    segments = []
    for i in range(1,len(QRs)):
        previous = QRs[i-1]
        current = QRs[i]

        segments.append(photo[
            (previous[1] + previous[3]):current[1],
             current[0]:(current[0]+current[2])])
        if i == len(QRs)-1:
            photoSize = photo.shape[:2]
            segments.append(photo[
                            (current[1] + current[3]):photoSize[0],
                            current[0]:(current[0] + current[2])])

    # cv2.imshow("segments", photo)

    return segments

# todo : numerate qrs for question

def find_answers(segments):
    ansNums = []
    for img in segments:
        height, width = img.shape[:2]
        _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        im2, contours, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rects = []
        for i in range(len(contours)):

            # remove small pieces
          if(cv2.contourArea(contours[i]) < 0.01 * width* height):
            cv2.drawContours(thresh, contours, i, (0, 0, 0), -1)
          else:
            x,y,w,h = cv2.boundingRect(contours[i])
            rects.append([x,y,w,h])

        rects.sort(key=lambda x: x[1])
        index = -1
        maxColor = 0
        for i in range(len(rects)):
            x, y, w, h = tuple(rects[i])
            aver = np.average(thresh[y:y + h, x:x + w]) # mean color
            if aver > 0.3 * 255 and aver > maxColor:
                maxColor = aver
                index = i
        ansNums.append(index)
    return ansNums

markerTop = cv2.imread('topRight.jpg',0)
markerBottom = cv2.imread('bottomLeft.jpg',0)
photo = cv2.imread('input/6.jpg',0) # trainImage
# photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("picture")
photo = rescale(photo)
print("Scaled.")
work_space = extract_workspace(markerTop, markerBottom, photo)

answers = []
if work_space is not False:
    print("Workspace found.")
    QRbounds, QRimages = extract_QRs(work_space)
    QRbounds.sort(key=lambda x:x[1]) # sort from top to bottom
    print("QRs are ready.")
    answers = extract_answers(QRbounds, work_space)
    print("Answers cut")
    answersNums = find_answers(answers)

    for i in range(len(answers)):
        print(str(i + 1) + "st question answer #" + str(answersNums[i] + 1))

    # CONGRATS!
    # Results are:
    # QRimages
    # answerNums
else: print("Workspace not found.")

pause()
