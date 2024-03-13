import requests
import yt_dlp
from PIL import Image
from io import BytesIO
from window.main_window_class import Ui_MainWindow, QMainWindow, QPixmap, QSize
from PySide6.QtCore import Qt

YDL_OPTS = {
    'quiet': True,  # чтобы снизить уровень вывода
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__init_reaction()

    def __init_reaction(self):
        self.ui.line_edit_url.editingFinished.connect(self.__load_image)

    def __load_image(self):
        url = self.ui.line_edit_url.text()
        if url == '':
            pass

        with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
            info_dict = ydl.extract_info(url, download=False)  # получение информации о видео без загрузки
            image_url = info_dict.get('thumbnail')
        response = requests.get(image_url)
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
        img_qt = QPixmap()
        img_qt.loadFromData(bytes_io.getvalue())
        scaled_pixmap = img_qt.scaled(self.ui.label_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.label_image.setPixmap(scaled_pixmap)
