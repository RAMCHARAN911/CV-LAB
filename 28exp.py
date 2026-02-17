import cv2

def detect_vehicle(video_path):
    cap = cv2.VideoCapture(video_path)
    car_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_car.xml")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("Vehicle Detection", frame)
        if cv2.waitKey(1)==27:
            break

    cap.release()
    cv2.destroyAllWindows()

detect_vehicle("video.mp4")
