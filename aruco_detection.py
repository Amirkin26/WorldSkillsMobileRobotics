import cv2
import cv2.aruco as aruco
cap=cv2.VideoCapture(0)
key=1
key_stop=32
dictionary=aruco.Dictionary_get(aruco.DICT_4X4_50)
while key!=key_stop:
    isRead, image=cap.read()
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    marker_grounds,ids,service=aruco.detectMarkers(image_gray,dictionary)
    aruco.drawDetectedMarkers(image,marker_grounds)
    i=0
    for grounds in marker_grounds:
        id = ids[i]
        i = i+1
        grounds=grounds[0]
        x1,y1=grounds[0]
        x2, y2 = grounds[1]
        x3, y3 = grounds[2]
        x4, y4 = grounds[3]
        xc, yc = (x1 + x3) // 2, (y1 + y3) // 2
        cv2.putText(image,str(id), (int(xc),int(yc)), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
        cv2.circle(image, (int(xc), int(yc)), 10, (0, 255, 0), -1)
        cv2.circle(image,(int(x1),int(y1)),10,(0,255,0),-1)
        cv2.circle(image, (int(x2), int(y2)), 10, (0, 255, 0), -1)
        cv2.circle(image, (int(x3), int(y3)), 10, (0, 255, 0), -1)
        cv2.circle(image, (int(x4), int(y4)), 10, (0, 255, 0), -1)
    cv2.putText(image, str(i), (10,50), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
    cv2.imshow('w',image)
    key=cv2.waitKey(20)
cap.release()