from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


def SelectImage(self, TXT_OPEN_IMAGE, ERR_UPLOAD):
    file_path, _ = QFileDialog.getOpenFileName(self, TXT_OPEN_IMAGE)
    pixmap = QPixmap(file_path).scaled(
        100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    if pixmap.isNull():
        self.handle_errors_and_text(self.label, ERR_UPLOAD)
        self.oi = False
        return
    self.oi = True
    self.oimg = file_path
    self.label.setPixmap(pixmap)
