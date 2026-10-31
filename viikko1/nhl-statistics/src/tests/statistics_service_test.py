import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_pelaajan(self):
        pelaaja = self.stats.search("Kurri")

        self.assertIsNotNone(pelaaja)
        self.assertEqual(pelaaja.name, "Kurri")

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        pelaaja = self.stats.search("Selänne")

        self.assertIsNone(pelaaja)

    def test_team_palauttaa_joukkueen_pelaajat(self):
        pelaajat = self.stats.team("EDM")
        nimet = [pelaaja.name for pelaaja in pelaajat]

        self.assertEqual(nimet, ["Semenko", "Kurri", "Gretzky"])

    def test_team_palauttaa_tyhjan_listan_jos_joukkuetta_ei_loydy(self):
        pelaajat = self.stats.team("BOS")

        self.assertEqual(pelaajat, [])

    def test_top_palauttaa_kolme_parasta_pistejarjestyksessa(self):
        pelaajat = self.stats.top(3)
        nimet = [pelaaja.name for pelaaja in pelaajat]

        self.assertEqual(nimet, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_jarjestaa_maalien_perusteella(self):
        pelaajat = self.stats.top(3, SortBy.GOALS)
        nimet = [pelaaja.name for pelaaja in pelaajat]

        self.assertEqual(nimet, ["Lemieux", "Yzerman", "Kurri"])

    def test_top_jarjestaa_syottojen_perusteella(self):
        pelaajat = self.stats.top(3, SortBy.ASSISTS)
        nimet = [pelaaja.name for pelaaja in pelaajat]

        self.assertEqual(nimet, ["Gretzky", "Yzerman", "Lemieux"])

    def test_top_jarjestaa_pisteiden_perusteella(self):
        pelaajat = self.stats.top(3, SortBy.POINTS)
        nimet = [pelaaja.name for pelaaja in pelaajat]

        self.assertEqual(nimet, ["Gretzky", "Lemieux", "Yzerman"])