import cv2

video=cv2.VideoCapture('videos/Lamborghini Made From Cardboard!.mp4')

while cv2.waitKey(0) & 0xFF!=ord('q'):
    succ,img =video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('faces.xml')

    results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in results:
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
        cv2.circle(img, (x+(w//2),y+(h//2)), (h+w)//4, (0,0,255), thickness=3)
        # img = cv2.GaussianBlur(img, (9, 9), 0)

    # img= cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.imshow("result",img)
    # cv2.waitKey(0)
