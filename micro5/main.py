from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


if __name__ == '__main__':
    import sys
    application = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(320, 240)
    widget.setWindowTitle("Hello, World!")
    widget.show()
    sys.exit(application.exec_())
