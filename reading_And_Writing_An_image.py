import cv2
import numpy as np

# resim1 = cv2.imread("opencv-4.x/opencv-4/samples/data/fruits.jpg")
resim1 = cv2.imread("fruits.jpg")
cv2.imshow("Fruits", resim1)

print(resim1.size)

print(resim1.dtype)
print(resim1.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
# import cv2
# import numpy as np
# height = 512
# width = 512
# img = np.random.randint(255, size=(height, width, 1), dtype=np.uint8)
#
# cv2.imshow('Binary', img)
