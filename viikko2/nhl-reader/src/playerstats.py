class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        def sorting(player):
            return player[0]
        players = []
        for player in self.players:
            if player.nationality == nationality:
                score = player.goals + player.goals
                players.append((score, player))
        players.sort(key=sorting, reverse=True)
        just_players = []
        for player in players:
            just_players.append(player[1])
        return just_players