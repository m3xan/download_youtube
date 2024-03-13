from window.main_window_class import Ui_MainWindow, QMainWindow

class MainWindow(QMainWindow):
     def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
