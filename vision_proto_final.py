# SENIOR DESIGN: FREIGHT CONFIGURATOR
# IMAGE PROCESSING MASTER FILE - DO NOT ALTER THIS FILE
# AUTHOR: DARREL ROMBA
#------------------------------------------------------------------------------
# README:

# coordinate mapping and RGB/HSV comment section is for reference when 
# setting bounds of BODY and LIGHT masks. DO NOT CHANGE THESE COMMENTS.
#==============================================================================

import cv2 as cv
import numpy as np

#------------------------------------------------------------------------------
# VIDEOCAPTURE
#------------------------------------------------------------------------------

vcap_left = cv.VideoCapture(0)
vcap_right = cv.VideoCapture(1)

img_count = 1

#------------------------------------------------------------------------------
# READ FRAMES IF CAMERAS ON
#------------------------------------------------------------------------------

while(1):
    
    _, frame_left = vcap_left.read()
    _, frame_right = vcap_right.read()
    
#------------------------------------------------------------------------------
# user CAPTURE or QUIT 
#------------------------------------------------------------------------------    
    
    k = cv.waitKey(1) & 0xFF

    if k == ord("c"):
        
        img_name_left = "LEFT_frame_{}.png".format(img_count)
        cv.imwrite(img_name_left, frame_left)
        print("{} written".format(img_name_left))
        
        img_name_right = "RIGHT_frame_{}.png".format(img_count)
        cv.imwrite(img_name_right, frame_right)
        print("{} written".format(img_name_right))
        
        img_count += 1

    elif k == ord("q"):
        print("exiting program")
        break    
    
#------------------------------------------------------------------------------
# OPEN IMAGES
#------------------------------------------------------------------------------

# original image
    img = cv.imread('C:/Users/Darrel/Desktop/SD_PYTHON/CV/FINAL/opencv_frame_1.png')
    
# inverted image
    img_not = cv.bitwise_not(img)

#------------------------------------------------------------------------------
# BGR to HSV CONVERT
#------------------------------------------------------------------------------

#hsv for original img
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
#hsv copy for inverted img
    hsv_not = cv.cvtColor(img_not, cv.COLOR_BGR2HSV)
    
#grayscale and binary converted copy of img
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    ret, binary = cv.threshold(gray, 109, 255, cv.THRESH_BINARY)
    #ret, bin_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)

#==============================================================================
# COORDINATE MAPPING and RGB/HSV COLOR VALUES
#==============================================================================
    
# BODY MASK: main part of the body -> maps to cardboard color
# LIGHT MASK: box edges light alters coloring -> maps to daylight/cardboard color 

#------------------------------------------------------------------------------
# (CENTER OF BOX) REFERENCE VALUES FOR NORMAL MASK/IMAGE
#------------------------------------------------------------------------------
# COORDINATES MAPPED 
        
    # X : (332 -> 375)
    # Y : (235 -> 297)
    
#------------------------------------------------------------------------------
# MODE

    # R_mode = 147   
    # G_mode = 118   
    # B_mode = 107   
    
# HSV(FOR MODE)   

    # H = 8 
    # S = 69
    # V = 147
    
#------------------------------------------------------------------------------
# MEAN

    # R_mean = 145  
    # G_mean = 116  
    # B_mean = 105
    
# HSV(FOR MEAN)

    # H = 8 
    # S = 70
    # V = 145
    
#------------------------------------------------------------------------------
# (CENTER OF BOX) REFERENCE VALUES FOR INVERTED MASK/IMAGE
#------------------------------------------------------------------------------
# COORDINATES MAPPED

    # X: (345 -> 358)
    # Y: (255 -> 268)
        
# MODE

    # R_MODE = 108
    # G_MODE = 138
    # B_MODE = 146
    
# HSV(FOR MODE)
    
    # H = 96
    # S = 66
    # V = 146
        
# MEAN

    # R_MEAN = 109
    # G_MEAN = 138
    # B_MEAN = 147
    
# HSV(FOR MEAN)
    
    # H = 97
    # S = 65
    # V = 147

#==============================================================================
# UPPER and LOWER BOUNDS for REGULAR MASK
#------------------------------------------------------------------------------
    
    hsv_1_lo = np.array([0,49,136],np.uint8)
    hsv_1_hi = np.array([14,150,180],np.uint8)
    
    hsv_1_full = cv.inRange(hsv,hsv_1_lo,hsv_1_hi)
    
#------------------------------------------------------------------------------
# UPPER and LOWER BOUNDS for INVERTED MASK
#------------------------------------------------------------------------------

    #hsv_2_lo = np.array([91,35,136],np.uint8)
    #hsv_2_hi = np.array([105,148,165],np.uint8)
    
    #hsv_2_full = cv.inRange(hsv_not, hsv_2_lo, hsv_2_hi)
    
#------------------------------------------------------------------------------
# 
#------------------------------------------------------------------------------

    
    
    bit_hsv = cv.bitwise_and(hsv_1_full,binary)
    
    opening = cv.morphologyEx(bit_hsv, cv.MORPH_OPEN,(3,3))
    
    #erode = cv.erode(bit_hsv,(3,3),iterations=1)


#------------------------------------------------------------------------------
# EDGE DETECT
#------------------------------------------------------------------------------
    
    #edges = cv.Canny(dilate_mask,150,200)
    
#------------------------------------------------------------------------------
# FIND and DRAW CONTOURS
#------------------------------------------------------------------------------

    #contours, hierarchy = cv.findContours(edges,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

    #cntrs = cv.drawContours(img,contours,-1,(0,0,255),3)
    
#------------------------------------------------------------------------------
# SHOW WINDOW
#------------------------------------------------------------------------------

    #cv.imshow('CONTOURS',cntrs)
    #cv.imshow('edges',edges)
    #cv.imshow('normal',hsv_1_full)
    #cv.imshow('inverted',hsv_2_full)
    #cv.imshow('bitwise',bit_hsv)
    #cv.imshow('erode',erode)
    #cv.imshow('binary',binary)
    #cv.imshow('binary inv',bin_inv)
    cv.imshow('open',opening)


#------------------------------------------------------------------------------
vcap_left.release()
vcap_right.release()
cv.destroyAllWindows()     
#==============================================================================



