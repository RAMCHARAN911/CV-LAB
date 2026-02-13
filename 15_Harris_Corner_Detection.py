import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to float32 (Required for Harris)
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Dilate corner points for visibility
    corners = cv2.dilate(corners, None)

    # Mark corners in red color
    image[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Create windows
    cv2.namedWindow("Original Image with Corners", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original Image with Corners", 700, 500)

    # Show image
    cv2.imshow("Original Image with Corners", image)

    # Save result
    cv2.imwrite("harris_corners.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
