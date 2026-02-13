import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    watermarked = image.copy()

    # Define watermark text
    text = "© My Watermark"

    # Set font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Get image dimensions
    h, w = image.shape[:2]

    # Put watermark text (bottom-right corner)
    cv2.putText(watermarked,
                text,
                (w-250, h-20),
                font,
                1,
                (255, 255, 255),
                2,
                cv2.LINE_AA)

    # Blend original and watermark (for transparency effect)
    output = cv2.addWeighted(watermarked, 0.7, image, 0.3, 0)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Watermarked Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Watermarked Image", 600, 400)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", output)

    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Watermarked Image", 750, 100)

    # Save result
    cv2.imwrite("watermarked_image.jpg", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
