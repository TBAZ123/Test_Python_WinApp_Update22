import requests
import subprocess
import sys
from PyQt5.QtWidgets import QMessageBox

def check_for_updates(current_version):
    try:
        response = requests.get('https://github.com/TBAZ123/Test_Python_WinApp_Update22')
        if response.status_code != 200:
            raise Exception(f'Failed to fetch latest release: {response.text}')
        latest_release = response.json()
        latest_version = latest_release['tag_name'].strip('v')
        if latest_version > current_version:
            reply = QMessageBox.question(None, 'Update available',
                                         f'A new version ({latest_version}) is available. Do you want to update?',
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Download the latest release of the application along with its version file.
                for asset in latest_release['assets']:
                    url = asset['browser_download_url']
                    filename = asset['name']
                    if filename == 'main.py' or filename == 'version.txt':
                        response = requests.get(url)
                        with open(filename, 'wb') as f:
                            f.write(response.content)
                # Exit the current instance of the application and launch the newly downloaded executable.
                subprocess.Popen(['python', 'main.py'])
                sys.exit(0)
        else:
            QMessageBox.information(None, 'No update available', 'You have the latest version of the application.')
    except Exception as e:
        QMessageBox.critical(None, 'Error', f'Failed to check for updates: {e}')
