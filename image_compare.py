import cv2 as c
img = c.imread('./image1.jpg',0)
c.imshow('patna university',img)
# c.imshow('patna university',img 0)
c.waitKey(0)
c.destroyAllWindows()