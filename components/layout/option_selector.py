from PySide6.QtWidgets import QLabel, QCheckBox


def OptionSelector(self):
    self.option_label = QLabel("Select option:", self)
    self.option_label.move(10, 50)
    self.checkbox = QCheckBox("Save to file", self)
    self.checkbox.move(113, 50)
    self.checkbox.setFixedWidth(self.checkbox.fontMetrics(
    ).boundingRect(self.checkbox.text()).width() + 41)
