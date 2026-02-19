import cv2

lambo=cv2.imread('C-Program/lambo01.jpg',-1)
lambo=cv2.resize(lambo,(600,400))#,fx=0.5,fy=0.5)
#lambo=cv2.rotate(lambo, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Image",lambo)   
cv2.waitKey(0)
cv2.destroyAllWindows()