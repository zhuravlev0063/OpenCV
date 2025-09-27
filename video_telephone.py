import cv2

# URL вашей камеры. Замените на тот, который показало приложение.
url = 'http://10.248.165.23:8080/video'
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Нет сигнала с камеры")
        break

    cv2.imshow('Phone Camera', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()