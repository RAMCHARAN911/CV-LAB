import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create resizable windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)

    # Set window size (SMALL)
    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Gray Image", 600, 400)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gray Image", gray_image)

    # Move windows side-by-side
    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Gray Image", 750, 100)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
