from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel

WIDTH = 192
HEIGHT = 108
MARGIN = 10
TITLE_LIMIT = 26

class WindowPreview(QFrame):
    def __init__(self, title: str, image: QPixmap) -> None:
        super().__init__()
        self.title = (title[:TITLE_LIMIT] + '...') if len(title) > TITLE_LIMIT else title
        self.image = image
        self.init_ui()


    def init_ui(self) -> None:
        self.setFixedWidth(WIDTH + 2 * MARGIN)
        layout = QVBoxLayout()
        layout.setContentsMargins(MARGIN, MARGIN, MARGIN, MARGIN)
        self.setLayout(layout)

        # Title label
        title_label = QLabel(self.title)
        title_label.setFixedSize(WIDTH, 16)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Image label
        picture_box = QLabel()
        picture_box.setFixedSize(WIDTH, HEIGHT)
        picture_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        picture_box.setPixmap(self.image.scaled(WIDTH, HEIGHT, Qt.AspectRatioMode.KeepAspectRatio))
        layout.addWidget(picture_box)

        title_label.setStyleSheet('QWidget { color: white; border: none; }')
        picture_box.setStyleSheet('QWidget { background-color: #1e1f22; border-radius: 10px; border: none; }')
        self.setStyleSheet('QFrame { background-color: #313338; border-radius: 10px; } QFrame:hover { border: solid; border-width: 2px; border-radius: 10px; border-color: #5865f2; }')
