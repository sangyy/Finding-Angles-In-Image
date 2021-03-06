import cv2
import math
###################################
widthImg = 640
heightImg = 390
#####################################

path = 'angle.png'
img = cv2.imread(path)

img = cv2.resize(img, (widthImg, heightImg))
pointsList = []


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:

        if size != 0 and size % 3 != 0:
            # cv2.line(img, tuple(
            #     pointsList[round((size-1)/3)*3]), (x, y), (0, 0, 255), 2)
            cv2.line(img, tuple(
                pointsList[::3][-1]), (x, y), (0, 0, 255), 2)

        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        pointsList.append([x, y])


def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
    cv2.putText(img, str(angD), (pt1[0]+40, pt1[1]+20),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (0, 0, 255))


def gradient(pt1, pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])


while True:
    cv2.imshow('Image', img)
    size = len(pointsList)

    cv2.setMouseCallback("Image", mousePoints)

    if size != 0 and size % 3 == 0:
        getAngle(pointsList)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)
        img = cv2.resize(img, (widthImg, heightImg))
