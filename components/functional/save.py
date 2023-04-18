from time import gmtime, strftime


def Save(self, result):
    if self.checkbox.isChecked():
        output_file = str(strftime("%Y-%m-%d-%H-%M-%S", gmtime()))
        with open(f"{output_file}.txt", "w") as f:
            f.write(result)
