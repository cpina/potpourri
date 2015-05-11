#!/usr/bin/python

""" Some OpenCV test, just following a tutorial and playing with it."""

# Standard imports
import cv2
import numpy as np;
import itertools

def find_object(o, keypoints):
    print "Object:",o
    print "keypoints",keypoints

    for i in itertools.combinations(keypoints, 2):
        print "0:",i[0].pt
        print "1:",i[1].pt

# Read image
im = cv2.imread("stars.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE)

cv2.imshow("original", im)
cv2.waitKey(0)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

params.blobColor = 255 # by default is 0, which is to extract black blobs

# Change thresholds
params.minThreshold = 1
params.maxThreshold = 255

params.minDistBetweenBlobs = 0


# Filter by Area.
#params.filterByArea = True
#params.minArea = 10
#params.maxArea = 9999999999

# Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1

# Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87

# Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector(params)


# Detect blobs.
keypoints = detector.detect(im)
# print "keypoints:",keypoints

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (255,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)


image2 = np.zeros((im.shape[0], im.shape[1], 3), np.uint8)
image2[:] = (0,0,0)
cv2.imshow("black", image2)
cv2.waitKey(0)

image3 = np.zeros((im.shape[0], im.shape[1], 3), np.uint8)
image3[:] = (0,0,0)
im2_with_keypoints = cv2.drawKeypoints(image2, keypoints, np.array([]), (255,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("more", im2_with_keypoints)
cv2.waitKey(0)

for keypoint in keypoints:
    print keypoint.pt

o = [(0,2), (1,2), (2,2)]
find_object(o, keypoints)

