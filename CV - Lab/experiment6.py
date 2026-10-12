import cv2
import numpy as np

# Read the image
image = cv2.imread("photo.jpg")

if image is None:
    print("Image not found")
else:
    # Create a kernel
    kernel = np.ones((56, 56), np.uint8)

    # Apply erosion
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display eroded image
    cv2.imshow("Eroded Image", eroded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()