import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    rows, cols = image.shape[:2]

    # Define 4 source points (corners of image)
    pts1 = np.float32([[0, 0],
                       [cols-1, 0],
                       [0, rows-1],
                       [cols-1, rows-1]])

    # Define 4 destination points (changed perspective)
    pts2 = np.float32([[50, 50],
                       [cols-100, 0],
                       [0, rows-100],
                       [cols-50, rows-50]])

    # Get perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply transformation
    transformed = cv2.warpPerspective(image, matrix, (cols, rows))

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Perspective Transformed Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Perspective Transformed Image", 600, 400)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformed Image", transformed)

    # Arrange windows
    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Perspective Transformed Image", 750, 100)

    # Save result
    cv2.imwrite("perspective_transformed.jpg", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
