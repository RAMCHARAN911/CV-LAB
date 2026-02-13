import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    rows, cols = image.shape[:2]

    # Define 3 original points
    pts1 = np.float32([[50, 50],
                       [200, 50],
                       [50, 200]])

    # Define 3 transformed points
    pts2 = np.float32([[10, 100],
                       [200, 50],
                       [100, 250]])

    # Get affine transformation matrix
    matrix = cv2.getAffineTransform(pts1, pts2)

    # Apply affine transformation
    transformed = cv2.warpAffine(image, matrix, (cols, rows))

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Affine Transformed Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Affine Transformed Image", 600, 400)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformed Image", transformed)

    # Arrange windows
    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Affine Transformed Image", 750, 100)

    # Save result
    cv2.imwrite("affine_transformed.jpg", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
