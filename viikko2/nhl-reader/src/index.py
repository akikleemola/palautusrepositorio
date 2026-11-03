import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

        players = sorted(
        players,
        key=lambda player: player.goals + player.assists,
        reverse=True
    )

    print("Players from FIN:")
    print()

    for player in players:
        if player.nationality == "FIN":
            print(player)

if __name__ == "__main__":
    main()
