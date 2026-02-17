import cv2

def smile_detection():
    img = cv2.imread("face.jpg")

    if img is None:
        print("Image not found!")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    smile_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_smile.xml"
    )

    smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)

    print("Smiles detected:", len(smiles))

    for (x, y, w, h) in smiles:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imwrite("output_smile.jpg", img)
    print("Output saved as output_smile.jpg")

    cv2.imshow("Smile Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

smile_detection()
