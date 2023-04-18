from PySide6.QtWidgets import QLabel, QPushButton


def ImageSelector(self):
    self.select_button = QPushButton("Original image", self)
    self.select_button.move(10, 100)
    self.select_button.clicked.connect(self.select_image)
    self.select_second_button = QPushButton("Second image", self)
    self.select_second_button.move(10, 150)
    self.select_second_button.clicked.connect(self.select_second_image)
    self.read_button = QPushButton("Read message", self)
    self.read_button.move(10, 200)
    self.read_button.clicked.connect(self.read_message)
    self.hide_button = QPushButton("Hide message", self)
    self.hide_button.move(10, 150)
    self.hide_button.clicked.connect(self.hide_message)
    self.hide_button.hide()

    self.label = QLabel(self)
    self.label.setGeometry(150, 100, 200, 100)
    self.label2 = QLabel(self)
    self.label2.setGeometry(280, 100, 200, 100)
