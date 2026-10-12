import cv2

# Read the image
image = cv2.imread("photo.jpg")

if image is None:
    print("Image not found")
else:
    # Get original image dimensions
    height, width = image.shape[:2]

    # Resize to a bigger size
    bigger_image = cv2.resize(image, (width * 2, height * 2))

    # Resize to a smaller size
    smaller_image = cv2.resize(image, (width // 2, height // 2))

    # Display all images
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger_image)
    cv2.imshow("Smaller Image", smaller_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()