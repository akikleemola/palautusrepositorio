class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player in self._players:
            if player.nationality == nationality:
                players.append(player)

        return sorted(
            players,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

    def top_scorers_by_team(self, team):
        players = []

        for player in self._players:
            teams = [player_team.strip() for player_team in player.team.split(",")]
            if team in teams:
                players.append(player)

        return sorted(
            players,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa.

        Pelaajat palautetaan maalimäärän mukaan laskevassa järjestyksessä.
        """
        return sorted(
            self._players,
            key=lambda player: player.goals,
            reverse=True
        )[:how_many]
