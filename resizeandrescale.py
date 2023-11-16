import cv2 as cv
# img =cv.imread('photos/cat_large2.jpg')
# cv.imshow('cat', img)

def rescaleFrame(frame, scale=0.75):
    # this will work in images, videos and live videos
    width=int(frame.shape[1]*scale)  #frame.shape[1] is width
    height=int(frame.shape[0]*scale)  #frame.shape[0] is height
    dimensions=(width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    #it only works in live videos
    capture.set(3, width)
    capture.set(4, height)

#reading video
capture=cv.VideoCapture('videos/dog.mp4')  #it takes either any integers or a path to a video 1)webcam is referecing by interger 0
while True:
    isTrue, frame=capture.read() #it reads videos frame by frame
    
    frame_resized=rescaleFrame(frame)
    # cv.imshow('video', frame)
    cv.imshow('video', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'): #if letter d is pressed then stop the video and break out from the loop
        break #to stoping videos playing indefinetly
    
capture.release()
cv.destroyAllWindows()

