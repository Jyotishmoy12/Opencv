import cv2 as cv
import numpy as np

#creating a blank image
             #width , height and number of colors
blank=np.zeros((500, 500, 3), dtype='uint8') #uint8 is basically a datatype of a image

cv.imshow('blank', blank)

#1) paint the image a cartain colour
# blank[:]=0,255,0  #referencing to all the pixels and color it in green
# # we can color a certain portion also
blank[200:300, 300:400]=0,0,255
cv.imshow('Green', blank)


# img=cv.imread('photos/cat.jpg')
# cv.imshow('cat', img)
cv.waitKey(0)
