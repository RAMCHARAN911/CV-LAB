import cv2

def segmentation():
    img = cv2.imread("face.jpg", 0)

    if img is None:
        print("Image not found!")
        return

    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    cv2.imwrite("output_segmentation.jpg", thresh)
    print("Output saved as output_segmentation.jpg")

    cv2.imshow("Segmentation", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

segmentation()
