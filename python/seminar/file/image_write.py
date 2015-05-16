﻿# -*- coding: utf-8 -*-

import cv2
import pylab as plt
import copy
from PyQt4.QtGui import *

def hist_g(gray):
    hist = cv2.calcHist([im],[0],None,[256],[0,256])
    plt.plot(hist)
    plt.xlim([0,256])

def threshold_im(gray):
    #判別分析法
    th,t_im = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print u"閾値:"+str(th)
    cv2.imshow("threshold",t_im)
    cv2.imwrite("threshold.jpg",t_im)

def gray_image(im):
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    cv2.imwrite("gray.jpg",gray)
    hist_g(gray)
    threshold_im(gray)

def gauss_f(im):
    im_g = cv2.GaussianBlur(im,(21,21),0)
    cv2.imshow("gauss",im_g)
    cv2.imwrite("gauss.jpg",im_g)

def face_know(im):
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    f_im = copy.deepcopy(im)
    face = cascade.detectMultiScale(f_im,1.1,3)
    for (x,y,w,h) in face:
        cv2.rectangle(f_im,(x,y),(x+w,y+h),(0,50,255),3)
    cv2.imshow("face_know",f_im)
    cv2.imwrite('face_know.jpg',f_im)
    return face


def trimming(face,im):
    for (x,y,w,h) in face:
        im_trim = im[y:y+h,x:x+w]
        cv2.imshow("trimming("+str(x)+","+str(y)+")",im_trim)
        cv2.imwrite("trimming("+str(x)+","+str(y)+").jpg",im_trim)

if __name__ == '__main__':
    im = cv2.imread("test.jpg",1)
    cv2.imshow("def",im)
    gray_image(im)
    gauss_f(im)
    face = face_know(im)
    trimming(face,im)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()