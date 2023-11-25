import cv2 as cv
import numpy as np
img=cv.imread('photos/park.jpg')
cv.imshow('img', img)

blank=np.zeros(img.shape[:2], dtype='uint8')

b,g,r=cv.split(img) # cv.split basically split images into blue, green and red components

blue=cv.merge([b, blank, blank]) #displaying blue channel only
green=cv.merge([blank, g, blank]) #displaying green channel only
red=cv.merge([blank, blank, r]) #displaying red channel only



cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

# cv.imshow('blue', b)
# cv.imshow('green', g)
# cv.imshow('red', r)
#if the color is more white in grayscale image that means the specific color in that region is more for eg in sky is more white in blue gary image that means the contrast of blue is more high in the sky

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge
merged_img=cv.merge([b,g,r])
cv.imshow('merged_img', merged_img)
cv.waitKey(0)
