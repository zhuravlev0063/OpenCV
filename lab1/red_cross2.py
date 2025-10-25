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
    if not (ret):
        break

    # Анализируем цвет центрального пикселя
    b, g, r = frame[center_height, center_width]
    if r > g and r > b:
        color = (0, 0, 255)  # Красный
    elif g > r and g > b:
        color = (0, 255, 0)  # Зеленый
    else:
        color = (255, 0, 0)  # Синий

    # Сначала рисуем залитый крестик (внутренняя часть)
    cv2.rectangle(frame,
                  (center_width - 9, center_height - 49),
                  (center_width + 9, center_height + 49),
                  color,  # Заливка цветом
                  -1)  # Толщина -1 означает заливку

    cv2.rectangle(frame,
                  (center_width + 49, center_height - 9),
                  (center_width - 49, center_height + 9),
                  color,  # Заливка цветом
                  -1)  # Толщина -1 означает заливку

    # Затем рисуем контур крестика (черная обводка)
    cv2.rectangle(frame,
                  (center_width - 10, center_height - 50),
                  (center_width + 10, center_height + 50),
                  (0, 0, 0),  # Черный контур
                  2)  # Толщина контура

    cv2.rectangle(frame,
                  (center_width + 50, center_height - 10),
                  (center_width - 50, center_height + 10),
                  (0, 0, 0),  # Черный контур
                  2)  # Толщина контура

    cv2.imshow('result', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()