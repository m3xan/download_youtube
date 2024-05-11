from window.second_window.download.download_class import Ui_Dialog, QDialog

class DownLoadDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()

    def update(self, signall):
        print(signall)
        self.ui.progressBar.setValue(signall)

    def _set(self, signall):
        self.ui.progressBar.setRange(signall[0], signall[1])
