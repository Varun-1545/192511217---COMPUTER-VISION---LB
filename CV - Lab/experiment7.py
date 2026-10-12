import cv2

# Read the captured video
video = cv2.VideoCapture("video.mp4")

if not video.isOpened():
    print("Video not found")
else:
    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Display the video
        cv2.imshow("Video", frame)

        # Press q to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()