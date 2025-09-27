import cv2

# Читаем изображение
img = cv2.imread('image.jpg')
if img is None:
    print("Ошибка загрузки изображения")
    exit()

# Конвертируем в HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Отображаем оба изображения
cv2.imshow('Original (BGR)', img)
cv2.imshow('HSV Conversion', hsv_img)

print("Нажмите любую клавишу для закрытия окон.")
cv2.waitKey(0)
cv2.destroyAllWindows()
