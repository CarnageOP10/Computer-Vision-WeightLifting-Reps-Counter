import cv2
import mediapipe as mp
import time
import PoseDetectionModule as pdm
import numpy as np

cap = cv2.VideoCapture("TrainerFiles\\1.mp4")
detector = pdm.poseDetector()
count = 0
dir = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img,(1280, 1000))
    # img = cv2.imread("TrainerFiles\\2.jpg")
    img = detector.findPose(img, False)



    lmlist = detector.findPosition(img, False)
    if len(lmlist)!=0:
     # print(lmlist)
     # left arm
     angle = detector.findAngle(img,12,14,16)
    #   right arm
    #  detector.findAngle(img,11,13,15)
     per = np.interp(angle,(208,250),(0,100))
     bar = np.interp(angle, (208, 250), (650, 100))
     # print(angle, per)

    # check for the no of reps
     color = (255, 0, 255)
     if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
     if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0

     # Draw Bar
     cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
     cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
     cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,color, 4)
    # Draw Curl Count
     cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
     cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                (255, 0, 0), 25)

     cv2.imshow("Image", img)
     cv2.waitKey(1)
