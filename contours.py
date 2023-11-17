import cv2 as cv
img=cv.imread('photos/cats.jpg')
cv.imshow('cat', img)

#contours are basically boundaries of objects the line
# or curve that joins the countious points along the boundary of an object

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur=cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny=cv.Canny(blur, 125,175)
cv.imshow('Canny', canny)


# this function looks for edges of a image and returns to list they are a python list
#CHAIN_APPROX_NONE --> it returns all the points in a line(line for example)
#CHAIN_APPROX_SIMPLE--> it returns only two points in a line(example-->line)
contours, hierarchies=cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')


cv.waitKey(0)
