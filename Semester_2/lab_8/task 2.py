import cv2


def video_processing():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    #fly = cv2.imread('fly64.png')
    fly = cv2.imread('fly64.png', cv2.IMREAD_UNCHANGED)
    fly_rgb = fly[:, :, :3]
    alpha = fly[:, :, 3] / 255.0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            fly_y, fly_x = fly.shape[:2]
            center_x = x + w // 2
            center_y = y + h // 2
            y1, y2 = center_y - fly_y // 2, center_y + fly_y // 2
            x1, x2 = center_x - fly_x // 2, center_x + fly_x // 2

            cv2.putText(frame, f'{center_x}:{center_y}', (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            if 32 < center_x < (frame.shape[1] - 32) and 32 < center_y < (frame.shape[0] - 32):
                for c in range(3):
                    frame[y1:y2, x1:x2, c] = (alpha * fly_rgb[:, :, c] + (1.0 - alpha) * frame[y1:y2, x1:x2, c])

        cv2.imshow('cam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

video_processing()
cv2.waitKey(0)
cv2.destroyAllWindows()