import unittest

from player import Player
from player_stats import PlayerStats


class StubPlayerReader:
    def get_players(self):
        return [
            Player({
                "name": "Alex Ovechkin",
                "nationality": "RUS",
                "team": "WSH",
                "goals": 50,
                "assists": 40
            }),
            Player({
                "name": "Nathan MacKinnon",
                "nationality": "CAN",
                "team": "COL, CAR, DAL",
                "goals": 45,
                "assists": 60
            }),
            Player({
                "name": "Connor McDavid",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 40,
                "assists": 70
            }),
            Player({
                "name": "Sebastian Aho",
                "nationality": "FIN",
                "team": "CAR",
                "goals": 30,
                "assists": 50
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(StubPlayerReader())

    def test_top_scorers_by_nationality_returns_players_in_points_order(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Connor McDavid", "Nathan MacKinnon"]
        )

    def test_top_scorers_by_team_returns_players_in_points_order(self):
        players = self.stats.top_scorers_by_team("CAR")

        self.assertEqual(
            [player.name for player in players],
            ["Nathan MacKinnon", "Sebastian Aho"]
        )

    def test_top_goal_scorers_returns_requested_number_in_goal_order(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in players],
            ["Alex Ovechkin", "Nathan MacKinnon"]
        )


if __name__ == "__main__":
    unittest.main()
