from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QComboBox, QLineEdit, QListWidget, \
    QListWidgetItem
import XmlManager
from Data import FilterFields
from GameManager import GameManager


class GuiManager(QWidget):
    def __init__(self, game_manager):
        super().__init__()
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
        self.game_manager = game_manager
        self.filter_fields_combo = None
        self.filter_value_input = None

        self.init_ui()

    def __str__(self):
        return f"ID:Name: {self.name}"

    def init_ui(self):
        self.setWindowTitle('Мое кроссплатформенное приложение')
        self.open_xml_button = QPushButton('Открыть файл XML')

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.open_xml_button)

        self.name_field = QLineEdit()
        self.region_field = QLineEdit()
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

        self.open_xml_button.clicked.connect(self.open_file_button)

    def open_file_button(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Открыть файл XML', '', 'XML Files (*.xml)')

        if file_path:
            xml_data = XmlManager.read_xml(file_path)
            self.original_games = xml_data  # Сохраняем оригинальные данные
            self.game_manager = GameManager(xml_data)
            self.clear_layout()  # Очистить текущий макет

            self.add_filter_list_fields()
            self.add_filter_value_field()
            self.add_search_button()
            self.add_widget_search_list()

    def show_filtered_games(self):
        selected_field = self.filter_fields_combo.currentText().lower()
        filter_value = self.filter_value_input.text()

        self.game_list_widget.clear()

        # Применяем фильтрацию к оригинальным данным
        self.game_manager = GameManager(self.original_games)
        self.game_manager.filter_games(selected_field, filter_value)

        for game in self.game_manager.games:
            item = QListWidgetItem(f" {game.name}")
            self.game_list_widget.addItem(item)

        self.game_list_widget.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item):
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
            self.region_field.setText(selected_game.region)
            self.players_field.setText(selected_game.players)
            self.rating_field.setText(selected_game.rating)
            self.publisher_field.setText(selected_game.publisher)
            self.developer_field.setText(selected_game.developer)
            self.genre_field.setText(selected_game.genre)
            self.description_field.setText(selected_game.desc)
            self.path_field.setText(selected_game.path)

        # Добавляем QLineEdit в макет, если его еще нет
        if self.layout.indexOf(self.name_field) == -1:
            self.layout.addWidget(name_label)
            self.layout.addWidget(self.name_field)
            self.layout.addWidget(region_label)
            self.layout.addWidget(self.region_field)
            self.layout.addWidget(players_label)
            self.layout.addWidget(self.players_field)
            self.layout.addWidget(rating_label)
            self.layout.addWidget(self.rating_field)
            self.layout.addWidget(publisher_label)
            self.layout.addWidget(self.publisher_field)
            self.layout.addWidget(developer_label)
            self.layout.addWidget(self.developer_field)
            self.layout.addWidget(genre_label)
            self.layout.addWidget(self.genre_field)
            self.layout.addWidget(description_label)
            self.layout.addWidget(self.description_field)
            self.layout.addWidget(self.path_field)

        self.add_save_changes_button()

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widgetToRemove = self.layout.itemAt(i).widget()
            self.layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

    def add_widget_search_list(self):
        # Создаем виджет для отображения списка найденных игр
        self.game_list_widget = QListWidget(self)
        self.layout.addWidget(self.game_list_widget)

    def add_search_button(self):
        # Создаем кнопку "Найти"
        self.find_button = QPushButton('Найти')
        self.layout.addWidget(self.find_button)
        self.find_button.clicked.connect(self.show_filtered_games)

    def add_save_changes_button(self):
        if self.layout.indexOf(self.save_button) == -1:
            self.save_button = QPushButton('Сохранить изменения')
            self.layout.addWidget(self.save_button)
        # Создаем кнопку "Сохранить изменнеия"
        self.save_button.clicked.connect(self.save_changes)

    def save_changes(self):

        edited_name = self.name_field.text()
        edited_region = self.region_field.text()
        edited_players = self.players_field.text()
        edited_rating = self.rating_field.text()
        edited_publisher = self.publisher_field.text()
        edited_developer = self.developer_field.text()
        edited_genre = self.genre_field.text()
        edited_desc = self.genre_field.text()

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
        self.layout.addWidget(self.filter_value_input)

    def add_filter_list_fields(self):
        # Создаем выпадающий список для выбора полей для фильтрации
        self.filter_fields_combo = QComboBox(self)
        for field in FilterFields:
            self.filter_fields_combo.addItem(field.value)
        self.layout.addWidget(self.filter_fields_combo)
