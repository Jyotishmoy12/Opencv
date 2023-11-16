import cv2 as cv 
#reading images

# img=cv.imread('photos/cat.jpg')
# cv.imshow('meow',img)  #window name and the variable name in this case it is img
# cv.waitKey(0); #it waits for a specific delay in miliseconds

#now reading videos

capture=cv.VideoCapture('videos/dog.mp4')  #it takes either any integers or a path to a video 1)webcam is referecing by interger 0
while True:
    isTrue, frame=capture.read() #it reads videos frame by frame
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'): #if letter d is pressed then stop the video and break out from the loop
        break #to stoping videos playing indefinetly
    
capture.release()
cv.destroyAllWindows()
    

        

