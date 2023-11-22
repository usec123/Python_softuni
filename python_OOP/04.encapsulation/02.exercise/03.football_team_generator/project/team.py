from .player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f'Player {player.name} has already joined'
        self.__players.append(player)
        return f'Player {player.name} joined team {self.__name}'

    def remove_player(self, player_name: str):
        for x in range(len(self.__players)):
            if self.__players[x].name == player_name:
                return self.__players.pop(x)
        return f'Player {player_name} not found'

    