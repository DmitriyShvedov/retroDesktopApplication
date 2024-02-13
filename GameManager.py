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
        elif field == "missing region":
            for game in self.games:
                if getattr(game, "region") is None:
                    filtered_games.append(game)

        elif field == "missing developer":
            for game in self.games:
                if getattr(game, "developer") is None:
                    filtered_games.append(game)

        elif field == "missing publisher":
            for game in self.games:
                if getattr(game, "publisher") is None:
                    filtered_games.append(game)

        elif field == "missing genre":
            for game in self.games:
                if getattr(game, "genre") is None:
                    filtered_games.append(game)

        elif field == "missing rating":
            for game in self.games:
                if getattr(game, "rating") is None:
                    filtered_games.append(game)

        elif field == "missing number of players":
            for game in self.games:
                if getattr(game, "players") is None:
                    filtered_games.append(game)

        elif field == "missing picture":
            for game in self.games:
                if getattr(game, "image") is None:
                    filtered_games.append(game)

        elif field == "missing video":
            for game in self.games:
                if getattr(game, "video") is None:
                    filtered_games.append(game)

        elif field == "missing date":
            for game in self.games:
                date_game = game.releaseDate
                if date_game is None:
                    filtered_games.append(game)

        elif field == "missing description":
            for game in self.games:
                if getattr(game, "desc") is None:
                    filtered_games.append(game)

        elif field == "date":
            date = Game.convertDateToISO(value)
            for game in self.games:
                date_game = game.releaseDate
                if date_game is not None and date in date_game:
                    filtered_games.append(game)

        else:
            for game in self.games:
                if hasattr(game, field):
                    attr_value = getattr(game, field)
                    if isinstance(attr_value, str) and value in attr_value:
                        filtered_games.append(game)
        self.games = filtered_games
