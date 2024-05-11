
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import requests
import yt_dlp
from PIL import Image
from PySide6.QtCore import Qt

from PySide6.QtCore import QThread, Signal
from window.second_window.download.download import DownLoadDialog

from window.main_window_class import Ui_MainWindow, QMainWindow, QPixmap

YDL_OPTS = {
    'quiet': True,
    'writethumbnail': False,
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'outtmpl': 'downloads{/%(title)s.%(ext)s}',
    'socket_timeout': 5,  # чтобы снизить уровень вывода
    'allow_multiple_video_streams': True,
    'retries': 20,
    'fragment_retries': 10,
    'ffmpeg_location': 'ffmpeg',
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__init_reaction()

    def __init_reaction(self):
        self.ui.line_edit_url.editingFinished.connect(self.__load_image)
        self.ui.push_button_download.clicked.connect(self.__load_video)
        
    def __load_video(self):
        url = self.ui.line_edit_url.text()
        if url == '':
            pass
        self.window_download = DownLoadDialog()
        self.window_download.exec()
        self.tread = DownLoadThread(url, self)
        self.tread.update.connect(self.window_download.update)
        self.tread._range.connect(self.window_download._set)
        self.tread.start()

    def __load_image(self):
        url = self.ui.line_edit_url.text()
        if url == '':
            pass
        self.load_thead = LoadImageThread(url)
        self.load_thead.pix_map.connect(self.__set_pix_map)
        self.load_thead.start()

    def __set_pix_map(self, pixmap: QPixmap):
        scaled_pixmap = pixmap.scaled(self.ui.label_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.label_image.setPixmap(scaled_pixmap)

class DownLoadThread(QThread):
    """
    Core for download
    """
    update: Signal = Signal(int)
    _range: Signal = Signal(tuple)
    def  __init__(self, url: str, perent: MainWindow):
        super().__init__()
        self.url = url
        self.perent = perent
        self.setRange = False
        self.YDL_OPTS = {
            'quiet': True,
            'writethumbnail': False,
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            'outtmpl': f'downloads{'/%(title)s.%(ext)s'}',
            'socket_timeout': 5,  # чтобы снизить уровень вывода
            'allow_multiple_video_streams': True,
            'retries': 20,
            'fragment_retries': 10,
            'ffmpeg_location': 'ffmpeg',
            'progress_hooks': [self.my_hook]
        }

    def run(self):
        with yt_dlp.YoutubeDL(self.YDL_OPTS) as ydl:
            ydl.download([self.url])

    def my_hook(self, d):
        if d['status'] == 'downloading':
            if self.setRange:
                self._range.emit((0, d["fragment_count"]))
                self.update.emit(d["fragment_index"])
            else:
                self.update.emit(d["fragment_index"])

class LoadImageThread(QThread):
    """
    Core for download
    """
    pix_map: Signal = Signal(QPixmap)
    def  __init__(self, url: str):
        super().__init__()
        self.url = url

    def run(self):
        with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
            info_dict = ydl.extract_info(self.url, download=False)  # получение информации о видео без загрузки
            image_url = info_dict.get('thumbnail')
        executor = ThreadPoolExecutor()
        future = executor.submit(self.load_image, image_url)
        img_qt = future.result()  # Получаем результат выполнения функции в отдельном потоке

        self.pix_map.emit(img_qt)

    @staticmethod
    def load_image(image_url):
        response = requests.get(image_url, timeout=10)
        image_data = BytesIO(response.content)

        img_pil = Image.open(image_data)
        img_pil = img_pil.convert("RGBA")

        bytes_io = BytesIO()
        img_pil.save(bytes_io, format="PNG")
        bytes_io.seek(0)

        img_qt = QPixmap()
        img_qt.loadFromData(bytes_io.getvalue())
        return img_qt
