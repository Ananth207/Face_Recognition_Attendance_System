#import cv2
#img = cv2.imread("krishna.jpg")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("krishna",img)
# cv2.imshow("krishnaGray",imgGray)
#cv2.waitKey(0)

# frameWidth = 300
# frameHeight = 200
# cap = cv2.VideoCapture("testVideo.mp4")
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)
#
# while True:
#     success,imge=cap.read()
#     cv2.imshow("Video",imge)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# # Import OpenCV
import numpy as np
import cv2
import numpy as np
import math
def nothing(x):
    pass

# Initialize camera
cam = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
# 0- Primary camera ,1- External camera

# colour to be masked - blue.
# param1 = [5, 150, 50]  # Setting the lower pixel for blue (BGR)
# param2 = [255, 255, 180]  # Setting the upper pixel for blue (BGR)

# Video Loop - Real time processing

while (1):

    # Read the image
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    #Do the processing
    # lower = np.array(param1)  # Assigning the lower and upper index values (param1 and param2)
    # upper = np.array(param2)
    # mask = cv2.inRange(hsv, lower, upper)
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Masking of the image to produce a binary image.
    mask1=cv2.GaussianBlur(mask,(5,5),100)
    #cv2.imshow("blur",mask1)   #blurring the image
    res = cv2.bitwise_and(frame, frame, mask=mask)#the masked blue part of img
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    thresh=cv2.Canny(gray,127,255)
    #cv2.imshow('Canny Image',thresh)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(res,contours,-1,(255,0,0),3)
    # The masked blue part of the image.
    # Show the image
    cv2.imshow('image', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cnt= max(contours,key=lambda x:cv2.contourArea(x))  #contour of max area

    cv2.imshow("resultant",res)
    hull=cv2.convexHull(cnt)
    cv2.drawContours(res,[hull],-1,(0,255,255),2)  #convex hull
    cv2.imshow("hull",res)

    # hull = cv2.convexHull(contours, returnPoints=False)
    # defects = cv2.convexityDefects(contours, hull)
    # if defects is not None:
    #     cnt = 0
    # for i in range(defects.shape[0]):  # calculate the angle
    #     s, e, f, d = defects[i][0]
    #     start = tuple(contours[s][0])
    #     end = tuple(contours[e][0])
    #     far = tuple(contours[f][0])
    #     a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
    #     b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
    #     c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
    #     angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
    #     if angle <= np.pi / 2:  # angle less than 90 degree, treat as fingers
    #         cnt += 1
    #         cv2.circle(res, far, 4, [0, 0, 255], -1)
    # if cnt > 0:
    #     cnt = cnt + 1
    # cv2.putText(res, str(cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    #cv2.imshow('final_result', res)

    # End the video loop
    if cv2.waitKey(1) == 27:  # when to exit
        break

# Close and exit from camera
# not necessary

cv2.destroyAllWindows()

## Import OpenCV
import numpy as np


## Do the processing
# i = 3  # Draw contour(i)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convert to binary image
##ret,thresh = cv2.threshold(gray,127,255,0)

## Canny edge detectionto find threshold insead of using the above function(cv2.threshold())
# thresh=cv2.Canny(img,100,200)
# cv2.imshow('Canny Image',thresh)
# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,contours,i,(255,0,0),3)
# print(len(contours))# Total number of contours in the image
# print("Area = ", cv2.contourArea(contours[i]))
# print("Perimeter = ", cv2.arcLength(contours[i],True))

## Show the image
#cv2.imshow('image',img)

## Close and exit
# cv2.waitKey(0)
# cv2.destroyAllWindows()