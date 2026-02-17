import cv2

def eye_detection():
    img = cv2.imread("face.jpg")

    if img is None:
        print("Image not found!")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye.xml"
    )

    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    print("Eyes detected:", len(eyes))

    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imwrite("output_eye.jpg", img)
    print("Output saved as output_eye.jpg")

    cv2.imshow("Eye Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

eye_detection()
