import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

APP_VERSION = "1.0.1"
APP_PATH = "D:\Works\STD\Test_Python_WinApp_Update22"
GIT_REMOTE_URL  = "https://github.com/TBAZ123/Test_Python_WinApp_Update22.git"

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
        latest_version = self.check_for_updates()
        if latest_version != APP_VERSION:
            reply = QMessageBox.question(self, 'Update Available', f"A new version ({latest_version}) is available! Would you like to download and install it now?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.update_application(latest_version)
        else:
            QMessageBox.information(self, 'Message', 'Hello, world! (no update available)')

    def check_for_updates(self):
        # Fetch the latest changes from the remote repository
        subprocess.run(f"cd {APP_PATH} && git fetch", shell=True)
        # Get the latest version number from the remote repository
        latest_version = subprocess.check_output(f"cd {APP_PATH} && git tag | sort -V | tail -1", shell=True).decode().strip()
        return latest_version

    def update_application(self, latest_version):
        # Update the application to the latest version
        subprocess.run(f"cd {APP_PATH} && git checkout {latest_version}", shell=True)
        # Update the version number of the application
        with open(f"{APP_PATH}/version.txt", "w") as f:
            f.write(latest_version)
        # Download the latest version of the application
        subprocess.run(f"cd {APP_PATH} && wget -O latest_version.zip {GIT_REMOTE_URL}/archive/{latest_version}.zip", shell=True)
        # Check if the file exists before removing it
        if os.path.exists(f"{APP_PATH}/latest_version.zip"):
            # Remove the previous installation
            subprocess.run(f"cd {APP_PATH} && rm -rf *", shell=True)
            # Unzip the latest version of the application
            subprocess.run(f"cd {APP_PATH} && unzip latest_version.zip -d .", shell=True)
            # Install any dependencies required by the new version of the application
            subprocess.run(f"cd {APP_PATH} && pip install -r requirements.txt", shell=True)
            QMessageBox.information(self, 'Message', 'Installation complete!')
        else:
            QMessageBox.warning(self, 'Error', 'Failed to download the latest version.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
