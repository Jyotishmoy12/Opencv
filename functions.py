import cv2 as cv
img =cv.imread('photos/park.jpg')
cv.imshow('cat', img)
#converting image to grayscale

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('cat', gray)

#Blur   to increase th blur size we can increase the kernal size i.e (7,7) it has to be odd always

blur=cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('cat', blur)

#Edge cascade i.e how many edges are present in an image

canny=cv.Canny(blur, 125, 175)
cv.imshow('canny edges', canny)

#Dialating the image

dilated=cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

#Eroding
eroded=cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

#resize

resized=cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#croping
cropped=img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)
