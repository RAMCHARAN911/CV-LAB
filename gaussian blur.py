import cv2

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Create resizable windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Gaussian Blur Image", cv2.WINDOW_NORMAL)

    # Set small window size
    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Gaussian Blur Image", 600, 400)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blur Image", blurred_image)

    # Move windows side by side
    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Gaussian Blur Image", 750, 100)

    # Save blurred image
    cv2.imwrite("gaussian_blur.jpg", blurred_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
