import requests
from player import Player
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    """url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    def sorting(player):
        return player[0]
    
    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)
    
    FIN_players = []


    print("Players from FIN \n")
    for player in players:
        if player.nationality == "FIN":
            score = player.goals + player.goals
            FIN_players.append((score, player))
    
    FIN_players.sort(key=sorting, reverse=True)

    for player in FIN_players:
        print(f"{player[1].name:20}    {player[1].team}    {player[1].goals} + {player[1].assists} = {player[0]}")"""

    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
