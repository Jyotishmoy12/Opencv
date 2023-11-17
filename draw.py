import cv2 as cv
import numpy as np

#creating a blank image
             #width , height and number of colors
blank=np.zeros((500, 500, 4), dtype='uint8') #uint8 is basically a datatype of a image

cv.imshow('blank', blank)

#1) paint the image a cartain colour
# blank[:]=0,255,0  #referencing to all the pixels and color it in green
# # we can color a certain portion also
# blank[200:300, 300:400]=0,0,255
# cv.imshow('Green', blank)

# #2)Draw a rectangle
# cv.rectangle(blank, (0,0),(250,250), (0,250,0), thickness=cv.FILLED) #cv.Filled and -1 are the same
# cv.imshow('rectangle', blank)

# #2)Draw a cicle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40,(0,0,255), thickness=-3)
# cv.imshow('cicle', blank)

# #3)Draw a line
# cv.line(blank, (0,0), (250,250), (255,255,255),thickness=3)
# cv.imshow('line', blank)

#4)Write text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('line', blank)

cv.waitKey(0)
