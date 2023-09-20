import cv2
import numpy as np

img = cv2.imread("images/water-grass-bird-wildlife-beak-fauna-duck-goose-vertebrate-waterfowl-water-bird-mallard-ducks-geese-and-swans-497067.jpg")
img = cv2.resize(img, (1080, 720), 0.5, 0.5)


img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

# img = cv2.cvtColor(img,cv2.COLOR_LAB2RGB)

r, g, b= cv2.split(img)
img=cv2.merge([r,g,b ])

cv2.imshow("Result",img)
cv2.waitKey(0)
