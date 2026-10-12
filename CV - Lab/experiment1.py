import cv2

# Read the image
image = cv2.imread("photo.jpg")

# Check whether image was read successfully
if image is None:
    print("Image not found. Check the file name and location.")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display grayscale image
    cv2.imshow("Gray Image", gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()