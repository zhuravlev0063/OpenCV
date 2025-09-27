import cv2

# Путь к изображению (замените на свой)
img_path = 'image.jpg'

# Тестируем три флага для чтения
flags_read = [cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED]
flags_read_names = ['COLOR', 'GRAYSCALE', 'UNCHANGED']

# Тестируем три флага для создания окна
flags_window = [cv2.WINDOW_NORMAL, cv2.WINDOW_AUTOSIZE, cv2.WINDOW_FREERATIO]
flags_window_names = ['NORMAL', 'AUTOSIZE', 'FREERATIO']

for i, (flag_r, name_r) in enumerate(zip(flags_read, flags_read_names)):
    # Читаем изображение с текущим флагом
    img = cv2.imread(img_path, flag_r)
    if img is None:
        print(f"Ошибка загрузки изображения с флагом {name_r}")
        continue

    for j, (flag_w, name_w) in enumerate(zip(flags_window, flags_window_names)):
        # Создаем окно с текущим флагом
        win_name = f'Read: {name_r} | Window: {name_w}'
        cv2.namedWindow(win_name, flag_w)
        cv2.imshow(win_name, img)

        # Ждем нажатия любой клавиши для перехода к следующему
        print(f"Отображено: {win_name}. Нажмите любую клавишу для продолжения.")
        cv2.waitKey(0)
        cv2.destroyWindow(win_name)

cv2.destroyAllWindows()