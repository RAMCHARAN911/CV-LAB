import cv2

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Rotate 270° clockwise
    rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Rotated Image (270° CW)", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Rotated Image (270° CW)", 600, 400)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image (270° CW)", rotated)

    # Arrange windows
    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Rotated Image (270° CW)", 750, 100)

    # Save image
    cv2.imwrite("rotated_270_clockwise.jpg", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
