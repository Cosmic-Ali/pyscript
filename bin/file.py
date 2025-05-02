import cv2;import numpy as np; 

# img = cv2.imread("/Users/ali/Desktop/data_science/ML/computer_vision/Apple-logo-1977.jpg")
img = np.zeros((500,500),dtype=np.uint8)
cv2.line(img, (1,1),(499,499),(255),10)
cv2.imshow('img',img)
cv2.waitKey(2000)
cv2.destroyAllWindows()