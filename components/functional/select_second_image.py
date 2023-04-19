from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


def SelectSecondImage(self, TXT_OPEN_SECOND_IMAGE, ERR_UPLOAD):
    file_path, _ = QFileDialog.getOpenFileName(
        self, TXT_OPEN_SECOND_IMAGE)
    pixmap = QPixmap(file_path).scaled(
        100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    if pixmap.isNull():
        self.handle_errors_and_text(self.label2, ERR_UPLOAD)
        self.si = False
        return
    self.si = True
    self.simg = file_path
    self.label2.setPixmap(pixmap)
