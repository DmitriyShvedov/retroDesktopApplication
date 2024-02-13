import os
import xml.etree.ElementTree as ET

from Game import Game


def read_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    games_list = []
    for game_element in root.findall('game'):
        game_object = Game(game_element)
        games_list.append(game_object)

    get_regions(xml_path)
    return games_list


def get_regions(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    all_region_list = []
    for game_element in root.findall('game'):
        region = game_element.find("region")
        if region is not None:
            temp = region.text
            all_region_list.append(temp)

    region_list = list(dict.fromkeys(all_region_list))
    return region_list


def write_xml_changes(game):
    # Получаем абсолютный путь к текущей директории
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Формируем путь к файлу в текущей директории
    file_path = os.path.join(current_directory, "gamelist.xml")

    tree = ET.parse(file_path)
    root = tree.getroot()

    # Находим соответствующий элемент в XML по id
    for game_element in root.findall('game'):
        if game_element.get('id') == game.id:
            game_element.find('name').text = game.name
            game_element.find('region').text = game.region
            game_element.find('players').text = game.players
            game_element.find('rating').text = game.rating
            game_element.find('publisher').text = game.publisher
            game_element.find('developer').text = game.developer
            game_element.find('genre').text = game.genre
            game_element.find('desc').text = game.desc

    # Записываем изменения обратно в XML-файл
    tree.write(file_path)
