import cv2

# Read the image
image = cv2.imread("photo.jpg")

if image is None:
    print("Image not found")
else:
    # Apply strong Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (51, 51), 0)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display blurred image
    cv2.imshow("Strong Gaussian Blur", blurred_image)

    # Wait for a key
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()