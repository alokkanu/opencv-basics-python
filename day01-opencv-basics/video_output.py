import cv2 as cv

capture = cv.VideoCapture('videos/video.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break

    cv.imshow('Myvideo', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()