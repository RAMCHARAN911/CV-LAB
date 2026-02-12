import cv2

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur (to reduce noise)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blur, 100, 200)

    # Create resizable windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Canny Edge Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Canny Edge Image", 600, 400)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Image", edges)

    # Move windows side by side
    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Canny Edge Image", 750, 100)

    # Save edge image
    cv2.imwrite("canny_edges.jpg", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
