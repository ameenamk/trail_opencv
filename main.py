import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,720)