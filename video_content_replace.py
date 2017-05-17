import numpy as np
import cv2
from PIL import Image
import zbar
import time
import affine as af
from sys import argv

ad=cv2.imread("who.jpg")
print len(argv)
cap = cv2.VideoCapture(argv[1])
fps=cap.get(cv2.CAP_PROP_FPS)
print fps
size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out=cv2.VideoWriter("mark.avi", cv2.VideoWriter_fourcc('H', '2', '6', '4'), fps, size)

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')


def draw_img(frame, point):
	rect = cv2.minAreaRect(point)
	box = np.int0(cv2.boxPoints(rect))
	cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
	return frame

while(True):

    # try:
    #     print(port.readline())
    # except port.SerialTimeoutException:
    #     print('Data could not be read')

    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # width = np.size(frame, 1)  # here is why you need numpy!  (remember to "import numpy as np")
    # height = np.size(frame, 0)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #COLOR_BGR2HSV


    pil = Image.fromarray(gray)
    width, height = pil.size
    raw = pil.tobytes()

    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)
    #print dir(image)
  
    for symbol in image:
    	point = np.array(symbol.location)		
        print type(point),point
        #frame = draw_img(frame, point)
        frame=af.replace(frame,ad,point)			
    out.write(frame)        
    #cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
