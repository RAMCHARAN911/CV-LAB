import cv2

def segmentation(image_path, thresh_value):
    img = cv2.imread(image_path, 0)
    _, thresh = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY)

    cv2.imshow("Segmented", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

segmentation("image.jpg", 127)
