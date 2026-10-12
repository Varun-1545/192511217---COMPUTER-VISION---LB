import cv2

# Read the image
image = cv2.imread("photo.jpg")

if image is None:
    print("Image not found")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray_image, 100, 200)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display outline/edges
    cv2.imshow("Canny Edge Image", edges)

    # Wait for a key
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()