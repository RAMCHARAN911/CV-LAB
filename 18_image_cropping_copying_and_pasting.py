import cv2

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Make copy of original
    output = image.copy()

    # Select ROI coordinates
    # Format: image[y1:y2, x1:x2]
    roi = image[100:300, 200:400]   # Crop region

    # Paste ROI to new location
    output[350:550, 50:250] = roi

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Cropped ROI", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Pasted Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 500, 350)
    cv2.resizeWindow("Cropped ROI", 300, 200)
    cv2.resizeWindow("Pasted Image", 500, 350)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("Pasted Image", output)

    cv2.moveWindow("Original Image", 50, 100)
    cv2.moveWindow("Cropped ROI", 600, 100)
    cv2.moveWindow("Pasted Image", 950, 100)

    # Save result
    cv2.imwrite("cropped_roi.jpg", roi)
    cv2.imwrite("pasted_image.jpg", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
