import cv2
import numpy as np

photo = cv2.imread("images/water-grass-bird-wildlife-beak-fauna-duck-goose-vertebrate-waterfowl-water-bird-mallard-ducks-geese-and-swans-497067.jpg")
photo = cv2.resize(photo, (1080, 720), 0.5, 0.5)
img = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
square = cv2.rectangle(img.copy(), (170, 170), (360, 360), 255, -1)

img = cv2.bitwise_and(photo,photo,mask=square)
# img = cv2.bitwise_or(circle,square)
# img = cv2.bitwise_xor(circle,square)
# img = cv2.bitwise_not(square)

cv2.imshow("Result", img)
cv2.waitKey(0)
