import cv2
import matplotlib.pyplot as plt

# Function to analyze histogram based on color levels
def analyze_histogram(image):
    colors = ('b', 'g', 'r')

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Color Levels")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.show()


# Read the image
image = cv2.imread("photo.jpg")

if image is None:
    print("Image not found")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Analyze the histogram
    analyze_histogram(image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()