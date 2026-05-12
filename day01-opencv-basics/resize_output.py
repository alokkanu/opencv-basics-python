import cv2 as cv
img =cv.imread('photos/alok.jpg')
cv.imshow('Scene',img)
def rescaleFrame(frame,scale=0.75):
    width=frame.shape[1]*scale
    height=frame.shape[1]*scale
    dimensions=(int(width),int(height))
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)
cv.waitKey(0)
cv.destroyAllWindows()