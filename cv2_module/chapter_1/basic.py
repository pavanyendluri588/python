import cv2
img=cv2.imread("G:\Capture.PNG")
cv2.imshow("output",img)
#cv2.waitkey(10000)
camera=cv2.videocapture(0)
