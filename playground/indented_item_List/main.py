import sys
import ui
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ui.UI()
    sys.exit(app.exec())
