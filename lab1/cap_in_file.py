import cv2

cap = cv2.VideoCapture(0)

# Определяем кодек и создаем VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../webcam_output.avi', fourcc, 20.0, (640, 480)) # FPS и размер должны соответствовать источнику

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Записываем кадр
    out.write(frame)

    cv2.imshow('Webcam Recording', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()