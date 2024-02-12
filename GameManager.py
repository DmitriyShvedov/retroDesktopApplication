from typing import List

import Game


class GameManager:
    def __init__(self, xml_data):
        self.games = xml_data

    def filter_games(self, field, value):
        """Фильтрует игры по указанному полю и значению."""
        filtered_games = []
        if field == 'all':
            for game in self.games:
                for attr, attr_value in game.__dict__.items():
                    if isinstance(attr_value, str) and value in attr_value:
                        filtered_games.append(game)
                        break
        else:
            for game in self.games:
                if hasattr(game, field):
                    attr_value = getattr(game, field)
                    if isinstance(attr_value, str) and value in attr_value:
                        filtered_games.append(game)
        self.games = filtered_games


