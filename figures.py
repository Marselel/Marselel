import cv2
import numpy as np

photo = np.zeros((600, 600, 3), dtype='uint8')

# photo[100:150,200:560]=255,159,0
cv2.rectangle(photo, (0, 100), (90, 90), (255, 159, 0), thickness=4)

# cv2.line(photo, (photo.shape[1] // 2, photo.shape[0] // 2), (photo.shape[1] // 2, 0), (255, 159, 0), thickness=5)
#
# cv2.circle(photo,(photo.shape[1] // 2+120, photo.shape[0] // 2+100), 150,( 255, 159, 0), thickness=4)
#
cv2.putText(photo,'itProgger',(100,250),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,255,0),thickness=0)

# print(photo)
cv2.imshow('Photo', photo)
cv2.waitKey(0)
