'''
Function: cv2.goodFeaturesToTrack(image,maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]])
image – Input 8-bit or floating-point 32-bit, single-channel image.
maxCorners – You can specify the maximum no. of corners to be detected. (Strongest ones are returned if detected more than max.)
qualityLevel – Minimum accepted quality of image corners.
minDistance – Minimum possible Euclidean distance between the returned corners.
corners – Output vector of detected corners.
mask – Optional region of interest.
blockSize – Size of an average block for computing a derivative covariation matrix over each pixel neighborhood.
useHarrisDetector – Set this to True if you want to use Harris Detector with this function.
k – Free parameter of the Harris detector.
'''
import cv2
import numpy as np


def shi_tomasi(image):
    # Converting to grayscale
    image = cv2.imread(image)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Specifying maximum number of corners as 1000
    # 0.01 is the minimum quality level below which the corners are rejected
    # 10 is the minimum euclidean distance between two corners
    corners_img = cv2.goodFeaturesToTrack(gray_img, 1000, 0.01, 10)

    corners_img = np.int0(corners_img)

    for corners in corners_img:
        x, y = corners.ravel()
        # Circling the corners in green
        cv2.circle(image, (x, y), 3, [0, 255, 0], -1)

    return image


shi_tomasi('my_pic.jpg')