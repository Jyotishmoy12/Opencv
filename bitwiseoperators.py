import cv2 as cv
import numpy as np

#a pixel is turened off if it has a value 0 else if it is on it has a value 1
blank=np.zeros((400, 400), dtype='uint8')

rectangle=cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle=cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

#bitwise_and  --> it extracts common parts i.e intersections
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and', bitwise_and)

#bitwise OR--> union
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or', bitwise_or)

#bitwise Not--> negation
bitwise_not=cv.bitwise_not(rectangle, circle)
cv.imshow('bitwise_not', bitwise_not)

cv.waitKey(0)
