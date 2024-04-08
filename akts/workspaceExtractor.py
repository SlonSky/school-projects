"""
    Function extracts workspace of tests photo
    by given marker sample and photo (both are cv2 images).

    1. Detection:
        1.1 Create SIFT detector
        1.2 Detect features on the marker and photo
    2. Matching:
        2.1 Create BF matcher
        2.2 Find matches between marker and photo
    3. Clustering:
        ???
        3.2 Make clusters for every marker on photo,
            remove other wrong features
    4. Extraction:
        4.1 Bound clusters with shape (rect, ellipse, etc.)
        4.2 Find required bound points (for top markers
            on photo - bottom bound, for bottom markers
            - top)
        4.3 Make sub-image from photo based on found bounds.
"""

import cv2
import numpy as np
def extract_workspace(markerTop, markerBottom, photo):
    #######
    #    m# <- top marker
    #     #
    #m    # <- bottom marker
    #######
    top_rect = get_marker_rect(markerTop, photo)
    bottom_rect = get_marker_rect(markerBottom, photo)

    if top_rect and bottom_rect is False:
        return False

    top_left = {
        'x': bottom_rect['top_left']['x'],
        'y': top_rect['bottom_right']['y']
    }

    bottom_right = {
        'x': top_rect['bottom_right']['x'],
        'y': bottom_rect['top_left']['y']
    }

    return top_left, bottom_right

def get_marker_rect(marker, photo):

    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(marker, None)
    kp2, des2 = sift.detectAndCompute(photo, None)

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
