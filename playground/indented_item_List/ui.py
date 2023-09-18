from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QPushButton,
    QGridLayout,
    QCheckBox,
    QComboBox,
    QSlider,
    QFileDialog,
    QPlainTextEdit
)
from qt_material import apply_stylesheet


class UI(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initialize_ui()
        self.show()

    def initialize_ui(self) -> None:
        apply_stylesheet(self, theme='dark_lightgreen.xml')

        self.main_tabs = QTabWidget()

        box_layout = QVBoxLayout()
        box_layout.addWidget(self.main_tabs)

        self.setLayout(box_layout)
        self.setWindowTitle('Indented Item List')
