import cv2
import numpy as np
img = cv2.imread("C:/Users/AISHMA GIRI/Pictures/kitty.jpg")
output = img.copy()
roi = img[100:250, 100:250]
output[300:450, 300:450] = roi
combined = np.hstack((img, output))
cv2.imshow("Input (Left) | ROI Output (Right)", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
