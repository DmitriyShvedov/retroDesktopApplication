import pdb

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QComboBox, QLineEdit, QListWidget, \
    QListWidgetItem, QApplication, QHBoxLayout, QGridLayout, QSizePolicy
import XmlManager
from Data import FilterFields
from GameManager import GameManager


class GuiManager(QWidget):

    def __init__(self, game_manager):
        super().__init__()
        self.hbox = None
        self.path_field = None
        self.description_field = None
        self.genre_field = None
        self.developer_field = None
        self.publisher_field = None
        self.favorite_field = None
        self.hidden_field = None
        self.kid_game_field = None
        self.rating_field = None
        self.selected_game_id = None
        self.save_button = None
        self.name_field = None
        self.region_field = None
        self.players_field = None
        self.find_button = None
        self.original_games = None
        self.game_list_widget = None
        self.open_xml_button = None
        self.layout = None
        self.hbox = None
        self.game_manager = game_manager
        self.filter_fields_combo = None
        self.filter_value_input = None
        self.file_path = None

        self.init_ui()

    def __str__(self):
        return f"ID:Name: {self.name}"

    def init_ui(self):
        self.setWindowTitle('OLD SCHOOL')
        self.open_xml_button = QPushButton('Открыть файл XML')

        self.setGeometry(100, 100, 300, 300)  # Установите размер окна
        self.center()

        self.hbox = QGridLayout()
        self.hbox.setSpacing(10)

        self.hbox.addWidget(self.open_xml_button, 1, 0)

        self.setLayout(self.hbox)

        self.name_field = QLineEdit()
        self.region_field = QComboBox()
        self.players_field = QLineEdit()
        self.rating_field = QLineEdit()
        self.kid_game_field = QLineEdit()
        self.hidden_field = QLineEdit()
        self.favorite_field = QLineEdit()
        self.publisher_field = QLineEdit()
        self.developer_field = QLineEdit()
        self.genre_field = QLineEdit()
        self.description_field = QLineEdit()
        self.path_field = QLineEdit()

        self.save_button = QPushButton('Сохранить изменения')  # добавьте эту строку
        self.save_button.clicked.connect(self.save_changes)

        self.open_xml_button.clicked.connect(self.open_file_button)

    def open_file_button(self):
        file_dialog = QFileDialog()
        self.file_path, _ = file_dialog.getOpenFileName(self, 'Открыть файл XML', '', 'XML Files (*.xml)')

        if self.file_path:
            xml_data = XmlManager.read_xml(self.file_path)
            self.original_games = xml_data  # Сохраняем оригинальные данные
            self.game_manager = GameManager(xml_data)
            self.clear_layout()  # Очистить текущий макет

            self.add_filter_list_fields()
            self.add_filter_value_field()
            self.add_search_button()
            self.center()

    def show_filtered_games(self):
        selected_field = self.filter_fields_combo.currentText().lower()
        filter_value = self.filter_value_input.text()

        self.add_widget_search_list()
        self.game_list_widget.clear()

        # Применяем фильтрацию к оригинальным данным
        self.game_manager = GameManager(self.original_games)
        self.game_manager.filter_games(selected_field, filter_value)

        for game in self.game_manager.games:
            item = QListWidgetItem(f" {game.name}")
            self.game_list_widget.addItem(item)

        self.game_list_widget.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item):
        self.showMaximized()  # Вызов метода для центрирования
        # Очищаем текущее значение QLineEdit
        self.name_field.clear()
        self.region_field.clear()
        self.players_field.clear()
        self.rating_field.clear()
        self.kid_game_field.clear()
        self.hidden_field.clear()
        self.favorite_field.clear()
        self.publisher_field.clear()
        self.developer_field.clear()
        self.genre_field.clear()
        self.description_field.clear()
        self.path_field.clear()

        # Создаем метку
        name_label = QLabel("Name")
        region_label = QLabel("Region")
        players_label = QLabel("Players")
        rating_label = QLabel("Rating")
        publisher_label = QLabel("Publisher")
        developer_label = QLabel("Developer")
        genre_label = QLabel("Genre")
        description_label = QLabel("Description")

        # Находим соответствующий экземпляр Game по имени из списка
        selected_game = next((game for game in self.original_games if game.name == item.text().strip()), None)

        if selected_game:
            self.selected_game_id = selected_game.id
            self.name_field.setText(selected_game.name)

            # Очищаем текущий список значений и добавляем новые элементы из регионов
            self.region_field.clear()
            regions = XmlManager.get_regions(self.file_path)
            for region in regions:
                self.region_field.addItem(region)

            # Устанавливаем текущий регион выбранной игры
            index = self.region_field.findData(selected_game.region, Qt.DisplayRole)
            self.region_field.setCurrentIndex(index)

            self.players_field.setText(selected_game.players)
            self.rating_field.setText(selected_game.rating)
            self.publisher_field.setText(selected_game.publisher)
            self.developer_field.setText(selected_game.developer)
            self.genre_field.setText(selected_game.genre)
            self.description_field.setText(selected_game.desc)
            self.path_field.setText(selected_game.path)

        # Добавляем QLineEdit в макет, если его еще нет
        if self.hbox.indexOf(self.name_field) == -1:
            self.hbox.addWidget(name_label, 0, 1)
            self.hbox.addWidget(self.name_field, 1, 1)
            self.hbox.addWidget(region_label, 2, 1)
            self.hbox.addWidget(self.region_field, 3, 1)
            self.hbox.addWidget(players_label, 4, 1)
            self.hbox.addWidget(self.players_field, 5, 1)
            self.hbox.addWidget(rating_label, 6, 1)
            self.hbox.addWidget(self.rating_field, 7, 1)
            self.hbox.addWidget(publisher_label, 8, 1)
            self.hbox.addWidget(self.publisher_field, 9, 1)
            self.hbox.addWidget(developer_label, 10, 1)
            self.hbox.addWidget(self.developer_field, 11, 1)
            self.hbox.addWidget(genre_label, 12, 1)
            self.hbox.addWidget(self.genre_field, 13, 1)
            self.hbox.addWidget(description_label, 14, 1)
            self.hbox.addWidget(self.description_field, 15, 1, 5, 5)
            self.hbox.addWidget(self.path_field, 16, 1)

        if self.save_button:
            self.save_button.clicked.disconnect(self.save_changes)

        self.add_save_changes_button()
        self.save_button.clicked.connect(self.save_changes)

    def clear_layout(self):
        for i in reversed(range(self.hbox.count())):
            widgetItem = self.hbox.itemAt(i)
            if widgetItem is not None:
                widgetToRemove = widgetItem.widget()
                if widgetToRemove is not None:
                    self.hbox.removeWidget(widgetToRemove)
                    widgetToRemove.setParent(None)

    def add_widget_search_list(self):
        # Создаем виджет для отображения списка найденных игр
        self.game_list_widget = QListWidget(self)
        self.hbox.addWidget(self.game_list_widget, 3, 0, 10, 1)

    def add_search_button(self):
        # Создаем кнопку "Найти"
        self.find_button = QPushButton('Найти')
        self.hbox.addWidget(self.find_button)
        self.find_button.clicked.connect(self.show_filtered_games, 0, 2)


    def add_save_changes_button(self):
        if self.hbox.indexOf(self.save_button) == -1:
            self.save_button = QPushButton('Сохранить изменения')
            self.hbox.addWidget(self.save_button)

    def save_changes(self):

        edited_name = self.name_field.text()
        edited_region = self.region_field.currentText()
        edited_players = self.players_field.text()
        edited_rating = self.rating_field.text()
        edited_publisher = self.publisher_field.text()
        edited_developer = self.developer_field.text()
        edited_genre = self.genre_field.text()
        edited_desc = self.description_field.text()

        # Находим соответствующий экземпляр Game по имени из списка
        selected_game = next((game for game in self.original_games if game.id == self.selected_game_id), None)

        selected_game.name = edited_name
        selected_game.region = edited_region
        selected_game.players = edited_players
        selected_game.rating = edited_rating
        selected_game.publisher = edited_publisher
        selected_game.developer = edited_developer
        selected_game.genre = edited_genre
        selected_game.desc = edited_desc

        # Теперь обновляем XML-файл с использованием XmlManager
        XmlManager.write_xml_changes(selected_game)

        # Обновляем интерфейс, чтобы отобразить актуальные данные
        self.show_filtered_games()
        print("Changes saved successfully.")

    def add_filter_value_field(self):
        # Создаем поле ввода значения для фильтрации
        self.filter_value_input = QLineEdit(self)
        self.filter_value_input.setToolTip("Enter filter value")
        self.hbox.addWidget(self.filter_value_input, 1, 0)

    def add_filter_list_fields(self):
        # Создаем выпадающий список для выбора полей для фильтрации
        self.filter_fields_combo = QComboBox(self)
        for field in FilterFields:
            self.filter_fields_combo.addItem(field.value)
        self.hbox.addWidget(self.filter_fields_combo, 0, 0)

    def center(self):
        # Получим геометрию основного экрана
        screen_geometry = QApplication.desktop().screenGeometry()

        # Вычислим центральные координаты окна
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        # Установим окно по центру
        self.move(x, y)
