import cv2

def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    height, width, layers = frames[0].shape
    out = cv2.VideoWriter(output_path,
                          cv2.VideoWriter_fourcc(*'XVID'),
                          20, (width, height))

    for frame in reversed(frames):
        out.write(frame)

    out.release()

reverse_video("input.mp4", "reverse_output.avi")
