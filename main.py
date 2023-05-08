import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn = QPushButton('Click me', self)
        btn.setToolTip('Click to show message box')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(self.showMessageBox)

        self.setGeometry(300, 300, 1000, 400)
        self.setWindowTitle('Example')
        self.show()

    def showMessageBox(self):
        QMessageBox.information(self, 'Message', 'Hello, world!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
