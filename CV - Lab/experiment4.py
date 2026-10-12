import cv2

# Read the image
image = cv2.imread("photo.jpg")

if image is None:
    print("Image not found")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(gray_image)

    # Display original grayscale image
    cv2.imshow("Original Image", gray_image)

    # Display equalized image
    cv2.imshow("Histogram Equalized Image", equalized_image)

    # Wait for a key
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()