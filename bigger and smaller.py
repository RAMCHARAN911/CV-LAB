import cv2

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    
    # Resize Smaller (50%)
    smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Resize Bigger (150%)
    bigger = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Smaller Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Bigger Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 500, 350)
    cv2.resizeWindow("Smaller Image", 500, 350)
    cv2.resizeWindow("Bigger Image", 500, 350)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Smaller Image", smaller)
    cv2.imshow("Bigger Image", bigger)

    # Arrange windows
    cv2.moveWindow("Original Image", 50, 100)
    cv2.moveWindow("Smaller Image", 600, 100)
    cv2.moveWindow("Bigger Image", 1150, 100)

    # Save images
    cv2.imwrite("smaller_image.jpg", smaller)
    cv2.imwrite("bigger_image.jpg", bigger)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
