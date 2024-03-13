"""
Главный запускаемый файл проекта
"""
import sys

from PySide6.QtWidgets import QApplication

from window.main_window import MainWindow

def main() -> None:
    """
    Проверяет наличие файлов для загрузки и 
    открывает приложение
    """
    app = QApplication(sys.orig_argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
