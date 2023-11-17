import cv2 as cv
import numpy as np
img=cv.imread('photos/park.jpg')
cv.imshow('park', img)

# #Translation--> shifting the image along x axis and y axis along
# def translate(img, x, y):
#     transMat=np.float64([[1, 0, x], [0,1,y]])
#     dimesions=(img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimesions)

# # -x -->left
# # -y--> up
# #x--> right
# #y--> down
# translated=translate(img,100, 100)
# cv.imshow('translated', translated)

# #rotation
# def rotate(img, angle, rotPoint=None):
#     (height, width)=img.shape[:2]
    
#     if rotPoint is None:
#         rotPoint=(width//2, height//2) #rotate along center
#     rotMat=cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimesions=(width, height)
#     return cv.warpAffine(img, rotMat, dimesions)

# # if angle is in neg then clockwise else anticlockwise
# rotated=rotate(img, -45)
# cv.imshow('rotated', rotated)
    
# rotated_rotated=rotate(rotated,-45)
# cv.imshow('rotated_rotated', rotated_rotated)

#flipping
#0-->vertically over x axis
#1--> horizontally over y axis
#-1 --> both vertically and horizontally
flip=cv.flip(img, 0)
cv.imshow('flipped', flip)




cv.waitKey(0)
