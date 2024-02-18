import os

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QLabel, QListWidget, QLineEdit, QComboBox, QPushButton, \
    QApplication

from Data import FilterFields

# Получить текущую рабочую директорию
current_directory = os.getcwd()


def get_image():
    # Путь к вашему изображению
    image_path = "image.php.png"

    label = QLabel()
    pixmap = QPixmap(image_path)
    label.setPixmap(pixmap)
    label.show()
    return label



def hide_button(button, media_player):
    button.hide()
    media_player.play()

def get_video(video_layout, video_widget):
    # Получить текущую рабочую директорию
    current_directory = os.getcwd()

    # Создать путь к файлу в текущей директории
    file_name = 'Gals Panic SS Japan - Sega Saturn.mp4'
    # Путь к вашему файлу относительно текущей рабочей директории
    video_path = os.path.join(current_directory, file_name)

    # Создаем медиаплеер и настраиваем виджет видео
    media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
    video_player = QVideoWidget()
    video_layout.addWidget(video_player)

    # Создаем кнопку для воспроизведения видео
    play_button = QPushButton("Play")
    pause_button = QPushButton("Pause")
    video_layout.addWidget(play_button)
    video_layout.addWidget(pause_button)

    play_button.clicked.connect(lambda: media_player.play())
    pause_button.clicked.connect(lambda: media_player.pause())

    # Загружаем видео и отображаем виджет
    media_content = QMediaContent(QUrl.fromLocalFile(video_path))
    media_player.setMedia(media_content)
    media_player.setVideoOutput(video_player)
    video_widget.show()


def create_tab_widget():
    # Создаем QTabWidget
    tab_widget = QTabWidget()
    # Создаем вкладки
    video_widget = QWidget()
    picture = QWidget()

    # Добавляем содержимое на вкладки
    video_layout = QVBoxLayout(video_widget)
    video_layout.addWidget(get_video(video_layout, video_widget))
    video_widget.setLayout(video_layout)

    picture_layout = QVBoxLayout(picture)
    picture_layout.addWidget(get_image())
    picture.setLayout(picture_layout)

    # Добавляем вкладки в QTabWidget
    tab_widget.addTab(video_widget, "Video")
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
