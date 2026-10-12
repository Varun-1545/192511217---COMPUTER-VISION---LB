import cv2
import numpy as np

# Read the image
image = cv2.imread("photo.jpg")

if image is None:
    print("Image not found")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display dilated image
    cv2.imshow("Dilated Image", dilated_image)

    # Wait for a key
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()