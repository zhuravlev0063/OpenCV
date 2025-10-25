import cv2

# Источник видео (файл или камера)
cap = cv2.VideoCapture('../video1.mp4')

# Получаем параметры исходного видео
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Определяем кодек и создаем объект VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Пример кодека
out = cv2.VideoWriter('../output_video.avi', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)  # Записываем кадр

    cv2.imshow('Recording...', frame)
    if cv2.waitKey(10000) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()