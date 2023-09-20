import cv2
import numpy as np

img = cv2.imread(
    'images/water-grass-bird-wildlife-beak-fauna-duck-goose-vertebrate-waterfowl-water-bird-mallard-ducks-geese-and-swans-497067.jpg')
img = cv2.resize(img, (1080, 720), 0.5, 0.5)


# img = cv2.flip(img, -1)
def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return  cv2.warpAffine(img_param, mat, (width,height))

# img = rotate(img, -18)

def  transform(img_param, x, y):
    mat=np.float32([[1, 0, x],[0, 1, y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1],img_param.shape[0]))


img = transform(img, 30, 200)


cv2.imshow('Result', img)

cv2.waitKey()
