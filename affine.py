import cv2
import numpy as np

def retindex(location):
    i=0
    index=0
    length=len(location)
    #print location
    while(i<length):
        j=1
        while(j<length):
            if((location[i][0]+location[i][1])<(location[(i+j)%length][0]+location[(i+j)%length][1])):
            	j+=1
                if(j==length):
		    index=i
	    else:
		break
	i+=1
    return index

def return_corner(location,index):
    # org=np.array([])
    org=location[index]
    org=np.vstack((org, location[(index+3)%4]))
    org=np.vstack((org, location[(index+5)%4]))
    org=np.vstack((org, location[(index+6)%4]))
    return org
def crop(image,loc):
    mask = np.zeros(image.shape, dtype=np.uint8)
    # roi_corners = np.array([[(91, 323), (271, 307), (293, 475), (113, 491)]], dtype=np.int32)
    print "the loc", loc,type(loc)
    roi_corners =np.int32([loc])
    # fill the ROI so it doesn't get wiped out when the mask is applied
    channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,) * channel_count
    cv2.fillPoly(mask, roi_corners, ignore_mask_color)
    # from Masterfool: use cv2.fillConvexPoly if you know it's convex
    # apply the mask
    masked_image = cv2.bitwise_and(image, mask)  ##this is the mask with roi image
    subresult = cv2.subtract(image, masked_image)
   # cv2.imshow("sub", subresult)
    return subresult

def replace(src,wiki,location):
#src=cv2.imread("5-81.png")
#cv2.imshow("Original",src)
#wiki=cv2.imread("who.jpg")
# wiki=cv2.imread("E:\\fbb.jpg")
#cv2.imshow("wiki",wiki)
    kh,kw,kdim=wiki.shape
    print kh,kw,kdim
# wikigray=cv2.cvtColor()
    h,w,dim=src.shape
    print h,w,dim

    wikipt=np.float32([[0,0],
                       [kw,0],
                       [0,kh],
                       [kw,kh]])
# srcpt=np.float32([[91,323],
#                   [271,307],
#                   [113,491]])

    print location,type(location)
    min=retindex(location)
    loc=return_corner(location,min)
    srcpt=np.float32(loc)
    # M=cv2.getAffineTransform(wikipt,srcpt)
    M=cv2.getPerspectiveTransform(wikipt,srcpt)

    dst=cv2.warpPerspective(wiki,M,(w,h))
#cv2.imshow("ddd",dst)

    cropimg=crop(src,location)                     ##crop the qr-code area and set the area's pixel value is 0
    final=cv2.bitwise_or(dst,cropimg)    ##add the transforming image to the crop
    return final
#cv2.imshow("final",final)
    # cv2.imwrite("repalce.jpg",final)
    #cv2.waitKey(0)
    




