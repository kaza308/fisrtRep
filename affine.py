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
    



#############################

# videocapture=cv2.VideoCapture("E:\qrvideo.mp4")
# (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
# print(major_ver,minor_ver,subminor_ver)
# fps=videocapture.get(cv2.CAP_PROP_FPS)
# print("fps is:",fps)
# size=(int(videocapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(videocapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# out=cv2.VideoWriter("E:\draw.avi",-1,fps,size)
#
# count=0
# while(1):
#     ret,frame=videocapture.read()
#     # ret,frame=cap.read()
#     if ret==False:
#         break
#     else:
#         cv2.imshow('capture', frame)
#         frame = cv2.flip(frame, 0)
#         out.write(frame)
#         # frames.append(frame)
#         count+=1
#         # cv2.waitKey(0)
#         if cv2.waitKey(30) & 0xFF==ord('q'):
#             break
# print("cccc:",count)
# videocapture.release()
# out.release()
# cv2.destroyAllWindows()


# from pylab import *
# xx=[3,15]
# yy=[4,8]
# x,y=3,4
# zz=float(xx[0]-yy[0])/(xx[1]-yy[1])
# print(zz)
# print(math.hypot(x,y))



# coding ='utf-8'

# def show(img):
# 	fig, ax = plt.subplots(figsize=(16, 10))
# 	ax.imshow(img)
# 	fig.show()
#
# img = cv2.imread('E:\img\\01-3.jpg')
#
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gb = cv2.GaussianBlur(img_gray, (5,5), 0)
# img_edges = cv2.Canny(img_gray, 100, 200)
#
# show(img_edges)
# time.sleep(30)
#
#
#
# contours, hierarchy = cv2.findContours(img_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# hierarchy = hierarchy[0]
# found = []
# for i in range(len(contours)):
#     k = i
#     c = 0
#     while hierarchy[k][2] != -1:
#         k = hierarchy[k][2]
#         c = c + 1
#     if c >= 5:
#         found.append(i)
#
# for i in found:
# 	img_dc = img.copy()
# 	cv2.drawContours(img_dc, contours, i, (0, 255, 0), 3)
# 	show(img_dc)
# 	# time.sleep(3)
#
# #show(img_edges)
# #time.sleep(3)

#######this is a test##########


# print(a.trace())

# mu,sigma=2,0.5                
# v=np.random.normal(mu,sigma,1000)
# plt.hist(v,bins=50,normed=1)
#
# (n,bins)=np.histogram(v,bins=50,normed=True)
# plt.plot(.5*(bins[1:]+bins[:-1]),n,'bo')
# plt.show()



# def mandelbrot(h,w,maxit=20):
#     y,x=np.ogrid[-1.4:1.4:h*1j,-2:0.8:w*1j]
#     c=x+y*1j
#     z=c
#     divtime=maxit+np.zeros(z.shape,dtype=int)
#
#     for i in range(maxit):
#         z=z**2+c
#         diverge=z*np.conj(z)>2**2
#         div_now=diverge&(divtime==maxit)
#         divtime[div_now]=i
#         z[diverge]=2
#     return divtime
# plt.imshow(mandelbrot(400,400))
# plt.show()
