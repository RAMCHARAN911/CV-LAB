import cv2
import os

def detect_face_and_save(input_image, output_image):
    # Check if file exists
    if not os.path.exists(input_image):
        print("❌ Input image not found!")
        return

    # Read image
    img = cv2.imread(input_image)

    if img is None:
        print("❌ Error loading image!")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load face cascade
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    print("Number of faces detected:", len(faces))

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Save output image
    save_status = cv2.imwrite(output_image, img)

    if save_status:
        print("✅ Output image saved successfully as:", output_image)
    else:
        print("❌ Failed to save image")

    # Display image
    cv2.imshow("Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Use your file name here
detect_face_and_save("face.jpg", "output_face.jpg")
