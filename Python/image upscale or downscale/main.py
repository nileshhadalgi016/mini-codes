import cv2

image=cv2.imread('coffee.jpg')

smaller=cv2.pyrDown(image)
larger=cv2.pyrUp(image)

cv2.imshow('original',image)
cv2.imshow('smaller',smaller)
cv2.imshow('larger',larger)
cv2.waitKey(0)
cv2.destroyAllWindows()