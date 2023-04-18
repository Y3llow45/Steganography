from PySide6.QtWidgets import QLabel, QLineEdit


def InputSelector(self):
    self.input_label = QLabel("Output image: ", self)
    self.input_label.move(10, 50)
    self.input_label.hide()
    self.input = QLineEdit(self)
    self.input.setMinimumWidth(110)
    self.input.textChanged.connect(self.on_input_changed)
    self.input.move(110, 50)
    self.input.hide()
    self.input_label_warning = QLabel("", self)
    self.input_label_warning.move(230, 50)
    self.input_label_warning.setMinimumWidth(240)
    self.input_label_warning.hide()
