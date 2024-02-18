from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QLabel, QListWidget, QLineEdit, QComboBox

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


def add_widget_search_list(self, hbox):
    # Создаем виджет для отображения списка найденных игр
    self.game_list_widget = QListWidget(self)
    hbox.addWidget(self.game_list_widget, 2, 0, 23, 2)


def add_filter_value_field(self, hbox):
    # Создаем поле ввода значения для фильтрации
    self.filter_value_input = QLineEdit(self)
    self.filter_value_input.setToolTip("Enter filter value")
    self.hbox.addWidget(self.filter_value_input, 0, 0)

def add_filter_list_fields(self, hbox):
    # Создаем выпадающий список для выбора полей для фильтрации
    self.filter_fields_combo = QComboBox(self)
    for field in FilterFields:
        self.filter_fields_combo.addItem(field.value)
    self.hbox.addWidget(self.filter_fields_combo, 0, 1)


class GuiComponents:
    pass
