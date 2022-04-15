# pyuic5 youtube.ui -o youtube.py
# auto-py-to-exe

import os
import sys

import youtube_dl
from PyQt5.QtWidgets import QInputDialog
from youtube_dl.utils import DownloadError

from youtube import *


# Hook class. Required for progressbar
class QHook(QtCore.QObject):
    infoChanged = QtCore.pyqtSignal(dict)

    def __call__(self, d):
        self.infoChanged.emit(d.copy())


# The class to convert. Implemented with QThread. Thread for youtube_dl to work
class Downloader(QtCore.QThread):
    infoProgress = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.url = None
        self.ydl_opts = None

    def run(self):
        try:
            self.infoProgress.emit('start')
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url])

            self.infoProgress.emit('done')
            self.infoProgress.emit('stop')
        except DownloadError:
            self.infoProgress.emit('error')

    def init_args(self, url):
        self.url = url

    def init_ydl_opts(self, ydl_opts):
        self.ydl_opts = ydl_opts


# Interface operation class
class GUI(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.progressBar.hide()

        self.download_folder = None
        self.url = None
        self.bool_answer = None
        self.status_condition_check = None

        self.thread = Downloader()
        self.thread.infoProgress.connect(self.show_info_progress)

        self.ui.linkYouTube.clicked.connect(self.get_link)
        self.ui.placeHolderChoice.clicked.connect(self.get_folder)
        self.ui.downloadAudio.clicked.connect(self.start_audio)
        self.ui.downloadVideo.clicked.connect(self.start_video)

        self.qhook = QHook()
        self.qhook.infoChanged.connect(self.show_progress_bar)

    def get_link(self):
        self.url, self.bool_answer = QInputDialog.getText(self, 'YouTube посилання',
                                                          '          Вкажіть посилання для конвертації          ')

    def get_folder(self):
        self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Вибрати папку для збереження')
        self.ui.placeHolder.setText(self.download_folder)
        if self.download_folder:
            os.chdir(self.download_folder)

    def condition_check(self):
        if self.bool_answer and self.bool_answer is not None:
            if self.download_folder:
                self.status_condition_check = True
            else:
                QtWidgets.QMessageBox.warning(self, 'Помилка', 'Потрібно вибрати папку для збереження файлу')
        else:
            QtWidgets.QMessageBox.warning(self, 'Помилка', 'Вкажіть посилання для завантаження')

    def start_audio(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            "progress_hooks": [self.qhook],
        }
        self.condition_check()
        if self.status_condition_check:
            self.thread.init_args(self.url)
            self.thread.init_ydl_opts(ydl_opts)
            self.thread.start()
            self.lock_buttons(True)

    def start_video(self):
        ydl_opts = {'format': 'bestvideo' + 'bestaudio/best', "progress_hooks": [self.qhook]}
        self.condition_check()
        if self.status_condition_check:
            self.thread.init_args(self.url)
            self.thread.init_ydl_opts(ydl_opts)
            self.thread.start()
            self.lock_buttons(True)

    def show_progress_bar(self, d):
        if d["status"] == "downloading":
            self.ui.progressBar.show()
            total = d["total_bytes"]
            downloaded = d["downloaded_bytes"]
            self.ui.progressBar.setMaximum(total)
            self.ui.progressBar.setValue(downloaded)

    def show_info_progress(self, info_status):
        if info_status == 'start':
            self.ui.lineEdit.setText('Відбувається конвертація...')
        elif info_status == 'done':
            self.ui.lineEdit.setText('Конвертація завершена')
        elif info_status == 'stop':
            self.ui.lineEdit.clear()
            self.ui.progressBar.reset()
            self.lock_buttons(False)
        elif info_status == 'error':
            self.ui.lineEdit.setText('Некоректне посилання')
            self.lock_buttons(False)

    def lock_buttons(self, lock_value):
        buttons = [self.ui.linkYouTube, self.ui.placeHolderChoice, self.ui.downloadAudio, self.ui.downloadVideo]

        for button in buttons:
            button.setDisabled(lock_value)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
