from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage

import cv2
import datetime


class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)
    changeLabel = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True

    def run(self):
        cap = cv2.VideoCapture(self.stream)
		
        while self.isRunning:
            ret, frame = cap.read()

            if True:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

                # This signal can be used to show a failure on screen
                now = datetime.datetime.now()
                sec = now.second
                self.changeLabel.emit(str(sec))
            else:
                pass
                #break

    def stop(self):
        self.isRunning = False
        self.quit()
        self.wait()