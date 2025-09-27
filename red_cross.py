from random import randint
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
center_width = width // 2
center_height = height // 2

while cap.isOpened():
    ret, frame = cap.read()
    if not(ret):
        break

    # Убрали анализ цвета, теперь крестик всегда красный
    color = (0, 0, 255)  # Всегда красный цвет

    # Рисуем только контуры крестика (без заливки)
    cv2.rectangle(frame,
                  (center_width - 10, center_height - 50),
                  (center_width + 10, center_height + 50),
                  color,  # Всегда красный
                  5)
    cv2.rectangle(frame,
                  (center_width + 50, center_height - 10),
                  (center_width - 50, center_height + 10),
                  color,  # Всегда красный
                  5)

    cv2.imshow('result', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()