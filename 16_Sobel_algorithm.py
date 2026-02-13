import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel in X direction
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

    # Apply Sobel in Y direction
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Convert to absolute values
    abs_sobel_x = cv2.convertScaleAbs(sobel_x)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)

    # Combine both
    sobel_combined = cv2.addWeighted(abs_sobel_x, 0.5,
                                      abs_sobel_y, 0.5, 0)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Sobel Edge Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Sobel Edge Image", 600, 400)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Sobel Edge Image", sobel_combined)

    # Arrange windows
    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Sobel Edge Image", 750, 100)

    # Save result
    cv2.imwrite("sobel_edges.jpg", sobel_combined)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
