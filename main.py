import time

import cv2
import numpy as np

# img = cv2.imread('images/stih.jpg')
video=cv2.VideoCapture('videos/i_am_ya_2023-04-14-11-03-46_1681452226541.mp4')
k=0
while cv2.waitKey(1) & 0xFF !=ord('q'):
    # img_shape = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    succ,img=video.read()
    img = cv2.GaussianBlur(img, (9, 9), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.Canny(img,55,55)

    kernel = np.ones((3,3),np.uint8)
    img = cv2.dilate(img, kernel,iterations=1)
    cv2.putText(img,f'{k}', (0,0),cv2.FONT_HERSHEY_TRIPLEX,50,(0,0,255),thickness=0)
    img=cv2.erode(img,kernel,iterations=1)
    # img_shape[400:800,400:800]
    # cv2.putText(img, f'{k}', (0, 0), cv2.FONT_HERSHEY_TRIPLEX, 50, (0, 0, 255), thickness=0)
    cv2.imshow('Result', img)
    k+=1
    print(img.shape)

# print(img_shape.shape)
#
    cv2.waitKey(0)
