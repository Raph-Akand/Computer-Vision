# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 02:25:34 2019

@author: Akandison
"""

import cv2
import numpy as np
win="bos"
cv2.namedWindow(win)
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
while ret:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #BLUE
    low=np.array([100,50,50])
    high=np.array([140,255,255])
    image_mask=cv2.inRange(hsv,low,high)
    output=cv2.bitwise_and(frame,frame,mask=image_mask)
    cv2.imshow("mask",image_mask)
    cv2.imshow("tracking",output)
    cv2.imshow(win,frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()    