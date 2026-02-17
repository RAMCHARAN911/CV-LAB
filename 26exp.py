import cv2

def reverse_video():
    cap = cv2.VideoCapture("input_video.mp4")

    if not cap.isOpened():
        print("Error: Cannot open video file")
        return

    frames = []

    # Read all frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        print("No frames found!")
        return

    height, width, layers = frames[0].shape
    fps = 20

    # Create output video
    out = cv2.VideoWriter(
        "reverse_output.mp4",
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
    )

    # Write frames in reverse order
    for frame in reversed(frames):
        out.write(frame)

    out.release()

    print("✅ Reverse video saved as reverse_output.mp4")

reverse_video()
