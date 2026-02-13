import cv2

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Rotate 180 degrees
    rotated = cv2.rotate(image, cv2.ROTATE_180)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Rotated Image (180°)", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Rotated Image (180°)", 600, 400)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image (180°)", rotated)

    # Arrange windows
    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Rotated Image (180°)", 750, 100)

    # Save rotated image
    cv2.imwrite("rotated_180.jpg", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
