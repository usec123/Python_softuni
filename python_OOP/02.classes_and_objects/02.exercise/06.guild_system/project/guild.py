from .player import Player

class Guild:
    def __init__(self, name:str) -> None:
        self.name = name
        self.players = []
    
    def assign_player(self,player:Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self,player_name:str):
        for x in range(len(self.players)):
            if self.players[x].name == player_name:
                self.players[x].guild = 'Unaffiliated'
                self.players.pop(x)
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        players_text = "\n".join([player.player_info() for player in self.players])
        return f'Guild: {self.name}\n{players_text}'
