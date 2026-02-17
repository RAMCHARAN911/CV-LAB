def subtract_foreground(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0,0,200])
    upper = np.array([180,50,255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_not(mask)

    cv2.imshow("Foreground Removed", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

subtract_foreground("image.jpg")
