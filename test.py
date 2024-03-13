import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
import sys
from io import BytesIO
from PIL import Image

app = QApplication(sys.argv)

# Создаем главное окно
main_window = QMainWindow()
main_window.setGeometry(100, 100, 400, 200)

# Загружаем изображение из интернета
url = 'https://i.ytimg.com/vi/V4_QiGVQzKg/maxresdefault.jpg'
response = requests.get(url)
image_data = BytesIO(response.content)

# Открываем изображение с помощью PIL
img_pil = Image.open(image_data)

# Преобразуем изображение в формат, поддерживаемый PySide6
img_pil = img_pil.convert("RGBA")
# w, h = img_pil.size
bytes_io = BytesIO()
img_pil.save(bytes_io, format="PNG")
bytes_io.seek(0)

# Создаем QPixmap из изображения
pixmap = QPixmap()
pixmap.loadFromData(bytes_io.getvalue())

# Создаем QLabel и устанавливаем на нее изображение
label = QLabel(main_window)
label.setPixmap(pixmap)

# Отображаем окно
main_window.show()
sys.exit(app.exec())