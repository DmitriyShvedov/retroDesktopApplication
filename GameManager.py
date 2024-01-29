from typing import List

import Game


class GameManager:
    def __init__(self, xml_data):
        self.games = xml_data

    def filter_games(self, field, value):
        """Фильтрует игры по указанному полю и значению."""
        filtered_games = []
        if field == 'all':
            # TO DOO !!!!!!
            for game in self.games:
                match = all(getattr(game, game_field) == game_value for game_field, game_value in vars(game).items())
                if match:
                    filtered_games.append(game)
        else:
            for game in self.games:
                if getattr(game, field) == value:
                    filtered_games.append(game)
        self.games = filtered_games


