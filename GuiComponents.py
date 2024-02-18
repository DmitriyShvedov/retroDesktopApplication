from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QLabel, QListWidget, QLineEdit, QComboBox, QPushButton, \
    QApplication

from Data import FilterFields


def create_tab_widget():
    # Создаем QTabWidget
    tab_widget = QTabWidget()
    # Создаем вкладки
    video = QWidget()
    picture = QWidget()

    # Добавляем содержимое на вкладки
    video_layout = QVBoxLayout(video)
    video_layout.addWidget(QLabel("Content for Tab 1"))
    video.setLayout(video_layout)

    picture_layout = QVBoxLayout(picture)
    picture_layout.addWidget(QLabel("Content for Tab 2"))
    picture.setLayout(picture_layout)

    # Добавляем вкладки в QTabWidget
    tab_widget.addTab(video, "Video")
    tab_widget.addTab(picture, "Picture")
    return tab_widget


def add_widget_search_list(self):
    # Создаем виджет для отображения списка найденных игр
    self.game_list_widget.clear()
    self.hbox.addWidget(self.game_list_widget, 2, 0, 23, 2)


def add_filter_value_field(self):
    # Создаем поле ввода значения для фильтрации
    self.filter_value_input = QLineEdit(self)
    self.filter_value_input.setToolTip("Enter filter value")
    self.hbox.addWidget(self.filter_value_input, 0, 0)


def add_filter_list_fields(self):
    # Создаем выпадающий список для выбора полей для фильтрации
    self.filter_fields_combo = QComboBox(self)
    for field in FilterFields:
        self.filter_fields_combo.addItem(field.value)
    self.hbox.addWidget(self.filter_fields_combo, 0, 1)


def add_search_button(self):
    # Создаем кнопку "Найти"
    self.find_button = QPushButton('Search')
    self.hbox.addWidget(self.find_button, 1, 0, 1, 2)
    self.find_button.clicked.connect(self.show_filtered_games, 0, 2)


def center(self):
    # Получим геометрию основного экрана
    screen_geometry = QApplication.desktop().screenGeometry()

    # Вычислим центральные координаты окна
    x = (screen_geometry.width() - self.width()) // 2
    y = (screen_geometry.height() - self.height()) // 2

    # Установим окно по центру
    self.move(x, y)


def add_save_changes_button(self):
    if self.hbox.indexOf(self.save_button) == -1:
        self.hbox.addWidget(self.save_button, 25, 4, 1, 2)


def clear_layout(self):
    for i in reversed(range(self.hbox.count())):
        widgetItem = self.hbox.itemAt(i)
        if widgetItem is not None:
            widgetToRemove = widgetItem.widget()
            if widgetToRemove is not None:
                self.hbox.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)


class GuiComponents:
    pass
