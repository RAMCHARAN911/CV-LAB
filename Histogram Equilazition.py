import cv2

image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Histogram Equalization
    equalized = cv2.equalizeHist(gray)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Equalized Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Equalized Image", 600, 400)

    # 🔥 IMPORTANT CHANGE HERE
    cv2.imshow("Original Image", image)      # Show color original
    cv2.imshow("Equalized Image", equalized) # Show equalized gray

    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Equalized Image", 750, 100)

    cv2.imwrite("histogram_equalized.jpg", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
