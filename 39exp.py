def reverse_slow(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    for frame in reversed(frames):
        cv2.imshow("Reverse Slow", frame)
        if cv2.waitKey(100)==27:
            break

    cap.release()
    cv2.destroyAllWindows()

reverse_slow("video.mp4")
