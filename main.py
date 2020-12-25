import requests
import random
import time
import json
import sys
from PyQt5 import QtWidgets
import form
import threading


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start_button_clicked)
        self.ui.stop_button.clicked.connect(self.stop_button_clicked)
        self.ui.line_to.setText("60")
        self.ui.line_from.setText("30")
        self.flag = True

    def start_button_clicked(self):
        ids = self.get_scenes()
        time_from = self.ui.line_from.text()
        time_to = self.ui.line_to.text()
        self.flag = True
        t = threading.Thread(target=self.loop_scenes, args=(ids, time_from, time_to))
        t.start()

    def stop_button_clicked(self):
        self.flag = False
        self.ui.textBrowser.append('-----STOP LOOPING-----')

    def loop_scenes(self, ids, from_time, to_time):
        self.ui.textBrowser.append("-----START LOOPING-----")
        while self.flag:
            try:
                effect = random.choice(ids)
                data = '{"id":"%s","action":"activate"}' % effect
                requests.put('http://127.0.0.1:8888/api/scenes', data=data)
                loop_time = random.randint(int(from_time), int(to_time))
                if 'strobe' in effect:
                    loop_time = 10
                self.ui.textBrowser.append(f'switch preset {effect} for {loop_time} seconds')
                time.sleep(loop_time)
            except:
                self.ui.textBrowser.append("failed to connect to ledfx")
                return

    def get_scenes(self):
        try:
            scenes_ids = json.loads(requests.get('http://127.0.0.1:8888/api/scenes').text)
            ids = []
            for preset in scenes_ids['scenes']:
                ids.append(preset)
            return ids
        except:
            self.ui.textBrowser.append("failed to connect to ledfx")


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
