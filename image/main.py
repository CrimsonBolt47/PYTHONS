import cv2

img=cv2.imread("galaxy.jpg",0) #rbg-1,black& white-0



resize_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy",resize_img)

cv2.imwrite("Galaxy_resized.jpeg",resize_img)
cv2.waitKey(0)

cv2.destroyAllWindows()