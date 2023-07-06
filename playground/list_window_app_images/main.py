from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion, QImage
from PyQt6.QtCore import Qt
import sys
import capture
import win32gui
 
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('Python QLabel')
        self.setWindowIcon(QIcon('qt.png'))
 
        hwnd = win32gui.FindWindow(None, '계산기')
        img = capture.get_preview(hwnd)
 
        label = QLabel(self)
        pixmap = QPixmap(ImageQt(img))
        label.setPixmap(pixmap)
 
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())