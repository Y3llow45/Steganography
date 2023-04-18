from PySide6.QtWidgets import QLabel, QRadioButton


def ModeSelector(self):
    self.mode_label = QLabel("Select mode:", self)
    self.mode_label.move(10, 10)
    self.hide_button = QRadioButton("Hide message", self)
    self.hide_button.move(100, 10)
    self.hide_button.setMinimumWidth(400)
    self.hide_button.clicked.connect(self.set_hide_mode)
    self.read_button = QRadioButton("Read message", self)
    self.read_button.move(250, 10)
    self.read_button.setMinimumWidth(400)
    self.read_button.setChecked(True)
    self.read_button.clicked.connect(self.set_read_mode)
