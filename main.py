
from PyQt5.QtWidgets import QApplication

import GuiManager
from GameManager import GameManager

if __name__ == '__main__':
    app = QApplication([])
    xml_data = []  # Пустой список по умолчанию, будет заполнен при открытии файла
    game_manager = GameManager(xml_data)
    window = GuiManager.GuiManager(game_manager)
    window.show()
    app.exec_()
