import cv2

def vehicle_detection_save():
    cap = cv2.VideoCapture("traffic.avi")

    if not cap.isOpened():
        print("Error: Cannot open video")
        return

    # Load cascade file
    car_cascade = cv2.CascadeClassifier("cars.xml")

    if car_cascade.empty():
        print("Error: cars.xml not loaded!")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20

    # Create output video file
    out = cv2.VideoWriter(
        "vehicle_output.avi",
        cv2.VideoWriter_fourcc(*'XVID'),
        fps,
        (width, height)
    )

    print("Recording output video...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Save frame
        out.write(frame)

        cv2.imshow("Vehicle Detection", frame)

        if cv2.waitKey(30) == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print("✅ Saved as vehicle_output.avi")

vehicle_detection_save()
