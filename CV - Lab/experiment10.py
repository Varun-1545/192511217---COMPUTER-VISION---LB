
import cv2

# Read the image
image = cv2.imread("photo.jpg")

if image is None:
    print("Image not found")
else:
    # Rotate image 90 degrees clockwise
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
