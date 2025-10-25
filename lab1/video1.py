import cv2

cap = cv2.VideoCapture('../video1.mp4')

if not cap.isOpened():
    print("Ошибка открытия видео потока")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Изменение размера для удобства отображения
    frame = cv2.resize(frame, (640, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('Original', frame)
    cv2.imshow('Grayscale', gray)
    cv2.imshow('HSV', hsv)

    # Выход по 'q' с нормальной скоростью видео
    if cv2.waitKey(25000) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()