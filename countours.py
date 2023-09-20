import cv2
import numpy as np







img = cv2.imread('images\mashina.jpg')
img = cv2.resize(img, (1080, 720), 1, 1)


new_img = np.zeros(img.shape, dtype='uint8')



img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 0)

img = cv2.Canny(img,50, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# print(con)
cv2.drawContours(new_img, con, -1, (178, 65, 25), thickness=1)

cv2.imshow("Result",new_img)
cv2.waitKey(0)