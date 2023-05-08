import requests
import subprocess
import sys
import urllib3
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

APP_VERSION = "0.0.9"

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn = QPushButton('Click me', self)
        btn.setToolTip('Click to show message box')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(lambda: self.check_for_updates(APP_VERSION)) # call check_for_updates with current_version parameter
        # btn.clicked.connect(self.showMessageBox)

        self.setGeometry(300, 300, 1000, 400)
        self.setWindowTitle('Example')
        self.show()

    def showMessageBox(self):
        QMessageBox.information(self, 'Message', 'Hello, world!')

    def check_for_updates(self, current_version):     
        try:
            http = urllib3.PoolManager()
            url = 'https://raw.githubusercontent.com/TBAZ123/Test_Python_WinApp_Update22/main/version.txt'
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data)
            QMessageBox.critical(None, 'Error', f'Failed to check for updates: {soup}')
            # latest_release = response.json()
            latest_version = float(response.data)
            current_version = float(current_version)
            if latest_version > current_version:
                QMessageBox.critical(None, 'Error', f'Failed to check for updatessss: {response.data}')
                # reply = QMessageBox.question(None, 'Update available',
                #                              f'A new version ({latest_version}) is available. Do you want to update?',
                #                              QMessageBox.Yes | QMessageBox.No)
                # if reply == QMessageBox.Yes:
                #     # Download the latest release of the application along with its version file.
                #     for asset in latest_release['assets']:
                #         url = asset['browser_download_url']
                #         filename = asset['name']
                #         if filename == 'main.py' or filename == 'version.txt':
                #             response = requests.get(url)
                #             with open(filename, 'wb') as f:
                #                 f.write(response.content)
                #     # Exit the current instance of the application and launch the newly downloaded executable.
                #     subprocess.Popen(['python', 'main.py'])
                #     sys.exit(0)
            else:
                QMessageBox.information(None, 'No update available', 'You have the latest version of the application.')
        except Exception as e:
            QMessageBox.critical(None, 'Error', f'Failed to check for updates: {e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
