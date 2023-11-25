import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread('photos/park.jpg')
cv.imshow('park', img)
# plt.imshow(img)
# plt.show()

#Color spaces are basically a spaces of colors, a system of represting
#an array of pixel colors . RGB is a kind of space grayscale is color space
#BGR to grayscale


gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('park', gray)

#CONVERTING THE BGR to HSV format
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('park', hsv)

#hsv to bgr
hsv_bgr=cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('hsv-->bgr', hsv_bgr)

#BGR to LAB format
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('park', lab)

#LAB TO BGR
lab_bgr=cv.cvtColor(img, cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr', lab_bgr)
#BGR TO RGB
# rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('park', rgb)
# plt.imshow(rgb)
# plt.show()
#we can't convert grayscale image to hsv directly we have to convert it first in bgr format then we can do it manually



cv.waitKey(0)
