import cv2

cap = cv2.VideoCapture("input_video.mp4")

if not cap.isOpened():
    print("Error opening video")
else:

    # Create resizable windows
    cv2.namedWindow("Original Video", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Processed Video", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Video", 600, 400)
    cv2.resizeWindow("Processed Video", 600, 400)

    cv2.moveWindow("Original Video", 100, 100)
    cv2.moveWindow("Processed Video", 750, 100)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Example processing (grayscale)
        processed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Show both videos
        cv2.imshow("Original Video", frame)
        cv2.imshow("Processed Video", processed)

        key = cv2.waitKey(30)

        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
