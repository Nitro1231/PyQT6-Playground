import io
import sys
import capture
from controls import WindowPreview
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QListWidget, QListWidgetItem


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()


    def init_ui(self) -> None:
        self.setGeometry(200, 200, 700, 400)
        layout = QHBoxLayout()
        list_view = QListWidget()
        list_view.setSpacing(5)

        for hwnd, title in capture.get_open_windows():
            print(title)
            try:
                widget_object = WindowPreview(title, self.to_pixmap(capture.get_preview(hwnd)))

                widget_item = QListWidgetItem(list_view)
                widget_item.setSizeHint(widget_object.sizeHint())
                list_view.setItemWidget(widget_item, widget_object)
                list_view.addItem(widget_item)
            except Exception as e:
                print('Error:', e)

        layout.addWidget(list_view)
        self.setLayout(layout)


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
