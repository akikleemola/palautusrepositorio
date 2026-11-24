import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from player import Player
from query_parser import parse
from statistics import Statistics


class StaticPlayerReader:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


class QueryParserTests(unittest.TestCase):
    def test_parses_team_condition(self):
        matcher = parse("team = NYR")

        self.assertTrue(matcher.test(Player("Player", "NYR", 0, 0)))
        self.assertFalse(matcher.test(Player("Player", "PHI", 0, 0)))

    def test_parses_at_least_condition(self):
        matcher = parse("goals >= 10")

        self.assertTrue(matcher.test(Player("Player", "NYR", 10, 0)))
        self.assertFalse(matcher.test(Player("Player", "NYR", 9, 0)))

    def test_parses_fewer_than_condition(self):
        matcher = parse("goals < 10")

        self.assertTrue(matcher.test(Player("Player", "NYR", 9, 0)))
        self.assertFalse(matcher.test(Player("Player", "NYR", 10, 0)))

    def test_parses_signed_integer_values(self):
        self.assertTrue(parse("goals >= -1").test(Player("Player", "NYR", 0, 0)))
        self.assertTrue(parse("goals < +1").test(Player("Player", "NYR", 0, 0)))

    def test_combines_two_conditions_with_and(self):
        matcher = parse("team = NYR and goals >= 10")

        self.assertTrue(matcher.test(Player("Player", "NYR", 10, 0)))
        self.assertFalse(matcher.test(Player("Player", "NYR", 9, 0)))
        self.assertFalse(matcher.test(Player("Player", "PHI", 10, 0)))

    def test_combines_multiple_conditions_with_and(self):
        matcher = parse("team = NYR and assists >= 10 and goals < 20")

        self.assertTrue(matcher.test(Player("Player", "NYR", 15, 10)))
        self.assertFalse(matcher.test(Player("Player", "NYR", 20, 10)))
        self.assertFalse(matcher.test(Player("Player", "NYR", 15, 9)))

    def test_combines_conditions_with_or(self):
        matcher = parse("team = NYR or team = PHI")

        self.assertTrue(matcher.test(Player("Player", "NYR", 0, 0)))
        self.assertTrue(matcher.test(Player("Player", "PHI", 0, 0)))
        self.assertFalse(matcher.test(Player("Player", "EDM", 0, 0)))

    def test_and_binds_more_tightly_than_or(self):
        matcher = parse(
            "team = PHI and assists >= 10 and goals < 10 "
            "or team = EDM and points >= 50"
        )

        self.assertTrue(matcher.test(Player("PHI match", "PHI", 9, 10)))
        self.assertFalse(matcher.test(Player("PHI goals", "PHI", 10, 10)))
        self.assertFalse(matcher.test(Player("PHI assists", "PHI", 9, 9)))
        self.assertTrue(matcher.test(Player("EDM match", "EDM", 30, 20)))
        self.assertFalse(matcher.test(Player("EDM points", "EDM", 20, 29)))

    def test_invalid_queries_raise_value_error(self):
        for query in (
            "",
            "team =",
            "goals > 10",
            "goals >= ten",
            "team = NYR and",
            "team = NYR or",
        ):
            with self.subTest(query=query):
                with self.assertRaises(ValueError):
                    parse(query)

    def test_parsed_matcher_works_with_statistics_matches(self):
        players = [
            Player("NYR scorer", "NYR", 10, 0),
            Player("PHI scorer", "PHI", 10, 0),
        ]
        statistics = Statistics(StaticPlayerReader(players))

        matches = statistics.matches(parse("team = NYR and goals >= 10"))

        self.assertEqual(matches, [players[0]])


if __name__ == "__main__":
    unittest.main()
