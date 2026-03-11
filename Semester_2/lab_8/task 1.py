import cv2


img = cv2.imread('variant-1.jpg')
img = cv2.resize(img, (1080, 720))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
#print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()