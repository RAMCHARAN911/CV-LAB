import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_histogram(image_path):

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    # Show original image
    cv2.imshow("Original Image", image)

    # Colors in OpenCV (BGR)
    colors = ('b', 'g', 'r')

    # Plot histogram for each channel
    for i, col in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")

    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call function
analyze_histogram("input.jpg")
