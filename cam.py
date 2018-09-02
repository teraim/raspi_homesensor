#!/usr/bin/python
import os
import sys
import cv2
import numpy as np
import time
import datetime
from picamera.array import PiRGBArray
from picamera import PiCamera

def detect_face():
    print("camra ready...")
    camera = PiCamera()
    camera.hflip = False
    camera.vflip = True
    camera.resolution = (1920,1088)
    rawCapture = PiRGBArray(camera)
    time.sleep(1) ## warmup

    print("camera capture...")
    camera.capture(rawCapture, format="bgr")
    frame = rawCapture.array

    ## equalize histogram on YUV space
    print("equalize histgram...")
    yuvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    yuvframe[:,:,0] = cv2.equalizeHist(yuvframe[:,:,0])
    frame = cv2.cvtColor(yuvframe, cv2.COLOR_YUV2BGR)

    ##
    print("load cascade classifier")
    #cascade_path = '/usr/local/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml'
    #cascade_path = '/usr/local/share/OpenCV/lbpcascades/lbpcascade_frontalface_improved.xml'
    cascade_path1 = './cascades/haarcascade_frontalface_default.xml'
    cascade_path2 = './cascades/haarcascade_eye.xml'
    fc1 = cv2.CascadeClassifier(cascade_path1)
    fc2 = cv2.CascadeClassifier(cascade_path2)

    ## FaceDetection
    print("detect feature...")
    grayframe = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    grayframe = cv2.equalizeHist(grayframe)
    res1 = fc1.detectMultiScale(grayframe, scaleFactor=1.05, minNeighbors=10, minSize=(30,30))
    res2 = fc2.detectMultiScale(grayframe, scaleFactor=1.05, minNeighbors=10, minSize=(20,20))

    ## Draw Rectangle
    print("draw rectangles...")
    for (x, y, w, h) in res1:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for (x, y, w, h) in res2:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    ## Draw timestamp
    print("draw timestamp...")
    dt_now = datetime.datetime.now()
    dt_str = dt_now.stdftime("%Y/%m/%d %H:%M:%S")
    cv2.putText(frame, dt_std, (50,50), "Helvetica", 24, (255,255,255))

    ## Resize
    #print("resize...")
    #frame = cv2.resize(frame, (640,480));

    ## Save Image
    print("save image file...")
    fn = "image_%d_%d.jpg" % (len(res1), len(res2))
    cv2.imwrite(fn, frame)

if __name__ == '__main__':
    detect_face() 
