import cv2 as cv
import numpy as np

#------------------------------------------------------------------------------
# LOAD IMAGE
#------------------------------------------------------------------------------

pallet = cv.imread('C:/Users/Darrel/Desktop/img_diff/img_fgnd.png')

#------------------------------------------------------------------------------
# COLOR CONVERT 2 HSV -> BI LAT FILTER -> SPLIT
#------------------------------------------------------------------------------

img = cv.cvtColor(pallet,cv.COLOR_RGB2HSV)
img = cv.bilateralFilter(img,9,105,105)
R,G,B = cv.split(img)

#------------------------------------------------------------------------------
# EQUALIZE EACH CHANNEL -> MERGE CHANNELS -> CVT COLOR 2 GRAY
#------------------------------------------------------------------------------

equalize1 = cv.equalizeHist(R)
equalize2 = cv.equalizeHist(G)
equalize3 = cv.equalizeHist(B)

equalize = cv.merge((R,G,B))

equalize = cv.cvtColor(equalize,cv.COLOR_RGB2GRAY)

#------------------------------------------------------------------------------
# THRESH -> EQUALIZE
#------------------------------------------------------------------------------

ret,thresh = cv.threshold(equalize,0,255,cv.THRESH_OTSU + cv.THRESH_BINARY)
equalize = cv.equalizeHist(thresh)

#------------------------------------------------------------------------------
# CANNY -> CREATE KERNEL -> DILATE
#------------------------------------------------------------------------------

canny = cv.Canny(equalize,250,255)
canny = cv.convertScaleAbs(canny)

kernel = np.ones((3,3), np.uint8)

dilated = cv.dilate(canny,kernel,iterations=1)

#------------------------------------------------------------------------------
# FIND AND DRAW CONTOURS
#------------------------------------------------------------------------------

contours, hierarchy = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
contours = sorted(contours, key = cv.contourArea, reverse = True)[:10]
cnt = contours[0]
final = cv.drawContours(pallet, [cnt], -1, (0,0,255), 3)

#------------------------------------------------------------------------------
# MAKE NEW BLANK MASK
#------------------------------------------------------------------------------

mask = np.zeros(pallet.shape,np.uint8)

#------------------------------------------------------------------------------
# NEW IMAGE -> COLOR CONVERT 2 GRAY -> THRESH -> BITWISE
#------------------------------------------------------------------------------

new_img = cv.drawContours(mask,[cnt], -1, (255,255,255), -1)
new_gray = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)

ret, thresh1 = cv.threshold(new_gray, 100, 255, cv.THRESH_BINARY)

final = cv.bitwise_and(pallet, pallet, mask = thresh1)

#------------------------------------------------------------------------------
# GET PIXEL COORDINATES AND COMPUTE PALLET DIMENSIONS FROM CONTOURS
#------------------------------------------------------------------------------

print('pallet face area: ',cv.contourArea(cnt))

leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

print('left',leftmost)
print('right',rightmost)
print('top',topmost)
print('bottom',bottommost)

obj_height = tuple(map(lambda i, j: i - j, bottommost, topmost))
obj_width = tuple(map(lambda i, j: i - j, rightmost, leftmost))

print('tuple for pallet height: ',obj_height)
print('tuple for pallet width',obj_width)

print('pallet height: ',obj_height[1])
print('pallet width: ',obj_width[0]) 

#------------------------------------------------------------------------------


















#------------------------------------------------------------------------------
cv.waitKey(0)
cv.destroyAllWindows() 
#------------------------------------------------------------------------------






















