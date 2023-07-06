import io
import sys
import capture
import win32gui
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('Python QLabel')
 
        hwnd = win32gui.FindWindow(None, '계산기')
        img = capture.get_preview(hwnd)
 
        self.label = QLabel(self)
        self.label.setPixmap(self.to_pixmap(img))


    def to_pixmap(self, image: Image) -> QPixmap:
        byte_array = io.BytesIO()
        image.save(byte_array, format='PNG')
        qimage = QImage.fromData(byte_array.getvalue())
        return QPixmap.fromImage(qimage)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())