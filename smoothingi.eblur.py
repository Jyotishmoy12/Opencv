import cv2 as cv
import numpy as np
img=cv.imread('photos/cats.jpg')
cv.imshow('img', img)
#kernal size is basically number of rows and columns *more kernal size more blur

#Averaging --> average of all the pixel intensities on it's surroundings

average=cv.blur(img, (7,7)) #(3,3) is the keranl size
cv.imshow('average',average)

#gaussian blur t is less blur than average
gaussian=cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gaussian blur',gaussian)

#median blur
median=cv.medianBlur(img, 3)
cv.imshow('median blur',median)

#Bilateral--> it retain the edges
#larger the sigma color that means the more colors in the neighbourhood will be considered when blur is computed

bilateral=cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral filter',bilateral)


cv.waitKey(0)


